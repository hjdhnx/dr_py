#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : 酷云筛选.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/9/24
import requests

headers = {
"User-Agent": "Dalvik/2.1.0"
}


def getClass():
    url = 'http://api.kunyu77.com/api.php/provide/filter'
    r = requests.get(url, headers=headers)
    html = r.json()
    class_names = []
    class_urls = []
    data = html['data']
    for i in data:
        class_names.append(data[i][0]['cat'])
        class_urls.append(i)
    print('&'.join(class_names))
    print('&'.join(class_urls))

ft_dict = {}

def getCate():
    # url = 'http://api.kunyu77.com/api.php/provide/searchFilter?devid=EA83E58357FC020ABA526E9620AD7E89&package=com.sevenVideo.app.android&pcode=010110004&year=&category=&area=&pagenum=1&type_id=0&pagesize=24'
    url = 'http://api.kunyu77.com/api.php/provide/searchFilter?year=&category=&area=&pagenum=1&type_id=1&pagesize=24'
    r = requests.get(url,headers=headers)
    html = r.json()
    print(html)
    filters = html['data']['conditions']
    print(filters)

    cates = [0,1,2,3,4] # 全部&电影&电视剧&综艺&动漫
    for cate in cates:
        getOne(cate,filters)
    print(ft_dict)

def getOne(cate_id,filters):
    ft_dict[cate_id] = []
    print(filters)
    if 'cat' in filters.keys():
        del filters['cat']
    for key in (filters):
        value = [{"n":"全部","v":""}]
        name_dict = {
            'y':'年代',
            'a':'地区',
            'scat':'类型',
        }
        # value = []
        vl = [{"n": i['name'], "v": i.get('value', '')} for i in filters[key]]
        value.extend(vl)
        ft_dict[cate_id].append({
            'key': key,
            'name': name_dict[key],
            'value': value
        })
    return ft_dict

if __name__ == '__main__':
    getCate()