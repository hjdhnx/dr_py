#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : 下载jar.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/10/14

import requests

headers = {
    'user-agent':'okhttp/3.15'
}
r = requests.get('http://刚刚.live/jar2/0906.jar',headers=headers)
print(r.content)

with open('0906.jar','wb+') as f:
    f.write(r.content)