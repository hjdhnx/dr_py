#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : base_spider.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Author's Blog: https://blog.csdn.net/qq_32394351
# Date  : 2024/1/7

import os.path
import sys

sys.path.append('..')
try:
    # from base.spider import Spider as BaseSpider
    from base.spider import BaseSpider
except ImportError:
    from t4.base.spider import BaseSpider
import json
import time
import base64
import re
from pathlib import Path
import io
import tokenize
from urllib.parse import quote

"""
配置示例:
t4的配置里ext节点会自动变成api对应query参数extend,但t4的ext字符串不支持路径格式，比如./开头或者.json结尾
api里会自动含有ext参数是base64编码后的选中的筛选条件
 {
    "key":"hipy_t4_base_spider",
    "name":"base_spider(hipy_t4)",
    "type":4,
    "api":"http://192.168.31.49:5707/api/v1/vod/base_spider",
    "searchable":1,
    "quickSearch":0,
    "filterable":1,
    "ext":"base_spider"
},
{
    "key": "hipy_t3_base_spider",
    "name": "base_spider(hipy_t3)",
    "type": 3,
    "api": "{{host}}/txt/hipy/base_spider.py",
    "searchable": 1,
    "quickSearch": 0,
    "filterable": 1,
    "ext": "{{host}}/txt/hipy/base_spider.json"
},
"""


