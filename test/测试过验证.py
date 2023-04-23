#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : 测试过验证.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/8/30

import requests
# import ddddocr
from time import sleep,time
from urllib.parse import urljoin,quote,unquote
import requests.utils

url = 'https://cokemv.me/vodsearch/斗罗大陆----------1---.html'
PC_UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'

headers = {'user-agent':PC_UA}

def getHome(url):
    # http://www.baidu.com:9000/323
    urls = url.split('//')
    homeUrl = urls[0] + '//' + urls[1].split('/')[0]
    return homeUrl

def verifyCode(url,total_cnt=3):
    headers['Referer'] = getHome(url)
    cnt = 0
    ocr = ddddocr.DdddOcr()
    while cnt < total_cnt:
        s = requests.session()
        try:
            img = s.get(url="https://cokemv.me/index.php/verify/index.html?t="+str(time()), headers=headers,timeout=5).content
            code = ocr.classification(img)
            print('验证结果:',code)
            res = s.post(
                url=f"https://cokemv.me/index.php/ajax/verify_check?type=search&verify={code}",
                headers=headers
            ).json()
            if res["msg"] == "ok":
                cookies_dict = requests.utils.dict_from_cookiejar(s.cookies)
                cookie_str = ';'.join([f'{k}={cookies_dict[k]}' for k in cookies_dict])
                # return cookies_dict
                return cookie_str
        except:
            pass
        cnt += 1
        sleep(1)
    return ''

r = requests.get(url,headers=headers)
html = r.text
print(html)
if html.find('输入验证码') > -1:
    s = verifyCode(url)
    print(s)