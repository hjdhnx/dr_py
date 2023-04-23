#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : encode.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/8/29

import base64
import math
import re
from urllib.parse import urljoin,quote,unquote
from js2py.base import PyJsString
import requests,warnings
# 关闭警告
warnings.filterwarnings("ignore")
requests.packages.urllib3.disable_warnings()

import requests.utils
import hashlib
from time import sleep
import os
from utils.web import UC_UA,PC_UA
from ast import literal_eval
from utils.log import logger
import quickjs

def getPreJs():
    base_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))  # 上级目
    lib_path = os.path.join(base_path, f'libs/pre.js')
    with open(lib_path,encoding='utf-8') as f:
        code = f.read()
    return code

def getCryptoJS():
    base_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))  # 上级目
    os.makedirs(os.path.join(base_path, f'libs'), exist_ok=True)
    lib_path = os.path.join(base_path, f'libs/crypto-hiker.js')
    # print('加密库地址:', lib_path)
    if not os.path.exists(lib_path):
        return 'undefiend'
    with open(lib_path,encoding='utf-8') as f:
        code = f.read()
    return code

def md5(str):
    return hashlib.md5(str.encode(encoding='UTF-8')).hexdigest()

def getLib(js):
    base_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))  # 上级目录
    lib_path = os.path.join(base_path, f'libs/{js}')
    if not os.path.exists(lib_path):
        return ''
    with open(lib_path,encoding='utf-8') as f:
        return f.read()

# def atob(text):
#     if isinstance(text,PyJsString):
#         text = parseText(str(text))
#     qjs = quickjs.Context()
#     print(text)
#     js = getLib('atob.js')
#     print(js)
#     ret = qjs.eval(f'{js};atob("{text}")')
#     print(ret)

def atob(text):
    """
    解码
    :param text:
    :return:
    """
    if isinstance(text,PyJsString):
        text = parseText(str(text))
    return base64.b64decode(text.encode("utf8")).decode("latin1")

def btoa(text):
    """
    编码
    :param text:
    :return:
    """
    if isinstance(text,PyJsString):
        text = parseText(str(text))
    return base64.b64encode(text.encode("latin1")).decode("utf8")

def requireCache(lib:str):
    base_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))  # 上级目
    os.makedirs(os.path.join(base_path, f'libs'), exist_ok=True)
    logger.info(f'开始加载:{lib}')
    code = 'undefiend'
    if not lib.startswith('http'):
        lib_path = os.path.join(base_path, f'libs/{lib}')
        if not os.path.exists(lib_path):
            pass
        else:
            with open(lib_path, encoding='utf-8') as f:
                code = f.read()
    else:
        lib_path = os.path.join(base_path, f'libs/{md5(lib)}.js')
        if not os.path.exists(lib_path):
            try:
                r = requests.get(lib,headers={
                    'Referer': lib,
                    'User-Agent': UC_UA,
                },timeout=5,verify=False)
                with open(lib_path,mode='wb+') as f:
                    f.write(r.content)
                code =  r.text
            except Exception as e:
                print(f'获取远程依赖失败:{e}')
        else:
            with open(lib_path,encoding='utf-8') as f:
                code = f.read()
    # print(code)
    return code


def getHome(url):
    # http://www.baidu.com:9000/323
    urls = url.split('//')
    homeUrl = urls[0] + '//' + urls[1].split('/')[0]
    return homeUrl

class OcrApi:
    def __init__(self,api):
        self.api = api

    def classification(self,img):
        try:
            # code = requests.post(self.api,data=img,headers={'user-agent':PC_UA},verify=False).text
            code = requests.post(self.api,data=base64.b64encode(img).decode(),headers={'user-agent':PC_UA},verify=False).text
        except Exception as e:
            print(f'ocr识别发生错误:{e}')
            code = ''
        return code

def verifyCode(url,headers,timeout=5,total_cnt=3,api=None):
    if not api:
        # api = 'http://192.168.3.224:9000/api/ocr_img'
        api = 'https://api.nn.ci/ocr/b64/text'
    lower_keys = list(map(lambda x: x.lower(), headers.keys()))
    host = getHome(url)
    if not 'referer' in lower_keys:
        headers['Referer'] = host
    print(f'开始自动过验证,请求头:{headers}')
    cnt = 0
    ocr = OcrApi(api)
    while cnt < total_cnt:
        s = requests.session()
        try:
            img = s.get(url=f"{host}/index.php/verify/index.html", headers=headers,timeout=timeout,verify=False).content
            code = ocr.classification(img)
            print(f'第{cnt+1}次验证码识别结果:{code}')
            res = s.post(
                url=f"{host}/index.php/ajax/verify_check?type=search&verify={code}",
                headers=headers).json()
            if res["msg"] == "ok":
                cookies_dict = requests.utils.dict_from_cookiejar(s.cookies)
                cookie_str = ';'.join([f'{k}={cookies_dict[k]}' for k in cookies_dict])
                # return cookies_dict
                return cookie_str
        except:
            print(f'第{cnt+1}次验证码提交失败')
            pass
        cnt += 1
        sleep(1)
    return ''

