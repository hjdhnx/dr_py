#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : 哔滴影视.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Author's Blog: https://blog.csdn.net/qq_32394351
# Date  : 2024/1/10

import os.path
import sys

sys.path.append('..')
try:
    # from base.spider import Spider as BaseSpider
    from base.spider import BaseSpider
except ImportError:
    from t4.base.spider import BaseSpider

import json
from pathlib import Path
import base64

"""
配置示例:
t4的配置里ext节点会自动变成api对应query参数extend,但t4的ext字符串不支持路径格式，比如./开头或者.json结尾
api里会自动含有ext参数是base64编码后的选中的筛选条件
 {
    "key":"hipy_t4_哔滴影视",
    "name":"哔滴影视(hipy_t4)",
    "type":4,
    "api":"http://192.168.31.49:5707/api/v1/vod/哔滴影视",
    "searchable":1,
    "quickSearch":0,
    "filterable":1,
    "ext":""
},
{
    "key": "hipy_t3_哔滴影视",
    "name": "哔滴影视(hipy_t3)",
    "type": 3,
    "api": "{{host}}/txt/hipy/哔滴影视.py",
    "searchable": 1,
    "quickSearch": 0,
    "filterable": 1,
    "ext": ""
},
"""


class Spider(BaseSpider):  # 元类 默认的元类 type

    api: str = 'https://www.bdys03.com/api/v1'

    javar = None

    def getDependence(self):
        return ['base_java_loader']

    def getName(self):
        return "哔滴影视"

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
        print(f"============{extend}============")
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
                    self.javar = lib
                    break

        if self.javar:
            jar_file = os.path.join(os.path.dirname(__file__), './jars/bdys.jar')
            jar_file = Path(jar_file).as_posix()
            self.javar.init_jar(jar_file)
            self.class1 = self.javar.jClass('com.C4355b')
            self.token = str(self.class1.getToken())
            self.headers.update({'token': self.token})

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
        class_name = '电影&电视剧&动漫&综艺'  # 静态分类名称拼接
        class_url = '0&1001&21&35'  # 静态分类标识拼接

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
        url = self.api + f'/category/{tid}/{pg}?type=0'
        r = self.fetch(url, headers=self.headers)
        ret = r.json()
        data = self.decode(ret['data'])
        # print(data)
        page_count = 24  # 默认赋值一页列表24条数据

        d = [{
            'vod_name': vod['movieName'],
            'vod_id': vod['id'],
            'vod_pic': vod['cdnCover'],
            'vod_remarks': vod['rank'],
            'vod_content': vod['title'],
        } for vod in data['list']]
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
        url = self.api + f'/detail/{vod_id}'
        r = self.fetch(url, headers=self.headers)
        ret = r.json()
        data = self.decode(ret['data'])
        print(data)

        vod = data['movie']
        playlist = data['playlist']
        titles = []
        plays = {}
        for p in playlist:  # 选集列表
            title = p['title']
            titles.append(title)
            if not plays.get(title):
                plays[title] = []
            # print(p)
            if p.get('tosId') and len(playlist) < 2:
                purl = self.api + '/playurl/' + str(p['id']) + '?type=' + str(p.get('tosId') or '0')
                print(purl)
                r = self.fetch(purl, headers=self.headers)
                ret = r.json()
                data = self.decode(ret['data'])
                print(data)
                url = data['url']
                plays[title].append({'name': '至尊线路', 'url': url})

            if p.get('url'):
                for p0 in p['url'].split(','):
                    plays[title].append(
                        {'name': p0.split('#')[1] if len(p0.split('#')) > 1 else '道长线路', 'url': p0.split('#')[0]})

            if p.get('url1'):
                for p1 in p['url1'].split(','):
                    plays[title].append(
                        {'name': p1.split('#')[1] if len(p1.split('#')) > 1 else '道长线路', 'url': p1.split('#')[0]})

            if p.get('url2'):
                for p2 in p['url2'].split(','):
                    plays[title].append(
                        {'name': p2.split('#')[1] if len(p2.split('#')) > 1 else '道长线路', 'url': p2.split('#')[0]})

        tabs = {}
        # key 选集列表 value是线路列表
        for key, value in plays.items():
            for tab in value:
                if not tab['name'] in tabs:
                    tabs[tab['name']] = []

                tabs[tab['name']].append(f"{key}${tab['url']}")

        vod_play_from = '$$$'.join(tabs.keys())

        vod_play_urls = []
        for key, value in tabs.items():
            vod_play_urls.append('#'.join(value))
        vod_play_url = '$$$'.join(vod_play_urls)

        vod = {"vod_id": vod_id,
               "vod_name": vod['title'],
               "vod_pic": vod['cdnCover'],
               "type_name": ','.join(vod['m_type']),
               "vod_year": '',
               "vod_area": vod['area'],
               "vod_remarks": f"{vod['movieName']} {vod['rank']}",
               "vod_actor": ','.join(vod['m_performer']),
               "vod_director": ','.join(vod['m_director']),
               "vod_content": vod['intro'],
               "vod_play_from": vod_play_from,
               "vod_play_url": vod_play_url}
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
        url = self.api + f'/search/{wd}/{pg}'
        r = self.fetch(url, headers=self.headers)
        ret = r.json()
        data = self.decode(ret['data'])
        print(data)
        d = []
        for li in data['list']:
            d.append({
                'vod_name': li['movieName'],
                'vod_id': li['id'],
                'vod_pic': li['cdnCover'],
                'vod_remarks': li['curEp'],
                'vod_content': li['intro'],
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
        url = id
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
        }
        if 'm3u8' not in url:
            parse = 0
        else:
            parse = 1
        result = {
            'parse': parse,  # 1=嗅探,0=播放
            'playUrl': '',  # 解析链接
            'url': url,  # 直链或待嗅探地址
            'header': headers,  # 播放UA
        }
        return result

    config = {
        "player": {},
        "filter": {}
    }
    headers = {
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 7.0; HUAWEI MLA-AL10 Build/HUAWEIMLA-AL10)",
        "token": ""
    }

    def localProxy(self, param):
        return [200, "video/MP2T", action, ""]

    # -----------------------------------------------自定义函数-----------------------------------------------
    def decode(self, text):
        bt = base64.b64decode(text)
        res = self.class1.dec(bt)
        return self.str2json(str(res))


if __name__ == '__main__':
    from t4.core.loader import t4_spider_init

    spider = Spider()
    t4_spider_init(spider)
    # spider.init_api_ext_file()  # 生成筛选对应的json文件
    # spider.log({'key': 'value'})
    # spider.log('====文本内容====')
    # print(spider.homeContent(True))
    # print(spider.homeVideoContent())
    # print(spider.categoryContent('0', 1, False, None))
    # print(spider.detailContent([24420]))
    spider.searchContent('斗罗大陆')