class Spider(BaseSpider):  # 元类 默认的元类 type
    def getName(self):
        return "规则名称如:基础示例"

    def init_api_ext_file(self):
        """
        这个函数用于初始化py文件对应的json文件，用于存筛选规则。
        执行此函数会自动生成筛选文件
        @return:
        """
        ext_file = __file__.replace('.py', '.json')
        print(f'ext_file:{ext_file}')
        ext_file_dict = {
            "分类1": [{"key": "letter", "name": "首字母", "value": [{"n": "A", "v": "A"}, {"n": "B", "v": "B"}]}],
            "分类2": [{"key": "letter", "name": "首字母", "value": [{"n": "A", "v": "A"}, {"n": "B", "v": "B"}]},
                      {"key": "year", "name": "年份",
                       "value": [{"n": "2024", "v": "2024"}, {"n": "2023", "v": "2023"}]}],
        }
        with open(ext_file, mode='w+', encoding='utf-8') as f:
            f.write(json.dumps(ext_file_dict, ensure_ascii=False))

    def init(self, extend=""):
        """
        初始化加载extend，一般与py文件名同名的json文件作为扩展筛选
        @param extend:
        @return:
        """

        def init_file(ext_file):
            """
            根据与py对应的json文件去扩展规则的筛选条件
            """
            ext_file = Path(ext_file).as_posix()
            if os.path.exists(ext_file):
                with open(ext_file, mode='r', encoding='utf-8') as f:
                    try:
                        ext_dict = json.loads(f.read())
                        self.config['filter'].update(ext_dict)
                    except Exception as e:
                        print(f'更新扩展筛选条件发生错误:{e}')

        ext = self.extend
        print(f"============ext:{ext},extend:{extend}============")
        if isinstance(ext, str) and ext:
            if ext.startswith('./'):
                ext_file = os.path.join(os.path.dirname(__file__), ext)
                init_file(ext_file)
            elif ext.startswith('http'):
                try:
                    r = self.fetch(ext)
                    self.config['filter'].update(r.json())
                except Exception as e:
                    print(f'更新扩展筛选条件发生错误:{e}')
            elif not ext.startswith('./') and not ext.startswith('http'):
                ext_file = os.path.join(os.path.dirname(__file__), './' + ext + '.json')
                init_file(ext_file)

        # 装载模块，这里只要一个就够了
        if isinstance(extend, list):
            for lib in extend:
                if '.Spider' in str(type(lib)):
                    self.module = lib
                    break

    def isVideoFormat(self, url):
        pass

    def manualVideoCheck(self):
        pass

    def homeContent(self, filterable=False):
        """
        获取首页分类及筛选数据
        @param filterable: 能否筛选，跟t3/t4配置里的filterable参数一致
        @return:
        """
        class_name = '电影&电视剧&综艺&动漫'  # 静态分类名称拼接
        class_url = '1&2&3&4'  # 静态分类标识拼接

        result = {}
        classes = []

        if all([class_name, class_url]):
            class_names = class_name.split('&')
            class_urls = class_url.split('&')
            cnt = min(len(class_urls), len(class_names))
            for i in range(cnt):
                classes.append({
                    'type_name': class_names[i],
                    'type_id': class_urls[i]
                })

        result['class'] = classes
        if filterable:
            result['filters'] = self.config['filter']
        return result

    def homeVideoContent(self):
        """
        首页推荐列表
        @return:
        """
        d = []
        d.append({
            'vod_name': '测试',
            'vod_id': 'index.html',
            'vod_pic': 'https://gitee.com/CherishRx/imagewarehouse/raw/master/image/13096725fe56ce9cf643a0e4cd0c159c.gif',
            'vod_remarks': '原始hipy',
        })
        result = {
            'list': d
        }
        return result

    def categoryContent(self, tid, pg, filterable, extend):
        """
        返回一级列表页数据
        @param tid: 分类id
        @param pg: 当前页数
        @param filterable: 能否筛选
        @param extend: 当前筛选数据
        @return:
        """
        page_count = 24  # 默认赋值一页列表24条数据

        d = []
        d.append({
            'vod_name': '测试',
            'vod_id': 'index.html',
            'vod_pic': 'https://gitee.com/CherishRx/imagewarehouse/raw/master/image/13096725fe56ce9cf643a0e4cd0c159c.gif',
            'vod_remarks': '类型:' + tid,
        })
        result = {
            'list': d,
            'page': pg,
            'pagecount': 9999 if len(d) >= page_count else pg,
            'limit': 90,
            'total': 999999,
        }
        return result

    def detailContent(self, ids):
        """
        返回二级详情页数据
        @param ids: 一级传过来的vod_id列表
        @return:
        """
        vod_id = ids[0]
        vod = {"vod_id": vod_id,
               "vod_name": '测试二级',
               "vod_pic": 'https://gitee.com/CherishRx/imagewarehouse/raw/master/image/13096725fe56ce9cf643a0e4cd0c159c.gif',
               "type_name": '详情页类型',
               "vod_year": '详情页年份',
               "vod_area": '详情页地区',
               "vod_remarks": '详情页标签',
               "vod_actor": '详情页演员名称',
               "vod_director": '详情页导演名称',
               "vod_content": '详情页剧情描述',
               "vod_play_from": '测试线路1$$$测试线路2',
               "vod_play_url": '选集播放1$1.mp4#选集播放2$2.mp4$$$选集播放3$3.mp4#选集播放4$4.mp4'}
        result = {
            'list': [vod]
        }
        return result

    def searchContent(self, wd, quick=False, pg=1):
        """
        返回搜索列表
        @param wd: 搜索关键词
        @param quick: 是否来自快速搜索。t3/t4配置里启用了快速搜索，在快速搜索在执行才会是True
        @return:
        """
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36",
            "Host": "www.bttwo.net",
            "Referer": "https://www.bttwo.net/"
        }

        url = f'https://www.bttwo.net/xssearch?q={quote(wd)}'
        r = self.fetch(url, headers=headers)
        cookies = ['myannoun=1']
        for key, value in r.headers.items():
            if str(key).lower() == 'set-cookie':
                cookies.append(value.split(';')[0])
        new_headers = {
            'Cookie': ';'.join(cookies),
            # 'Pragma': 'no-cache',
            # 'Origin': 'https://www.bttwo.net',
            # 'Referer': url,
            # 'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            # 'Sec-Ch-Ua-Mobile': '?0',
            # 'Sec-Ch-Ua-Platform': '"Windows"',
            # 'Sec-Fetch-Dest': 'document',
            # 'Sec-Fetch-Mode': 'navigate',
            # 'Sec-Fetch-Site': 'same-origin',
            # 'Sec-Fetch-User': '?1',
            # 'Upgrade-Insecure-Requests': '1',
        }
        headers.update(new_headers)
        print(headers)

        html = self.html(r.text)
        captcha = ''.join(html.xpath('//*[@class="erphp-search-captcha"]/form/text()')).strip()
        print('验证码:', captcha)
        answer = self.eval_computer(captcha)
        print('回答:', captcha, answer)
        data = {'result': str(answer)}
        print('待post数据:', data)
        self.post(url, data=data, headers=headers, cookies=None)
        r = self.fetch(url, headers=headers)
        # print(r.text)
        html = self.html(r.text)
        lis = html.xpath('//*[contains(@class,"search_list")]/ul/li')
        print('搜索结果数:', len(lis))
        d = []
        if len(lis) < 1:
            d.append({
                'vod_name': wd,
                'vod_id': 'index.html',
                'vod_pic': 'https://gitee.com/CherishRx/imagewarehouse/raw/master/image/13096725fe56ce9cf643a0e4cd0c159c.gif',
                'vod_remarks': '测试搜索',
            })
        else:
            for li in lis:
                d.append({
                    'vod_name': ''.join(li.xpath('h3//text()')),
                    'vod_id': ''.join(li.xpath('a/@href')),
                    'vod_pic': ''.join(li.xpath('a/img/@data-original')),
                    'vod_remarks': ''.join(li.xpath('p//text()')),
                })
        result = {
            'list': d
        }
        print(result)
        return result

    def playerContent(self, flag, id, vipFlags):
        """
        解析播放,返回json。壳子视情况播放直链或进行嗅探
        @param flag: vod_play_from 播放来源线路
        @param id: vod_play_url 播放的链接
        @param vipFlags: vip标识
        @return:
        """
        # url = 'http://bizcommon.alicdn.com/l2nDqpMmn6DGHnWzZQA/Cg9qI5imMInpPvK5Mnm%40%40hd.m3u8'
        url = 'https://s1.bfzycdn.com/video/renmindemingyi/%E7%AC%AC07%E9%9B%86/index.m3u8'
        parse = 0
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
        }
        result = {
            'parse': parse,  # 1=嗅探,0=播放
            'playUrl': '',  # 解析链接
            'url': url,  # 直链或待嗅探地址
            'header': headers,  # 播放UA
        }
        return result

    @staticmethod
    def adRemove():
        return 'reg:/video/adjump.*?ts'

    config = {
        "player": {},
        "filter": {}
    }
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36",
        "Host": "www.baidu.com",
        "Referer": "https://www.baidu.com/"
    }

    def localProxy(self, params):
        # http://192.168.31.49:5707/api/v1/vod/哔滴影视?proxy=1&do=py&type=1.m3u8
        print(params)
        content = """
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-ALLOW-CACHE:YES
#EXT-X-MEDIA-SEQUENCE:170471784
#EXT-X-TARGETDURATION:10
#EXT-X-PROGRAM-DATE-TIME:2024-01-11T20:43:53+08:00
#EXTINF:10.000, no desc
http://gctxyc.liveplay.myqcloud.com/gc/gllj01_1_md-170471784.ts
#EXT-X-PROGRAM-DATE-TIME:2024-01-11T20:44:03+08:00
#EXTINF:10.000, no desc
http://gctxyc.liveplay.myqcloud.com/gc/gllj01_1_md-170471785.ts
#EXT-X-PROGRAM-DATE-TIME:2024-01-11T20:44:13+08:00
#EXTINF:10.000, no desc
http://gctxyc.liveplay.myqcloud.com/gc/gllj01_1_md-170471786.ts
#EXT-X-PROGRAM-DATE-TIME:2024-01-11T20:44:23+08:00
#EXTINF:10.000, no desc
http://gctxyc.liveplay.myqcloud.com/gc/gllj01_1_md-170471787.ts
            """.strip()
        return [200, 'text/plain', content]
        # return [404, 'text/plain', 'Not Found']
        # return [200, "video/MP2T", content]
        # return [200, "video/MP2T", ""]

    # -----------------------------------------------自定义函数-----------------------------------------------
    def eval_computer(self, text):
        """
        自定义的字符串安全计算器
        @param text:字符串的加减乘除
        @return:计算后得到的值
        """
        localdict = {}
        self.safe_eval(f'ret={text.replace("=", "")}', localdict)
        ret = localdict.get('ret') or None
        return ret

    def safe_eval(self, code: str = '', localdict: dict = None):
        code = code.strip()
        if not code:
            return {}
        if localdict is None:
            localdict = {}
        builtins = __builtins__
        if not isinstance(builtins, dict):
            builtins = builtins.__dict__.copy()
        else:
            builtins = builtins.copy()
        for key in ['__import__', 'eval', 'exec', 'globals', 'dir', 'copyright', 'open', 'quit']:
            del builtins[key]  # 删除不安全的关键字
        # print(builtins)
        global_dict = {'__builtins__': builtins,
                       'json': json, 'print': print,
                       're': re, 'time': time, 'base64': base64
                       }  # 禁用内置函数,不允许导入包
        try:
            self.check_unsafe_attributes(code)
            exec(code, global_dict, localdict)
            return localdict
        except Exception as e:
            return {'error': f'执行报错:{e}'}

    # ==================== 静态函数 ======================
    @staticmethod
    def check_unsafe_attributes(string):
        """
        安全检测需要exec执行的python代码
        :param string:
        :return:
        """
        g = tokenize.tokenize(io.BytesIO(string.encode('utf-8')).readline)
        pre_op = ''
        for toktype, tokval, _, _, _ in g:
            if toktype == tokenize.NAME and pre_op == '.' and tokval.startswith('_'):
                attr = tokval
                msg = "access to attribute '{0}' is unsafe.".format(attr)
                raise AttributeError(msg)
            elif toktype == tokenize.OP:
                pre_op = tokval


if __name__ == '__main__':
    spider = Spider()
    spider.init()
    # spider.init_api_ext_file()  # 生成筛选对应的json文件
    spider.log({'key': 'value'})
    spider.log('====文本内容====')
    with open('test_1.txt', encoding='utf-8') as f:
        code = f.read()
        a = spider.superStr2dict(code)
        print(type(a), a)
    # spider.searchContent('斗罗大陆')
    print(spider.playerContent(None, 1, None))
    with open('ad.m3u8', encoding='utf-8') as f:
        adt = f.read()
    url = adt.split('\n')[0]
    adt = '\n'.join(adt.split('\n')[1:])
    ad_remove = 'reg:/video/adjump(.*?)ts'
    print(spider.fixAdM3u8(adt, url, ad_remove))