def base64Encode(text):
    if isinstance(text,PyJsString):
        text = str(text).replace("'","").replace('"','')
    return base64.b64encode(text.encode("utf8")).decode("utf-8") #base64编码

def base64Decode(text):
    if isinstance(text,PyJsString):
        text = parseText(str(text))
    # print(text)
    return base64.b64decode(text).decode("utf-8") #base64解码

def encodeStr(input, encoding='GBK'):
    """
    指定字符串编码
    :param input:
    :param encoding:
    :return:
    """
    if isinstance(input,PyJsString):
        input = parseText(str(input))
    if isinstance(encoding,PyJsString):
        encoding = parseText(str(input))
    return quote(input.encode(encoding, 'ignore'))

def decodeStr(input, encoding='GBK'):
    """
    指定字符串解码
    :param input:
    :param encoding:
    :return:
    """
    if isinstance(input,PyJsString):
        input = parseText(str(input))
    if isinstance(encoding,PyJsString):
        encoding = parseText(str(input))
    return unquote(input,encoding)


def parseText(text:str):
    text = text.replace('false','False').replace('true','True').replace('null','None')
    # print(text)
    return literal_eval(text)

def setDetail(title:str,img:str,desc:str,content:str,tabs:list=None,lists:list=None):
    vod = {
        "vod_name": title.split('/n')[0],
        "vod_pic": img,
        "type_name": title,
        "vod_year": "",
        "vod_area": "",
        "vod_remarks": desc,
        "vod_actor": "",
        "vod_director": "",
        "vod_content": content
    }
    return vod

def urljoin2(a,b):
    a = str(a).replace("'",'').replace('"','')
    b = str(b).replace("'",'').replace('"','')
    # print(type(a),a)
    # print(type(b),b)
    ret = urljoin(a,b)
    return ret

def join(lists,string):
    """
    残废函数,没法使用
    :param lists:
    :param string:
    :return:
    """
    # FIXME
    lists1 = lists.to_list()
    string1 = str(string)
    print(type(lists1),lists1)
    print(type(string1),string1)
    try:
        ret = string1.join(lists1)
        print(ret)
        return ret
    except Exception as e:
        print(e)
        return ''

def dealObj(obj=None):
    if not obj:
        obj = {}
    encoding = obj.get('encoding') or 'utf-8'
    encoding = str(encoding).replace("'", "")
    # encoding = parseText(str(encoding))
    method = obj.get('method') or 'get'
    method = str(method).replace("'", "")
    # method = parseText(str(method))
    withHeaders = obj.get('withHeaders') or ''
    withHeaders = str(withHeaders).replace("'", "")
    # withHeaders = parseText(str(withHeaders))
    # print(type(url),url)
    # headers = dict(obj.get('headers')) if obj.get('headers') else {}
    # headers = obj.get('headers').to_dict() if obj.get('headers') else {}
    headers = obj.get('headers') if obj.get('headers') else {}
    new_headers = {}
    # print(type(headers),headers)
    for i in headers:
        new_headers[str(i).replace("'", "")] = str(headers[i]).replace("'", "")
    # print(type(new_headers), new_headers)

    timeout = float(obj.get('timeout').to_int()) if obj.get('timeout') else None
    # print(type(timeout), timeout)
    body = obj.get('body') if obj.get('body') else {}
    # print(body)
    # print(type(body))
    if isinstance(body,PyJsString):
        body = parseText(str(body))
        new_dict = {}
        new_tmp = body.split('&')
        for i in new_tmp:
            new_dict[i.split('=')[0]] = i.split('=')[1]
        body = new_dict

    new_body = {}
    for i in body:
        new_body[str(i).replace("'", "")] = str(body[i]).replace("'", "")
    return {
        'encoding':encoding,
        'headers':new_headers,
        'timeout':timeout,
        'body': new_body,
        'method':method,
        'withHeaders':withHeaders
    }

def coverDict2form(data:dict):
    forms = []
    for k,v in data.items():
        forms.append(f'{k}={v}')
    return '&'.join(forms)

