#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : 爱奇艺筛选.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/9/12
import json

import requests
from pprint import pprint

cates = '1&2&3&4&6&5&16'.split('&')
urls = [f'https://pcw-api.iqiyi.com/search/category/categoryinfo?brand=IQIYI&channel_id={cate}&include_knowledge_content_type=&locale=zh' for cate in cates]
print(urls)
headers = {'user-agent':'Mozilla/5.0 (Linux; Android 11; M2007J3SC Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045714 Mobile Safari/537.36'}

data = [{
        "id": "mode",
        "name": "综合排序",
        "child": [{
            "name": "热播榜",
            "id": 11
        }, {
            "name": "好评榜",
            "id": 8
        }, {
            "name": "新上线",
            "id": 4
        }]
    },
    {
        "id": "year",
        "name": "全部年份",
        "child": [{
            "name": "2022",
            "id": 2022
        }, {
            "name": "2021",
            "id": 2021
        }, {
            "name": "2020",
            "id": 2020
        }, {
            "name": "2019",
            "id": 2019
        }, {
            "name": "2018",
            "id": 2018
        }, {
            "name": "2017",
            "id": 2017
        }, {
            "name": "2016-2011",
            "id": "2011_2016"
        }, {
            "name": "2010-2000",
            "id": "2000_2010"
        }, {
            "name": "90年代",
            "id": "1990_1999"
        }, {
            "name": "80年代",
            "id": "1980_1989"
        }, {
            "name": "更早",
            "id": "1964_1979"
        }]
    },
    {
        "id": "is_purchase",
        "name": "全部资费",
        "child": [{
            "name": "免费",
            "id": 0
        }, {
            "name": "会员",
            "id": 1
        }, {
            "name": "付费",
            "id": 2
        }]
    }
]
ft_dict = {}
def getOne(url,cate):
    r = requests.get(url, headers=headers)
    html = r.json()
    filters = html['data']
    new_list = list(tuple(data))
    new_list.extend(filters)

    # cate_id = html['code']
    cate_id = cate
    ft_dict[cate_id] = []
    for i in range(len(new_list)):
        ft = new_list[i]
        if ft['name'] == '地区':
            ft['id'] = 'three_category_id'
        # elif ft['name'] == '类型':
        #     ft['id'] = 'type'
        # elif ft['name'] == '规格':
        #     ft['id'] = 'spec'

        value = [{"n":"全部","v":""}]
        vl = [{"n":i['name'],"v":i['id']} for i in ft['child']]
        value.extend(vl)
        ft_dict[cate_id].append({
                'key':str(ft['id']),
                'name':ft['name'],
                'value':value
        })
    return ft_dict
# print(ft_dict)
for i in range(len(urls)):
    url = urls[i]
    cate = cates[i]
    # print(getOne(urls[0]))
    # print(getOne(url))
    getOne(url,cate)
print(ft_dict)
with open('爱奇艺筛选.json',mode='w+',encoding='utf-8') as f:
    f.write(json.dumps(ft_dict,ensure_ascii=False,indent=4))
