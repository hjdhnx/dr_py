#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : 喵次元.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Author's Blog: https://blog.csdn.net/qq_32394351
# Date  : 2024/1/17

import sys
import time

sys.path.append('..')
try:
    from base.spider import BaseSpider
except ImportError:
    from t4.base.spider import BaseSpider

"""
配置示例:
t4的配置里ext节点会自动变成api对应query参数extend,但t4的ext字符串不支持路径格式，比如./开头或者.json结尾
api里会自动含有ext参数是base64编码后的选中的筛选条件
 {
    "key":"hipy_t4_喵次元",
    "name":"喵次元(hipy_t4)",
    "type":4,
    "api":"http://192.168.31.49:5707/api/v1/vod/喵次元",
    "searchable":1,
    "quickSearch":0,
    "filterable":1,
    "ext":""
},
{
    "key": "hipy_t3_喵次元",
    "name": "喵次元(hipy_t3)",
    "type": 3,
    "api": "{{host}}/txt/hipy/喵次元.py",
    "searchable": 1,
    "quickSearch": 0,
    "filterable": 1,
    "ext": ""
},
"""

# 全局变量
gParam = {
    "HomeDict": {},
    "TypeDict": {},
}


class Spider(BaseSpider):  # 元类 默认的元类 type
    key: str = 'sLunqcoH85Nm/jDmFKns7A==        '
    key_str: str = 'sLunqcoH85Nm/jDmFKns7A=='
    iv: str = 'fedcba9876543210'
    token: str = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJBcHBUbyIsImlhdCI6MTcwMDA3MTcwMiwiZXhwIjoxNzMxNjA3NzAyLCJuYmYiOjE3MDAwNzE3MDIsInN1YiI6IkFwcFRvIiwianRpIjoiYzRjNTAzOTQxYTM4NWI1MDMyMTAyYmY3Yzk1OGY4MzEiLCJkYXRhIjp7InVzZXJfaWQiOjI0ODc1NCwidXNlcl9jaGVjayI6ImUzYmQ3NmNhNTJhMGY4NjAwMTdjNjdkZGUwN2QzZTM3IiwidXNlcl9uYW1lIjoiaGV6aWh1aSJ9fQ.4LWs3rNL-os8_Pqa9LgKtvVG5f0aIxVyAjYIagvO1F4'
    ic: str = 'bmXes2xsCWvsSdfYav0s9D78Ly7w1o%2BOYXApKx6SUd4NWKsTsapbS52l7y%2FsTVCM2kcoLws2jryaDQlHLse5fxD2B2VXZXfaQo0eMTOv2Xq7CKoPa51uVt8WiIY2SPztc7wxGE89%2Fcw2Q3n85uUT3A%3D%3D'
    api: str = 'https://cym.zhui.la/api.php'
    api_cofig: str = api + '/type/get_list'
    api_home: str = api + '/video/index'
    api_cate: str = api + '/video/get_list'
    api_search: str = api + '/video/get_list'
    api_detail: str = api + '/video/get_detail'
    api_tabs: str = api + '/video/get_player'
    api_parse: str = api + '/video/get_definition'
    params: dict = {"versionName": "5.6.9", "uuid": "9cc01079c64e2495", "version": "4835d0a2", "versionCode": "35"}

    def getName(self):
        return "喵次元"

    def init(self, extend=""):
        """
        初始化加载extend，一般与py文件名同名的json文件作为扩展筛选
        @param extend:
        @return:
        """
        ext = self.extend
        self.log(f'ext:{ext}')
        key = self.key_str
        # 转hex
        key_hex_str = self.bytesToHexString(key.encode('utf-8'))
        # 右侧补16个0
        key_hex_str += '0' * 16
        key_hex = key_hex_str
        # key_hex = '734C756E71636F4838354E6D2F6A446D464B6E7337413D3D0000000000000000'
        # 转回来
        key = self.hexStringTobytes(key_hex).decode('utf-8')
        self.key = key

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
        filter_names = {
            'class': '分类',
            'area': '地区',
            'lang': '语言',
            'year': '年份',
            'star': '明星',
            'director': '导演',
            'state': '状态',
            'version': '版本',
        }
        ret = self.fetch(self.api_cofig).json()
        data = self.decode(ret['data'])
        result = {}
        classes = []
        filters = {}
        type_dict = {}
        for tp in data.get('list') or []:
            classes.append({
                'type_name': tp['type_name'],
                'type_id': tp['type_id']
            })
            type_dict[str(tp['type_id'])] = tp['type_name']
            tp_filters = []
            for key, value in tp['type_extend'].items():
                if value:
                    tp_filters.append({
                        'key': key,
                        'name': filter_names.get(key) or key,
                        'value': [{'n': '全部', 'v': ''}] + [{'n': i, 'v': i} for i in value.split(',') if i]
                    })
            filters[tp['type_id']] = tp_filters

        result['class'] = classes
        if filterable:
            result['filters'] = filters
        global gParam
        gParam['HomeDict'].update(result)
        gParam['TypeDict'].update(type_dict)
        return result

    def homeVideoContent(self):
        """
        首页推荐列表
        @return:
        """
        ret = self.fetch(self.api_home).json()
        data = self.decode(ret['data'])
        # print(data)
        d = []
        for cate_data in data:
            items = cate_data['video']
            for item in items:
                d.append({
                    'vod_name': item['vod_name'],
                    'vod_id': item['vod_id'],
                    'vod_pic': item['vod_pic'],
                    'vod_remarks': item['vod_remarks'],
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
        page_count = 21  # 默认赋值一页列表21条数据|这个值一定要写正确看他默认一页多少条
        fls = extend.keys()  # 哪些刷新数据
        new_params = self.params.copy()
        new_params.update({'type_id': str(tid), 'limit': str(page_count), 'page': str(pg),
                           'orderby': '', 'ctime': str(int(time.time()))
                           })
        for fl in fls:
            new_params[f'vod_{fl}'] = extend[fl]

        params = self.get_sign_params(new_params)
        # print(params)
        r = self.postJson(self.api_cate, json=params)
        ret = r.json()
        data = self.decode(ret['data'])
        # print(data)
        d = data['list']
        result = {
            'list': d,
            'page': pg,
            'pagecount': 9999 if len(d) >= page_count else pg,
            'limit': 90,
            'total': data['count'],
        }
        return result

    def detailContent(self, ids):
        """
        返回二级详情页数据
        @param ids: 一级传过来的vod_id列表
        @return:
        """
        # id=110102
        vod_id = ids[0]
        new_params = self.params.copy()
        new_params.update({'vod_id': str(vod_id), 'ctime': str(int(time.time()))})
        params = self.get_sign_params(new_params)
        # print(params)
        r = self.postJson(self.api_detail, json=params)
        ret = r.json()
        data = self.decode(ret['data'])
        # print(data)
        vod = {"vod_id": vod_id,
               "vod_name": data['vod_name'],
               "vod_pic": data['vod_pic'],
               "type_name": data['vod_en'],
               "vod_year": data['vod_year'],
               "vod_area": data['vod_area'],
               "vod_remarks": data['vod_remarks'],
               "vod_actor": data['vod_actor'],
               "vod_director": data['vod_director'],
               "vod_content": data['vod_blurb'],
               }
        episodes = data['player']
        play_map = {}
        play_from = []
        play_list = []
        for ep in episodes:
            player = ep["code"]
            source = ep["name"]
            new_params = self.params.copy()
            new_params.update({
                'vod_id': str(vod_id), 'ctime': str(int(time.time())),
                'limit': str(5000), 'page': str(1),
                'player': player,
            })
            params = self.get_sign_params(new_params)
            r = self.postJson(self.api_tabs, json=params)
            ret = r.json()
            data = self.decode(ret['data'])
            # print(data)
            for playurl in data['list']:
                if source not in play_map:
                    play_map[source] = []
                play_map[source].append(
                    playurl["drama"] + "$" + '&'.join(
                        [str(playurl["ju_id"]), str(playurl["plyer"]), str(playurl["video_id"])]))

        for key, value in play_map.items():
            play_from.append(key)
            play_list.append('#'.join(value))

        vod['vod_play_from'] = '$$$'.join(play_from)
        vod['vod_play_url'] = '$$$'.join(play_list)
        result = {
            'list': [vod]
        }
        # print(vod)
        return result

    def searchContent(self, wd, quick=False, pg=1):
        """
        返回搜索列表
        @param wd: 搜索关键词
        @param quick: 是否来自快速搜索。t3/t4配置里启用了快速搜索，在快速搜索在执行才会是True
        @param pg: 页数
        @return:
        """
        page_count = 21  # 默认赋值一页列表21条数据|这个值一定要写正确看他默认一页多少条
        new_params = self.params.copy()
        new_params.update({
            'orderby': 'up', 'ctime': str(int(time.time())),
            'limit': str(page_count), 'page': str(pg), 'vod_name': str(wd)
        })
        params = self.get_sign_params(new_params)
        # print(params)
        r = self.postJson(self.api_cate, json=params)
        ret = r.json()
        data = self.decode(ret['data'])
        # print(data)
        d = data['list']
        result = {
            'list': d
        }
        return result

    def playerContent(self, flag, id, vipFlags):
        """
        解析播放,返回json。壳子视情况播放直链或进行嗅探
        @param flag: vod_play_from 播放来源线路
        @param id: vod_play_url 播放的链接
        @param vipFlags: vip标识
        @return:
        """
        _v = id.split('&')
        ju_id = _v[0]
        plyer = _v[1]
        video_id = _v[2]
        new_params = self.params.copy()
        new_params.update({
            'player_id': str(plyer), 'ctime': str(int(time.time())),
            'ju_id': str(ju_id), 'vod_id': str(video_id)
        })
        params = self.get_sign_params(new_params)
        # print(params)
        r = self.postJson(self.api_parse, json=params)
        ret = r.json()
        data = self.decode(ret['data'])
        # print(data)
        # 列表里第1条的分辨率最高
        url = data[0]['url']
        # print(url)

        """
        
        # 原始key
        key = 'sLunqcoH85Nm/jDmFKns7A=='
        # 转hex
        key_hex_str = self.bytesToHexString(key.encode('utf-8')).replace(' ', '')
        # 右侧补16个0
        key_hex_str += '0'*16
        key_hex = key_hex_str
        # key_hex = '734C756E71636F4838354E6D2F6A446D464B6E7337413D3D0000000000000000'
        # 转回来
        key = self.hexStringTobytes(key_hex).decode('utf-8')
        # print(key)
        iv = 'fedcba9876543210'
        
        """

        # key = self.key
        # iv = self.iv
        # input = self.aes_cbc_decode(url,key,iv)

        input = self.decode_aes(url)
        parse = 0
        result = {
            'parse': parse,  # 1=嗅探,0=播放
            'playUrl': '',  # 解析链接
            'url': input,  # 直链或待嗅探地址
            # 'header': headers,  # 播放UA
        }
        return result

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
        return [200, "video/MP2T", ""]

    # -----------------------------------------------自定义函数-----------------------------------------------
    def get_sign_params(self, params: dict):
        keys = list(params.keys())
        keys.sort()
        str_list = []
        for key in keys:
            if params.get(key):
                str_list.append(params[key])
        str_list.append('alskeuscli')
        sign = self.md5(''.join(str_list))
        params['sign'] = sign
        return params

    def decode(self, text):
        return text
        # return self.str2json(self.aes_cbc_decode(text, self.key, self.iv))

    def decode_aes(self, text):
        key = self.key
        iv = self.iv
        input = self.aes_cbc_decode(text, key, iv)
        return input


if __name__ == '__main__':
    # 在线aes测试 https://config.net.cn/tools/AES.html
    # 分类页:http://60.204.185.245:7090/appto/v1/home/cateData?id=1
    # 推荐页:http://60.204.185.245:7090/appto/v1/config/get?p=android
    from t4.core.loader import t4_spider_init

    spider = Spider()
    t4_spider_init(spider)
    # spider.init_api_ext_file()  # 生成筛选对应的json文件

    # print(spider.homeContent(True))
    # print(spider.homeVideoContent())
    # print(spider.categoryContent('23', 1, True, {'year': '2024'}))
    # print(spider.detailContent([7533]))
    # print(spider.searchContent('斗罗大陆'))
    print(spider.playerContent('线路J', '1&duoduan&7533', None))
    print(spider.playerContent('线路Z', '1&ziru&7533', None))
