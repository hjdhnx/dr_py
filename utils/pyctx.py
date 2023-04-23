#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : pyctx.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/9/24

import json

import requests
from utils.web import *
from utils.log import logger
from utils.encode import base64Encode, base64Decode, fetch, post, request, getCryptoJS, getPreJs, buildUrl, getHome, \
    parseText, atob,btoa
from utils.encode import setDetail, join, urljoin2, parseText, requireCache, base64ToImage, encodeStr, decodeStr
from utils.encode import md5 as mmd5
from utils.parser import runPy, runJScode, JsObjectWrapper, PyJsObject, PyJsString
from urllib.parse import quote
from utils.htmlParser import jsoup
from controllers.service import storage_service


def setItem(key, value):
    lsg = storage_service()
    if isinstance(key, PyJsString):
        key = parseText(str(key))
    if isinstance(value, PyJsString):
        value = parseText(str(value))
    return lsg.setItem(key, value)


def getItem(key, value=''):
    lsg = storage_service()
    if isinstance(key, PyJsString):
        key = parseText(str(key))
    if isinstance(value, PyJsString):
        value = parseText(str(value))
    return lsg.getItem(key, value)


def clearItem(key):
    lsg = storage_service()
    if isinstance(key, PyJsString):
        key = parseText(str(key))
    return lsg.clearItem(key)


def encodeUrl(url):
    # return base64Encode(quote(url))
    # return base64Encode(url)
    # print(type(url))
    if isinstance(url, PyJsString):
        # obj = obj.to_dict()
        url = parseText(str(url))
    return quote(url)


def stringify(obj):
    if isinstance(obj, PyJsObject):
        # obj = obj.to_dict()
        obj = parseText(str(obj))
    return json.dumps(obj, separators=(',', ':'), ensure_ascii=False)


def requireObj(url):
    if isinstance(url, PyJsString):
        url = parseText(str(url))
    return requireCache(url)


def md5(text):
    if isinstance(text, PyJsString):
        text = parseText(str(text))
    return mmd5(text)


py_ctx = {
    'requests': requests, 'print': print, 'base64Encode': base64Encode, 'base64Decode': base64Decode,
    'log': logger.info, 'fetch': fetch, 'post': post, 'request': request, 'getCryptoJS': getCryptoJS,
    'buildUrl': buildUrl, 'getHome': getHome, 'setDetail': setDetail, 'join': join, 'urljoin2': urljoin2,
    'PC_UA': PC_UA, 'MOBILE_UA': MOBILE_UA, 'UC_UA': UC_UA, 'IOS_UA': IOS_UA,
    'setItem': setItem, 'getItem': getItem, 'clearItem': clearItem, 'stringify': stringify, 'encodeUrl': encodeUrl,
    'requireObj': requireObj, 'md5': md5, 'atob': atob, 'btoa':btoa,'base64ToImage': base64ToImage, 'encodeStr': encodeStr,
    'decodeStr': decodeStr
}
