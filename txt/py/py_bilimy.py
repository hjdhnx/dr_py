# coding=utf-8
# !/usr/bin/python
import sys

sys.path.append('..')
from base.spider import Spider
import json
import threading

class Spider(Spider):
    box_video_type = ''

    def getDependence(self):
        return ['py_bilibili']

    def getName(self):
        return "我的哔哩"

    def init(self, extend=""):
        self.bilibili = extend[0]
        print("============{0}============".format(extend))
        pass

    def isVideoFormat(self, url):
        pass

    def manualVideoCheck(self):
        pass

    def homeContent(self, filter):
        result = {}
        cateManual = {
            "动态": "动态",
            "UP": "UP",
            "关注": "关注",
            "追番": "追番",
            "追剧": "追剧",
            "收藏": "收藏",
            "历史记录": "历史记录",
            # ————————以下可自定义UP主，冒号后须填写UID————————
            #"虫哥说电影": "29296192",
            # ————————以下可自定义关键词，结果以搜索方式展示————————
            "周杰伦": "周杰伦",
            #"狗狗": "汪星人",
            #"猫咪": "喵星人",
        }
        classes = []
        for k in cateManual:
            classes.append({
                'type_name': k,
                'type_id': cateManual[k]
            })
        result['class'] = classes
        if (filter):
            filters = {}
            for lk in cateManual:
                if lk in self.bilibili.config['filter']:
                    filters.update({
                        cateManual[lk]: self.bilibili.config['filter'][lk]
                    })
                elif not cateManual[lk].isdigit():
                    link = cateManual[lk]
                    filters.update({
                        link: [{"key": "order", "name": "排序",
                                "value": [{"n": "综合排序", "v": "totalrank"}, {"n": "最新发布", "v": "pubdate"},
                                          {"n": "最多点击", "v": "click"}, {"n": "最多收藏", "v": "stow"},
                                          {"n": "最多弹幕", "v": "dm"}, ]},
                               {"key": "duration", "name": "时长",
                                "value": [{"n": "全部", "v": "0"}, {"n": "60分钟以上", "v": "4"},
                                          {"n": "30~60分钟", "v": "3"}, {"n": "5~30分钟", "v": "2"},
                                          {"n": "5分钟以下", "v": "1"}]}]
                    })
            result['filters'] = filters
        return result

    # 用户cookies，请在py_bilibili里填写，此处不用改
    cookies = ''
    userid = ''

    def getCookie(self):
        self.cookies = self.bilibili.getCookie()
        self.userid = self.bilibili.userid
        return self.cookies

    def homeVideoContent(self):
        result = {}
        videos = self.bilibili.get_dynamic(1)['list'][0:3]
        result['list'] = videos
        return result

    def get_follow(self, pg, order):
        if len(self.cookies) <= 0:
            self.getCookie()
        result = {}
        ps = 10
        url = 'https://api.bilibili.com/x/relation/followings?vmid={0}&order=desc&order_type={3}&ps={1}&pn={2}'.format(self.userid, ps, pg, order)
        rsp = self.fetch(url, headers=self.header, cookies=self.cookies)
        content = rsp.text
        jo = json.loads(content)
        follow = []
        for f in jo['data']['list']:
            mid = f['mid']
            title = str(f['uname']).strip()
            img = str(f['face']).strip()
            remark = ''
            if f['special'] == 1:
                remark = '特别关注'
            follow.append({
                "vod_id": str(mid) + '_mid',
                "vod_name": title,
                "vod_pic": img + '@672w_378h_1c.jpg',
                "vod_remarks": remark
            })
        total = jo['data']['total']
        pc = divmod(total, ps)
        if pc[1] != 0:
            pc = pc[0] + 1
        else:
            pc = pc[0]
        result['list'] = follow
        result['page'] = pg
        result['pagecount'] = pc
        result['limit'] = 2
        result['total'] = 999999
        return result

    def get_up_archive(self, pg, order):
        mid = self.bilibili.up_mid
        if mid.isdigit():
            return self.get_up_videos(mid, pg, order)
        else:
            return {}

    get_up_videos_mid = ''
    get_up_videos_pc = 1
    
    def get_up_videos(self, mid, pg, order):
        result = {}
        ps = 10
        order2 = ''
        if order == 'oldest':
            order2 = order
            order = 'pubdate'
        if order2 and int(pg) == 1:
            url = 'https://api.bilibili.com/x/space/arc/search?mid={0}&pn={1}&ps={2}&order={3}'.format(mid, pg, ps, order)
            rsp = self.fetch(url, headers=self.header, cookies=self.cookies)
            content = rsp.text
            jo = json.loads(content)
            if jo['code'] == 0:
                total = jo['data']['page']['count']
                pc = divmod(total, ps)
                if pc[1] != 0:
                    pc = pc[0] + 1
                else:
                    pc = pc[0]
                self.get_up_videos_mid = mid
                self.get_up_videos_pc = pc
        tmp_pg = pg
        if order2:
            tmp_pg = self.get_up_videos_pc - int(pg) + 1
        url = 'https://api.bilibili.com/x/space/arc/search?mid={0}&pn={1}&ps={2}&order={3}'.format(mid, tmp_pg, ps, order)
        rsp = self.fetch(url, headers=self.header, cookies=self.cookies)
        content = rsp.text
        jo = json.loads(content)
        if jo['code'] == 0:
            videos = []
            vodList = jo['data']['list']['vlist']
            for vod in vodList:
                aid = str(vod['aid']).strip()
                title = vod['title'].strip().replace("<em class=\"keyword\">", "").replace("</em>", "")
                img = vod['pic'].strip()
                remark = "观看:" + self.bilibili.zh(vod['play']) + "　 " + str(vod['length']).strip()
                videos.append({
                    "vod_id": aid,
                    "vod_name": title,
                    "vod_pic": img + '@672w_378h_1c.jpg',
                    "vod_remarks": remark
                })
            if order2:
                videos.reverse()
            if int(pg) == 1:
                info = {}
                self.bilibili.get_up_info(mid, info)
                gotoUPHome={
                    "vod_id": str(mid) + '_mid',
                    "vod_name": info['name'] + "  个人主页",
                    "vod_pic": info['face'] + '@672w_378h_1c.jpg',
                    "vod_remarks": info['following'] + '  投稿：' + str(info['vod_count'])
                }
                videos.insert(0, gotoUPHome)
            pc = self.get_up_videos_pc
            if self.get_up_videos_mid != mid:
                total = jo['data']['page']['count']
                pc = divmod(total, ps)
                if pc[1] != 0:
                    pc = pc[0] + 1
                else:
                    pc = pc[0]
                self.get_up_videos_mid = mid
                self.get_up_videos_pc = pc
            result['list'] = videos
            result['page'] = pg
            result['pagecount'] = pc
            result['limit'] = 2
            result['total'] = 999999
        return result

    def get_zhui(self, pg, mode):
        result = {}
        if len(self.cookies) <= 0:
            self.getCookie()
        url = 'https://api.bilibili.com/x/space/bangumi/follow/list?type={2}&pn={1}&ps=10&vmid={0}'.format(self.userid, pg, mode)
        rsp = self.fetch(url, headers=self.header, cookies=self.cookies)
        content = rsp.text
        jo = json.loads(content)
        videos = []
        vodList = jo['data']['list']
        for vod in vodList:
            aid = str(vod['season_id']).strip()
            title = vod['title']
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
        result['pagecount'] = 9999
        result['limit'] = 2
        result['total'] = 999999
        return result

    def categoryContent(self, tid, pg, filter, extend):
        if tid.isdigit():
            order = 'pubdate'
            if 'order' in extend:
                order = extend['order']
            return self.get_up_videos(tid, pg, order)
        elif tid == "关注":
            order = 'attention'
            if 'order' in extend:
                order = extend['order']
            return self.get_follow(pg, order)
        elif tid == "UP":
            order = 'pubdate'
            if 'order' in extend:
                order = extend['order']
            return self.get_up_archive(pg, order)
        elif tid == "追番":
            return self.get_zhui(pg, 1)
        elif tid == "追剧":
            return self.get_zhui(pg, 2)
        else:
            result = self.bilibili.categoryContent(tid, pg, filter, extend)
            return result

    def cleanSpace(self, str):
        return str.replace('\n', '').replace('\t', '').replace('\r', '').replace(' ', '')

    con = threading.Condition()

    def get_up_vod(self, mid, n, nList, urlList):
        # 获取UP主视频列表
        url = 'https://api.bilibili.com/x/space/arc/search?mid={0}&ps=50&pn={1}'.format(mid, n)
        try:
            rsp = self.fetch(url, headers=self.header, cookies=self.cookies)
            content = rsp.text
        except:
            with self.con:
                nList.remove(n)
                self.con.notifyAll()
            return
        jRoot = json.loads(content)
        jo = jRoot['data']['list']['vlist']
        if len(jo) == 0:
            with self.con:
                nList.remove(n)
                self.con.notifyAll()
            return
        playUrl = ''
        vodItems = []
        for tmpJo in jo:
            aid = tmpJo['aid']
            part = tmpJo['title'].replace("#", "-")
            url = '{0}${1}_cid'.format(part, aid)
            vodItems.append(url)
        playUrl = '#'.join(vodItems)
        with self.con:
            while True:
                if n == nList[0]:
                    urlList.append(playUrl)
                    nList.remove(n)
                    self.con.notifyAll()
                    break
                else:
                    self.con.wait()

    def detailContent(self, array):
        if 'mid' in array[0]:
            arrays = array[0].split("_")
            mid = arrays[0]
            self.bilibili.up_mid = mid
            info = {}
            i = threading.Thread(target=self.bilibili.get_up_info, args=(mid, info, ))
            i.start()
            #最多获取最近2页的投稿
            pn = 3
            urlList = []
            #nList = []
            #for n in range(pn):
            #    n += 1
            #    nList.append(n)
            #    with self.con:
            #        if threading.active_count() > 10:
            #            self.con.wait()
            #    t = threading.Thread(target=self.get_up_vod, args=(mid, n, nList, urlList, ))
            #    t.start()
            while True:
                _count = threading.active_count()
                #计算线程数，不出结果就调大，结果少了就调小
                if _count <= 2:
                    break
            vod = {
                "vod_id": mid,
                "vod_name": info['name'] + "  个人主页",
                "vod_pic": info['face'],
                "vod_area": "bilidanmu",
                "vod_remarks": "",  # 不会显示
                "vod_tags": 'mv',  # 不会显示
                "vod_actor": "粉丝数：" + info['fans'] + "　投稿数：" + info['vod_count'] + "　点赞数：" +info['like_num'],
                "vod_director": info['name'] + '　UID：' +str(mid) + "　" + info['following'],
                "vod_content": info['desc'],
                'vod_play_from': '更多视频在我的哔哩——UP标签，按上键刷新查看'
            }
            first = '点击相应按钮可以关注/取关$' + str(mid) + '_mid'
            follow = '关注$' + str(mid) + '_1_mid_follow'
            unfollow = '取消关注$' + str(mid) + '_2_mid_follow'
            doWhat = [first, follow, unfollow]
            urlList = doWhat + urlList
            vod['vod_play_url'] = '#'.join(urlList)

            result = {
                'list': [
                    vod
                ]
            }
            return result
        else:
            return self.bilibili.detailContent(array)

    def searchContent(self, key, quick):
        if len(self.cookies) <= 0:
            self.getCookie()
        url = 'https://api.bilibili.com/x/web-interface/search/type?search_type=bili_user&keyword={0}'.format(key)
        rsp = self.fetch(url, headers=self.header, cookies=self.cookies)
        content = rsp.text
        jo = json.loads(content)
        videos = []
        vodList = jo['data']['result']
        for vod in vodList:
            mid = str(vod['mid'])
            title = "UP主：" + vod['uname'].strip() + "  ☜" + key
            img = 'https:' + vod['upic'].strip()
            remark = "粉丝数" + self.bilibili.zh(vod['fans'])
            videos.append({
                "vod_id": mid + '_mid',
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
        }
    }

    header = {
        "Referer": "https://www.bilibili.com",
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }

    def localProxy(self, param):
        return [200, "video/MP2T", action, ""]
