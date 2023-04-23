#include <Python.h>
#include <time.h>

#include "third-party/quickjs.h"

// Node of Python callable that the context needs to keep available.
typedef struct PythonCallableNode PythonCallableNode;
struct PythonCallableNode {
	PyObject *obj;
	// Internal ID of the callable function. "magic" is QuickJS terminology.
	int magic;
	PythonCallableNode *next;
};

// Keeps track of the time if we are using a time limit.
typedef struct {
	clock_t start;
	clock_t limit;
} InterruptData;

// The data of the type _quickjs.Context.
typedef struct {
	PyObject_HEAD JSRuntime *runtime;
	JSContext *context;
	int has_time_limit;
	clock_t time_limit;
	// Used when releasing the GIL.
	PyThreadState *thread_state;
	InterruptData interrupt_data;
	// NULL-terminated singly linked list of callable Python objects that we need to keep alive.
	PythonCallableNode *python_callables;
} ContextData;

// The data of the type _quickjs.Object.
typedef struct {
	PyObject_HEAD;
	ContextData *context;
	JSValue object;
} ObjectData;

// The exception raised by this module.
static PyObject *JSException = NULL;
static PyObject *StackOverflow = NULL;
// Converts a JSValue to a Python object.
//
// Takes ownership of the JSValue and will deallocate it (refcount reduced by 1).
static PyObject *quickjs_to_python(ContextData *context_obj, JSValue value);
// Whether converting item to QuickJS would be possible.
static int python_to_quickjs_possible(ContextData *context, PyObject *item);
// Converts item to QuickJS.
//
// If the Python object is not possible to convert to JS, undefined will be returned. This fallback
// will not be used if python_to_quickjs_possible returns 1.
static JSValueConst python_to_quickjs(ContextData *context, PyObject *item);

static PyTypeObject Object;

// Returns nonzero if we should stop due to a time limit.
static int js_interrupt_handler(JSRuntime *rt, void *opaque) {
	InterruptData *data = opaque;
	if (clock() - data->start >= data->limit) {
		return 1;
	} else {
		return 0;
	}
}

// Sets up a context and an InterruptData struct if the context has a time limit.
static void setup_time_limit(ContextData *context, InterruptData *interrupt_data) {
	if (context->has_time_limit) {
		JS_SetInterruptHandler(context->runtime, js_interrupt_handler, interrupt_data);
		interrupt_data->limit = context->time_limit;
		interrupt_data->start = clock();
	}
}

// Restores the context if the context has a time limit.
static void teardown_time_limit(ContextData *context) {
	if (context->has_time_limit) {
		JS_SetInterruptHandler(context->runtime, NULL, NULL);
	}
}

// This method is always called in a context before running JS code in QuickJS. It sets up time
// limites, releases the GIL etc.
static void prepare_call_js(ContextData *context) {
	// We release the GIL in order to speed things up for certain use cases.
	assert(!context->thread_state);
	context->thread_state = PyEval_SaveThread();
	setup_time_limit(context, &context->interrupt_data);
}

// This method is called right after returning from running JS code. Aquires the GIL etc.
static void end_call_js(ContextData *context) {
	teardown_time_limit(context);
	assert(context->thread_state);
	PyEval_RestoreThread(context->thread_state);
	context->thread_state = NULL;
}

// Called when Python is called again from inside QuickJS.
static void prepare_call_python(ContextData *context) {
	assert(context->thread_state);
	PyEval_RestoreThread(context->thread_state);
	context->thread_state = NULL;
}

// Called when the operation started by prepare_call_python is done.
static void end_call_python(ContextData *context) {
	assert(!context->thread_state);
	context->thread_state = PyEval_SaveThread();
}

// GC traversal.
static int object_traverse(ObjectData *self, visitproc visit, void *arg) {
	Py_VISIT(self->context);
	return 0;
}

