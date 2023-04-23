#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : parse.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/9/24
from flask import Blueprint, jsonify,redirect,make_response
from utils.web import getParmas,get_interval
import os
from utils.cfg import cfg
from utils.log import logger
from utils.encode import OcrApi,base64ToImage
from controllers.service import storage_service
from utils.pyctx import py_ctx,getPreJs,runJScode,JsObjectWrapper,PyJsString,parseText,jsoup,time
from utils.env import get_env
import base64

parse = Blueprint("parse", __name__)

class R(object):

    @classmethod
    def ok(self, msg='操作成功', url=None, extra=None):
        if extra is None:
            extra = {}
        header = {
            "user-agent": "Mozilla/5.0"
        }
        if 'bilivideo.c' in url:
            header.update({
                'referer':'https://www.bilibili.com/'
            })
        result = {"code": 200, "msg": msg, "url":url}
        result.update(header)
        result.update(extra)
        return jsonify(result)

    @classmethod
    def error(self,msg="系统异常",code=404,extra=None):
        if extra is None:
            extra = {}
        result = {"code": code, "msg": msg}
        result.update(extra)
        return jsonify(result)

    @classmethod
    def success(self,msg='操作成功', url=None,extra=None):
        return self.ok(msg,url,extra)

    @classmethod
    def failed(self,msg="系统异常", code=404,extra=None):
        return self.error(msg,code,extra)

def 重定向(url:str):
    if isinstance(url, PyJsString):
        url = parseText(str(url))
    if str(url).startswith('http'):
        return f'redirect://{url}'
    else:
        return str(url)

def toast(url:str):
    if isinstance(url, PyJsString):
        url = parseText(str(url))
    return f'toast://{url}'

def image(text:str):
    if isinstance(text, PyJsString):
        text = parseText(str(text))
    return f'image://{text}'

@parse.route('/api/<path:filename>')
def parse_home(filename):
    url = getParmas('url')
    # http://localhost:5705/parse/api/%E6%97%A0%E5%90%8D.js?url=https://www.iqiyi.com/v_ik3832z0go.html
    # http://localhost:5705/parse/api/哔哩.js?url=https://www.bilibili.com/bangumi/play/ep704873
    if not url or not url.startswith('http'):
        return R.failed(f'url必填!{url},且必须是http开头')
    base_path = 'jiexi'
    os.makedirs(base_path, exist_ok=True)
    file_path = os.path.join(base_path, filename)
    if not os.path.exists(file_path):
        return R.failed(f'{file_path}文件不存在')
    logger.info(f'开始尝试通过{filename}解析:{url}')

    jsp = jsoup(url)
    env = get_env()
    py_ctx.update({
        'vipUrl': url,
        'fetch_params': {'headers': {'Referer':url}, 'timeout': 10, 'encoding': 'utf-8'},
        'jsp':jsp,
        '重定向':重定向,
        'toast':toast,
        'env':env,
        'image':image,
        'print':print,
        'log':logger.info,
        'getParmas':getParmas,
        'params':getParmas()
    })
    ctx = py_ctx
    with open(file_path,encoding='utf-8') as f:
        code = f.read()
    jscode = getPreJs() + code.strip().replace('js:', '', 1)
    # print(jscode)
    t1 = time()
    try:
        loader, _ = runJScode(jscode, ctx=ctx)
        realUrl = loader.eval('realUrl')
        if not realUrl:
            return R.failed(f'解析失败:{realUrl}')
        if isinstance(realUrl, PyJsString):
            realUrl = parseText(str(realUrl))
        if not realUrl or realUrl == url:
            return R.failed(f'解析失败',extra={'from':realUrl})
        # print(realUrl)
        if str(realUrl).startswith('redirect://'):
            return redirect(realUrl.split('redirect://')[1])
        elif str(realUrl).startswith('toast://'):
            return R.failed(str(realUrl).split('toast://')[1],extra={'from':url})
        elif str(realUrl).startswith('image://'):
            img_data = base64ToImage(str(realUrl).split('image://')[1])
            response = make_response(img_data)
            response.headers['Content-Type'] = 'image/jpeg'
            return response
        return R.success(f'{filename}解析成功',realUrl,{'time':f'{get_interval(t1)}毫秒','from':url})
    except Exception as e:
        msg = f'{filename}解析出错:{e}'
        logger.info(msg)
        return R.failed(msg,extra={'time':f'{get_interval(t1)}毫秒','from':url})

@parse.route('/ocr',methods=['POST'])
def base64_ocr():
    lsg = storage_service()
    ocr_api = lsg.getItem('OCR_API',cfg.OCR_API)
    # print(ocr_api)
    # print('params:',getParmas())
    img = getParmas('img')
    # print(img)
    if not img:
        return R.failed('识别失败:缺少img参数')
    try:
        img_bytes = base64.b64decode(img)
    except:
        return R.failed('识别失败:img参数不是正确的base64格式')
    # print(img_bytes)
    img_path = 'txt/pluto'
    os.makedirs(img_path,exist_ok=True)
    with open(f'{img_path}/yzm.png','wb+') as f:
        f.write(img_bytes)
    ocr = OcrApi(ocr_api)
    code = ocr.classification(img_bytes)
    # resp = R.success('识别成功',code)
    # print(resp.json)
    resp = code
    return resp
