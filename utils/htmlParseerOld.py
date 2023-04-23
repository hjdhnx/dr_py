#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : htmlParser.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/8/25
import json

from pyquery import PyQuery as pq
from lxml import etree
from urllib.parse import urljoin
import re
from jsonpath import jsonpath

PARSE_CACHE = True  # 解析缓存

class jsoup:
    def __init__(self,MY_URL=''):
        self.MY_URL = MY_URL
        self.pdfh_html = ''
        self.pdfa_html = ''

        self.pdfh_doc = None
        self.pdfa_doc = None

    def test(self, text:str, string:str):
        searchObj = re.search(rf'{text}', string, re.M | re.I)
        test_ret = True if searchObj else False
        return test_ret

    def pdfh(self,html,parse:str,add_url=False):
        if not parse:
            return ''
        if PARSE_CACHE:
            if self.pdfh_html != html:
                self.pdfh_html = html
                self.pdfh_doc = pq(html)
            doc = self.pdfh_doc
        else:
            doc = pq(html)
        if parse == 'body&&Text' or parse == 'Text':
            text = doc.text()
            return text
        elif parse == 'body&&Html' or parse == 'Html':
            return doc.html()
        option = None
        if parse.find('&&') > -1:
            option = parse.split('&&')[-1]
            parse = parse.split('&&')[:-1]  # 如果只有一个&& 取的就直接是0
            if len(parse) > 1:  # 如果不大于1可能就是option操作,不需要拼eq
                parse = ' '.join([i if self.test(':eq|:lt|:gt|#',i) else f'{i}:eq(0)' for i in parse])
            else:
                parse = parse[0] if self.test(':eq|:lt|:gt|#',parse[0]) else f'{parse[0]}:eq(0)'
        # FIXME 暂时不支持jsonpath那样的|| 分割取或属性
        if option:
            # print(f'parse:{parse}=>(option:{option})')
            if ':eq(-1)' in parse:
                # 处理 eq(-1)的情况,兼容性差，暂时只支持一层eq
                ret = doc(parse.replace(':eq(-1)','')).eq(-1)
            else:
                ret = doc(parse)
            # print(html)
            # FIXME 解析出来有多个的情况应该自动取第一个
            if option == 'Text':
                ret = ret.text()
            elif option == 'Html':
                ret = ret.html()
            else:
                ret = ret.attr(option) or ''
                if option.lower().find('style')>-1 and ret.find('url(')>-1:
                    try:
                        ret = re.search('url\((.*?)\)',ret,re.M|re.S).groups()[0]
                    except:
                        pass

                if ret and add_url:
                    # pd_list = 'url|src|href|data-original|data-src|data-play|data-url'.split('|')
                    # need_add = option in pd_list

                    need_add = re.search('(url|src|href|-original|-src|-play|-url)$', option, re.M | re.I)
                    # print(f'option:{option},need_add:{need_add}')
                    if need_add:
                        if 'http' in ret:
                            ret = ret[ret.find('http'):]
                        else:
                            ret = urljoin(self.MY_URL,ret)
                        # print(ret)
        else:
            # ret = doc(parse+':first')
            ret = doc(parse) # 由于是生成器,直接转str就能拿到第一条数据,不需要next
            # ret = ret.next()  # 取第一条数据
            # ret = doc(parse) # 下面注释的写法不对的
            # ret = ret.find(':first')
            # ret = ret.children(':first')
            # print(parse)
            # ret = str(ret)
            ret = ret.outerHtml()
        return ret

    def pdfa(self,html,parse:str):
        # 看官方文档才能解决这个问题!!!
        # https://pyquery.readthedocs.io/en/latest/api.html
        if not parse:
            return []
        if parse.find('&&') > -1:
            parse = parse.split('&&')  # 带&&的重新拼接
            # print(f"{parse[0]},{self.test(':eq|:lt|:gt', parse[0])}")
            parse = ' '.join([parse[i] if self.test(':eq|:lt|:gt', parse[i]) or i>=len(parse)-1 else f'{parse[i]}:eq(0)' for i in range(len(parse))])
        print(f'pdfa:{parse}')
        # print(html)
        if PARSE_CACHE:
            if self.pdfa_html != html:
                self.pdfa_html = html
                self.pdfa_doc = pq(html)
            doc = self.pdfa_doc
        else:
            doc = pq(html)
        result = doc(parse)
        # 节点转字符串
        # print(str(etree.tostring(result[0], pretty_print=True), 'utf-8'))
        # res = [item for item in result.items()]
        # print(res)
        res = [item.outerHtml() for item in result.items()] #  这个才是对的！！str() item str(etree.tostring 统统错误
        # res = [str(item) for item in result.items()]
        # res = [str(etree.tostring(item, pretty_print=True), 'utf-8') for item in result]
        # print(len(res),res)
        # print('pdfa执行结果数:',len(res))
        return res

    def pd(self,html,parse:str):
        return self.pdfh(html,parse,True)

    def pq(self,html:str):
        return pq(html)

    def pjfh(self,html,parse:str,add_url=False):
        if not parse:
            return ''
        if isinstance(html,str):
            # print(html)
            try:
               html = json.loads(html)
               # html = eval(html)
            except:
                print('字符串转json失败')
                return ''
        if not parse.startswith('$.'):
            parse = f'$.{parse}'
        ret = ''
        for ps in parse.split('||'):
            ret = jsonpath(html,ps)
            if isinstance(ret,list):
                ret = str(ret[0]) if ret[0] else ''
            else:
                ret = str(ret) if ret else ''
            if add_url and ret:
                ret = urljoin(self.MY_URL, ret)
            if ret:
                break
        # print(ret)
        return ret

    def pj(self, html, parse:str):
        return self.pjfh(html, parse, True)

    def pjfa(self,html,parse:str):
        if not parse:
            return []
        if isinstance(html,str):
            try:
               html = json.loads(html)
            except:
                return ''
        if not parse.startswith('$.'):
            parse = f'$.{parse}'
        # print(html)
        # print(parse)
        ret = jsonpath(html,parse)
        # print(ret)
        # print(type(ret))
        # print(type(ret[0]))
        # print(len(ret))
        if isinstance(ret,list) and isinstance(ret[0],list) and len(ret) == 1:
            # print('自动解包')
            ret  = ret[0] # 自动解包
        return ret or []

if __name__ == '__main__':
    import requests
    from parsel import Selector
    url = 'http://360yy.cn'
    jsp = jsoup(url)
    def pdfa2(html,parse):
        if not parse:
            return []
        if parse.find('&&') > -1:
            parse = parse.split('&&')  # 带&&的重新拼接
            # print(f"{parse[0]},{self.test(':eq|:lt|:gt', parse[0])}")
            # parse = ' '.join([parse[i] if self.test(':eq|:lt|:gt', parse[i]) or i>=len(parse)-1 else f'{parse[i]}:eq(0)' for i in range(len(parse))])
            parse = ' '.join([parse[i] if jsoup().test(':eq|:lt|:gt', parse[i]) or i>=len(parse)-1 else f'{parse[i]}:nth-child(1)' for i in range(len(parse))])
        # print(f'pdfa:{parse}')
        selector = Selector(text=html)
        print(parse)
        items = selector.css(parse)
        return [str(item) for item in items]
    r = requests.get(url)
    html = r.text
    # parsel 不好用啊,很难实现封装pdfa之类的函数
    items = pdfa2(html,'.fed-pops-navbar&&ul.fed-part-rows&&a')
    print(items)