// Creates an instance of the Object class.
static PyObject *object_new(PyTypeObject *type, PyObject *args, PyObject *kwds) {
	ObjectData *self = PyObject_GC_New(ObjectData, type);
	if (self != NULL) {
		self->context = NULL;
	}
	return (PyObject *)self;
}

// Deallocates an instance of the Object class.
static void object_dealloc(ObjectData *self) {
	if (self->context) {
		PyObject_GC_UnTrack(self);
		JS_FreeValue(self->context->context, self->object);
		// We incremented the refcount of the context when we created this object, so we should
		// decrease it now so we don't leak memory.
		Py_DECREF(self->context);
	}
	PyObject_GC_Del(self);
}

// _quickjs.Object.get
//
// Gets a Javascript property of the object.
static PyObject *object_get(ObjectData *self, PyObject *args) {
	const char *name;
	if (!PyArg_ParseTuple(args, "s", &name)) {
		return NULL;
	}
	JSValue value = JS_GetPropertyStr(self->context->context, self->object, name);
	return quickjs_to_python(self->context, value);
}

static JSValue js_c_function(
    JSContext *ctx, JSValueConst this_val, int argc, JSValueConst *argv, int magic) {
	ContextData *context = (ContextData *)JS_GetContextOpaque(ctx);
	if (context->has_time_limit) {
		return JS_ThrowInternalError(ctx, "Can not call into Python with a time limit set.");
	}
	PythonCallableNode *node = context->python_callables;
	while (node && node->magic != magic) {
		node = node->next;
	}
	if (!node) {
		return JS_ThrowInternalError(ctx, "Internal error.");
	}
	prepare_call_python(context);

	PyObject *args = PyTuple_New(argc);
	if (!args) {
		end_call_python(context);
		return JS_ThrowOutOfMemory(ctx);
	}
	int tuple_success = 1;
	for (int i = 0; i < argc; ++i) {
		PyObject *arg = quickjs_to_python(context, JS_DupValue(ctx, argv[i]));
		if (!arg) {
			tuple_success = 0;
			break;
		}
		PyTuple_SET_ITEM(args, i, arg);
	}
	if (!tuple_success) {
		Py_DECREF(args);
		end_call_python(context);
		return JS_ThrowInternalError(ctx, "Internal error: could not convert args.");
	}

	PyObject *result = PyObject_CallObject(node->obj, args);
	Py_DECREF(args);
	if (!result) {
		end_call_python(context);
		return JS_ThrowInternalError(ctx, "Python call failed.");
	}
	JSValue js_result = JS_NULL;
	if (python_to_quickjs_possible(context, result)) {
		js_result = python_to_quickjs(context, result);
	} else {
		PyErr_Clear();
		js_result = JS_ThrowInternalError(ctx, "Can not convert Python result to JS.");
	}
	Py_DECREF(result);

	end_call_python(context);
	return js_result;
}

// _quickjs.Object.set
//
// Sets a Javascript property to the object. Callables are supported.
static PyObject *object_set(ObjectData *self, PyObject *args) {
	const char *name;
	PyObject *item;
	if (!PyArg_ParseTuple(args, "sO", &name, &item)) {
		return NULL;
	}
	int ret = 0;
	if (PyCallable_Check(item) && (!PyObject_IsInstance(item, (PyObject *)&Object) || JS_IsFunction(
		self->context->context, ((ObjectData *)item)->object))) {
		PythonCallableNode *node = PyMem_Malloc(sizeof(PythonCallableNode));
		if (!node) {
			return NULL;
		}
		Py_INCREF(item);
		node->magic = 0;
		if (self->context->python_callables) {
			node->magic = self->context->python_callables->magic + 1;
		}
		node->obj = item;
		node->next = self->context->python_callables;
		self->context->python_callables = node;

		JSValue function = JS_NewCFunctionMagic(
			self->context->context,
			js_c_function,
			name,
			0,  // TODO: Should we allow setting the .length of the function to something other than 0?
			JS_CFUNC_generic_magic,
			node->magic);
		// If this fails we don't notify the caller of this function.
		ret = JS_SetPropertyStr(self->context->context, self->object, name, function);
		if (ret != 1) {
			PyErr_SetString(PyExc_TypeError, "Failed setting the variable as a callable.");
			return NULL;
		} else {
			Py_RETURN_NONE;
		}
	} else {
		if (python_to_quickjs_possible(self->context, item)) {
			ret = JS_SetPropertyStr(self->context->context, self->object, name,
			                        python_to_quickjs(self->context, item));
			if (ret != 1) {
				PyErr_SetString(PyExc_TypeError, "Failed setting the variable.");
			}
		}
		if (ret == 1) {
			Py_RETURN_NONE;
		} else {
			return NULL;
		}
	}
}

