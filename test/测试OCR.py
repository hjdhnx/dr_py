#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : 测试OCR.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Author's Blog: https://blog.csdn.net/qq_32394351
# Date  : 2023/3/28

import requests
import base64
requests.packages.urllib3.disable_warnings()
PC_UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
UA = 'Mozilla/5.0'
# api = 'https://api.nn.ci/ocr/b64/text'
api = 'http://192.168.10.99:9898/ocr/b64/text'
api2 = 'http://dm.mudery.com:10000'
api3 = 'http://localhost:5705/parse/ocr'
# api4 = 'http://192.168.10.99:9898/ocr/drpy/text'
api4 = 'http://drpy.nokia.press:8028/ocr/drpy/text'
# api3 = 'http://cms.nokia.press:5707/parse/ocr'
def test():
    with open('yzm1.png',mode='rb') as f:
        img = f.read()
    try:
        print(base64.b64encode(img).decode())
        # code = requests.post(api, data=base64.b64encode(img).decode(), headers={'user-agent': PC_UA}, verify=False).text
        # code = requests.post(api, data=base64.b64encode(img).decode(), headers={'user-agent': PC_UA}, verify=False).text
        # code = requests.post(api3, data={"img":base64.b64encode(img).decode()}, headers={'user-agent': PC_UA}, verify=False).text
        # code = requests.post(api4, data={"img":base64.b64encode(img).decode()}, headers={'user-agent': PC_UA}, verify=False).text
        code = requests.post(api3, data={"img":base64.b64encode(img).decode()}, headers={'user-agent': PC_UA}, verify=False).text
    except Exception as e:
        print(f'ocr识别发生错误:{e}')
        code = ''
    print(f'验证码为:{code}')
    return code

if __name__ == '__main__':
    test()