def base_request(url,obj):
    # verify=False 关闭证书验证
    # print(obj)
    url = str(url).replace("'", "")
    method = obj.get('method') or ''
    withHeaders = obj.get('withHeaders') or ''
    # print(f'withHeaders:{withHeaders}')
    if not method:
        method = 'get'
        obj['method'] = 'method'
    # print(obj)
    print(f"{method}:{url}:{obj['headers']}:{obj.get('body','')},请求超时:{obj['timeout']}")
    try:
        # r = requests.get(url, headers=headers, params=body, timeout=timeout)
        if method.lower() == 'get':
            r = requests.get(url, headers=obj['headers'], params=obj['body'], timeout=obj['timeout'],verify=False)
        else:
            # if isinstance(obj['body'],dict):
            #     obj['body'] = coverDict2form(obj['body'])
            # print(obj['body'])
            # 亲测不需要转换data 格式的dict 为 form都正常 (gaze规则和奇优搜索)
            r = requests.post(url, headers=obj['headers'], data=obj['body'], timeout=obj['timeout'],verify=False)
        # r = requests.get(url, timeout=timeout)
        # r = requests.get(url)
        # print(encoding)
        r.encoding = obj['encoding']
        # print(f'源码:{r.text}')
        if withHeaders:
            backObj = {
                'url':r.url,
                'body':r.text,
                'headers':r.headers
            }
            return backObj
        else:
            return r.text
    except Exception as e:
        print(f'{method}请求发生错误:{e}')
        return {} if withHeaders else ''

def fetch(url,obj):
    # print('fetch')
    obj = dealObj(obj)
    if not obj.get('headers') or not any([obj['headers'].get('User-Agent'),obj['headers'].get('user-agent')]):
        obj['headers']['User-Agent'] = obj['headers'].get('user-agent',PC_UA)
    return base_request(url,obj)

def post(url,obj):
    obj = dealObj(obj)
    obj['method'] = 'post'
    return base_request(url,obj)

def request(url,obj):
    obj = dealObj(obj)
    # print(f'{method}:{url}')
    if not obj.get('headers') or not any([obj['headers'].get('User-Agent'),obj['headers'].get('user-agent')]):
        obj['headers']['User-Agent'] = obj['headers'].get('user-agent',UC_UA)

    return base_request(url, obj)

def redx(text):
    """
    修正js2py交互的字符串自动加前后引号问题
    :param text:
    :return:
    """
    # return text.replace("'", "").replace('"', "")
    text = str(text)
    if text.startswith("'") and text.endswith("'"):
        text = text[1:-1]
    return text

def buildUrl(url,obj=None):
    # url = str(url).replace("'", "")
    url = redx(url)
    if not obj:
        obj = {}
    new_obj = {}
    for i in obj:
        # new_obj[str(i).replace("'", "")] = str(obj[i]).replace("'", "")
        new_obj[redx(i)] = redx(obj[i])

    if str(url).find('?') < 0:
        url = str(url) + '?'
    param_list = [f'{i}={new_obj[i]}' for i in new_obj]
    # print(param_list)
    prs = '&'.join(param_list)
    if len(new_obj) > 0 and not str(url).endswith('?'):
        url += '&'
    # url = (url + prs).replace('"','').replace("'",'')
    url = url + prs
    # print(url)
    return url

def forceOrder(lists:list,key:str=None,option=None):
    """
    强制正序
    :param lists:
    :param key:
    :return:
    """
    start = math.floor(len(lists)/2)
    end = min(len(lists)-1,start+1)
    if start >= end:
        return lists
    first = lists[start]
    second = lists[end]
    if key:
        try:
            first = first[key]
            second = second[key]
        except:
            pass
    if option and hasattr(option, '__call__'):
        try:
            first = option(first)
            second = option(second)
            # print(f'first:{first},second:{second}')
        except Exception as e:
            print(f'强制排序执行option发生了错误:{e}')
    first = str(first)
    second = str(second)
    if re.search(r'(\d+)',first) and re.search(r'(\d+)',second):
        num1 = int(re.search(r'(\d+)',first).groups()[0])
        num2 = int(re.search(r'(\d+)',second).groups()[0])
        if num1 > num2:
            lists.reverse()

    return lists

def base64ToImage(image_base64:str):
    if isinstance(image_base64,PyJsString):
        image_base64 = parseText(str(image_base64))
    if ',' in image_base64:
        image_base64 = image_base64.split(',')[1]
    img_data = base64.b64decode(image_base64)
    return img_data