// _quickjs.Object.__call__
static PyObject *object_call(ObjectData *self, PyObject *args, PyObject *kwds);

// _quickjs.Object.json
//
// Returns the JSON representation of the object as a Python string.
static PyObject *object_json(ObjectData *self) {
	JSContext *context = self->context->context;
	JSValue json_string = JS_JSONStringify(context, self->object, JS_UNDEFINED, JS_UNDEFINED);
	return quickjs_to_python(self->context, json_string);
}

// All methods of the _quickjs.Object class.
static PyMethodDef object_methods[] = {
    {"get", (PyCFunction)object_get, METH_VARARGS, "Gets a Javascript property of the object."},
    {"set", (PyCFunction)object_set, METH_VARARGS, "Sets a Javascript property to the object."},
    {"json", (PyCFunction)object_json, METH_NOARGS, "Converts to a JSON string."},
    {NULL} /* Sentinel */
};

// Define the quickjs.Object type.
static PyTypeObject Object = {PyVarObject_HEAD_INIT(NULL, 0).tp_name = "_quickjs.Object",
                              .tp_doc = "Quickjs object",
                              .tp_basicsize = sizeof(ObjectData),
                              .tp_itemsize = 0,
                              .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HAVE_GC,
                              .tp_traverse = (traverseproc)object_traverse,
                              .tp_new = object_new,
                              .tp_dealloc = (destructor)object_dealloc,
                              .tp_call = (ternaryfunc)object_call,
                              .tp_methods = object_methods};

// Whether converting item to QuickJS would be possible.
static int python_to_quickjs_possible(ContextData *context, PyObject *item) {
	if (PyBool_Check(item)) {
		return 1;
	} else if (PyLong_Check(item)) {
		return 1;
	} else if (PyFloat_Check(item)) {
		return 1;
	} else if (item == Py_None) {
		return 1;
	} else if (PyUnicode_Check(item)) {
		return 1;
	} else if (PyObject_IsInstance(item, (PyObject *)&Object)) {
		ObjectData *object = (ObjectData *)item;
		if (object->context != context) {
			PyErr_Format(PyExc_ValueError, "Can not mix JS objects from different contexts.");
			return 0;
		}
		return 1;
	} else {
		PyErr_Format(PyExc_TypeError,
		             "Unsupported type when converting a Python object to quickjs: %s.",
		             Py_TYPE(item)->tp_name);
		return 0;
	}
}

// Converts item to QuickJS.
//
// If the Python object is not possible to convert to JS, undefined will be returned. This fallback
// will not be used if python_to_quickjs_possible returns 1.
static JSValueConst python_to_quickjs(ContextData *context, PyObject *item) {
	if (PyBool_Check(item)) {
		return JS_MKVAL(JS_TAG_BOOL, item == Py_True ? 1 : 0);
	} else if (PyLong_Check(item)) {
		int overflow;
		long value = PyLong_AsLongAndOverflow(item, &overflow);
		if (overflow) {
			PyObject *float_value = PyNumber_Float(item);
			double double_value = PyFloat_AsDouble(float_value);
			Py_DECREF(float_value);
			return JS_NewFloat64(context->context, double_value);
		} else {
			return JS_MKVAL(JS_TAG_INT, value);
		}
	} else if (PyFloat_Check(item)) {
		return JS_NewFloat64(context->context, PyFloat_AsDouble(item));
	} else if (item == Py_None) {
		return JS_NULL;
	} else if (PyUnicode_Check(item)) {
		return JS_NewString(context->context, PyUnicode_AsUTF8(item));
	} else if (PyObject_IsInstance(item, (PyObject *)&Object)) {
		return JS_DupValue(context->context, ((ObjectData *)item)->object);
	} else {
		// Can not happen if python_to_quickjs_possible passes.
		return JS_UNDEFINED;
	}
}

