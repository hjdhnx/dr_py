#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : 搜狗筛选.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/9/11
import requests
from pprint import pprint

cates = 'teleplay&film&cartoon&tvshow&documentary'.split('&')
urls = [f'https://waptv.sogou.com/napi/video/classlist?abtest=0&iploc=CN1304&spver=&listTab={cate}&filter=&start=0&len=15&fr=filter' for cate in cates]
print(urls)
headers = {'user-agent':'Mozilla/5.0 (Linux; Android 11; M2007J3SC Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045714 Mobile Safari/537.36'}

ft_dict = {}
def getOne(url):
    r = requests.get(url, headers=headers)
    html = r.json()
    filters = html['listData']['list']['filter_list']
    cate_id = html['listData']['list']['entity']
    ft_dict[cate_id] = []
    for i in range(len(filters)):
        ft = filters[i]
        value = [{"n":"全部","v":""}]
        vl = [{"n":i,"v":i} for i in ft['option_list']]
        value.extend(vl)
        ft_dict[cate_id].append({
                'key':ft['option_name'],
                'name':ft['name'],
                'value':value
        })
    return ft_dict
# print(ft_dict)
for url in urls:
    # print(getOne(urls[0]))
    # print(getOne(url))
    getOne(url)
print(ft_dict)