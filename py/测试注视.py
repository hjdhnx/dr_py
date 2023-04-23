#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : 测试注释.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/10/20


import requests
import ujson

data = {'album': 'all', 'mcountry': 'all', 'mform': 'all', 'page': '1', 'sort': 'all', 'tag_arr%5B%5D': 'all', 'title': ''}
headers = {
    'Referer': 'https://gaze.run',
   'User-Agent': 'Mozilla/5.0 (Linux; Android 11; M2007J3SC Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045714 Mobile Safari/537.36',
   # 'cookie': 'PHPSESSID=e7ht5hvema4sg0o8l1o5k0bqt1; Hm_lvt_eebb854b7348edadfb6b433786f5d059=1666239708; Hm_lpvt_eebb854b7348edadfb6b433786f5d059=1666244071',
   'x-requested-with': 'XMLHttpRequest'
}
# form = ujson.dumps(data)
# form = data
# print(form)
form = 'mform=1&mcountry=all&tag_arr%5B%5D=3&page=1&sort=updatetime&album=all&title='
form = 'mform=1&mcountry=all&tag_arr%5B%5D=all&page=1&sort=default&album=all&title='
print(form)
r = requests.post('https://gaze.run/filter_movielist',data=form,headers=headers)
print(r.text)