// _quickjs.Object.__call__
static PyObject *object_call(ObjectData *self, PyObject *args, PyObject *kwds) {
	if (self->context == NULL) {
		// This object does not have a context and has not been created by this module.
		Py_RETURN_NONE;
	}

	// We first loop through all arguments and check that they are supported without doing anything.
	// This makes the cleanup code simpler for the case where we have to raise an error.
	const int nargs = PyTuple_Size(args);
	for (int i = 0; i < nargs; ++i) {
		PyObject *item = PyTuple_GetItem(args, i);
		if (!python_to_quickjs_possible(self->context, item)) {
			return NULL;
		}
	}

	// Now we know that all arguments are supported and we can convert them.
	JSValueConst *jsargs = malloc(nargs * sizeof(JSValueConst));
	for (int i = 0; i < nargs; ++i) {
		PyObject *item = PyTuple_GetItem(args, i);
		jsargs[i] = python_to_quickjs(self->context, item);
	}

	prepare_call_js(self->context);
	JSValue value;
	value = JS_Call(self->context->context, self->object, JS_NULL, nargs, jsargs);
	for (int i = 0; i < nargs; ++i) {
		JS_FreeValue(self->context->context, jsargs[i]);
	}
	free(jsargs);
	end_call_js(self->context);
	return quickjs_to_python(self->context, value);
}

// Converts the current Javascript exception to a Python exception via a C string.
static void quickjs_exception_to_python(JSContext *context) {
	JSValue exception = JS_GetException(context);
	const char *cstring = JS_ToCString(context, exception);
	const char *stack_cstring = NULL;
	if (!JS_IsNull(exception) && !JS_IsUndefined(exception)) {
		JSValue stack = JS_GetPropertyStr(context, exception, "stack");
		if (!JS_IsException(stack)) {
			stack_cstring = JS_ToCString(context, stack);
			JS_FreeValue(context, stack);
		}
	}
	if (cstring != NULL) {
		const char *safe_stack_cstring = stack_cstring ? stack_cstring : "";
		if (strstr(cstring, "stack overflow") != NULL) {
			PyErr_Format(StackOverflow, "%s\n%s", cstring, safe_stack_cstring);
		} else {
			PyErr_Format(JSException, "%s\n%s", cstring, safe_stack_cstring);
		}
	} else {
		// This has been observed to happen when different threads have used the same QuickJS
		// runtime, but not at the same time.
		// Could potentially be another problem though, since JS_ToCString may return NULL.
		PyErr_Format(JSException,
					 "(Failed obtaining QuickJS error string. Concurrency issue?)");
	}
	JS_FreeCString(context, cstring);
	JS_FreeCString(context, stack_cstring);
	JS_FreeValue(context, exception);
}

