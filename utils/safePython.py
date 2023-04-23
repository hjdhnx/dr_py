#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : safePython.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/8/28

import io
import tokenize

from func_timeout import func_set_timeout
from func_timeout.exceptions import FunctionTimedOut
from urllib.parse import urljoin,quote,unquote
import requests
import time
import json
import re
from lxml import etree
import datetime
import base64
from utils.log import logger

time_out_sec = 8  # 安全执行python代码超时
class my_exception(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        message = f'函数执行超时: "{self.message}"'
        return message

@func_set_timeout(time_out_sec)
def excute(*args):
    exec(*args)

def check_unsafe_attributes(string):
    """
    安全检测需要exec执行的python代码
    :param string:
    :return:
    """
    g = tokenize.tokenize(io.BytesIO(string.encode('utf-8')).readline)
    pre_op = ''
    for toktype, tokval, _, _, _ in g:
        if toktype == tokenize.NAME and pre_op == '.' and tokval.startswith('_'):
            attr = tokval
            msg = "access to attribute '{0}' is unsafe.".format(attr)
            raise AttributeError(msg)
        elif toktype == tokenize.OP:
            pre_op = tokval

DEFAULT_PYTHON_CODE = """# 可用内置环境变量:
#  - log: log(message): 打印日志功能
#  - error: 弹出用户错误的弹窗
# 返回变量值: result = {...}\n\n
zyw_lists = env['hikerule.zyw.list'].with_context(active_test=True).sudo().search(
                    [('option', '=', 'zy'), ('cate_id.name', '!=', '18+'),('cate_id.is_bad', '!=', True)])
result = env['hikerule.zyw.list2data.wizard'].sudo().get_publish_value(zyw_lists)
"""

class safePython:
    def __init__(self,name, code):
        self.name = name or '未定义'
        self.code = code

    def action_task_exec(self,call=None,params=None):
        """
        接口调用执行函数
        :return:
        """
        if not params:
            params = []
        builtins = __builtins__
        builtins = dict(builtins).copy()
        for key in ['__import__','eval','exec','globals','dir','copyright','open','quit']:
            del builtins[key]  # 删除不安全的关键字
        # print(builtins)
        global_dict = {'__builtins__': builtins,
                       'requests': requests, 'urljoin':urljoin,'quote':quote,'unquote': unquote,
                       'log': logger.info, 'json': json,'print':print,
                       're':re,'etree':etree,'time':time,'datetime':datetime,'base64':base64
                       }  # 禁用内置函数,不允许导入包
        try:
            check_unsafe_attributes(self.code)
            localdict = {'result': None}
            # 待解决windows下运行超时的问题
            base_code = self.code.strip()
            if call:
                logger.info(f'开始执行:{call}')
            try:
                # excute(to_run_code, global_dict, localdict)
                excute(base_code, global_dict, localdict)
                run = localdict.get(call)
                if run:
                    localdict['result'] = run(*params)
            except FunctionTimedOut:
                raise my_exception(f'函数[{self.name}]运行时间超过{time_out_sec}秒，疑似死循环，已被系统切断')
        except Exception as e:
            ret = f'执行报错:{e}'
            logger.info(ret)
            return ret
        else:
            # print(global_dict)
            # print(localdict)
            ret = localdict['result']
            return ret