#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : gaze筛选.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/10/20

import re

import requests
from utils.htmlParser import jsoup

headers = {'user-agent':'Mozilla/5.0 (Linux; Android 11; M2007J3SC Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045714 Mobile Safari/537.36'}

def getFilters(url):
    # cate_id = str(re.search('.*/(\d+)', url).groups()[0])
    # print(cate_id)
    jsp = jsoup(url)
    pdfh = jsp.pdfh
    pdfa = jsp.pdfa
    print(jsp)
    r = requests.get(url,headers=headers)
    r.encoding = r.apparent_encoding
    html = r.text
    cls_list = pdfa(html,'.mform&&div')
    print(len(cls_list))
    print(cls_list)
    # ft_dict = {cate_id:[]}
    ft_dict = {}

    def getCate(cls):
        key = cls
        name = pdfh(html, f'.{cls}&&div:eq(0)&&a&&Text').replace('全部', '')
        values = pdfa(html, f'.{cls}&&div')
        # vl = [{"n":pdfh(i,'a&&Text'),"v":pdfh(i,'a&&href')} for i in values]
        # vl = [{"n":pdfh(i,'a&&Text'),"v":re.search('(.*?)-(.*)',pdfh(i,'a&&data-filter'),re.M|re.I|re.S).groups()[1].replace('.html','').replace('-','')} for i in values]
        vl = [{"n": pdfh(i, 'a&&Text'), "v": pdfh(i, 'a&&data-filter')} for i in values]

        return {
            'key': key,
            'name': name,
            'value': vl
        }
    for cls in cls_list:
        cate_id = pdfh(cls,'a&&data-filter')
        # key = pdfh(html,'.mcountry&&div:eq(0)&&a&&data-filter')
        # key = 'mcountry'
        # name = pdfh(html,'.mcountry&&div:eq(0)&&a&&Text').replace('全部','')
        # values = pdfa(html,'.mcountry&&div')
        # vl = [{"n":pdfh(i,'a&&Text'),"v":pdfh(i,'a&&data-filter')} for i in values]

        ft_dict[cate_id] = []
        for c in ['mcountry','mtag','sort','album']:
            d = getCate(c)
            ft_dict[cate_id].append(d)
    print(ft_dict)
    # return ft_dict

if __name__ == '__main__':
    getFilters('https://gaze.run/filter')