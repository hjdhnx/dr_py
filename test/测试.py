#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : 测试.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/8/28

import re
from urllib.parse import quote,unquote
txt = 'var player_aaaa={"flag":"play","encrypt":3,"trysee":0,"points":0,"link":"\/vodplay\/44640-1-1.html","link_next":"","link_pre":"","url":"Zd2fZg56c6y10828ZDRiNzZjNzk1Y2E3OWQzNmQzYWEyM2IwODM0ZjM3MgO0O0OO0O0O","url_next":"d","from":"vip","server":"no","note":"","id":"44640","sid":1,"nid":1}'
ret = re.search('var player_(.*?)=(.*?)<',txt,re.M|re.I)
print(ret)

def encodeStr(input, encoding='GBK'):
    """
    指定字符串编码
    :param input:
    :param encoding:
    :return:
    """
    return quote(input.encode(encoding, 'ignore'))

def lazyParse(input,jsp,getParse,saveParse,headers,encoding):
    pass
str1 = '星'
key = str1.encode('gb2312','ignore')
print(quote(key))
print(quote(str1))
# print(str1.decode('utf-8',))
# str_gbk = str1.encode("gbk",ignore=True).strip()
# print("转码结果："+repr(str_gbk))
# print( unquote('%D0%C7','GBK'))
print(encodeStr('星','utf-8'))
print(encodeStr('斗罗大陆','gbk')) # %B6%B7%C2%DE%B4%F3%C2%BD