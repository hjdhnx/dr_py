#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : parser.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/8/25

import os
import shutil

import requests
from flask import make_response, jsonify,render_template_string
from functools import partial  # 这玩意儿能锁定一个函数的参数
import subprocess
subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")  # 固定写法
# 解决execjs执行js时产生的乱码报错，需要在导入该模块之前，让Popen的encoding参数锁定为utf-8
# import execjs
import js2py
from js2py.base import JsObjectWrapper,PyJsString,PyJsObject

# os.environ["EXECJS_RUNTIME"] = "JScript"
# print(execjs.get().name)

def runJScode(jscode,loader=None,ctx=None):
    if loader is None:
        if ctx is None:
            ctx = {}
        loader = js2py.EvalJs(ctx,enable_require=False) # enable_require启用require关键字,会自动获取系统nodejs环境
    loader.execute(jscode)
    return loader, jscode

def runJs(jsPath, before='', after='', ctx=None):
    # base_path = os.path.dirname(os.path.abspath(__file__)) # 当前文件所在目录
    # base_path = os.path.dirname(os.getcwd()) # 当前主程序所在工作目录
    # base_path = os.path.dirname(os.path.abspath('.')) # 上级目录
    # js_code = 'var rule={}'
    if ctx is None:
        ctx = {}
    base_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))  # 上级目录
    if str(jsPath).startswith('http'):
        js_name = jsPath.split('/')[-1]
        cache_path = os.path.join(base_path, f'cache/{js_name}')
        if not os.path.exists(cache_path):
            try:
                print(f'开始缓存远程规则:{js_name},来源{jsPath}')
                js_code = requests.get(url=jsPath,timeout=3).text
                # js_code = requests.get(jsPath).text
                with open(cache_path,mode='w+',encoding='utf-8') as f:
                    f.write(js_code)
            except Exception as e:
                print('发生了错误:',e)
                return None, ''
        else:
            with open(cache_path, 'r', encoding='UTF-8') as fp:
                js_code = fp.read()
    else:
        js_path = os.path.join(base_path, jsPath)
        if not os.path.exists(js_path):
            return None,''
        js_name = jsPath.split('/')[-1]
        cache_path = os.path.join(base_path, f'cache/{js_name}')
        if not str(jsPath).startswith('js/') and not os.path.exists(cache_path) and os.path.exists(js_path):
            shutil.copy(js_path,cache_path) # 本地txt目录的复制过去凑数,实际不使用
        # print(js_path)
        with open(js_path, 'r', encoding='UTF-8') as fp:
            js_code = fp.read()
    # print(js_code)
    jscode_to_run = js_code
    # print(jscode_to_run)
    if before:
        jscode_to_run = before + jscode_to_run
    if after:
        jscode_to_run += after
    loader = js2py.EvalJs(ctx)
    return runJScode(jscode_to_run,loader)
    # loader = execjs.compile(jscode_to_run)
    # print(jscode_to_run)
    # loader.execute(jscode_to_run)
    # return loader,js_code

def toJs(jsPath,jsRoot='cache',env=None):
    base_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__))) # 上级目录
    js_path = os.path.join(base_path, f'{jsRoot}/{jsPath}')
    # print(js_path)
    if not os.path.exists(js_path):
        return jsonify({'code': -2, 'msg': f'非法猥亵,文件不存在'})
    with open(js_path, 'r', encoding='UTF-8') as fp:
        js = fp.read()
    if env:
        # js = render_template_string(js,env=env)
        for k in env:
            # print(f'${k}', f'{env[k]}')
            if f'${k}' in js:
                js = js.replace(f'${k}', f'{env[k]}')
        # js = render_template_string(js,**env)
    response = make_response(js)
    response.headers['Content-Type'] = 'text/javascript; charset=utf-8'
    return response

def getJs(jsPath,jsRoot='cache'):
    base_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))  # 上级目录
    js_path = os.path.join(base_path, f'{jsRoot}/{jsPath}')
    # print(js_path)
    if not os.path.exists(js_path):
        return ''
    with open(js_path, 'r', encoding='UTF-8') as fp:
        js = fp.read()
    return js

def toHtml(jsPath):
    base_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__))) # 上级目录
    js_path = os.path.join(base_path, f'cache/{jsPath}')
    with open(js_path, 'r', encoding='UTF-8') as fp:
        js = fp.read()
    response = make_response(js)
    response.headers['Content-Type'] = 'text/html; charset=utf-8'
    return response

def runPy(pyPath):
    # base_path = os.path.dirname(os.path.abspath(__file__)) # 当前文件所在目录
    # base_path = os.path.dirname(os.getcwd()) # 当前主程序所在工作目录
    # base_path = os.path.dirname(os.path.abspath('.')) # 上级目录
    # js_code = 'var rule={}'
    if pyPath and not str(pyPath).endswith('.py'):
        pyPath += '.py'
    base_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))  # 上级目录
    if str(pyPath).startswith('http'):
        py_name = pyPath.split('/')[-1]
        cache_path = os.path.join(base_path, f'cache/{py_name}')
        print('远程免嗅:',py_name)
        if not os.path.exists(cache_path):
            try:
                py_code = requests.get(pyPath,timeout=2).text
                with open(cache_path,mode='w+',encoding='utf-8') as f:
                    f.write(py_code)
            except Exception as e:
                print('发生了错误:',e)
                return None
        else:
            with open(cache_path, 'r', encoding='UTF-8') as fp:
                py_code = fp.read()
    else:
        py_root = os.path.join(base_path, 'py/')
        os.makedirs(py_root,exist_ok=True)
        py_path = os.path.join(py_root, pyPath)
        if not os.path.exists(py_path):
            return ''
        with open(py_path, 'r', encoding='UTF-8') as fp:
            py_code = fp.read()
    # print(js_code)
    return py_code

def covert_demo():
    ctx = {'py_sum':sum,'requests':requests}
    loader = js2py.EvalJs(ctx)
    # loader.execute('var a=py_sum(2,3);function f(x) {return x*x} var b=[a,"5"];var c={"a":a};')
    # loader.execute('var a=py_sum(2,3);function f(x) {return x*x}')
    loader.execute('function f(x) {return x*x};var a=py_sum([2,3]);var b=[a,5];var c={"a":a};')
    f = loader.f
    print(f(8))
    print(f.toString())
    print(loader.eval('py_sum(new Array(1, 2, 3))'))
    print(loader.eval('py_sum([1, 2])'))
    a = loader.a
    print(type(a),a)
    b = loader.b
    b.push(6)
    print(type(b),b)
    b = b.to_list()
    print(type(b),b)
    c = loader.c
    print(type(c),c)
    c = c.to_dict()
    print(type(c), c)
    # CryptoJS = js2py.require('crypto-js')
    # print(type(CryptoJS))
    # print(js2py.require('underscore'))
    JSON = js2py.eval_js('JSON')
    r = JSON.parse('[{"a":1}]')
    print(type(r),r)
    print(r[0].a)
    print(loader.eval('r = requests.get("https://www.baidu.com/");r.encoding = "utf-8";r.text'))
    # 下面是错误用法,没有loader环境没法正确eval_js,有loader用eval不需要eval_js
    # print(js2py.eval_js('r = requests.get("https://www.baidu.com/");r.encoding = "utf-8";r.text'))
    with open('../js/蓝莓影视.js',encoding='utf-8') as f:
        yk = f.read()
    print(yk)


if __name__ == '__main__':
    covert_demo()