# coding=utf-8
# !/usr/bin/python
import sys

sys.path.append('..')
from base.spider import Spider
import json
import requests
import threading
import time

class Spider(Spider):

    def getName(self):
        return "哔哩哔哩"

    # 主页
    def homeContent(self, filter):
        result = {}
        cateManual = {
            #"动态": "动态",
            "推荐": "推荐",
            "热门": "热门",
            "排行榜": "排行榜",
            #"历史记录": "历史记录",
            # "稍后再看":"稍后再看",     #意义不大，隐藏该项
            #"收藏": "收藏",
            "每周必看": "每周必看",
            "频道": "频道",
            "动画": "1",
            "音乐": "3",
            "舞蹈": "129",
            "游戏": "4",
            "鬼畜": "119",
            "知识": "36",
            "科技": "188",
            "运动": "234",
            "生活": "160",
            "美食": "211",
            "动物": "217",
            "汽车": "223",
            "时尚": "155",
            "娱乐": "5",
            "影视": "181",
            "入站必刷": "入站必刷",
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
    userid = ''
    csrf = ''

    def getCookie(self):
        import http.cookies
        # ----↓↓↓↓↓↓↓----在下方raw_cookie_line后的双引号内填写----↓↓↓↓↓↓↓----
        raw_cookie_line = ""
        simple_cookie = http.cookies.SimpleCookie(raw_cookie_line)
        cookie_jar = requests.cookies.RequestsCookieJar()
        cookie_jar.update(simple_cookie)
        rsp = requests.session()
        rsp.cookies = cookie_jar
        url = 'http://api.bilibili.com/x/web-interface/nav'
        content = self.fetch(url, headers=self.header, cookies=rsp.cookies)
        res = json.loads(content.text)
        if res["code"] == 0:
            self.cookies = rsp.cookies
            self.userid = res["data"].get('mid')
            self.csrf = rsp.cookies['bili_jct']
        return cookie_jar

    def __init__(self):
        self.getCookie()
        url = 'https://api.bilibili.com/x/v3/fav/folder/created/list-all?up_mid=%s&jsonp=jsonp' % self.userid
        rsp = self.fetch(url, headers=self.header, cookies=self.cookies)
        content = rsp.text
        jo = json.loads(content)
        fav_list = []
        if jo['code'] == 0:
            for fav in jo['data'].get('list'):
                fav_dict = {
                    'n': fav['title'].replace("<em class=\"keyword\">", "").replace("</em>", "").replace("&quot;",
                                                                                                         '"').strip(),
                    'v': fav['id']}
                fav_list.append(fav_dict)
        if self.config["filter"].get('收藏'):
            for i in self.config["filter"].get('收藏'):
                if i['key'] == 'mlid':
                    i['value'] = fav_list

    def init(self, extend=""):
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

    # 将秒数转化为 时分秒的格式
    def second_to_time(self, a):
        if a < 3600:
            return time.strftime("%M:%S", time.gmtime(a))
        else:
            return time.strftime("%H:%M:%S", time.gmtime(a))

    # 字符串时分秒以及分秒形式转换成秒
    def str2sec(self, x):
        x = str(x)
        try:
            h, m, s = x.strip().split(':')  # .split()函数将其通过':'分隔开，.strip()函数用来除去空格
            return int(h) * 3600 + int(m) * 60 + int(s)  # int()函数转换成整数运算
        except:
            m, s = x.strip().split(':')  # .split()函数将其通过':'分隔开，.strip()函数用来除去空格
            return int(m) * 60 + int(s)  # int()函数转换成整数运算

    # 按时间过滤
    def filter_duration(self, vodlist, key):
        if key == '0':
            return vodlist
        else:
            vod_list_new = [i for i in vodlist if
                            self.time_diff1[key][0] <= self.str2sec(str(i["vod_remarks"])) < self.time_diff1[key][1]]
            return vod_list_new

    time_diff1 = {'1': [0, 300],
                  '2': [300, 900], '3': [900, 1800], '4': [1800, 3600],
                  '5': [3600, 99999999999999999999999999999999]
                  }
    time_diff = '0'

    dynamic_offset = ''

    def get_dynamic(self, pg):
        result = {}
        if str(pg) == '1':
            url = 'https://api.bilibili.com/x/polymer/web-dynamic/v1/feed/all?timezone_offset=-480&type=video&page=%s' % pg
        else:
            # print('偏移',self.dynamic_offset)
            url = 'https://api.bilibili.com/x/polymer/web-dynamic/v1/feed/all?timezone_offset=-480&type=video&offset=%s&page=%s' % (self.dynamic_offset, pg)
        rsp = self.fetch(url, headers=self.header, cookies=self.cookies)
        content = rsp.text
        jo = json.loads(content)
        if jo['code'] == 0:
            self.dynamic_offset = jo['data'].get('offset')
            videos = []
            vodList = jo['data']['items']
            for vod in vodList:
                up = vod['modules']["module_author"]['name']
                ivod = vod['modules']['module_dynamic']['major']['archive']
                aid = str(ivod['aid']).strip()
                title = ivod['title'].strip().replace("<em class=\"keyword\">", "").replace("</em>", "")
                img = ivod['cover'].strip()
                # remark = str(ivod['duration_text']).strip()
                remark = str(self.second_to_time(self.str2sec(ivod['duration_text']))).strip() + '  ' + str(
                    up).strip()  # 显示分钟数+up主名字
                videos.append({
                    "vod_id": aid,
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
        url = 'https://api.bilibili.com/x/web-interface/popular?ps=10&pn={0}&ps=9'.format(pg)
        rsp = self.fetch(url, headers=self.header, cookies=self.cookies)
        content = rsp.text
        jo = json.loads(content)
        if jo['code'] == 0:
            videos = []
            vodList = jo['data']['list']
            for vod in vodList:
                aid = str(vod['aid']).strip()
                title = vod['title'].strip().replace("<em class=\"keyword\">", "").replace("</em>", "")
                img = vod['pic'].strip()
                reason=vod['rcmd_reason']['content'].strip()
                if reason == '':
                    reason= ''
                else:
                    reason= '  ' + reason
                remark = "观看:" + self.zh(vod['stat']['view']) + "　" + str(self.second_to_time(vod['duration'])).strip()
                videos.append({
                    "vod_id": aid,
                    "vod_name": title,
                    "vod_pic": img + '@672w_378h_1c.jpg',
                    "vod_remarks": remark + reason
                })
            result['list'] = videos
            result['page'] = pg
            result['pagecount'] = 9999
            result['limit'] = 2
            result['total'] = 999999
        return result

    def get_rcmd(self, pg):
        result = {}
        url = 'https://api.bilibili.com/x/web-interface/index/top/feed/rcmd?y_num={0}&fresh_type=3&feed_version=SEO_VIDEO&fresh_idx_1h=1&fetch_row=1&fresh_idx=1&brush=0&homepage_ver=1&ps=10'.format(
            pg)
        rsp = self.fetch(url, headers=self.header, cookies=self.cookies)
        content = rsp.text
        jo = json.loads(content)
        if jo['code'] == 0:
            videos = []
            vodList = jo['data']['item']
            for vod in vodList:
                if vod['duration'] > 0:
                    aid = str(vod['id']).strip()
                    title = vod['title'].strip().replace("<em class=\"keyword\">", "").replace("</em>", "")
                    img = vod['pic'].strip()
                    if 'content' in vod['rcmd_reason']:
                        reason= '  ' + vod['rcmd_reason']['content'].strip()
                    else:
                        reason= ''
                    remark = "观看:" + self.zh(vod['stat']['view']) + "　" + str(self.second_to_time(vod['duration'])).strip()
                    videos.append({
                        "vod_id": aid,
                        "vod_name": title,
                        "vod_pic": img + '@672w_378h_1c.jpg',
                        "vod_remarks": remark + reason
                    })
            result['list'] = videos
            result['page'] = pg
            result['pagecount'] = 9999
            result['limit'] = 2
            result['total'] = 999999
        return result

    def get_rank(self, pg):
        ps=9
        pg_max= int(pg) * ps
        pg_min= pg_max - ps
        result = {}
        url = 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=0&type=all'
        rsp = self.fetch(url, headers=self.header, cookies=self.cookies)
        content = rsp.text
        jo = json.loads(content)
        if jo['code'] == 0:
            videos = []
            vodList = jo['data']['list']
            pc = int(len(vodList) / ps) + 1
            vodList = vodList[pg_min:pg_max]
            for vod in vodList:
                aid = str(vod['aid']).strip()
                title = vod['title'].strip().replace("<em class=\"keyword\">", "").replace("</em>", "")
                img = vod['pic'].strip()
                remark = "观看:" + self.zh(vod['stat']['view']) + "　" + str(self.second_to_time(vod['duration'])).strip()
                videos.append({
                    "vod_id": aid,
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

    def get_history(self, pg):
        result = {}
        url = 'https://api.bilibili.com/x/v2/history?pn=%s&ps=10' % pg
        rsp = self.fetch(url, headers=self.header, cookies=self.cookies)
        content = rsp.text
        jo = json.loads(content)  # 解析api接口,转化成json数据对象
        if jo['code'] == 0:
            videos = []
            vodList = jo['data']
            for vod in vodList:
                if vod['duration'] > 0:  # 筛选掉非视频的历史记录
                    aid = str(vod["aid"]).strip()
                    if 'redirect_url' in vod:
                        if 'bangumi' in vod['redirect_url']:
                            redirect_url = str(vod['redirect_url']).strip()
                            ep_id = redirect_url.split(r"/")[-1]
                            aid = ep_id.split(r"?")[0]
                    title = vod["title"].replace("<em class=\"keyword\">", "").replace("</em>", "").replace("&quot;",
                                                                                                            '"')
                    img = vod["pic"].strip()
                    # 获取已观看时间
                    if str(vod['progress']) == '-1':
                        process = str(self.second_to_time(vod['duration'])).strip()
                    else:
                        process = str(self.second_to_time(vod['progress'])).strip()
                    # 获取视频总时长
                    total_time = str(self.second_to_time(vod['duration'])).strip()
                    # 组合 已观看时间 / 总时长 ,赋值给 remark
                    remark = process + ' / ' + total_time
                    # 视频类型
                    type = str(vod["type"]).strip()
                    videos.append({
                        "vod_id": aid,
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

    def get_fav(self, pg, order, extend):
        mlid = ''
        fav_config = self.config["filter"].get('收藏')
        # 默认显示第一个收藏内容
        if fav_config:
            for i in fav_config:
                if i['key'] == 'mlid':
                    if len(i['value']) > 0:
                        mlid = i['value'][0]['v']
        # print(self.config["filter"].get('收藏'))
        if 'mlid' in extend:
            mlid = extend['mlid']
        if mlid:
            return self.get_fav_detail(pg=pg, mlid=mlid, order=order)
        else:
            return {}

    def get_fav_detail(self, pg, mlid, order):
        result = {}
        url = 'https://api.bilibili.com/x/v3/fav/resource/list?media_id=%s&order=%s&pn=%s&ps=10&platform=web&type=0' % (mlid, order, pg)
        rsp = self.fetch(url, headers=self.header, cookies=self.cookies)
        content = rsp.text
        jo = json.loads(content)
        if jo['code'] == 0:
            videos = []
            vodList = jo['data']['medias']
            for vod in vodList:
                # print(vod)
                # 只展示类型为 视频的条目
                # 过滤去掉收藏中的 已失效视频;如果不喜欢可以去掉这个 if条件
                if vod.get('type') in [2] and vod.get('title') != '已失效视频':
                    aid = str(vod['id']).strip()
                    title = vod['title'].replace("<em class=\"keyword\">", "").replace("</em>", "").replace("&quot;",
                                                                                                            '"')
                    img = vod['cover'].strip()
                    remark = "观看:" + self.zh(vod['cnt_info']['play']) + "　" + str(self.second_to_time(vod['duration'])).strip()
                    videos.append({
                        "vod_id": aid + '_mlid' + str(mlid),
                        "vod_name": title,
                        "vod_pic": img + '@672w_378h_1c.jpg',
                        "vod_remarks": remark
                    })
            # videos=self.filter_duration(videos, duration_diff)
            result['list'] = videos
            result['page'] = pg
            result['pagecount'] = 9999
            result['limit'] = 2
            result['total'] = 999999
        return result

    def get_up_info(self, mid, info):
        url = "https://api.bilibili.com/x/web-interface/card?mid={0}".format(mid)
        rsp = self.fetch(url, headers=self.header, cookies=self.cookies)
        jRoot = json.loads(rsp.text)
        jo = jRoot['data']['card']
        info['mid'] = mid
        info['name'] = jo['name'].replace("<em class=\"keyword\">", "").replace("</em>", "")
        info['face'] = jo['face']
        info['fans'] = self.zh(jo['fans'])
        info['like_num'] = self.zh(jRoot['data']['like_num'])
        info['vod_count'] = str(jRoot['data']['archive_count']).strip()
        info['desc'] = jo['Official']['desc'] + "　" + jo['Official']['title']
        if jRoot['data']['following'] == True:
            info['following'] = '已关注'
            info['followAct'] = 2
            info['followActName'] = '取消关注'
        else:
            info['following'] = '未关注'
            info['followAct'] = 1
            info['followActName'] = '关注'

    def get_zone(self, tid, pg):
        ps=9
        pg_max= int(pg) * ps
        pg_min= pg_max - ps
        result = {}
        url = 'https://api.bilibili.com/x/web-interface/ranking/v2?rid={0}&type=all'.format(tid)
        rsp = self.fetch(url, headers=self.header, cookies=self.cookies)
        content = rsp.text
        jo = json.loads(content)
        if jo['code'] == 0:
            videos = []
            vodList = jo['data']['list']
            pc = int(len(vodList) / ps) + 1
            vodList = vodList[pg_min:pg_max]
            for vod in vodList:
                aid = str(vod['aid']).strip()
                title = vod['title'].strip().replace("<em class=\"keyword\">", "").replace("</em>", "")
                img = vod['pic'].strip()
                remark = "观看:" + self.zh(vod['stat']['view']) + "　" + str(self.second_to_time(vod['duration'])).strip()
                videos.append({
                    "vod_id": aid,
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

    def get_weekly(self, pg):
        ps=9
        pg_max= int(pg) * ps
        pg_min= pg_max - ps
        result = {}
        url1 = 'https://api.bilibili.com/x/web-interface/popular/series/list'
        rsp1 = self.fetch(url1, headers=self.header, cookies=self.cookies)
        content1 = rsp1.text
        jo1 = json.loads(content1)
        number = jo1['data']['list'][0]['number']
        url = 'https://api.bilibili.com/x/web-interface/popular/series/one?number=' + str(number)
        rsp = self.fetch(url, headers=self.header, cookies=self.cookies)
        content = rsp.text
        jo = json.loads(content)
        if jo['code'] == 0:
            videos = []
            vodList = jo['data']['list']
            pc = int(len(vodList) / ps) + 1
            vodList = vodList[pg_min:pg_max]
            for vod in vodList:
                aid = str(vod['aid']).strip()
                title = vod['title'].strip()
                img = vod['pic'].strip()
                remark = "观看:" + self.zh(vod['stat']['view']) + "　" + str(self.second_to_time(vod['duration'])).strip()
                videos.append({
                    "vod_id": aid,
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

    def get_must_watch(self, pg):
        ps=9
        pg_max= int(pg) * ps
        pg_min= pg_max - ps
        result = {}
        url = 'https://api.bilibili.com/x/web-interface/popular/precious?page_size={0}&page={1}'.format(ps, pg)
        rsp = self.fetch(url, headers=self.header, cookies=self.cookies)
        content = rsp.text
        jo = json.loads(content)
        if jo['code'] == 0:
            videos = []
            vodList = jo['data']['list']
            pc = int(len(vodList) / ps) + 1
            vodList = vodList[pg_min:pg_max]
            for vod in vodList:
                aid = str(vod['aid']).strip()
                title = vod['title'].strip()
                img = vod['pic'].strip()
                remark = "观看:" + self.zh(vod['stat']['view']) + "　" + str(self.second_to_time(vod['duration'])).strip()
                videos.append({
                    "vod_id": aid,
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

    def get_toview(self, pg):
        ps=9
        pg_max= int(pg) * ps
        pg_min= pg_max - ps
        result = {}
        url = 'https://api.bilibili.com/x/v2/history/toview'
        rsp = self.fetch(url, headers=self.header, cookies=self.cookies)
        content = rsp.text
        jo = json.loads(content)  # 解析api接口,转化成json数据对象
        if jo['code'] == 0:
            videos = []
            vodList = jo['data']['list']
            pc = int(len(vodList) / ps) + 1
            vodList = vodList[pg_min:pg_max]
            for vod in vodList:
                if vod['duration'] > 0:
                    aid = str(vod["aid"]).strip()
                    title = vod["title"].replace("<em class=\"keyword\">", "").replace("</em>", "").replace("&quot;",
                                                                                                            '"')
                    img = vod["pic"].strip()
                    if str(vod['progress']) == '-1':
                        process = str(self.second_to_time(vod['duration'])).strip()
                    else:
                        process = str(self.second_to_time(vod['progress'])).strip()
                    # 获取视频总时长
                    total_time = str(self.second_to_time(vod['duration'])).strip()
                    # 组合 已观看时间 / 总时长 ,赋值给 remark
                    remark = process + ' / ' + total_time
                    videos.append({
                        "vod_id": aid + '&toview',
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

    chanel_offset = ''

    def get_channel(self, pg, cid, extend, order, duration_diff):
        result = {}
        url = 'https://api.bilibili.com/x/web-interface/search/type?search_type=video&keyword={0}&page={1}&duration={2}&order={3}&page_size=10'.format(
            cid, pg, duration_diff, order)
        rsp = self.fetch(url, headers=self.header, cookies=self.cookies)
        content = rsp.text
        jo = json.loads(content)
        if jo.get('code') == 0:
            videos = []
            vodList = jo['data']['result']
            for vod in vodList:
                aid = str(vod['aid']).strip()
                title = vod['title'].replace("<em class=\"keyword\">", "").replace("</em>", "").replace("&quot;", '"')
                img = 'https:' + vod['pic'].strip()
                remark = "观看:" + self.zh(vod['play']) + "　 " + str(self.second_to_time(self.str2sec(vod['duration']))).strip()
                videos.append({
                    "vod_id": aid,
                    "vod_name": title,
                    "vod_pic": img + '@672w_378h_1c.jpg',
                    "vod_remarks": remark
                })
            # videos=self.filter_duration(videos, duration_diff)
            result['list'] = videos
            result['page'] = pg
            result['pagecount'] = 9999
            result['limit'] = 2
            result['total'] = 999999
        return result

    def homeVideoContent(self):
        result = {}
        videos = self.get_rank(pg=1)['list'][0:3]
        result['list'] = videos
        return result

    def categoryContent(self, tid, pg, filter, extend):
        result = {}
        if len(self.cookies) <= 0:
            self.getCookie()
        if tid == "动态":
            return self.get_dynamic(pg=pg)
        elif tid == "热门":
            return self.get_hot(pg=pg)
        elif tid == '推荐':
            return self.get_rcmd(pg=pg)
        elif tid == "排行榜":
            return self.get_rank(pg=pg)
        elif tid == '历史记录':
            return self.get_history(pg=pg)
        elif tid == "每周必看":
            return self.get_weekly(pg=pg)
        elif tid == "入站必刷":
            return self.get_must_watch(pg=pg)
        elif tid == '稍后再看':
            return self.get_toview(pg=pg)
        elif tid in ("1", "3", "129", "4", "119", "36", "188", "234", "160", "211", "217", "223", "155", "5", "181"):
            return self.get_zone(tid=tid, pg=pg)

        elif tid == "收藏":
            order = 'mtime'
            if 'order' in extend:
                order = extend['order']
            return self.get_fav(pg=pg, order=order, extend=extend)

        elif tid == '频道':
            cid = '搞笑'
            if 'cid' in extend:
                cid = extend['cid']
            duration_diff = '0'
            if 'duration' in extend:
                duration_diff = extend['duration']
            order = 'totalrank'
            if 'order' in extend:
                order = extend['order']
            return self.get_channel(pg=pg, cid=cid, extend=extend, order=order, duration_diff=duration_diff)

        else:
            duration_diff = '0'
            if 'duration' in extend:
                duration_diff = extend['duration']
            order = 'totalrank'
            if 'order' in extend:
                order = extend['order']
            url = 'https://api.bilibili.com/x/web-interface/search/type?search_type=video&keyword={0}&page={1}&duration={2}&order={3}&page_size=10'.format(
                tid, pg, duration_diff, order)
            rsp = self.fetch(url, headers=self.header, cookies=self.cookies)
            content = rsp.text
            jo = json.loads(content)
            if jo.get('code') == 0:
                videos = []
                vodList = jo['data']['result']
                for vod in vodList:
                    aid = str(vod['aid']).strip()
                    title = vod['title'].replace("<em class=\"keyword\">", "").replace("</em>", "").replace("&quot;",
                                                                                                            '"')
                    img = 'https:' + vod['pic'].strip()
                    # remark = str(vod['duration']).strip()
                    remark = "观看:" + self.zh(vod['play']) + "　 " + str(self.second_to_time(self.str2sec(vod['duration']))).strip()
                    videos.append({
                        "vod_id": aid,
                        "vod_name": title,
                        "vod_pic": img + '@672w_378h_1c.jpg',
                        "vod_remarks": remark
                    })
                # videos=self.filter_duration(videos, duration_diff)
                result['list'] = videos
                result['page'] = pg
                result['pagecount'] = 9999
                result['limit'] = 2
                result['total'] = 999999
        return result

    def cleanSpace(self, str):
        return str.replace('\n', '').replace('\t', '').replace('\r', '').replace(' ', '')

    up_mid = ''

    def detailContent(self, array):
        aid = array[0]
        if not aid.isdigit() and not 'mlid' in aid:
            return self.ysContent(array)
        mlid = ''
        if 'mlid' in aid:
            aid = aid.split('_')
            mlid = aid[1].replace('mlid', '')
            aid = aid[0]
        url = "https://api.bilibili.com/x/web-interface/view?aid={0}".format(aid)
        rsp = self.fetch(url, headers=self.header, cookies=self.cookies)
        jRoot = json.loads(rsp.text)
        jo = jRoot['data']
        if 'redirect_url' in jo:
            if 'bangumi' in jo['redirect_url']:
                redirect_url = str(jo['redirect_url']).strip()
                ep_id = redirect_url.split(r"/")[-1]
                ep_id = ep_id.split(r"?")[0]
                new_array = []
                for i in array:
                    new_array.append(i)
                new_array[0] = ep_id
                return self.ysContent(new_array)
        self.up_mid = str(jo['owner']['mid'])
        info = {}
        self.get_up_info(self.up_mid, info)
        title = jo['title'].replace("<em class=\"keyword\">", "").replace("</em>", "")
        pic = jo['pic']
        up_name = jo['owner']['name']
        if not up_name in title:
            title += '【' + up_name + "】"
        desc = jo['desc']
        typeName = jo['tname']
        date = time.strftime("%Y%m%d", time.localtime(jo['pubdate']))  # 投稿时间本地年月日表示
        stat = jo['stat']
        # 演员项展示视频状态，包括以下内容：
        status = "播放: " + self.zh(stat['view']) + "　弹幕: " + self.zh(stat['danmaku']) + "　点赞: " + self.zh(stat['like']) + "　收藏: " + self.zh(stat['favorite']) + "　投币: " + self.zh(stat['coin'])
        remark = str(jo['duration']).strip()
        vod = {
            "vod_id": aid,
            "vod_name": title, 
            "vod_pic": pic,
            "type_name": typeName,
            "vod_year": date,
            "vod_area": "bilidanmu",
            "vod_remarks": remark,  # 不会显示
            'vod_tags': 'mv',  # 不会显示
            "vod_actor": status,
            'vod_director': up_name + '  ' + info['following'],
            "vod_content": desc,
            'vod_play_from': 'B站$$$做点什么'
            #'vod_play_from': 'B站'
        }
        ja = jo['pages']
        playUrl = ''
        for tmpJo in ja:
            cid = tmpJo['cid']
            part = tmpJo['part'].replace("#", "-")
            playUrl +=  '{0}${1}_{2}#'.format(part, aid, cid)
        follow = '关注UP$' + str(self.up_mid) + '_1_notplay_follow'
        unfollow = '取消关注$' + str(self.up_mid) + '_2_notplay_follow'
        like = '点赞$' + str(aid) + '_1_notplay_like'
        unlike = '取消点赞$' + str(aid) + '_2_notplay_like'
        coin1 = '投1币并点赞$' + str(aid) + '_1_notplay_coin'
        coin2 = '投2币并点赞$' + str(aid) + '_2_notplay_coin'
        fav = '收藏$' + str(aid) + '_0_notplay_fav'
        triple = '一键三连$' + str(aid) + '_notplay_triple'
        secondPList = [triple, like, coin1, coin2, fav, unlike]
        if mlid:
            favdel = '取消收藏$' + str(aid) + '_'+ str(mlid) + '_notplay_fav'
            secondPList.append(favdel)
        secondP = '#'.join(secondPList)
        vod['vod_play_url'] = playUrl + '$$$' +  secondP
        #vod['vod_play_url'] = playUrl
        
        if 'ugc_season' in jRoot['data']:
            season_title = jRoot['data']['ugc_season']['title'].replace("#", "-")
            sections = jRoot['data']['ugc_season']['sections']
            sec_len = len(sections)
            for section in sections:
                episodes = section['episodes']
                playUrl = ''
                for episode in episodes:
                    aid = episode['aid']
                    cid = episode['cid']
                    ep_title = episode['title'].replace("#", "-")
                    playUrl += '{0}${1}_{2}#'.format(ep_title, aid, cid)
                if sec_len > 1:
                    sec_title = season_title + section['title'].replace("#", "-")
                else:
                    sec_title = season_title
                vod['vod_play_from'] += '$$$' + sec_title
                vod['vod_play_url'] += '$$$' + playUrl
        
        result = {
            'list': [
                vod
            ]
        }
        return result

    con = threading.Condition()

    def get_season(self, n, nList, fromList, urlList, season_id, season_title):
        url = 'https://api.bilibili.com/pgc/view/web/season?season_id={0}'.format(season_id)
        try:
            rsp = self.fetch(url, headers=self.header, cookies=self.cookies)
            season = json.loads(rsp.text)
        except:
            with self.con:
                nList.remove(n)
                self.con.notifyAll()
            return
        episode = season['result']['episodes']
        if len(episode) == 0:
            with self.con:
                nList.remove(n)
                self.con.notifyAll()
            return
        playUrl = ''
        for tmpJo in episode:
            aid = tmpJo['aid']
            cid = tmpJo['cid']
            part = tmpJo['title'].replace("#", "-")
            if tmpJo['badge'] != '':
                part += '【' + tmpJo['badge'].replace("#", "-") + '】'
            part += tmpJo['long_title'].replace("#", "-")
            playUrl += '{0}${1}_{2}_bangumi#'.format(part, aid, cid)
        with self.con:
            while True:
                if n == nList[0]:
                    fromList.append(season_title)
                    urlList.append(playUrl)
                    nList.remove(n)
                    self.con.notifyAll()
                    break
                else:
                    self.con.wait()

    def ysContent(self, array):
        aid = array[0]
        if 'ep' in aid:
            aid = 'ep_id=' + aid.replace('ep', '')
        elif 'ss' in aid:
            aid = 'season_id=' + aid.replace('ss', '')
        else:
            aid = 'season_id=' + aid
        url = "https://api.bilibili.com/pgc/view/web/season?{0}".format(aid)
        rsp = self.fetch(url, headers=self.header, cookies=self.cookies)
        jRoot = json.loads(rsp.text)
        jo = jRoot['result']
        id = jo['season_id']
        title = jo['title']
        s_title = jo['season_title']
        pic = jo['cover']
        # areas = jo['areas']['name']  改bilidanmu显示弹幕
        typeName = jo['share_sub_title']
        date = jo['publish']['pub_time'][0:4]
        dec = jo['evaluate']
        remark = jo['new_ep']['desc']
        stat = jo['stat']
        # 演员和导演框展示视频状态，包括以下内容：
        status = "弹幕: " + self.zh(stat['danmakus']) + "　点赞: " + self.zh(stat['likes']) + "　投币: " + self.zh(
            stat['coins']) + "　追番追剧: " + self.zh(stat['favorites'])
        if 'rating' in jo:
            score = "评分: " + str(jo['rating']['score']) + '　' + jo['subtitle']
        else:
            score = "暂无评分" + '　' + jo['subtitle']
        vod = {
            "vod_id": id,
            "vod_name": title,
            "vod_pic": pic,
            "type_name": typeName,
            "vod_year": date,
            "vod_area": "bilidanmu",
            "vod_remarks": remark,
            "vod_actor": status,
            "vod_director": score,
            "vod_content": dec
        }
        playUrl = ''
        for tmpJo in jo['episodes']:
            aid = tmpJo['aid']
            cid = tmpJo['cid']
            part = tmpJo['title'].replace("#", "-")
            if tmpJo['badge'] != '':
                part += '【' + tmpJo['badge'].replace("#", "-") + '】'
            part += tmpJo['long_title'].replace("#", "-")
            playUrl += '{0}${1}_{2}_bangumi#'.format(part, aid, cid)
        fromList = []
        urlList = []
        if playUrl != '':
            fromList.append(s_title)
            urlList.append(playUrl)
        nList = []
        if len(jo['seasons']) > 1:
            n = 0
            for season in jo['seasons']:
                season_id = season['season_id']
                season_title = season['season_title']
                if season_id == id and len(fromList) > 0:
                    isHere = fromList.index(s_title)
                    fromList[isHere] = season_title
                    continue
                n +=1
                nList.append(n)
                t = threading.Thread(target=self.get_season, args=(n, nList, fromList, urlList, season_id, season_title, ))
                t.start()

        while True:
            _count = threading.active_count()
            #计算线程数，不出结果就调大，结果少了就调小
            if _count <= 2:
                break
        fromList.insert(1, '追番剧/不追')
        urlList.insert(1, '追番剧$' + str(id) + '_add_zhui#取消追番剧$' + str(id) + '_del_zhui')
        vod['vod_play_from'] = '$$$'.join(fromList)
        vod['vod_play_url'] = '$$$'.join(urlList)
        
        result = {
            'list': [
                vod
            ]
        }
        return result

    def searchContent(self, key, quick):
        url = 'https://api.bilibili.com/x/web-interface/search/type?search_type=video&keyword={0}&page=1'.format(key)
        rsp = self.fetch(url, cookies=self.cookies, headers=self.header)
        content = rsp.text
        jo = json.loads(content)
        if jo['code'] != 0:
            rspRetry = self.fetch(url, cookies=self.cookies, headers=self.header)
            content = rspRetry.text
        jo = json.loads(content)
        videos = []
        vodList = jo['data']['result']
        for vod in vodList:
            aid = str(vod['aid']).strip()
            title = vod['title'].replace("<em class=\"keyword\">", "").replace("</em>", "").replace("&quot;", '"') + '[' + key + ']'
            img = 'https:' + vod['pic'].strip()
            remark = str(self.second_to_time(self.str2sec(vod['duration']))).strip()
            videos.append({
                "vod_id": aid,
                "vod_name": title,
                "vod_pic": img + '@672w_378h_1c.jpg',
                "vod_remarks": remark
            })
        result = {
            'list': videos
        }
        return result

    def post_history(self, aid, cid):
        data= {'aid': str(aid), 'cid': str(cid), 'csrf': str(self.csrf)}
        url = 'http://api.bilibili.com/x/v2/history/report'
        self.post(url=url, headers=self.header, cookies=self.cookies, data=data)

    def do_follow(self, mid, act):
        data= {'fid': str(mid), 'act': str(act), 'csrf': str(self.csrf)}
        url = 'https://api.bilibili.com/x/relation/modify'
        self.post(url=url, headers=self.header, cookies=self.cookies, data=data)

    def do_like(self, aid, act):
        data= {'aid': str(aid), 'like': str(act), 'csrf': str(self.csrf)}
        url = 'https://api.bilibili.com/x/web-interface/archive/like'
        self.post(url=url, headers=self.header, cookies=self.cookies, data=data)

    def do_coin(self, aid, coin_num):
        data= {'aid': str(aid), 'multiply': str(coin_num), 'select_like': '1', 'csrf': str(self.csrf)}
        url = 'https://api.bilibili.com/x/web-interface/coin/add'
        self.post(url=url, headers=self.header, cookies=self.cookies, data=data)

    def do_fav(self, aid, act):
        data= {'rid': str(aid), 'type': '2', 'csrf': str(self.csrf)}
        if str(act) == '0':
            data['add_media_ids'] = '0'
        else:
            data['del_media_ids'] = str(act)
        url = 'https://api.bilibili.com/x/v3/fav/resource/deal'
        self.post(url=url, headers=self.header, cookies=self.cookies, data=data)

    def do_triple(self, aid):
        data= {'aid': str(aid), 'csrf': str(self.csrf)}
        url = 'https://api.bilibili.com/x/web-interface/archive/like/triple'
        self.post(url=url, headers=self.header, cookies=self.cookies, data=data)

    def do_zhui(self, season_id, act):
        data= {'season_id': str(season_id), 'csrf': str(self.csrf)}
        url = 'https://api.bilibili.com/pgc/web/follow/{0}'.format(act)
        self.post(url=url, headers=self.header, cookies=self.cookies, data=data)

    def playerContent(self, flag, id, vipFlags):
        if len(self.cookies) <= 0:
            self.getCookie()
        result = {}
        ids = id.split("_")
        if len(ids) < 2:
            return result
        elif len(ids) >= 2:
            aid = ids[0]
            cid = ids[1]
            if 'zhui' in ids:
                self.do_zhui(aid, cid)
                return result
            if 'follow' in ids:
                self.do_follow(aid, cid)
                return result
            if 'notplay' in ids:
                if 'like' in ids:
                    self.do_like(aid, cid)
                elif 'coin' in ids:
                    self.do_coin(aid, cid)
                elif 'fav' in ids:
                    self.do_fav(aid, cid)
                elif 'do_triple' in ids:
                    self.do_dislike(aid)
                return result
            if cid == 'cid':
                url = "https://api.bilibili.com/x/web-interface/view?aid=%s" % str(aid)
                rsp = self.fetch(url, headers=self.header, cookies=self.cookies)
                jRoot = json.loads(rsp.text)
                cid = jRoot['data']['cid']
            url = 'https://api.bilibili.com:443/x/player/playurl?avid={0}&cid={1}&qn=116'.format(aid, cid)
            if 'bangumi' in ids:
                url = 'https://api.bilibili.com/pgc/player/web/playurl?aid={0}&cid={1}&qn=116'.format(aid, cid)
        self.post_history(aid, cid)  # 回传播放历史记录
        rsp = self.fetch(url, cookies=self.cookies, headers=self.header)
        jRoot = json.loads(rsp.text)
        if jRoot['code'] == 0:
            if 'data' in jRoot:
                jo = jRoot['data']
            elif 'result' in jRoot:
                jo = jRoot['result']
            else:
                return result
        else:
            return result
        ja = jo['durl']
        maxSize = -1
        position = -1
        for i in range(len(ja)):
            tmpJo = ja[i]
            if maxSize < int(tmpJo['size']):
                maxSize = int(tmpJo['size'])
                position = i
        url = ''
        if len(ja) > 0:
            if position == -1:
                position = 0
            url = ja[position]['url']

        result["parse"] = 0
        result["playUrl"] = ''
        result["url"] = url
        result["header"] = {
            "Referer": "https://www.bilibili.com",
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
        }
        result["contentType"] = 'video/x-flv'
        return result

    config = {
        "player": {},
        "filter": {
            "关注": [{
                "key": "order",
                "name": "排序",
                "value": [
                    {
                        "n": "最常访问",
                        "v": "attention"
                    },
                    {
                        "n": "最近添加",
                        "v": ""
                    }
                ]
            }],
            "UP": [{
                "key": "order",
                "name": "排序",
                "value": [
                    {
                        "n": "最新发布",
                        "v": "pubdate"
                    },
                    {
                        "n": "最多播放",
                        "v": "click"
                    },
                    {
                        "n": "最多收藏",
                        "v": "stow"
                    },
                    {
                        "n": "最早发布",
                        "v": "oldest"
                    }
                ]
            }],
            "收藏": [{
                "key": "order",
                "name": "排序",
                "value": [
                    {
                        "n": "收藏时间",
                        "v": "mtime"
                    },
                    {
                        "n": "播放量",
                        "v": "view"
                    },
                    {
                        "n": "投稿时间",
                        "v": "pubtime"
                    }
                ]
            },
                {
                    "key": "mlid",
                    "name": "收藏分区",
                    "value": []
                }],

            "频道": [{
                "key": "order",
                "name": "排序",
                "value": [

                    {
                        "n": "综合排序",
                        "v": "totalrank"
                    },

                    {
                        "n": "最新发布",
                        "v": "pubdate"
                    },

                    {
                        "n": "最多点击",
                        "v": "click"
                    },
                    {
                        "n": "最多收藏",
                        "v": "stow"
                    },

                    {
                        "n": "最多弹幕",
                        "v": "dm"
                    },

                ]
            },
                {
                    "key": "duration",
                    "name": "时长",
                    "value": [{
                        "n": "全部",
                        "v": "0"
                    },
                        {
                            "n": "60分钟以上",
                            "v": "4"
                        },

                        {
                            "n": "30~60分钟",
                            "v": "3"
                        },
                        {
                            "n": "5~30分钟",
                            "v": "2"
                        },
                        {
                            "n": "5分钟以下",
                            "v": "1"
                        }
                    ]
                }, {"key": "cid", "name": "分类",
                    "value": [{'n': '搞笑', 'v': '搞笑'}, {'n': '美食', 'v': '美食'}, {'n': '鬼畜', 'v': '鬼畜'},
                              {'n': '美妆', 'v': '美妆'}, {'n': 'mmd', 'v': 'mmd'}, {'n': '科普', 'v': '科普'},
                              {'n': 'COSPLAY', 'v': 'COSPLAY'}, {'n': '漫展', 'v': '漫展'}, {'n': 'MAD', 'v': 'MAD'},
                              {'n': '手书', 'v': '手书'}, {'n': '穿搭', 'v': '穿搭'}, {'n': '发型', 'v': '发型'},
                              {'n': '化妆教程', 'v': '化妆教程'}, {'n': '电音', 'v': '电音'}, {'n': '欧美音乐', 'v': '欧美音乐'},
                              {'n': '中文翻唱', 'v': '中文翻唱'}, {'n': '洛天依', 'v': '洛天依'}, {'n': '翻唱', 'v': '翻唱'},
                              {'n': '日文翻唱', 'v': '日文翻唱'}, {'n': '科普', 'v': '科普'}, {'n': '技术宅', 'v': '技术宅'},
                              {'n': '历史', 'v': '历史'}, {'n': '科学', 'v': '科学'}, {'n': '人文', 'v': '人文'},
                              {'n': '科幻', 'v': '科幻'}, {'n': '手机', 'v': '手机'}, {'n': '手机评测', 'v': '手机评测'},
                              {'n': '电脑', 'v': '电脑'}, {'n': '摄影', 'v': '摄影'}, {'n': '笔记本', 'v': '笔记本'},
                              {'n': '装机', 'v': '装机'}, {'n': '课堂教育', 'v': '课堂教育'}, {'n': '公开课', 'v': '公开课'},
                              {'n': '演讲', 'v': '演讲'}, {'n': 'PS教程', 'v': 'PS教程'}, {'n': '编程', 'v': '编程'},
                              {'n': '英语学习', 'v': '英语学习'}, {'n': '喵星人', 'v': '喵星人'}, {'n': '萌宠', 'v': '萌宠'},
                              {'n': '汪星人', 'v': '汪星人'}, {'n': '大熊猫', 'v': '大熊猫'}, {'n': '柴犬', 'v': '柴犬'},
                              {'n': '田园犬', 'v': '田园犬'}, {'n': '吱星人', 'v': '吱星人'}, {'n': '美食', 'v': '美食'},
                              {'n': '甜点', 'v': '甜点'}, {'n': '吃货', 'v': '吃货'}, {'n': '厨艺', 'v': '厨艺'},
                              {'n': '烘焙', 'v': '烘焙'}, {'n': '街头美食', 'v': '街头美食'},
                              {'n': 'A.I.Channel', 'v': 'A.I.Channel'}, {'n': '虚拟UP主', 'v': '虚拟UP主'},
                              {'n': '神楽めあ', 'v': '神楽めあ'}, {'n': '白上吹雪', 'v': '白上吹雪'}, {'n': '婺源', 'v': '婺源'},
                              {'n': 'hololive', 'v': 'hololive'}, {'n': 'EXO', 'v': 'EXO'},
                              {'n': '防弹少年团', 'v': '防弹少年团'}, {'n': '肖战', 'v': '肖战'}, {'n': '王一博', 'v': '王一博'},
                              {'n': '易烊千玺', 'v': '易烊千玺'}, {'n': '赵今麦', 'v': '赵今麦'}, {'n': '宅舞', 'v': '宅舞'},
                              {'n': '街舞', 'v': '街舞'}, {'n': '舞蹈教学', 'v': '舞蹈教学'}, {'n': '明星舞蹈', 'v': '明星舞蹈'},
                              {'n': '韩舞', 'v': '韩舞'}, {'n': '古典舞', 'v': '古典舞'}, {'n': '旅游', 'v': '旅游'},
                              {'n': '绘画', 'v': '绘画'}, {'n': '手工', 'v': '手工'}, {'n': 'vlog', 'v': 'vlog'},
                              {'n': 'DIY', 'v': 'DIY'}, {'n': '手绘', 'v': '手绘'}, {'n': '综艺', 'v': '综艺'},
                              {'n': '国家宝藏', 'v': '国家宝藏'}, {'n': '脱口秀', 'v': '脱口秀'}, {'n': '日本综艺', 'v': '日本综艺'},
                              {'n': '国内综艺', 'v': '国内综艺'}, {'n': '人类观察', 'v': '人类观察'}, {'n': '影评', 'v': '影评'},
                              {'n': '电影解说', 'v': '电影解说'}, {'n': '影视混剪', 'v': '影视混剪'}, {'n': '影视剪辑', 'v': '影视剪辑'},
                              {'n': '漫威', 'v': '漫威'}, {'n': '超级英雄', 'v': '超级英雄'}, {'n': '影视混剪', 'v': '影视混剪'},
                              {'n': '影视剪辑', 'v': '影视剪辑'},
                              {'n': '诸葛亮', 'v': '诸葛亮'}, {'n': '韩剧', 'v': '韩剧'}, {'n': '王司徒', 'v': '王司徒'},
                              {'n': '泰剧', 'v': '泰剧'},
                              {'n': '郭德纲', 'v': '郭德纲'}, {'n': '相声', 'v': '相声'}, {'n': '张云雷', 'v': '张云雷'},
                              {'n': '秦霄贤', 'v': '秦霄贤'}, {'n': '孟鹤堂', 'v': '孟鹤堂'}, {'n': '岳云鹏', 'v': '岳云鹏'},
                              {'n': '假面骑士', 'v': '假面骑士'}, {'n': '特摄', 'v': '特摄'}, {'n': '奥特曼', 'v': '奥特曼'},
                              {'n': '迪迦奥特曼', 'v': '迪迦奥特曼'}, {'n': '超级战队', 'v': '超级战队'}, {'n': '铠甲勇士', 'v': '铠甲勇士'},
                              {'n': '健身', 'v': '健身'}, {'n': '篮球', 'v': '篮球'}, {'n': '体育', 'v': '体育'},
                              {'n': '帕梅拉', 'v': '帕梅拉'}, {'n': '极限运动', 'v': '极限运动'}, {'n': '足球', 'v': '足球'},
                              {'n': '星海', 'v': '星海'}, {'n': '张召忠', 'v': '张召忠'}, {'n': '航母', 'v': '航母'},
                              {'n': '航天', 'v': '航天'}, {'n': '导弹', 'v': '导弹'}, {'n': '战斗机', 'v': '战斗机'}]
                    }
            ],
        }
    }

    header = {
        "Referer": "https://www.bilibili.com",
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }

    def localProxy(self, param):

        return [200, "video/MP2T", action, ""]
