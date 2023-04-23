#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : 通用免嗅.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/8/28
import requests
import re
import json
from urllib.parse import urljoin,quote,unquote
import base64

def lazyParse(input,d):
    print('通用免嗅:',input)
    r = requests.get(input, headers=d.headers,timeout=d.timeout)
    r.encoding = d.encoding
    html = r.text
    # print(html)
    # js = jsp.pdfh(html,'.stui-player__video script:eq(0)&&Html')
    # print(js)
    try:
        ret = re.search('var player_(.*?)=(.*?)<', html, re.M | re.I).groups()[1]
        ret = json.loads(ret)
        url = ret.get('url','')
        if len(url) > 10:
            if url.find('.m3u8') > -1 or url.find('.mp4') > -1:
                return url
            elif url.find('http') < 0:
                try:
                    l = unquote(base64.b64decode(url).decode("utf-8"))
                    print(l)
                    return l
                except Exception as e:
                    print(f'非url和base64编码:{e}')
                    return input
        else:
            return input
    except Exception as e:
        print(f'错误:{e}')
    return input