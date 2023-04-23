#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : 九酷.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/12/14
import hashlib

import requests
import time
import ujson

def md5(str):
    return hashlib.md5(str.encode(encoding='UTF-8')).hexdigest()

headers = {
    # 'x-requested-with':'XMLHttpRequest',
    'user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
    # 'Cookie':'ecPopup=1;crisp-client%2Fsession%2Fba128124-8ac1-44d1-8420-98420b4da478=session_8d89f90c-4b46-4895-86d8-03a74770b741'
}
# s = requests.session()
# s.get('https://jiuku.site/index.php/vod/type/id/1.html')
# print(s.cookies)

fyclass = 1
fypage = 1
tm = int(time.time())
# tm = ''
print(tm)
key = md5("DS"+str(tm)+"DCC147D11943AF75")
print(key)
data = f'type={fyclass}&page={fypage}&time={tm}&key={key}'
data_dict = {}
for dt in data.split('&'):
    data_dict[dt.split('=')[0]] = dt.split('=')[1]
print(data_dict)
# data_dict = ujson.dumps(data_dict)
r = requests.post('https://jiuku.site/index.php/api/vod',data=data_dict,headers=headers)
print(r.text)

"""
解析免嗅:
"https://jiuku.site/addons/dp/player/dp.php?key=0&from=&id="+vod_id+"&api=&url="+"vipUrl
专线m3u8:
unescape(base64Decode(jsurl))
"""
