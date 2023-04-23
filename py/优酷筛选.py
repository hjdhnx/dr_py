#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : 优酷筛选.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/9/23
import json
import re

import requests
from pprint import pprint

# cates = 'teleplay&film&cartoon&tvshow&documentary'.split('&')
headers1 = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 11; M2007J3SC Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045714 Mobile Safari/537.36'
        # ,'x-requested-with':'XMLHttpRequest'
        # ,'sec-fetch-site':'same-origin'
        # ,'sec-fetch-mode':'cors'
        # ,'referer':'https://www.youku.com/category/show/type_%E7%94%B5%E8%A7%86%E5%89%A7_mainArea_%E4%B8%AD%E5%9B%BD%E5%86%85%E5%9C%B0_tags_%E9%9D%92%E6%98%A5.html?spm=a2ha1.14919748_WEBTV_JINGXUAN.drawer3.27'
        ,'referer':'https://www.youku.com'
    }
r = requests.get('https://www.youku.com/category/data?params=%7B%22type%22%3A%22%E7%94%B5%E5%BD%B1%22%7D&optionRefresh=1&pageNo=1',headers=headers1)
html = r.json()
cates_data = html['data']['filterData']['filter']['filterData'][0]['subFilter']
cates_data = list(map(lambda x:x['title'],cates_data))
print(cates_data)
exit()
# cates = cates_data[:1]
cates = cates_data
urls = ['https://www.youku.com/category/data?params='+'{"type":"'+cate+'"}&optionRefresh=1&pageNo=1' for cate in cates]
print(urls)
headers = {'user-agent':'Mozilla/5.0 (Linux; Android 11; M2007J3SC Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045714 Mobile Safari/537.36'}

ft_dict = {}

def getHtml(url):
    r = requests.get(url, headers=headers)
    html = r.text
    html = '{' + re.search('window.__INITIAL_DATA__.*?{(.*?);', html, re.S | re.M).groups()[0]
    undefined = null = None
    false = False
    true = True
    html = eval(html)
    print(type(html), html)
    url1 = 'https://www.youku.com/category/data?params=%7B%22type%22%3A%22%E7%94%B5%E8%A7%86%E5%89%A7%22%2C%22tags%22%3A%22%E9%9D%92%E6%98%A5%22%7D&optionRefresh=1&pageNo=1'


def getOne(url):
    r = requests.get(url,headers=headers1)
    print(r.text)
    html = r.json()
    filters = html['data']['filterData']['filter']['filterData'][1:]
    cate_id = html['data']['filterData']['cateKey']

    ft_dict[cate_id] = []
    for i in range(len(filters)):
        ft = filters[i]
        # value = [{"n":"全部","v":""}]
        value = []
        vl = [{"n":i['title'],"v":i.get('value','')} for i in ft['subFilter']]
        value.extend(vl)
        ft_dict[cate_id].append({
                'key':ft['filterType'],
                'name':ft['subFilter'][0]['title'],
                'value':value
        })
    return ft_dict
# print(ft_dict)
for url in urls:
    # print(getOne(urls[0]))
    # print(getOne(url))
    getOne(url)
print(ft_dict)
print(json.dumps(ft_dict,ensure_ascii=False))