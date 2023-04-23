# coding=utf-8
# !/usr/bin/python
import sys

sys.path.append('..')
from base.spider import Spider
import json

class Spider(Spider):
    def getDependence(self):
        return ['py_bilibili']

    def getName(self):
        return "哔哩直播"

    # 主页
    def homeContent(self, filter):
        result = {}
        cateManual = {
            "我的关注": "我的关注",
            "观看记录": "观看记录",
            "推荐": "推荐",
            "热门": "热门",
            "网游": "2",
            "手游": "3",
            "单机": "6",
            "娱乐": "1",
            "生活": "10",
            "知识": "11",
            "赛事": "13",
            "电台": "5",
            "虚拟": "9",

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

    def init(self, extend=""):
        self.bilibili = extend[0]
        print("============{0}============".format(extend))
        pass

    def isVideoFormat(self, url):
        pass

    def manualVideoCheck(self):
        pass

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

    uname = ''

    def get_live_userInfo(self, uid):
        url = 'https://api.live.bilibili.com/live_user/v1/Master/info?uid=%s' % uid
        rsp = self.fetch(url, headers=self.header, cookies=self.cookies)
        content = rsp.text
        jo = json.loads(content)
        if jo['code'] == 0:
            return jo['data']["info"]["uname"]

    def homeVideoContent(self,):
        result = {}
        videos = self.get_hot(1)['list'][0:3]
        result['list'] = videos
        return result

    def get_recommend(self, pg):
        result = {}
        url = 'https://api.live.bilibili.com/xlive/web-interface/v1/webMain/getList?platform=web&page=%s' % pg
        rsp = self.fetch(url, headers=self.header, cookies=self.cookies)
        content = rsp.text
        jo = json.loads(content)
        if jo['code'] == 0:
            videos = []
            vodList = jo['data']['recommend_room_list']
            for vod in vodList:
                aid = str(vod['roomid']).strip()
                title = vod['title'].replace("<em class=\"keyword\">", "").replace("</em>", "").replace("&quot;", '"')
                img = vod['keyframe'].strip()
                remark = vod['watched_show']['text_small'].strip() + "  " + vod['uname'].strip()
                videos.append({
                    "vod_id": aid + '&live',
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

    def get_hot(self, pg):
        result = {}
        url = 'https://api.live.bilibili.com/room/v1/room/get_user_recommend?page=%s&page_size=10' % pg
        rsp = self.fetch(url, headers=self.header, cookies=self.cookies)
        content = rsp.text
        jo = json.loads(content)
        if jo['code'] == 0:
            videos = []
            vodList = jo['data']
            for vod in vodList:
                aid = str(vod['roomid']).strip()
                title = vod['title'].replace("<em class=\"keyword\">", "").replace("</em>", "").replace("&quot;", '"')
                img = vod['user_cover'].strip()
                remark = vod['watched_show']['text_small'].strip() + "  " + vod['uname'].strip()
                videos.append({
                    "vod_id": aid + '&live',
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

    def get_live(self, pg, parent_area_id, area_id):
        result = {}
        url = 'https://api.live.bilibili.com/xlive/web-interface/v1/second/getList?platform=web&parent_area_id=%s&area_id=%s&sort_type=online&page=%s' % (
        parent_area_id, area_id, pg)
        rsp = self.fetch(url, headers=self.header, cookies=self.cookies)
        content = rsp.text
        jo = json.loads(content)
        if jo['code'] == 0:
            videos = []
            vodList = jo['data']['list']
            for vod in vodList:
                aid = str(vod['roomid']).strip()
                title = vod['title'].replace("<em class=\"keyword\">", "").replace("</em>", "").replace("&quot;", '"')
                img = vod.get('cover').strip()
                remark = vod['watched_show']['text_small'].strip() + "  " + vod['uname'].strip()
                videos.append({
                    "vod_id": aid + '&live',
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

    def get_fav(self, pg):
        result = {}
        url = 'https://api.live.bilibili.com/xlive/web-ucenter/v1/xfetter/GetWebList?page=%s&page_size=10' % pg
        rsp = self.fetch(url, headers=self.header, cookies=self.cookies)
        content = rsp.text
        jo = json.loads(content)
        videos = []
        vodList = jo['data']['rooms']
        for vod in vodList:
            aid = str(vod['room_id']).strip()
            title = vod['title'].replace("<em class=\"keyword\">", "").replace("</em>", "").replace("&quot;", '"')
            img = vod['cover_from_user'].strip()
            remark = vod['uname'].strip()
            videos.append({
                "vod_id": aid + '&live',
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

    def get_history(self):
        result = {}
        url = 'https://api.bilibili.com/x/web-interface/history/cursor?ps=21&type=live'
        rsp = self.fetch(url, headers=self.header, cookies=self.cookies)
        content = rsp.text
        jo = json.loads(content)
        if jo['code'] == 0:
            videos = []
            vodList = jo['data']['list']
            for vod in vodList:
                aid = str(vod['history']['oid']).strip()
                title = vod['title'].replace("<em class=\"keyword\">", "").replace("</em>", "").replace("&quot;", '"')
                img = vod['cover'].strip()
                remark = str(vod['live_status']).replace("0", "未开播").replace("1", "") +"  " + vod['author_name'].strip()
                videos.append({
                    "vod_id": aid + '&live',
                    "vod_name": title,
                    "vod_pic": img + '@672w_378h_1c.jpg',
                    "vod_remarks": remark
                })
            result['list'] = videos
            result['page'] = 1
            result['pagecount'] = 1
            result['limit'] = 90
            result['total'] = 999999
        return result

    def categoryContent(self, tid, pg, filter, extend):
        result = {}
        if len(self.cookies) <= 0:
            self.getCookie()
        if tid.isdigit():
            parent_area_id = tid
            area_id = 0
            if 'area_id' in extend:
                area_id = extend['area_id']
            return self.get_live(pg=pg, parent_area_id=parent_area_id, area_id=area_id)
        if tid == "推荐":
            return self.get_recommend(pg)
        if tid == "热门":
            return self.get_hot(pg)
        if tid == "我的关注":
            return self.get_fav(pg)
        if tid == "观看记录":
            return self.get_history()
        return result

    def cleanSpace(self, str):
        return str.replace('\n', '').replace('\t', '').replace('\r', '').replace(' ', '')

    def detailContent(self, array):
        arrays = array[0].split("&")
        room_id = arrays[0]
        url = "https://api.live.bilibili.com/room/v1/Room/get_info?room_id=%s" % room_id
        rsp = self.fetch(url, headers=self.header, cookies=self.cookies)
        jRoot = json.loads(rsp.text)
        if jRoot.get('code') == 0:
            jo = jRoot['data']
            title = jo['title'].replace("<em class=\"keyword\">", "").replace("</em>", "")
            pic = jo.get("user_cover")
            desc = jo.get('description')
            uid = str(jo["uid"])
            info = {}
            self.bilibili.get_up_info(uid, info)
            dire = self.get_live_userInfo(uid)
            self.bilibili.up_mid = uid
            typeName = jo['parent_area_name'] + '--' + jo['area_name']
            if jo['live_status'] == 0:
                live_status = "未开播"
            else:
                live_status = "开播时间：" + jo['live_time']
            remark = '在线人数:' + str(jo['online']).strip()
            vod = {
                "vod_id": room_id,
                "vod_name": title,
                "vod_pic": pic,
                "type_name": typeName,
                "vod_year": "",
                "vod_area": "bilidanmu",
                "vod_remarks": remark,
                "vod_actor": "关注：" + self.zh(jo.get('attention')) + "　房间号：" + room_id +  "　UID：" + uid,
                "vod_director": dire + '　　' + info['following'] + "　　" + live_status,
                "vod_content": desc,
            }
            playUrl = 'flv线路原画$platform=web&quality=4_' + room_id + '#flv线路高清$platform=web&quality=3_' + room_id + '#h5线路原画$platform=h5&quality=4_' + room_id + '#h5线路高清$platform=h5&quality=3_' + room_id

            vod['vod_play_from'] = 'B站$$$关注/取关'
            secondP = info['followActName'] + '$' + str(uid) + '_' + str(info['followAct']) + '_follow#'
            vod['vod_play_url'] = playUrl + '$$$' +  secondP
            result = {
                'list': [
                    vod
                ]
            }
        return result

    def searchContent(self, key, quick):
        url = 'https://api.bilibili.com/x/web-interface/search/type?search_type=live&keyword={0}&page=1'.format(key)
        if len(self.cookies) <= 0:
            self.getCookie()
        rsp = self.fetch(url, cookies=self.cookies, headers=self.header)
        content = rsp.text
        jo = json.loads(content)
        if jo['code'] != 0:
            rspRetry = self.fetch(url, cookies=self.cookies, headers=self.header)
            content = rspRetry.text
        jo = json.loads(content)
        videos1 = []
        if jo['data']['pageinfo']['live_room']['numResults'] != 0:
            vodList = jo['data']['result']['live_room']
            for vod in vodList:
                aid = str(vod['roomid']).strip()
                title = "直播间：" + vod['title'].strip().replace("<em class=\"keyword\">", "").replace("</em>", "") + "⇦" + key
                img = 'https:' + vod['user_cover'].strip()
                remark = vod['watched_show']['text_small'].strip() + "  " + vod['uname'].strip()
                videos1.append({
                    "vod_id": aid,
                    "vod_name": title,
                    "vod_pic": img + '@672w_378h_1c.jpg',
                    "vod_remarks": remark
                })
        videos2 = []
        if jo['data']['pageinfo']['live_user']['numResults'] != 0:
            vodList = jo['data']['result']['live_user']
            for vod in vodList:
                aid = str(vod['roomid']).strip()
                title = "直播间：" + vod['uname'].strip().replace("<em class=\"keyword\">", "").replace("</em>", "") + " ⇦" + key
                img = 'https:' + vod['uface'].strip()
                remark = str(vod['live_status']).replace("0", "未开播").replace("1", "") + "  关注：" + self.zh(vod['attentions'])
                videos2.append({
                    "vod_id": aid,
                    "vod_name": title,
                    "vod_pic": img + '@672w_378h_1c.jpg',
                    "vod_remarks": remark
                })
        videos = videos1 + videos2
        result = {
            'list': videos
        }
        return result

    def playerContent(self, flag, id, vipFlags):
        result = {}
        ids = id.split("_")
        if 'follow' in ids:
            self.bilibili.do_follow(ids[0], ids[1])
            return result
        url = 'https://api.live.bilibili.com/room/v1/Room/playUrl?cid=%s&%s' % (ids[1], ids[0])
        # raise Exception(url)
        if len(self.cookies) <= 0:
            self.getCookie()
        rsp = self.fetch(url, headers=self.header, cookies=self.cookies)
        jRoot = json.loads(rsp.text)
        if jRoot['code'] == 0:

            jo = jRoot['data']
            ja = jo['durl']

            url = ''
            if len(ja) > 0:
                url = ja[0]['url']

            result["parse"] = 0
            # result['type'] ="m3u8"
            result["playUrl"] = ''
            result["url"] = url
            result["header"] = {
                "Referer": "https://live.bilibili.com",
                "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
            }

            if "h5" in ids[0]:
                result["contentType"] = ''
            else:
                result["contentType"] = 'video/x-flv'
        return result

    config = {
        "player": {},
        "filter": {
            "1": [
                {
                    "key": "area_id",
                    "name": "全部分类",
                    "value": [
                        {
                            "n": "舞见",
                            "v": "207"
                        },
                        {
                            "n": "视频唱见",
                            "v": "21"
                        },
                        {
                            "n": "萌宅领域",
                            "v": "530"
                        },

                        {
                            "n": "视频聊天",
                            "v": "145"
                        },

                        {
                            "n": "情感",
                            "v": "706"
                        },
                        {
                            "n": "户外",
                            "v": "123"
                        },
                        {
                            "n": "日常",
                            "v": "399"
                        },
                    ]
                },
            ],
            "2": [
                {
                    "key": "area_id",
                    "name": "热门分类",
                    "value": [
                        {
                            "n": "英雄联盟",
                            "v": "86"
                        },
                        {
                            "n": "DOTA2",
                            "v": "92"
                        },
                        {
                            "n": "CS:GO",
                            "v": "89"
                        },

                        {
                            "n": "APEX英雄",
                            "v": "240"
                        },

                        {
                            "n": "永劫无间",
                            "v": "666"
                        },
                        {
                            "n": "穿越火线",
                            "v": "88"
                        },
                        {
                            "n": "守望先锋",
                            "v": "87"
                        },
                    ]
                },
            ],
            "3": [
                {
                    "key": "area_id",
                    "name": "热门分类",
                    "value": [
                        {
                            "n": "王者荣耀",
                            "v": "35"
                        },
                        {
                            "n": "和平精英",
                            "v": "256"
                        },
                        {
                            "n": "LOL手游",
                            "v": "395"
                        },

                        {
                            "n": "原神",
                            "v": "321"
                        },

                        {
                            "n": "第五人格",
                            "v": "163"
                        },
                        {
                            "n": "明日方舟",
                            "v": "255"
                        },
                        {
                            "n": "哈利波特：魔法觉醒",
                            "v": "474"
                        },
                    ]
                },
            ],
            "6": [
                {
                    "key": "area_id",
                    "name": "热门分类",
                    "value": [
                        {
                            "n": "主机游戏",
                            "v": "236"
                        },
                        {
                            "n": "战神",
                            "v": "579"
                        },
                        {
                            "n": "我的世界",
                            "v": "216"
                        },

                        {
                            "n": "独立游戏",
                            "v": "283"
                        },

                        {
                            "n": "怀旧游戏",
                            "v": "237"
                        },
                        {
                            "n": "大多数",
                            "v": "726"
                        },
                        {
                            "n": "弹幕互动玩法",
                            "v": "460"
                        },
                    ]
                },
            ],
            "5": [
                {
                    "key": "area_id",
                    "name": "全部分类",
                    "value": [
                        {
                            "n": "唱见电台",
                            "v": "190"
                        },
                        {
                            "n": "聊天电台",
                            "v": "192"
                        },
                        {
                            "n": "配音",
                            "v": "193"
                        },
                    ]
                },
            ],
            "9": [
                {
                    "key": "area_id",
                    "name": "全部分类",
                    "value": [
                        {
                            "n": "虚拟主播",
                            "v": "371"
                        },
                        {
                            "n": "3D虚拟主播",
                            "v": "697"
                        },
                    ]
                },
            ],
            "10": [
                {
                    "key": "area_id",
                    "name": "全部分类",
                    "value": [
                        {
                            "n": "生活分享",
                            "v": "646"
                        },
                        {
                            "n": "运动",
                            "v": "628"
                        },
                        {
                            "n": "搞笑",
                            "v": "624"
                        },

                        {
                            "n": "手工绘画",
                            "v": "627"
                        },

                        {
                            "n": "萌宠",
                            "v": "369"
                        },
                        {
                            "n": "美食",
                            "v": "367"
                        },
                        {
                            "n": "时尚",
                            "v": "378"
                        },
                        {
                            "n": "影音馆",
                            "v": "33"
                        },
                    ]
                },
            ],
            "11": [
                {
                    "key": "area_id",
                    "name": "全部分类",
                    "value": [
                        {
                            "n": "社科法律心理",
                            "v": "376"
                        },
                        {
                            "n": "人文历史",
                            "v": "702"
                        },
                        {
                            "n": "校园学习",
                            "v": "372"
                        },

                        {
                            "n": "职场·技能",
                            "v": "377"
                        },

                        {
                            "n": "科技",
                            "v": "375"
                        },
                        {
                            "n": "科学科普",
                            "v": "710"
                        },
                    ]
                },
            ],
            "13": [
                {
                    "key": "area_id",
                    "name": "全部分类",
                    "value": [
                        {
                            "n": "游戏赛事",
                            "v": "561"
                        },
                        {
                            "n": "体育赛事",
                            "v": "562"
                        },
                        {
                            "n": "赛事综合",
                            "v": "563"
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
