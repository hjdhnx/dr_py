#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : mxpro筛选.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/9/13
import re

import requests
from utils.htmlParser import jsoup

headers = {'user-agent':'Mozilla/5.0 (Linux; Android 11; M2007J3SC Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045714 Mobile Safari/537.36'}


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
    cls_list = pdfa(html,'.module-class&&.module-class-items')
    print(len(cls_list))
    ft_dict = {cate_id:[]}
    for cls in cls_list:
        tt = pdfh(cls,'.module-item-title&&Text')
        values = pdfa(cls,'.module-item-box&&a')
        # vl = [{"n":pdfh(i,'a&&Text'),"v":pdfh(i,'a&&href')} for i in values]
        vl = [{"n":pdfh(i,'a&&Text'),"v":re.search('(.*?)-(.*)',pdfh(i,'a&&href'),re.M|re.I|re.S).groups()[1].replace('.html','').replace('-','')} for i in values]
        ft_dict[cate_id].append({
            'key': tt,
            'name': tt,
            'value': vl
        })
    print(ft_dict)
    return ft_dict

if __name__ == '__main__':
    new_dict = {}
    for i in '20&1&2&3&4&23'.split('&'):
        ft_dict = getFilters(f'https://lanmeiguojiang.com/show/{i}-----------.html')
        new_dict.update(ft_dict)
    print(new_dict)


