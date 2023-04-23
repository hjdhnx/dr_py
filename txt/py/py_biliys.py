# coding=utf-8
# !/usr/bin/python
import sys

sys.path.append('..')
from base.spider import Spider
import json
from requests import session, utils
import os
import time
import base64

class Spider(Spider):
    def getDependence(self):
        return ['py_bilibili']

    def getName(self):
        return "哔哩影视"

    def init(self, extend=""):
        self.bilibili = extend[0]
        print("============{0}============".format(extend))
        pass

    def isVideoFormat(self, url):
        pass

    def manualVideoCheck(self):
        pass

    # 主页
    def homeContent(self, filter):
        result = {}
        cateManual = {
            "番剧": "1",
            "国创": "4",
            "电影": "2",
            "电视剧": "5",
            "纪录片": "3",
            "综艺": "7",
            "全部": "全部",
            "时间表": "时间表",
            # ————————以下可自定义关键字，结果以影视类搜索展示————————
            # "喜羊羊": "喜羊羊"

        }
        classes = []
        for k in cateManual:
            classes.append({
                'type_name': k,
                'type_id': cateManual[k]
            })
        result['class'] = classes
        if (filter):
            result['filters'] = self.config['filter']
        return result

    # 用户cookies
    cookies = ''

    def getCookie(self):
        self.cookies = self.bilibili.getCookie()
        return self.cookies

    # 将超过10000的数字换成成以万和亿为单位
    def zh(self, num):
        if int(num) >= 100000000:
            p = round(float(num) / float(100000000), 1)
            p = str(p) + '亿'
        else:
            if int(num) >= 10000:
                p = round(float(num) / float(10000), 1)
                p = str(p) + '万'
            else:
                p = str(num)
        return p

    def homeVideoContent(self):
        result = {}
        videos = self.get_rank2(tid=4, pg=1)['list'][0:3]
        #videos = self.get_rank(tid=1, pg=1)['list'][0:5]
        #for i in [4, 2, 5, 3, 7]:
        #    videos += self.get_rank2(tid=i, pg=1)['list'][0:5]
        result['list'] = videos
        return result

    def get_rank(self, tid, pg):
        ps=9
        pg_max= int(pg) * ps
        pg_min= pg_max - ps
        result = {}
        url = 'https://api.bilibili.com/pgc/web/rank/list?season_type={0}&day=3'.format(tid)
        rsp = self.fetch(url, headers=self.header, cookies=self.cookies)
        content = rsp.text
        jo = json.loads(content)
        if jo['code'] == 0:
            videos = []
            vodList = jo['result']['list']
            pc = int(len(vodList) / ps) + 1
            vodList = vodList[pg_min:pg_max]
            for vod in vodList:
                aid = str(vod['season_id']).strip()
                title = vod['title'].strip()
                img = vod['cover'].strip()
                remark = ''
                if 'index_show' in vod['new_ep']:
                    remark = vod['new_ep']['index_show']
                videos.append({
                    "vod_id": 'ss' + aid,
                    "vod_name": title,
                    "vod_pic": img + '@672w_378h_1c.jpg',
                    "vod_remarks": remark
                })
            result['list'] = videos
            result['page'] = pg
            result['pagecount'] = pc
            result['limit'] = 2
            result['total'] = 999999
        return result

    def get_rank2(self, tid, pg):
        ps=9
        pg_max= int(pg) * ps
        pg_min= pg_max - ps
        result = {}
        url = 'https://api.bilibili.com/pgc/season/rank/web/list?season_type={0}&day=3'.format(tid)
        rsp = self.fetch(url, headers=self.header, cookies=self.cookies)
        content = rsp.text
        jo = json.loads(content)
        if jo['code'] == 0:
            videos = []
            vodList = jo['data']['list']
            pc = int(len(vodList) / ps) + 1
            vodList = vodList[pg_min:pg_max]
            for vod in vodList:
                aid = str(vod['season_id']).strip()
                title = vod['title'].strip()
                img = vod['cover'].strip()
                remark = ''
                if 'index_show' in vod['new_ep']:
                    remark = vod['new_ep']['index_show']
                videos.append({
                    "vod_id": 'ss' + aid,
                    "vod_name": title,
                    "vod_pic": img + '@672w_378h_1c.jpg',
                    "vod_remarks": remark
                })
            result['list'] = videos
            result['page'] = pg
            result['pagecount'] = pc
            result['limit'] = 2
            result['total'] = 999999
        return result

    def get_all(self, tid, pg, order, season_status, extend):
        result = {}
        if len(self.cookies) <= 0:
            self.getCookie()
        url = 'https://api.bilibili.com/pgc/season/index/result?order={2}&pagesize=10&type=1&season_type={0}&page={1}&season_status={3}'.format(tid, pg, order, season_status)
        rsp = self.fetch(url, headers=self.header, cookies=self.cookies)
        content = rsp.text
        jo = json.loads(content)
        videos = []
        vodList = jo['data']['list']
        for vod in vodList:
            aid = str(vod['season_id']).strip()
            title = vod['title']
            img = vod['cover'].strip()
            remark = vod['index_show'].strip()
            videos.append({
                "vod_id": 'ss' + aid,
                "vod_name": title,
                "vod_pic": img + '@672w_378h_1c.jpg',
                "vod_remarks": remark
            })
        result['list'] = videos
        result['page'] = pg
        result['pagecount'] = 9999
        result['limit'] = 2
        result['total'] = 999999
        return result

    def get_timeline(self, tid, pg):
        result = {}
        url = 'https://api.bilibili.com/pgc/web/timeline/v2?season_type={0}&day_before=2&day_after=4'.format(tid)
        rsp = self.fetch(url, headers=self.header, cookies=self.cookies)
        content = rsp.text
        jo = json.loads(content)
        if jo['code'] == 0:
            videos1 = []
            vodList = jo['result']['latest']
            for vod in vodList:
                aid = str(vod['season_id']).strip()
                title = vod['title'].strip()
                img = vod['cover'].strip()
                remark = vod['pub_index'] + '　' + vod['follows'].replace('系列', '')
                videos1.append({
                    "vod_id": 'ss' + aid,
                    "vod_name": title,
                    "vod_pic": img + '@672w_378h_1c.jpg',
                    "vod_remarks": remark
                })
            videos2 = []
            for i in range(0, 7):
                vodList = jo['result']['timeline'][i]['episodes']
                for vod in vodList:
                    if str(vod['published']) == "0":
                        aid = str(vod['season_id']).strip()
                        title = str(vod['title']).strip()
                        img = str(vod['cover']).strip()
                        date = str(time.strftime("%m-%d %H:%M", time.localtime(vod['pub_ts'])))
                        remark = date + "   " + vod['pub_index']
                        videos2.append({
                            "vod_id": 'ss' + aid,
                            "vod_name": title,
                            "vod_pic": img + '@672w_378h_1c.jpg',
                            "vod_remarks": remark
                        })
            result['list'] = videos2 + videos1
            result['page'] = 1
            result['pagecount'] = 1
            result['limit'] = 90
            result['total'] = 999999
        return result

    def categoryContent(self, tid, pg, filter, extend):
        result = {}
        if len(self.cookies) <= 0:
            self.getCookie()
        if tid == "1":
            return self.get_rank(tid=tid, pg=pg)
        elif tid in {"2", "3", "4", "5", "7"}:
            return self.get_rank2(tid=tid, pg=pg)
        elif tid == "全部":
            tid = '1'    # 全部界面默认展示最多播放的番剧
            order = '2'
            season_status = '-1'
            if 'tid' in extend:
                tid = extend['tid']
            if 'order' in extend:
                order = extend['order']
            if 'season_status' in extend:
                season_status = extend['season_status']
            return self.get_all(tid, pg, order, season_status, extend)
        elif tid == "时间表":
            tid = 1
            if 'tid' in extend:
                tid = extend['tid']
            return self.get_timeline(tid, pg)
        else:
            result = self.searchContent(key=tid,  quick="false")
        return result

    def cleanSpace(self, str):
        return str.replace('\n', '').replace('\t', '').replace('\r', '').replace(' ', '')

    def detailContent(self, array):
        return self.bilibili.ysContent(array)

    def searchContent(self, key, quick):
        if len(self.cookies) <= 0:
            self.getCookie()
        url1 = 'https://api.bilibili.com/x/web-interface/search/type?search_type=media_bangumi&keyword={0}'.format(
            key)  # 番剧搜索
        rsp1 = self.fetch(url1, headers=self.header, cookies=self.cookies)
        content1 = rsp1.text
        jo1 = json.loads(content1)
        rs1 = jo1['data']
        url2 = 'https://api.bilibili.com/x/web-interface/search/type?search_type=media_ft&keyword={0}'.format(
            key)  # 影视搜索
        rsp2 = self.fetch(url2, headers=self.header, cookies=self.cookies)
        content2 = rsp2.text
        jo2 = json.loads(content2)
        rs2 = jo2['data']
        videos = []
        if rs1['numResults'] == 0:
            vodList = jo2['data']['result']
        elif rs2['numResults'] == 0:
            vodList = jo1['data']['result']
        else:
            vodList = jo1['data']['result'] + jo2['data']['result']
        for vod in vodList:
            aid = str(vod['season_id']).strip()
            title = key + '➢' + vod['title'].strip().replace("<em class=\"keyword\">", "").replace("</em>", "")
            img = vod['cover'].strip()  # vod['eps'][0]['cover'].strip()原来的错误写法
            remark = vod['index_show']
            videos.append({
                "vod_id": 'ss' + aid,
                "vod_name": title,
                "vod_pic": img + '@672w_378h_1c.jpg',
                "vod_remarks": remark
            })
        result = {
            'list': videos
        }
        return result

    def playerContent(self, flag, id, vipFlags):
        return self.bilibili.playerContent(flag, id, vipFlags)

    config = {
        "player": {},
        "filter": {
            "全部": [
                {
                    "key": "tid",
                    "name": "分类",
                    "value": [{
                        "n": "番剧",
                        "v": "1"
                    },
                        {
                            "n": "国创",
                            "v": "4"
                        },

                        {
                            "n": "电影",
                            "v": "2"
                        },
                        {
                            "n": "电视剧",
                            "v": "5"
                        },
                        {
                            "n": "记录片",
                            "v": "3"
                        },
                        {
                            "n": "综艺",
                            "v": "7"
                        }

                    ]
                },
                {
                    "key": "order",
                    "name": "排序",
                    "value": [

                        {
                            "n": "播放数量",
                            "v": "2"
                        },

                        {
                            "n": "更新时间",
                            "v": "0"
                        },

                        {
                            "n": "最高评分",
                            "v": "4"
                        },
                        {
                            "n": "弹幕数量",
                            "v": "1"
                        },
                        {
                            "n": "追看人数",
                            "v": "3"
                        },

                        {
                            "n": "开播时间",
                            "v": "5"
                        },
                        {
                            "n": "上映时间",
                            "v": "6"
                        },

                    ]
                },
                {
                    "key": "season_status",
                    "name": "付费",
                    "value": [
                        {
                            "n": "全部",
                            "v": "-1"
                        },
                        {
                            "n": "免费",
                            "v": "1"
                        },

                        {
                            "n": "付费",
                            "v": "2%2C6"
                        },

                        {
                            "n": "大会员",
                            "v": "4%2C6"
                        },

                    ]
                },
            ],


            "时间表": [{
                "key": "tid",
                "name": "分类",
                "value": [

                    {
                        "n": "番剧",
                        "v": "1"
                    },

                    {
                        "n": "国创",
                        "v": "4"
                    },

                ]
            },
            ],
        }
    }


    header = {
        "Referer": "https://www.bilibili.com",
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }

    def localProxy(self, param):
        return [200, "video/MP2T", action, ""]
