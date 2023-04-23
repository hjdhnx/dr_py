#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : quickjs_py交互.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/10/12


from quickjs import Context, Object as QuickJSObject
import json
from pprint import pp
from uuid import UUID
from datetime import date, datetime

# https://github.com/PetterS/quickjs/pull/82  py交互扩展
# print(QuickJSObject)
# QuickJSObject.set('a',1)
# print(Context.get_global())
# exit()

class JS:
    interp = None
    # Store global variables here. Reference from javascript by path
    _globals = None

    # Used for generating unique ids in Context namespace
    _incr = 0

    # I cache the values passed from python to js. Otherwise, we create new representation
    # objects each time a value is referenced.
    _cache = None

    def __init__(self):
        self.interp = Context()
        self._globals = {}
        self._cache = {}

        # Install js proxy logic
        self.interp.add_callable("proxy_get", self.proxy_get)
        self.interp.add_callable("proxy_set", self.proxy_set)
        self.interp.eval("""
        var handler = {
            get(target, property) {
                rv = proxy_get(target.path, property)
                if (typeof rv == 'string' && rv.substr(0, 5) == 'eval:') {
                    eval(rv.substr(5));
                    return eval(rv.substr(5));
                }
                return rv
            },
            set(target, property, value) {
                return proxy_set(target.path, property, value)
            }
        }
        var mk_proxy = function(path) {
            return new Proxy({path: path}, handler);
        }
        """)

    def set(self, **kwargs):
        for (k, v) in kwargs.items():
            self.interp.set(k, v)

    def __call__(self, s):
        return self.interp.eval(s)

    # -----------------------------------------------------------------
    def to_non_proxied(self, v):
        # returns True/False and a value if the value can be represented
        # by a Javascript type (not proxied)
        if v in [None, True, False]:
            return True, v

        if type(v) in [QuickJSObject, str, int, float]:
            return True, v

        if type(v) in [UUID]:
            return True, str(v)

        return False, None

    def to_eval_str(self, v, path=None):
        # The value will be produced via eval if it is a string starting with eval:

        # Cache results
        if id(v) and id(v) in self._cache:
            return self._cache[id(v)]

        # If the value is a list, create a list of return values. Problem is
        # that these have no path in the self._globals dict. They will have to
        # be duplicated if they are objects.

        # BUG here - every reference to the list, create another copy - need to cache
        if type(v) == list:
            rv = []

            for v1 in v:
                can_non_proxy, non_proxied = self.to_non_proxied(v1)
                if can_non_proxy:
                    self._incr += 1
                    self.interp.set("_lv%s" % self._incr, v1)
                    rv.append("_lv%s" % self._incr)
                else:
                    rv.append(self.to_eval_str(v1))
            rv = "[" + ",".join(rv) + "]"
            self._cache[id(v)] = rv
            return rv

        if type(v) == date:
            rv = "new Date(%s, %s, %s)" % (v.year, v.month - 1, v.day)
            self._cache[id(v)] = rv
            return rv

        if type(v) == datetime:
            rv = "new Date('%s')" % v.isoformat()
            self._cache[id(v)] = rv
            return rv

        # this creates a function, which can never be garbage collected
        if callable(v):
            self._incr += 1
            gname = "_fn%s" % self._incr
            self.interp.add_callable(gname, v)
            rv = "%s" % gname
            self._cache[id(v)] = rv
            return rv

        # Anonymous variables are created by values inside lists
        if path is None:
            self._incr += 1
            path = "_anon%s" % self._incr
            self._globals[path] = v

        # I need to do this for objects and try getattr
        if type(v) == dict:
            rv = "mk_proxy('%s')" % path
            self._cache[id(v)] = rv
            return rv

        # Should be a user defined object to get here. Proxy it.
        rv = "mk_proxy('%s')" % path
        self._cache[id(v)] = rv
        return rv

    # -----------------------------------------------------------------
    # Proxy Callback Points
    def proxy_variable(self, **kwargs):
        for (k, v) in kwargs.items():
            self._globals[k] = v
            self.interp.set(k, None)
            js("""%s = mk_proxy("%s");""" % (k, k))

    def eval_path(self, path):
        parts = path.split(".")
        root = self._globals
        for part in parts:
            root = root[part]
        return root

    def proxy_get(self, path, property):
        # print(path, property)
        root = self.eval_path(path)
        try:
            rv = root.get(property, None)
        except:
            # Object
            rv = getattr(root, property)

        # print(path, property, rv)

        can_non_proxy, non_proxied = self.to_non_proxied(rv)
        if can_non_proxy:
            return rv

        new_path = path + "." + property
        estr = self.to_eval_str(rv, path=new_path)
        # print("eval:" + estr)
        return "eval:" + estr

    def proxy_set(self, path, property, value):
        # print(path, property, value)
        root = self.eval_path(path)
        root[property] = value

if __name__ == '__main__':
    # Example access class attributes
    class example:
        a = "I am a"
        a1 = 111

        def fn(self, a='not set'):
            print("fn() called, a = ", a)


    # Example access dict
    l = {
        "a": 1,
        "fn": lambda: "XXXX",
        "p1": None,
        "p2": {
            "p3": "PPP333"
        },
        "p4": ["A", 4, None, example()],
        "p5": example()
    }

    js = JS()

    # Standard Variables
    js.set(v1="Set via python")
    print("v1 = ", js("v1"))
    assert (js("v1") == "Set via python")
    js.set(v2=None)
    print("v2 = ", js("v2"))
    assert (js("v2") is None)

    js.proxy_variable(l=l)

    # null
    print("p1 = ", js("l.p1"))
    assert (l['p1'] == js("l.p1"))

    # Access dict values
    print("l.a = ", js("l.a"))
    assert (l['a'] == js("l.a"))
    js("l.b = 4")
    print("l.b = ", js("l.b"))
    assert (l['b'] == 4)
    print("fn() = ", js("l.fn()"))

    # Undefined attribute
    print("l.undef = ", js("l.undef"))

    # Nested dict
    print("l.p2.p3 = ", js("l.p2.p3"))
    assert (l['p2']['p3'] == js("l.p2.p3"))

    # Dict assigned from JS - Need to use .json() to unwrap in Python
    js("l.c = {d: 4}")
    print("l.c = ", js("l.c"))
    print("l.c.d = ", js("l.c.d"))
    print("l.c = ", l['c'].json())

    # List
    print("l.p4[1] =", js("l.p4[1]"))
    assert (js("l.p4[1]") == l['p4'][1])
    print("calling l.p4[3].fn('called')")
    js("l.p4[3].fn('called')")

    # THIS FAILS  - p4 was copied and the original variable is never referenced.
    js("l.p4.push('added')")
    print("l.p4 = ", l['p4'])

    # Python Object accesss
    print("l.p5 =", js("l.p5"))
    print("l.p5.a1 =", js("l.p5.a1"))
    assert (l['p5'].a1 == js("l.p5.a1"))
    print("calling l.p5.fn(444)")
    js("l.p5.fn(444)")

    # Print the global variables - will see anonymous variables
    pp(js._globals)