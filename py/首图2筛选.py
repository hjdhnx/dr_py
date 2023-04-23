#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : 首图2筛选.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/9/30

import re

import requests
from utils.htmlParser import jsoup

headers = {'user-agent':'Mozilla/5.0 (Linux; Android 11; M2007J3SC Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045714 Mobile Safari/537.36'}


kv_list = {
    '按剧情':'vtype',
    '按地区':'varea',
    '按年份':'vyear',
    '按语言':'vlang',
    '按字母':'vword',

}
def getFilters(url):
    cate_id = str(re.search('.*/(\d+)', url).groups()[0])
    print(cate_id)
    jsp = jsoup(url)
    pdfh = jsp.pdfh
    pdfa = jsp.pdfa
    print(jsp)
    r = requests.get(url,headers=headers)
    r.encoding = r.apparent_encoding
    html = r.text
    cls_list = pdfa(html,'ul.stui-screen__list')
    print(len(cls_list))
    ft_dict = {cate_id:[]}
    for cls in cls_list:
        tt = pdfh(cls,'li&&Text')
        if tt.find('按类型')>-1:
            continue
        values = pdfa(cls,'ul&&a')
        # vl = [{"n":pdfh(i,'a&&Text'),"v":pdfh(i,'a&&href')} for i in values]
        vl = [{"n":pdfh(i,'a&&Text'),"v":re.search('(.*?)-(.*)',pdfh(i,'a&&href'),re.M|re.I|re.S).groups()[1].replace('.html','').replace('-','')} for i in values]
        ft_dict[cate_id].append({
            # 'key': kv_list[tt],
            'key': tt.replace('按',''),
            'name': tt,
            'value': vl
        })
    print(ft_dict)
    return ft_dict

if __name__ == '__main__':
    new_dict = {}
    for i in '1&2&3&4'.split('&'):
        ft_dict = getFilters(f'https://www.zbkk.net/vodshow/{i}--------2---.html')
        new_dict.update(ft_dict)
    print(new_dict)