// Converts a JSValue to a Python object.
//
// Takes ownership of the JSValue and will deallocate it (refcount reduced by 1).
static PyObject *quickjs_to_python(ContextData *context_obj, JSValue value) {
	JSContext *context = context_obj->context;
	int tag = JS_VALUE_GET_TAG(value);
	// A return value of NULL means an exception.
	PyObject *return_value = NULL;

	if (tag == JS_TAG_INT) {
		return_value = Py_BuildValue("i", JS_VALUE_GET_INT(value));
	} else if (tag == JS_TAG_BIG_INT) {
		const char *cstring = JS_ToCString(context, value);
		return_value = PyLong_FromString(cstring, NULL, 10);
		JS_FreeCString(context, cstring);
	} else if (tag == JS_TAG_BOOL) {
		return_value = Py_BuildValue("O", JS_VALUE_GET_BOOL(value) ? Py_True : Py_False);
	} else if (tag == JS_TAG_NULL) {
		return_value = Py_None;
	} else if (tag == JS_TAG_UNDEFINED) {
		return_value = Py_None;
	} else if (tag == JS_TAG_EXCEPTION) {
		quickjs_exception_to_python(context);
	} else if (tag == JS_TAG_FLOAT64) {
		return_value = Py_BuildValue("d", JS_VALUE_GET_FLOAT64(value));
	} else if (tag == JS_TAG_STRING) {
		const char *cstring = JS_ToCString(context, value);
		return_value = Py_BuildValue("s", cstring);
		JS_FreeCString(context, cstring);
	} else if (tag == JS_TAG_OBJECT || tag == JS_TAG_MODULE || tag == JS_TAG_SYMBOL) {
		// This is a Javascript object or function. We wrap it in a _quickjs.Object.
		return_value = PyObject_CallObject((PyObject *)&Object, NULL);
		ObjectData *object = (ObjectData *)return_value;
		// This is important. Otherwise, the context may be deallocated before the object, which
		// will result in a segfault with high probability.
		Py_INCREF(context_obj);
		object->context = context_obj;
		PyObject_GC_Track(object);
		object->object = JS_DupValue(context, value);
	} else {
		PyErr_Format(PyExc_TypeError, "Unknown quickjs tag: %d", tag);
	}

	JS_FreeValue(context, value);
	if (return_value == Py_None) {
		// Can not simply return PyNone for refcounting reasons.
		Py_RETURN_NONE;
	}
	return return_value;
}

static PyObject *test(PyObject *self, PyObject *args) {
	return Py_BuildValue("i", 42);
}

// Global state of the module. Currently none.
struct module_state {};

// GC traversal.
static int context_traverse(ContextData *self, visitproc visit, void *arg) {
	PythonCallableNode *node = self->python_callables;
	while (node) {
		Py_VISIT(node->obj);
		node = node->next;
	}
	return 0;
}

// GC clearing. Object does not have a clearing method, therefore dependency cycles
// between Context and Object will always be cleared starting here.
static int context_clear(ContextData *self) {
	PythonCallableNode *node = self->python_callables;
	while (node) {
		Py_CLEAR(node->obj);
		node = node->next;
	}
	return 0;
}

// Creates an instance of the _quickjs.Context class.
static PyObject *context_new(PyTypeObject *type, PyObject *args, PyObject *kwds) {
	ContextData *self = PyObject_GC_New(ContextData, type);
	if (self != NULL) {
		// We never have different contexts for the same runtime. This way, different
		// _quickjs.Context can be used concurrently.
		self->runtime = JS_NewRuntime();
		self->context = JS_NewContext(self->runtime);
		self->has_time_limit = 0;
		self->time_limit = 0;
		self->thread_state = NULL;
		self->python_callables = NULL;
		JS_SetContextOpaque(self->context, self);
		PyObject_GC_Track(self);
	}
	return (PyObject *)self;
}

// Deallocates an instance of the _quickjs.Context class.
static void context_dealloc(ContextData *self) {
	JS_FreeContext(self->context);
	JS_FreeRuntime(self->runtime);
	PyObject_GC_UnTrack(self);
	PythonCallableNode *node = self->python_callables;
	self->python_callables = NULL;
	while (node) {
		PythonCallableNode *this = node;
		node = node->next;
		// this->obj may already be NULL if GC'ed right before through context_clear.
		Py_XDECREF(this->obj);
		PyMem_Free(this);
	}
	PyObject_GC_Del(self);
}

