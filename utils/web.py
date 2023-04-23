#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : web.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/9/6
import os

from flask import request,jsonify
import hashlib
# from utils.cfg import cfg
from controllers.service import storage_service
from utils.ua import *

def getParmas(key=None,value=''):
    """
    获取链接参数
    :param key:
    :return:
    """
    content_type = request.headers.get('Content-Type')
    # print(content_type)
    args = {}
    if request.method == 'POST':
        if 'application/x-www-form-urlencoded' in content_type or 'multipart/form-data' in content_type:
            args = request.form
        elif 'application/json' in content_type:
            args = request.json
        elif 'text/plain' in content_type:
            args = request.data
        else:
            args = request.args
    elif request.method == 'GET':
        args = request.args
    if key:
        return args.get(key,value)
    else:
        return args

def layuiBack(msg:str, data=None,code:int=0,count:int=0):
    if data is None:
        data = []
    return jsonify({
        'msg':msg,
        'code':code,
        'data':data,
        'count':count or len(data)
    })

def md5(str):
    return hashlib.md5(str.encode(encoding='UTF-8')).hexdigest()

def verfy_token(token=None):
    if not token:
        cookies = request.cookies
        token = cookies.get('token', '')
    if not token or len(str(token)) != 32:
        return False
    lsg = storage_service()
    # username = cfg.get('UNAME','')
    username = lsg.getItem('UNAME','')
    # pwd = cfg.get('PWD','')
    pwd = lsg.getItem('PWD','')
    ctoken = md5(f'{username};{pwd}')
    # print(f'username:{username},pwd:{pwd},current_token:{ctoken},input_token:{ctoken}')
    if token != ctoken:
        return False
    return True