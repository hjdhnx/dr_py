from quickjs import Function,Context
import requests
from time import time
import js2py
import json
ctx = Context()
ctx.add_callable("print", print)
def print2(text):
    print('print2:',text)
# ctx.set('print2',print2)
ctx.add_callable("print2", print2)
# ctx.add_callable("ua", 'mobile')
gg="""
    function adder(a, b) {
        c=[1,2].filter(it=>it>1);
        print(c);
        print(ua);
        print(c.join('$'))
        print(typeof c)
        print(Array.isArray(c))
        return a + b+`你这个a是${a},c是${c}`;
    }
    
    function bd(){
    let html = request('https://www.baidu.com/')
    }
    
    
    function f(a, b) {
        let e = print2;
        e(2222);
        return adder(a, b);
    }
    var d = 123;
    print2('我是注入的');
    print2(typeof(ccc));
    var gs = {a:1};
    print2(gs)
    // print2(ccc(gs))
    var qw = [1,2,3]
    print2(mmp)
    """


# f = Function("f",gg)
#print(f(1,3))
#assert f(1, 2) == 3
# ctx.add_callable("f", f)
# ctx.add_callable("f", f)
ctx.set('ua','mobile')
cc = {
    # "json":json
    "json":'22323'
    # json:json
}
def ccc(aa):
    return json.dumps(aa)
# ctx.add_callable('json',json)
# ctx.set('cc',cc) # 报错
ctx.add_callable('ccc',ccc)
# ctx.eval(gg)
ctx.set('mmp','我的mm')
#ctx.eval(f(1,3))
ctx.eval(gg+'let lg = print;lg(111);lg(f(1,3))')
ctx.set("v", 10**25)
print('v',type(ctx.eval("v")),ctx.eval("v"))
print(ctx.get('d'))
gs = ctx.get('gs')
qw = ctx.get('qw')
print('qw',qw)
print(qw.json())
print('gs',gs)

print(gs.json())
print(json.loads(gs.json()))
print(ctx.get('e'))
print(ctx.get('print2'))
print(11,ctx.parse_json('{"a":1}'))

def request(url):
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    html = r.text
    print(html)
    return html

ctx.add_callable('request',request)
ctx.eval('bd()')

t1 = time()
rule_file = '555影视.js'
with open('../../js/模板.js', encoding='utf-8') as f:
    before = f.read().split('export')[0]

with open(f'../../js/{rule_file}',encoding='utf-8') as f1:
    jscode = f1.read()
    jscode = before + jscode
    print(jscode)

ctx1 = Context()
ctx1.eval(jscode)
ret = ctx1.get('rule')
# print(type(ret.json()),ret.json())
# print(json.loads(ret.json()))
ret = json.loads(ret.json())
print(type(ret),ret)
t2 = time()
print(f'quickjs耗时:{round((t2-t1)*1000,2)}毫秒')
tt1 = time()
ctx1.eval(jscode)
ret = ctx1.get('rule')
print(type(ret.json()),ret.json())
print(json.loads(ret.json()))
tt2 = time()
print(f'quickjs第2次耗时:{round((tt2-tt1)*1000,2)}毫秒')

t3 = time()
with open(f'../../js/{rule_file}',encoding='utf-8') as f1:
    jscode = f1.read()
    jscode = before + jscode
    # print(jscode)
ctx2 = js2py.EvalJs({},enable_require=False) # enable_require启用require关键字,会自动获取系统nodejs环境
ctx2.execute(jscode)
ret = ctx2.rule.to_dict()
print(type(ret),ret)
t4 = time()
print(f'js2py耗时:{round((t4-t3)*1000,2)}毫秒')
t5 = time()
ctx2.execute(jscode)
ret = ctx2.rule.to_dict()
print(type(ret),ret)
t6 = time()
print(f'js2py第2次耗时:{round((t6-t5)*1000,2)}毫秒')
# 报错提示:(没法把python对象给qkjs,基础数据类型字典也不行,json等包更不行了)  Unsupported type when converting a Python object to quickjs: dict.