// Evaluates a Python string as JS and returns the result as a Python object. Will return
// _quickjs.Object for complex types (other than e.g. str, int).
static PyObject *context_eval_internal(ContextData *self, PyObject *args, int eval_type) {
	const char *code;
	if (!PyArg_ParseTuple(args, "s", &code)) {
		return NULL;
	}
	prepare_call_js(self);
	JSValue value;
	value = JS_Eval(self->context, code, strlen(code), "<input>", eval_type);
	end_call_js(self);
	return quickjs_to_python(self, value);
}

// _quickjs.Context.eval
//
// Evaluates a Python string as JS and returns the result as a Python object. Will return
// _quickjs.Object for complex types (other than e.g. str, int).
static PyObject *context_eval(ContextData *self, PyObject *args) {
	return context_eval_internal(self, args, JS_EVAL_TYPE_GLOBAL);
}

// _quickjs.Context.module
//
// Evaluates a Python string as JS module. Otherwise identical to eval.
static PyObject *context_module(ContextData *self, PyObject *args) {
	return context_eval_internal(self, args, JS_EVAL_TYPE_MODULE);
}

// _quickjs.Context.execute_pending_job
//
// If there are pending jobs, executes one and returns True. Else returns False.
static PyObject *context_execute_pending_job(ContextData *self) {
	prepare_call_js(self);
	JSContext *ctx;
	int ret = JS_ExecutePendingJob(self->runtime, &ctx);
	end_call_js(self);
	if (ret > 0) {
		Py_RETURN_TRUE;
	} else if (ret == 0) {
		Py_RETURN_FALSE;
	} else {
		quickjs_exception_to_python(ctx);
		return NULL;
	}
}

// _quickjs.Context.parse_json
//
// Evaluates a Python string as JSON and returns the result as a Python object. Will
// return _quickjs.Object for complex types (other than e.g. str, int).
static PyObject *context_parse_json(ContextData *self, PyObject *args) {
	const char *data;
	if (!PyArg_ParseTuple(args, "s", &data)) {
		return NULL;
	}
	JSValue value;
	Py_BEGIN_ALLOW_THREADS;
	value = JS_ParseJSON(self->context, data, strlen(data), "context_parse_json.json");
	Py_END_ALLOW_THREADS;
	return quickjs_to_python(self, value);
}

// _quickjs.Context.get_global
//
// Retrieves the global object of the JS context.
static PyObject *context_get_global(ContextData *self) {
	return quickjs_to_python(self, JS_GetGlobalObject(self->context));
}

// _quickjs.Context.get
//
// Retrieves a global variable from the JS context.
static PyObject *context_get(ContextData *self, PyObject *args) {
	PyErr_WarnEx(PyExc_DeprecationWarning,
	             "Context.get is deprecated, use Context.get_global().get instead.", 1);
	PyObject *global = context_get_global(self);
	if (global == NULL) {
		return NULL;
	}
	PyObject *ret = object_get((ObjectData *)global, args);
	Py_DECREF(global);
	return ret;
}

// _quickjs.Context.set
//
// Sets a global variable to the JS context.
static PyObject *context_set(ContextData *self, PyObject *args) {
	PyErr_WarnEx(PyExc_DeprecationWarning,
	             "Context.set is deprecated, use Context.get_global().set instead.", 1);
	PyObject *global = context_get_global(self);
	if (global == NULL) {
		return NULL;
	}
	PyObject *ret = object_set((ObjectData *)global, args);
	Py_DECREF(global);
	return ret;
}

// _quickjs.Context.set_memory_limit
//
// Sets the memory limit of the context.
static PyObject *context_set_memory_limit(ContextData *self, PyObject *args) {
	Py_ssize_t limit;
	if (!PyArg_ParseTuple(args, "n", &limit)) {
		return NULL;
	}
	JS_SetMemoryLimit(self->runtime, limit);
	Py_RETURN_NONE;
}

