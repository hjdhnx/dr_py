#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : 测试pdf.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/11/14

from utils.ua import MOBILE_UA
from utils.htmlParser import jsoup
import requests
from pyquery import PyQuery as pq


def main():
    r = requests.get('http://m.ysxs8.vip',headers={
        'User-Agent':MOBILE_UA
    })
    r.encoding = 'gb18030'
    html = r.text
    # print(html)

    jsp = jsoup(r.url)
    lis = jsp.pdfa(html,'.list-ul:eq(-1)')
    print(len(lis),lis)
    print(lis[0])
    a = jsp.pdfh(lis[0],'a&&li&&img&&alt')
    print(a)
    a = jsp.pdfh(lis[0], 'a&&li&&img&&data-original')
    print(a)
    a = jsp.pdfh(lis[0], 'a:eq(1)&&li&&Html')
    print(a)
    a = jsp.pdfh(lis[0], 'a:eq(1) li img')
    print(a)
    a = jsp.pd(lis[0], 'a:eq(1)&&li&&img&&src')
    print('src:',a)
    a = jsp.pd(lis[0], 'a&&href')
    print('href:', a)

def main1():
    url = 'https://www.lanhua.tv/voddetail/7420.html'
    r = requests.get(url, headers={
        'User-Agent': MOBILE_UA
    })
    # r.encoding = 'gb18030'
    html = r.text
    # print(html)

    jsp = jsoup(r.url)
    a = jsp.pdfh(html,'.content_min&&ul&&li:eq(2) a&&Text')
    print(a)
    a = jsp.pdfh(html, '.content_min&&ul&&li:eq(2)&&Text')
    print(a)

def main2():
    url = 'http://www.tvyb03.com/vod/detail/id/117659.html'
    r = requests.get(url, headers={
        'User-Agent': MOBILE_UA
    })
    html = r.text
    jsp = jsoup(r.url)
    a = jsp.pdfa(html, '.myui-panel__head h3')
    print(len(a))
    a = jsp.pdfa(html, '.myui-panel__head:eq(1) h3')
    print(len(a))
    a = jsp.pdfh(html,'h1&&Text')
    print(a)
    a = jsp.pdfh(html, 'h1')
    print(a)
    a = jsp.pdfa(html, 'h1')
    print(a)

def main3():
    html = """
    <div>
<p>内容1<span id='exd1'>我不获取的内容1</span><span id='exd2'>我不获取的内容2</span>内容2</p>
</div>
    """
    jsp = jsoup('https://www.cnblogs.com/lizhibk/p/8623543.html')
    a = jsp.pdfh(html, 'div p:eq(0)--span&&Text')
    print(a)
    a = jsp.pdfh(html,'div p--span&&Text')
    print(a)
    a = jsp.pdfh(html, 'div p:eq(0)--#exd1&&Text')
    print(a)
    a = jsp.pdfh(html, 'div p:eq(0)--#exd2&&Text')
    print(a)
    a = jsp.pdfh(html, 'div p:eq(0)--#exd2--#exd1&&Text')
    print(a)
    # a = jsp.pdfh(html, 'div p--#exd1&&Text')
    a = jsp.pdfh(html, 'div p--#exd1')
    print(a)
    a = jsp.pdfh(html, 'div p:first--#exd1')
    print(a)

    html = requests.get('https://www.leyupro.com/lyd/139451.html').text
    a = jsp.pdfa(html,'.yunplay&&.downtitle&&ul li')
    print(a)

def main4():
    a = '唐人街电影.html'
    a = '日常.html'
    with open(a,encoding='utf-8') as f:
        html = f.read()
    # print(html)
    二级 =  {"title": "h2&&Text;.content_detail.content_min.fl .data_style&&Text",
         "img": ".content_thumb .vodlist_thumb&&data-original",
         "desc": ".content_detail.content_min.fl li:eq(0)&&Text;.content_detail.content_min.fl li:eq(2)&&Text;.content_detail.content_min.fl li:eq(3)&&Text",
         "content": ".content&&Text", "tabs": ".play_source_tab:eq(0) a", "lists": ".content_playlist:eq(#id) li"}
    print(二级)
    jsp = jsoup('https://www.tangrenjie.tv/vod/detail/id/218945.html')
    # print(jsp.pdfa(html, 'h2'))
    # print('h2&&Text',jsp.pdfh(html, 'h2&&Text'))
    for i in 二级['title'].split(';'):
        print(i)
        print(jsp.pdfh(html,i))
    for i in 二级['desc'].split(';'):
        print(i)
        print(jsp.pdfh(html,i))

    for i in 二级['content'].split(';'):
        print(i)
        print(jsp.pdfh(html,i))

    for i in 二级['img'].split(';'):
        print(i)
        print(jsp.pd(html,i))
    print(jsp.pdfa(html,'.play_source_tab:eq(0) a'))
    print(jsp.pdfa(html,'#playlistbox&&.content_playlist:eq(1) li'))
    # doc = pq(html)
    # print(doc)
    # print('h2',doc.find('h2'))
    # print('h2',doc('.title'))
    # print('h2:',doc('h2'))
if __name__ == '__main__':
    # main()
    # main1()
    # main2()
    main3()
    # main4()