// _quickjs.Context.set_time_limit
//
// Sets the CPU time limit of the context. This will be used in an interrupt handler.
static PyObject *context_set_time_limit(ContextData *self, PyObject *args) {
	double limit;
	if (!PyArg_ParseTuple(args, "d", &limit)) {
		return NULL;
	}
	if (limit < 0) {
		self->has_time_limit = 0;
	} else {
		self->has_time_limit = 1;
		self->time_limit = (clock_t)(limit * CLOCKS_PER_SEC);
	}
	Py_RETURN_NONE;
}

// _quickjs.Context.set_max_stack_size
//
// Sets the max stack size in bytes.
static PyObject *context_set_max_stack_size(ContextData *self, PyObject *args) {
	Py_ssize_t limit;
	if (!PyArg_ParseTuple(args, "n", &limit)) {
		return NULL;
	}
	JS_SetMaxStackSize(self->runtime, limit);
	Py_RETURN_NONE;
}

// _quickjs.Context.memory
//
// Sets the CPU time limit of the context. This will be used in an interrupt handler.
static PyObject *context_memory(ContextData *self) {
	PyObject *dict = PyDict_New();
	if (dict == NULL) {
		return NULL;
	}
	JSMemoryUsage usage;
	JS_ComputeMemoryUsage(self->runtime, &usage);
#define MEM_USAGE_ADD_TO_DICT(key)                          \
	{                                                       \
		PyObject *value = PyLong_FromLongLong(usage.key);   \
		if (PyDict_SetItemString(dict, #key, value) != 0) { \
			return NULL;                                    \
		}                                                   \
		Py_DECREF(value);                                   \
	}
	MEM_USAGE_ADD_TO_DICT(malloc_size);
	MEM_USAGE_ADD_TO_DICT(malloc_limit);
	MEM_USAGE_ADD_TO_DICT(memory_used_size);
	MEM_USAGE_ADD_TO_DICT(malloc_count);
	MEM_USAGE_ADD_TO_DICT(memory_used_count);
	MEM_USAGE_ADD_TO_DICT(atom_count);
	MEM_USAGE_ADD_TO_DICT(atom_size);
	MEM_USAGE_ADD_TO_DICT(str_count);
	MEM_USAGE_ADD_TO_DICT(str_size);
	MEM_USAGE_ADD_TO_DICT(obj_count);
	MEM_USAGE_ADD_TO_DICT(obj_size);
	MEM_USAGE_ADD_TO_DICT(prop_count);
	MEM_USAGE_ADD_TO_DICT(prop_size);
	MEM_USAGE_ADD_TO_DICT(shape_count);
	MEM_USAGE_ADD_TO_DICT(shape_size);
	MEM_USAGE_ADD_TO_DICT(js_func_count);
	MEM_USAGE_ADD_TO_DICT(js_func_size);
	MEM_USAGE_ADD_TO_DICT(js_func_code_size);
	MEM_USAGE_ADD_TO_DICT(js_func_pc2line_count);
	MEM_USAGE_ADD_TO_DICT(js_func_pc2line_size);
	MEM_USAGE_ADD_TO_DICT(c_func_count);
	MEM_USAGE_ADD_TO_DICT(array_count);
	MEM_USAGE_ADD_TO_DICT(fast_array_count);
	MEM_USAGE_ADD_TO_DICT(fast_array_elements);
	MEM_USAGE_ADD_TO_DICT(binary_object_count);
	MEM_USAGE_ADD_TO_DICT(binary_object_size);
	return dict;
}

// _quickjs.Context.gc
//
// Runs garbage collection.
static PyObject *context_gc(ContextData *self) {
	JS_RunGC(self->runtime);
	Py_RETURN_NONE;
}

static PyObject *context_add_callable(ContextData *self, PyObject *args) {
	PyErr_WarnEx(PyExc_DeprecationWarning,
	             "Context.add_callable is deprecated, use Context.get_global().set instead.", 1);
	PyObject *global = context_get_global(self);
	if (global == NULL) {
		return NULL;
	}
	PyObject *ret = object_set((ObjectData *)global, args);
	Py_DECREF(global);
	return ret;
}

// All methods of the _quickjs.Context class.
static PyMethodDef context_methods[] = {
    {"eval", (PyCFunction)context_eval, METH_VARARGS, "Evaluates a Javascript string."},
    {"module",
     (PyCFunction)context_module,
     METH_VARARGS,
     "Evaluates a Javascript string as a module."},
    {"execute_pending_job", (PyCFunction)context_execute_pending_job, METH_NOARGS, "Executes a pending job."},
    {"parse_json", (PyCFunction)context_parse_json, METH_VARARGS, "Parses a JSON string."},
    {"get_global", (PyCFunction)context_get_global, METH_NOARGS, "Gets the Javascript global object."},
    {"get", (PyCFunction)context_get, METH_VARARGS, "Gets a Javascript global variable."},
    {"set", (PyCFunction)context_set, METH_VARARGS, "Sets a Javascript global variable."},
    {"set_memory_limit",
     (PyCFunction)context_set_memory_limit,
     METH_VARARGS,
     "Sets the memory limit in bytes."},
    {"set_time_limit",
     (PyCFunction)context_set_time_limit,
     METH_VARARGS,
     "Sets the CPU time limit in seconds (C function clock() is used)."},
    {"set_max_stack_size",
     (PyCFunction)context_set_max_stack_size,
     METH_VARARGS,
     "Sets the maximum stack size in bytes. Default is 256kB."},
    {"memory", (PyCFunction)context_memory, METH_NOARGS, "Returns the memory usage as a dict."},
    {"gc", (PyCFunction)context_gc, METH_NOARGS, "Runs garbage collection."},
    {"add_callable", (PyCFunction)context_add_callable, METH_VARARGS, "Wraps a Python callable."},
    {NULL} /* Sentinel */
};

// Define the _quickjs.Context type.
static PyTypeObject Context = {PyVarObject_HEAD_INIT(NULL, 0).tp_name = "_quickjs.Context",
                               .tp_doc = "Quickjs context",
                               .tp_basicsize = sizeof(ContextData),
                               .tp_itemsize = 0,
                               .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HAVE_GC,
                               .tp_traverse = (traverseproc)context_traverse,
                               .tp_clear = (inquiry)context_clear,
                               .tp_new = context_new,
                               .tp_dealloc = (destructor)context_dealloc,
                               .tp_methods = context_methods};

// All global methods in _quickjs.
static PyMethodDef myextension_methods[] = {{"test", (PyCFunction)test, METH_NOARGS, NULL},
                                            {NULL, NULL}};

// Define the _quickjs module.
static struct PyModuleDef moduledef = {PyModuleDef_HEAD_INIT,
                                       "quickjs",
                                       NULL,
                                       sizeof(struct module_state),
                                       myextension_methods,
                                       NULL,
                                       NULL,
                                       NULL,
                                       NULL};

// This function runs when the module is first imported.
PyMODINIT_FUNC PyInit__quickjs(void) {
	if (PyType_Ready(&Context) < 0) {
		return NULL;
	}
	if (PyType_Ready(&Object) < 0) {
		return NULL;
	}

	PyObject *module = PyModule_Create(&moduledef);
	if (module == NULL) {
		return NULL;
	}

	JSException = PyErr_NewException("_quickjs.JSException", NULL, NULL);
	if (JSException == NULL) {
		return NULL;
	}
	StackOverflow = PyErr_NewException("_quickjs.StackOverflow", JSException, NULL);
	if (StackOverflow == NULL) {
		return NULL;
	}

	Py_INCREF(&Context);
	PyModule_AddObject(module, "Context", (PyObject *)&Context);
	Py_INCREF(&Object);
	PyModule_AddObject(module, "Object", (PyObject *)&Object);
	PyModule_AddObject(module, "JSException", JSException);
	PyModule_AddObject(module, "StackOverflow", StackOverflow);
	return module;
}
