# coding=utf-8
# !/usr/bin/python
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
from urllib import request, parse
from pathlib import Path
import urllib
import urllib.request

"""
配置示例:
t4的配置里ext节点会自动变成api对应query参数extend,但t4的ext字符串不支持路径格式，比如./开头或者.json结尾
api里会自动含有ext参数是base64编码后的选中的筛选条件

错误示例,ext含有json:
{
    "key":"hipy_cntv央视",
    "name":"cntv央视(hipy_t4)",
    "type":4,
    "api":"http://192.168.31.49:5707/api/v1/vod/cntv央视?api_ext={{host}}/txt/hipy/cntv央视.json",
    "searchable":1,
    "quickSearch":1,
    "filterable":0,
    "ext":"cntv央视.json"
 }
 正确示例。同时存在ext和api_ext会优先取ext作为extend加载init
 {
    "key":"hipy_t4_cntv央视",
    "name":"cntv央视(hipy_t4)",
    "type":4,
    "api":"http://192.168.31.49:5707/api/v1/vod/cntv央视?api_ext={{host}}/txt/hipy/cntv央视.json",
    "searchable":1,
    "quickSearch":0,
    "filterable":1,
    "ext":"cntv央视"
 },
 {
    "key": "hipy_t3_cntv央视",
    "name": "cntv央视(hipy_t3)",
    "type": 3,
    "api": "{{host}}/txt/hipy/cntv央视.py",
    "searchable": 1,
    "quickSearch": 0,
    "filterable": 1,
    "ext": "{{host}}/txt/hipy/cntv央视.json"
},
"""


class Spider(BaseSpider):  # 元类 默认的元类 type
    module = None

    def getDependence(self):
        return ['base_spider']

    def getName(self):
        return "中央电视台"  # 可搜索

    def init_api_ext_file(self):
        ext_file = __file__.replace('.py', '.json')
        print(f'ext_file:{ext_file}')
        # 特别节目网页: https://tv.cctv.com/yxg/index.shtml?spm=C28340.PlFTqGe6Zk8M.E2PQtIunpEaz.65
        # 特别节目分类筛选获取页面: https://tv.cctv.com/yxg/tbjm/index.shtml
        # 纪录片网页: https://tv.cctv.com/yxg/index.shtml?spm=C28340.PlFTqGe6Zk8M.E2PQtIunpEaz.65
        # 纪录片分类筛选获取页面:https://tv.cctv.com/yxg/jlp/index.shtml
        # ==================== 获取特别节目的筛选条件 ======================
        r = self.fetch('https://tv.cctv.com/yxg/tbjm/index.shtml')
        html = r.text
        html = self.html(html)

        filter_tbjm = []
        lis = html.xpath('//*[@id="pindao"]/li')
        li_value = []
        for li in lis:
            li_value.append({
                'n': ''.join(li.xpath('./span//text()')),
                'v': ''.join(li.xpath('@datacd')),
            })
        # print(li_value)
        filter_tbjm.append({
            "key": "datapd-channel",
            "name": "频道",
            "value": li_value
        })

        lis = html.xpath('//*[@id="fenlei"]/li')
        li_value = []
        for li in lis:
            li_value.append({
                'n': ''.join(li.xpath('./span//text()')),
                'v': ''.join(li.xpath('@datalx')),
            })
        # print(li_value)
        filter_tbjm.append({
            "key": "datafl-sc",
            "name": "类型",
            "value": li_value
        })

        lis = html.xpath('//*[@id="zimu"]/li')
        li_value = []
        for li in lis:
            li_value.append({
                'n': ''.join(li.xpath('./span//text()')),
                'v': ''.join(li.xpath('@datazm')),
            })
        # print(li_value)
        filter_tbjm.append({
            "key": "dataszm-letter",
            "name": "首字母",
            "value": li_value
        })

        print(filter_tbjm)

        # ==================== 纪录片筛选获取 ======================
        r = self.fetch('https://tv.cctv.com/yxg/jlp/index.shtml')
        html = r.text
        html = self.html(html)

        filter_jlp = []
        lis = html.xpath('//*[@id="pindao"]/li')
        li_value = []
        for li in lis:
            li_value.append({
                'n': ''.join(li.xpath('./span//text()')),
                'v': ''.join(li.xpath('@datacd')),
            })
        # print(li_value)
        filter_jlp.append({
            "key": "datapd-channel",
            "name": "频道",
            "value": li_value
        })

        lis = html.xpath('//*[@id="fenlei"]/li')
        li_value = []
        for li in lis:
            li_value.append({
                'n': ''.join(li.xpath('./span//text()')),
                'v': ''.join(li.xpath('@datalx')),
            })
        # print(li_value)
        filter_jlp.append({
            "key": "datafl-sc",
            "name": "类型",
            "value": li_value
        })

        lis = html.xpath('//*[@id="nianfen"]/li')
        li_value = []
        for li in lis:
            li_value.append({
                'n': ''.join(li.xpath('./span//text()')),
                'v': ''.join(li.xpath('@datanf')),
            })
        # print(li_value)
        filter_jlp.append({
            "key": "datanf-year",
            "name": "年份",
            "value": li_value
        })

        lis = html.xpath('//*[@id="zimu"]/li')
        li_value = []
        for li in lis:
            li_value.append({
                'n': ''.join(li.xpath('./span//text()')),
                'v': ''.join(li.xpath('@datazm')),
            })
        # print(li_value)
        filter_jlp.append({
            "key": "dataszm-letter",
            "name": "首字母",
            "value": li_value
        })

        print(filter_jlp)

        ext_file_dict = {
            "特别节目": filter_tbjm,
            "纪录片": filter_jlp,
        }

        # print(json.dumps(ext_file_dict,ensure_ascii=False,indent=4))
        with open(ext_file, mode='w+', encoding='utf-8') as f:
            # f.write(json.dumps(ext_file_dict,ensure_ascii=False,indent=4))
            f.write(json.dumps(ext_file_dict, ensure_ascii=False))

    def init(self, extend=""):
        def init_file(ext_file):
            ext_file = Path(ext_file).as_posix()
            # print(f'ext_file:{ext_file}')
            if os.path.exists(ext_file):
                # print('存在扩展文件')
                with open(ext_file, mode='r', encoding='utf-8') as f:
                    try:
                        ext_dict = json.loads(f.read())
                        # print(ext_dict)
                        self.config['filter'].update(ext_dict)
                    except Exception as e:
                        print(f'更新扩展筛选条件发生错误:{e}')

        print("============依赖列表:{0}============".format(extend))
        ext = self.extend
        print("============ext:{0}============".format(ext))
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

    def homeContent(self, filter):
        result = {}
        cateManual = {
            "4K专区": "4K专区",
            "栏目大全": "栏目大全",
            "特别节目": "特别节目",
            "纪录片": "纪录片",
            "电视剧": "电视剧",
            "动画片": "动画片"
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

    def homeVideoContent(self):
        result = {
            'list': []
        }
        if self.module:
            result = self.module.homeVideoContent()
        return result

    def categoryContent(self, tid, pg, filter, extend):
        result = {}
        month = ""  # 月
        year = ""  # 年
        area = ''  # 地区
        channel = ''  # 频道
        datafl = ''  # 类型
        letter = ''  # 字母
        pagecount = 24
        if tid == '动画片':
            id = urllib.parse.quote(tid)
            if 'datadq-area' in extend.keys():
                area = urllib.parse.quote(extend['datadq-area'])
            if 'dataszm-letter' in extend.keys():
                letter = extend['dataszm-letter']
            if 'datafl-sc' in extend.keys():
                datafl = urllib.parse.quote(extend['datafl-sc'])
            url = 'https://api.cntv.cn/list/getVideoAlbumList?channelid=CHAL1460955899450127&area={0}&sc={4}&fc={1}&letter={2}&p={3}&n=24&serviceId=tvcctv&topv=1&t=json'.format(
                area, id, letter, pg, datafl)
        elif tid == '纪录片':
            id = urllib.parse.quote(tid)
            if 'datapd-channel' in extend.keys():
                channel = urllib.parse.quote(extend['datapd-channel'])
            if 'datafl-sc' in extend.keys():
                datafl = urllib.parse.quote(extend['datafl-sc'])
            if 'datanf-year' in extend.keys():
                year = extend['datanf-year']
            if 'dataszm-letter' in extend.keys():
                letter = extend['dataszm-letter']
            url = 'https://api.cntv.cn/list/getVideoAlbumList?channelid=CHAL1460955924871139&fc={0}&channel={1}&sc={2}&year={3}&letter={4}&p={5}&n=24&serviceId=tvcctv&topv=1&t=json'.format(
                id, channel, datafl, year, letter, pg)
        elif tid == '电视剧':
            id = urllib.parse.quote(tid)
            if 'datafl-sc' in extend.keys():
                datafl = urllib.parse.quote(extend['datafl-sc'])
            if 'datanf-year' in extend.keys():
                year = extend['datanf-year']
            if 'dataszm-letter' in extend.keys():
                letter = extend['dataszm-letter']
            url = 'https://api.cntv.cn/list/getVideoAlbumList?channelid=CHAL1460955853485115&area={0}&sc={1}&fc={2}&year={3}&letter={4}&p={5}&n=24&serviceId=tvcctv&topv=1&t=json'.format(
                area, datafl, id, year, letter, pg)
        elif tid == '特别节目':
            id = urllib.parse.quote(tid)
            if 'datapd-channel' in extend.keys():
                channel = urllib.parse.quote(extend['datapd-channel'])
            if 'datafl-sc' in extend.keys():
                datafl = urllib.parse.quote(extend['datafl-sc'])
            if 'dataszm-letter' in extend.keys():
                letter = extend['dataszm-letter']
            url = 'https://api.cntv.cn/list/getVideoAlbumList?channelid=CHAL1460955953877151&channel={0}&sc={1}&fc={2}&bigday=&letter={3}&p={4}&n=24&serviceId=tvcctv&topv=1&t=json'.format(
                channel, datafl, id, letter, pg)
        elif tid == '栏目大全':
            cid = ''  # 频道
            if 'cid' in extend.keys():
                cid = extend['cid']
            fc = ''  # 分类
            if 'fc' in extend.keys():
                fc = extend['fc']
            fl = ''  # 字母
            if 'fl' in extend.keys():
                fl = extend['fl']
            url = 'https://api.cntv.cn/lanmu/columnSearch?&fl={0}&fc={1}&cid={2}&p={3}&n=20&serviceId=tvcctv&t=json&cb=ko'.format(
                fl, fc, cid, pg)
            pagecount = 20
        elif tid == '4K专区':
            cid = 'CHAL1558416868484111'
            url = 'https://api.cntv.cn/NewVideo/getLastVideoList4K?serviceId=cctv4k&cid={0}&p={1}&n={2}&t=json&cb=ko'.format(
                cid, pg, pagecount
            )
        else:
            url = 'https://tv.cctv.com/epg/index.shtml'

        videos = []
        htmlText = self.fetch(url).text
        if tid == '栏目大全':
            index = htmlText.rfind(');')
            if index > -1:
                htmlText = htmlText[3:index]
                videos = self.get_list1(html=htmlText, tid=tid)
        elif tid == '4K专区':
            index = htmlText.rfind(');')
            if index > -1:
                htmlText = htmlText[3:index]
                videos = self.get_list_4k(html=htmlText, tid=tid)

        else:
            videos = self.get_list(html=htmlText, tid=tid)
        # print(videos)

        result['list'] = videos
        result['page'] = pg
        result['pagecount'] = 9999 if len(videos) >= pagecount else pg
        result['limit'] = 90
        result['total'] = 999999
        return result

    def detailContent(self, array):
        result = {}
        aid = array[0].split('||')
        tid = aid[0]
        logo = aid[3]
        lastVideo = aid[2]
        title = aid[1]
        id = aid[4]

        vod_year = aid[5]
        actors = aid[6] if len(aid) > 6 else ''
        brief = aid[7] if len(aid) > 7 else ''  # get请求最长255，这个描述会有可能直接被干没了。
        fromId = 'CCTV'
        if tid == "栏目大全":
            lastUrl = 'https://api.cntv.cn/video/videoinfoByGuid?guid={0}&serviceId=tvcctv'.format(id)
            # htmlTxt = self.webReadFile(urlStr=lastUrl, header=self.header)
            htmlTxt = self.fetch(lastUrl).text
            topicId = json.loads(htmlTxt)['ctid']
            Url = "https://api.cntv.cn/NewVideo/getVideoListByColumn?id={0}&d=&p=1&n=100&sort=desc&mode=0&serviceId=tvcctv&t=json".format(
                topicId)
            # htmlTxt = self.webReadFile(urlStr=Url, header=self.header)
            htmlTxt = self.fetch(Url).text
        elif tid == "4K专区":
            Url = 'https://api.cntv.cn/NewVideo/getVideoListByAlbumIdNew?id={0}&serviceId=cctv4k&p=1&n=100&mode=0&pub=1'.format(
                id)
            print(Url)
        else:
            Url = 'https://api.cntv.cn/NewVideo/getVideoListByAlbumIdNew?id={0}&serviceId=tvcctv&p=1&n=100&mode=0&pub=1'.format(
                id)
        jRoot = ''
        videoList = []
        try:
            if tid == "搜索":
                fromId = '中央台'
                videoList = [title + "$" + lastVideo]
            else:
                # htmlTxt = self.webReadFile(urlStr=Url, header=self.header)
                htmlTxt = self.fetch(Url).text
                jRoot = json.loads(htmlTxt)
                data = jRoot['data']
                jsonList = data['list']
                videoList = self.get_EpisodesList(jsonList=jsonList)
                if len(videoList) < 1:
                    # htmlTxt = self.webReadFile(urlStr=lastVideo, header=self.header)
                    htmlTxt = self.fetch(lastVideo).text
                    if tid == "电视剧" or tid == "纪录片" or tid == "4K专区":
                        patternTxt = r"'title':\s*'(?P<title>.+?)',\n{0,1}\s*'brief':\s*'(.+?)',\n{0,1}\s*'img':\s*'(.+?)',\n{0,1}\s*'url':\s*'(?P<url>.+?)'"
                    elif tid == "特别节目":
                        patternTxt = r'class="tp1"><a\s*href="(?P<url>https://.+?)"\s*target="_blank"\s*title="(?P<title>.+?)"></a></div>'
                    elif tid == "动画片":
                        patternTxt = r"'title':\s*'(?P<title>.+?)',\n{0,1}\s*'img':\s*'(.+?)',\n{0,1}\s*'brief':\s*'(.+?)',\n{0,1}\s*'url':\s*'(?P<url>.+?)'"
                    elif tid == "栏目大全":
                        patternTxt = r'href="(?P<url>.+?)" target="_blank" alt="(?P<title>.+?)" title=".+?">'
                    videoList = self.get_EpisodesList_re(htmlTxt=htmlTxt, patternTxt=patternTxt)
                    fromId = '央视'
        except:
            pass
        if len(videoList) == 0:
            return {}
        vod = {
            "vod_id": array[0],
            "vod_name": title.replace(' ', ''),
            "vod_pic": logo,
            "type_name": tid,
            "vod_year": vod_year,
            "vod_area": "",
            "vod_remarks": '',
            "vod_actor": actors,
            "vod_director": '',
            "vod_content": brief
        }
        vod['vod_play_from'] = fromId
        vod['vod_play_url'] = "#".join(videoList)
        result = {
            'list': [
                vod
            ]
        }
        return result

    def get_lineList(self, Txt, mark, after):
        circuit = []
        origin = Txt.find(mark)
        while origin > 8:
            end = Txt.find(after, origin)
            circuit.append(Txt[origin:end])
            origin = Txt.find(mark, end)
        return circuit

    def get_RegexGetTextLine(self, Text, RegexText, Index):
        returnTxt = []
        pattern = re.compile(RegexText, re.M | re.S)
        ListRe = pattern.findall(Text)
        if len(ListRe) < 1:
            return returnTxt
        for value in ListRe:
            returnTxt.append(value)
        return returnTxt

    def searchContent(self, key, quick, pg=1):
        key = urllib.parse.quote(key)
        Url = 'https://search.cctv.com/ifsearch.php?page=1&qtext={0}&sort=relevance&pageSize=20&type=video&vtime=-1&datepid=1&channel=&pageflag=0&qtext_str={0}'.format(
            key)
        # htmlTxt = self.webReadFile(urlStr=Url, header=self.header)
        htmlTxt = self.fetch(Url).text
        videos = self.get_list_search(html=htmlTxt, tid='搜索')
        result = {
            'list': videos
        }
        return result

    def playerContent(self, flag, id, vipFlags):
        result = {}
        url = ''
        parse = 0
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
        }
        if flag == 'CCTV':
            url = self.get_m3u8(urlTxt=id)
        else:
            try:
                # htmlTxt = self.webReadFile(urlStr=id, header=self.header)
                htmlTxt = self.fetch(id).text
                guid = self.get_RegexGetText(Text=htmlTxt, RegexText=r'var\sguid\s*=\s*"(.+?)";', Index=1)
                url = self.get_m3u8(urlTxt=guid)
            except:
                url = id
                parse = 1
        if url.find('https:') < 0:
            url = id
            parse = 1
        result["parse"] = parse  # 1=嗅探,0=播放
        result["playUrl"] = ''
        result["url"] = url
        result["header"] = headers
        return result

    # 分类抓取地址:
    # 栏目大全:https://tv.cctv.com/lm/index.shtml?spm=C28340.Pu9TN9YUsfNZ.E2PQtIunpEaz.24
    # 电视剧:https://tv.cctv.com/yxg/index.shtml?spm=C28340.PlFTqGe6Zk8M.E2PQtIunpEaz.65#datacid=dsj&datafl=&datadq=&fc=%E7%94%B5%E8%A7%86%E5%89%A7&datanf=&dataszm=
    # 动画片:https://tv.cctv.com/yxg/index.shtml?spm=C28340.PlFTqGe6Zk8M.E2PQtIunpEaz.65#datacid=dhp&datafl=&datadq=&fc=%E5%8A%A8%E7%94%BB%E7%89%87&dataszm=
    # 记录片:https://tv.cctv.com/yxg/index.shtml?spm=C28340.PlFTqGe6Zk8M.E2PQtIunpEaz.65#datacid=jlp&datapd=&datafl=&fc=%E7%BA%AA%E5%BD%95%E7%89%87&datanf=&dataszm=
    # 特别节目:https://tv.cctv.com/yxg/index.shtml?spm=C28340.PlFTqGe6Zk8M.E2PQtIunpEaz.65#datacid=tbjm&datapd=&datafl=&fc=%E7%89%B9%E5%88%AB%E8%8A%82%E7%9B%AE&datajr=&dataszm=
    config = {
        "player": {},
        "filter": {
            "电视剧": [
                {"key": "datafl-sc", "name": "类型",
                 "value": [{"n": "全部", "v": ""}, {"n": "谍战", "v": "谍战"}, {"n": "悬疑", "v": "悬疑"},
                           {"n": "刑侦", "v": "刑侦"}, {"n": "历史", "v": "历史"}, {"n": "古装", "v": "古装"},
                           {"n": "武侠", "v": "武侠"}, {"n": "军旅", "v": "军旅"}, {"n": "战争", "v": "战争"},
                           {"n": "喜剧", "v": "喜剧"}, {"n": "青春", "v": "青春"}, {"n": "言情", "v": "言情"},
                           {"n": "偶像", "v": "偶像"}, {"n": "家庭", "v": "家庭"}, {"n": "年代", "v": "年代"},
                           {"n": "革命", "v": "革命"}, {"n": "农村", "v": "农村"}, {"n": "都市", "v": "都市"},
                           {"n": "其他", "v": "其他"}]},
                {"key": "datadq-area", "name": "地区",
                 "value": [{"n": "全部", "v": ""}, {"n": "中国大陆", "v": "中国大陆"}, {"n": "中国香港", "v": "香港"},
                           {"n": "美国", "v": "美国"}, {"n": "欧洲", "v": "欧洲"}, {"n": "泰国", "v": "泰国"}]},
                {"key": "datanf-year", "name": "年份",
                 "value": [{"n": "全部", "v": ""}, {"n": "2024", "v": "2024"}, {"n": "2023", "v": "2023"},
                           {"n": "2022", "v": "2022"},
                           {"n": "2021", "v": "2021"}, {"n": "2020", "v": "2020"}, {"n": "2019", "v": "2019"},
                           {"n": "2018", "v": "2018"}, {"n": "2017", "v": "2017"}, {"n": "2016", "v": "2016"},
                           {"n": "2015", "v": "2015"}, {"n": "2014", "v": "2014"}, {"n": "2013", "v": "2013"},
                           {"n": "2012", "v": "2012"}, {"n": "2011", "v": "2011"}, {"n": "2010", "v": "2010"},
                           {"n": "2009", "v": "2009"}, {"n": "2008", "v": "2008"}, {"n": "2007", "v": "2007"},
                           {"n": "2006", "v": "2006"}, {"n": "2005", "v": "2005"}, {"n": "2004", "v": "2004"},
                           {"n": "2003", "v": "2003"}, {"n": "2002", "v": "2002"}, {"n": "2001", "v": "2001"},
                           {"n": "2000", "v": "2000"}, {"n": "1999", "v": "1999"}, {"n": "1998", "v": "1998"},
                           {"n": "1997", "v": "1997"}]},
                {"key": "dataszm-letter", "name": "字母",
                 "value": [{"n": "全部", "v": ""}, {"n": "A", "v": "A"}, {"n": "C", "v": "C"}, {"n": "E", "v": "E"},
                           {"n": "F", "v": "F"}, {"n": "G", "v": "G"}, {"n": "H", "v": "H"}, {"n": "I", "v": "I"},
                           {"n": "J", "v": "J"}, {"n": "K", "v": "K"}, {"n": "L", "v": "L"}, {"n": "M", "v": "M"},
                           {"n": "N", "v": "N"}, {"n": "O", "v": "O"}, {"n": "P", "v": "P"}, {"n": "Q", "v": "Q"},
                           {"n": "R", "v": "R"}, {"n": "S", "v": "S"}, {"n": "T", "v": "T"}, {"n": "U", "v": "U"},
                           {"n": "V", "v": "V"}, {"n": "W", "v": "W"}, {"n": "X", "v": "X"}, {"n": "Y", "v": "Y"},
                           {"n": "Z", "v": "Z"}, {"n": "0-9", "v": "0-9"}]}
            ],
            "动画片": [
                {"key": "datafl-sc", "name": "类型",
                 "value": [{"n": "全部", "v": ""}, {"n": "亲子", "v": "亲子"}, {"n": "搞笑", "v": "搞笑"},
                           {"n": "冒险", "v": "冒险"}, {"n": "动作", "v": "动作"}, {"n": "宠物", "v": "宠物"},
                           {"n": "体育", "v": "体育"}, {"n": "益智", "v": "益智"}, {"n": "历史", "v": "历史"},
                           {"n": "教育", "v": "教育"}, {"n": "校园", "v": "校园"}, {"n": "言情", "v": "言情"},
                           {"n": "武侠", "v": "武侠"}, {"n": "经典", "v": "经典"}, {"n": "未来", "v": "未来"},
                           {"n": "古代", "v": "古代"}, {"n": "神话", "v": "神话"}, {"n": "真人", "v": "真人"},
                           {"n": "励志", "v": "励志"}, {"n": "热血", "v": "热血"}, {"n": "奇幻", "v": "奇幻"},
                           {"n": "童话", "v": "童话"}, {"n": "剧情", "v": "剧情"}, {"n": "夺宝", "v": "夺宝"},
                           {"n": "其他", "v": "其他"}]},
                {"key": "datadq-area", "name": "地区",
                 "value": [{"n": "全部", "v": ""}, {"n": "中国大陆", "v": "中国大陆"}, {"n": "美国", "v": "美国"},
                           {"n": "欧洲", "v": "欧洲"}]},
                {"key": "dataszm-letter", "name": "字母",
                 "value": [{"n": "全部", "v": ""}, {"n": "A", "v": "A"}, {"n": "C", "v": "C"}, {"n": "E", "v": "E"},
                           {"n": "F", "v": "F"}, {"n": "G", "v": "G"}, {"n": "H", "v": "H"}, {"n": "I", "v": "I"},
                           {"n": "J", "v": "J"}, {"n": "K", "v": "K"}, {"n": "L", "v": "L"}, {"n": "M", "v": "M"},
                           {"n": "N", "v": "N"}, {"n": "O", "v": "O"}, {"n": "P", "v": "P"}, {"n": "Q", "v": "Q"},
                           {"n": "R", "v": "R"}, {"n": "S", "v": "S"}, {"n": "T", "v": "T"}, {"n": "U", "v": "U"},
                           {"n": "V", "v": "V"}, {"n": "W", "v": "W"}, {"n": "X", "v": "X"}, {"n": "Y", "v": "Y"},
                           {"n": "Z", "v": "Z"}, {"n": "0-9", "v": "0-9"}]}
            ],
            "纪录片": [
                {"key": "datapd-channel", "name": "频道",
                 "value": [{"n": "全部", "v": ""}, {"n": "CCTV{1 综合", "v": "CCTV{1 综合"},
                           {"n": "CCTV{2 财经", "v": "CCTV{2 财经"}, {"n": "CCTV{3 综艺", "v": "CCTV{3 综艺"},
                           {"n": "CCTV{4 中文国际", "v": "CCTV{4 中文国际"}, {"n": "CCTV{5 体育", "v": "CCTV{5 体育"},
                           {"n": "CCTV{6 电影", "v": "CCTV{6 电影"}, {"n": "CCTV{7 国防军事", "v": "CCTV{7 国防军事"},
                           {"n": "CCTV{8 电视剧", "v": "CCTV{8 电视剧"}, {"n": "CCTV{9 纪录", "v": "CCTV{9 纪录"},
                           {"n": "CCTV{10 科教", "v": "CCTV{10 科教"}, {"n": "CCTV{11 戏曲", "v": "CCTV{11 戏曲"},
                           {"n": "CCTV{12 社会与法", "v": "CCTV{12 社会与法"},
                           {"n": "CCTV{13 新闻", "v": "CCTV{13 新闻"}, {"n": "CCTV{14 少儿", "v": "CCTV{14 少儿"},
                           {"n": "CCTV{15 音乐", "v": "CCTV{15 音乐"},
                           {"n": "CCTV{17 农业农村", "v": "CCTV{17 农业农村"}]},
                {"key": "datafl-sc", "name": "类型",
                 "value": [{"n": "全部", "v": ""}, {"n": "人文历史", "v": "人文历史"}, {"n": "人物", "v": "人物"},
                           {"n": "军事", "v": "军事"}, {"n": "探索", "v": "探索"}, {"n": "社会", "v": "社会"},
                           {"n": "时政", "v": "时政"}, {"n": "经济", "v": "经济"}, {"n": "科技", "v": "科技"}]},
                {"key": "datanf-year", "name": "年份",
                 "value": [{"n": "全部", "v": ""}, {"n": "2024", "v": "2024"}, {"n": "2023", "v": "2023"},
                           {"n": "2022", "v": "2022"},
                           {"n": "2021", "v": "2021"}, {"n": "2020", "v": "2020"}, {"n": "2019", "v": "2019"},
                           {"n": "2018", "v": "2018"}, {"n": "2017", "v": "2017"}, {"n": "2016", "v": "2016"},
                           {"n": "2015", "v": "2015"}, {"n": "2014", "v": "2014"}, {"n": "2013", "v": "2013"},
                           {"n": "2012", "v": "2012"}, {"n": "2011", "v": "2011"}, {"n": "2010", "v": "2010"},
                           {"n": "2009", "v": "2009"}, {"n": "2008", "v": "2008"}]},
                {"key": "dataszm-letter", "name": "字母",
                 "value": [{"n": "全部", "v": ""}, {"n": "A", "v": "A"}, {"n": "C", "v": "C"}, {"n": "E", "v": "E"},
                           {"n": "F", "v": "F"}, {"n": "G", "v": "G"}, {"n": "H", "v": "H"}, {"n": "I", "v": "I"},
                           {"n": "J", "v": "J"}, {"n": "K", "v": "K"}, {"n": "L", "v": "L"}, {"n": "M", "v": "M"},
                           {"n": "N", "v": "N"}, {"n": "O", "v": "O"}, {"n": "P", "v": "P"}, {"n": "Q", "v": "Q"},
                           {"n": "R", "v": "R"}, {"n": "S", "v": "S"}, {"n": "T", "v": "T"}, {"n": "U", "v": "U"},
                           {"n": "V", "v": "V"}, {"n": "W", "v": "W"}, {"n": "X", "v": "X"}, {"n": "Y", "v": "Y"},
                           {"n": "Z", "v": "Z"}, {"n": "0-9", "v": "0-9"}]}
            ],
            "特别节目": [
                {"key": "datapd-channel", "name": "频道",
                 "value": [{"n": "全部", "v": ""}, {"n": "CCTV{1 综合", "v": "CCTV{1 综合"},
                           {"n": "CCTV{2 财经", "v": "CCTV{2 财经"}, {"n": "CCTV{3 综艺", "v": "CCTV{3 综艺"},
                           {"n": "CCTV{4 中文国际", "v": "CCTV{4 中文国际"}, {"n": "CCTV{5 体育", "v": "CCTV{5 体育"},
                           {"n": "CCTV{6 电影", "v": "CCTV{6 电影"}, {"n": "CCTV{7 国防军事", "v": "CCTV{7 国防军事"},
                           {"n": "CCTV{8 电视剧", "v": "CCTV{8 电视剧"}, {"n": "CCTV{9 纪录", "v": "CCTV{9 纪录"},
                           {"n": "CCTV{10 科教", "v": "CCTV{10 科教"}, {"n": "CCTV{11 戏曲", "v": "CCTV{11 戏曲"},
                           {"n": "CCTV{12 社会与法", "v": "CCTV{12 社会与法"},
                           {"n": "CCTV{13 新闻", "v": "CCTV{13 新闻"}, {"n": "CCTV{14 少儿", "v": "CCTV{14 少儿"},
                           {"n": "CCTV{15 音乐", "v": "CCTV{15 音乐"},
                           {"n": "CCTV{17 农业农村", "v": "CCTV{17 农业农村"}]},
                {"key": "datafl-sc", "name": "类型",
                 "value": [{"n": "全部", "v": ""}, {"n": "全部", "v": "全部"}, {"n": "新闻", "v": "新闻"},
                           {"n": "经济", "v": "经济"}, {"n": "综艺", "v": "综艺"}, {"n": "体育", "v": "体育"},
                           {"n": "军事", "v": "军事"}, {"n": "影视", "v": "影视"}, {"n": "科教", "v": "科教"},
                           {"n": "戏曲", "v": "戏曲"}, {"n": "青少", "v": "青少"}, {"n": "音乐", "v": "音乐"},
                           {"n": "社会", "v": "社会"}, {"n": "公益", "v": "公益"}, {"n": "其他", "v": "其他"}]},
                {"key": "dataszm-letter", "name": "字母",
                 "value": [{"n": "全部", "v": ""}, {"n": "A", "v": "A"}, {"n": "C", "v": "C"}, {"n": "E", "v": "E"},
                           {"n": "F", "v": "F"}, {"n": "G", "v": "G"}, {"n": "H", "v": "H"}, {"n": "I", "v": "I"},
                           {"n": "J", "v": "J"}, {"n": "K", "v": "K"}, {"n": "L", "v": "L"}, {"n": "M", "v": "M"},
                           {"n": "N", "v": "N"}, {"n": "O", "v": "O"}, {"n": "P", "v": "P"}, {"n": "Q", "v": "Q"},
                           {"n": "R", "v": "R"}, {"n": "S", "v": "S"}, {"n": "T", "v": "T"}, {"n": "U", "v": "U"},
                           {"n": "V", "v": "V"}, {"n": "W", "v": "W"}, {"n": "X", "v": "X"}, {"n": "Y", "v": "Y"},
                           {"n": "Z", "v": "Z"}, {"n": "0-9", "v": "0-9"}]}
            ],
            "栏目大全": [{"key": "cid", "name": "频道",
                          "value": [{"n": "全部", "v": ""}, {"n": "CCTV-1综合", "v": "EPGC1386744804340101"},
                                    {"n": "CCTV-2财经", "v": "EPGC1386744804340102"},
                                    {"n": "CCTV-3综艺", "v": "EPGC1386744804340103"},
                                    {"n": "CCTV-4中文国际", "v": "EPGC1386744804340104"},
                                    {"n": "CCTV-5体育", "v": "EPGC1386744804340107"},
                                    {"n": "CCTV-6电影", "v": "EPGC1386744804340108"},
                                    {"n": "CCTV-7国防军事", "v": "EPGC1386744804340109"},
                                    {"n": "CCTV-8电视剧", "v": "EPGC1386744804340110"},
                                    {"n": "CCTV-9纪录", "v": "EPGC1386744804340112"},
                                    {"n": "CCTV-10科教", "v": "EPGC1386744804340113"},
                                    {"n": "CCTV-11戏曲", "v": "EPGC1386744804340114"},
                                    {"n": "CCTV-12社会与法", "v": "EPGC1386744804340115"},
                                    {"n": "CCTV-13新闻", "v": "EPGC1386744804340116"},
                                    {"n": "CCTV-14少儿", "v": "EPGC1386744804340117"},
                                    {"n": "CCTV-15音乐", "v": "EPGC1386744804340118"},
                                    {"n": "CCTV-16奥林匹克", "v": "EPGC1634630207058998"},
                                    {"n": "CCTV-17农业农村", "v": "EPGC1563932742616872"},
                                    {"n": "CCTV-5+体育赛事", "v": "EPGC1468294755566101"}]},
                         {"key": "fc", "name": "分类",
                          "value": [{"n": "全部", "v": ""}, {"n": "新闻", "v": "新闻"}, {"n": "体育", "v": "体育"},
                                    {"n": "综艺", "v": "综艺"}, {"n": "健康", "v": "健康"}, {"n": "生活", "v": "生活"},
                                    {"n": "科教", "v": "科教"}, {"n": "经济", "v": "经济"}, {"n": "农业", "v": "农业"},
                                    {"n": "法治", "v": "法治"}, {"n": "军事", "v": "军事"}, {"n": "少儿", "v": "少儿"},
                                    {"n": "动画", "v": "动画"}, {"n": "纪实", "v": "纪实"}, {"n": "戏曲", "v": "戏曲"},
                                    {"n": "音乐", "v": "音乐"}, {"n": "影视", "v": "影视"}]},
                         {"key": "fl", "name": "字母",
                          "value": [{"n": "全部", "v": ""}, {"n": "A", "v": "A"}, {"n": "B", "v": "B"},
                                    {"n": "C", "v": "C"}, {"n": "D", "v": "D"}, {"n": "E", "v": "E"},
                                    {"n": "F", "v": "F"}, {"n": "G", "v": "G"}, {"n": "H", "v": "H"},
                                    {"n": "I", "v": "I"}, {"n": "J", "v": "J"}, {"n": "K", "v": "K"},
                                    {"n": "L", "v": "L"}, {"n": "M", "v": "M"}, {"n": "N", "v": "N"},
                                    {"n": "O", "v": "O"}, {"n": "P", "v": "P"}, {"n": "Q", "v": "Q"},
                                    {"n": "R", "v": "R"}, {"n": "S", "v": "S"}, {"n": "T", "v": "T"},
                                    {"n": "U", "v": "U"}, {"n": "V", "v": "V"}, {"n": "W", "v": "W"},
                                    {"n": "X", "v": "X"}, {"n": "Y", "v": "Y"}, {"n": "Z", "v": "Z"}]},
                         ]
        }
    }
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36",
        "Host": "tv.cctv.com",
        "Referer": "https://tv.cctv.com/"
    }

    def localProxy(self, param):
        return [200, "video/MP2T", action, ""]

    # -----------------------------------------------自定义函数-----------------------------------------------
    # 访问网页
    def webReadFile(self, urlStr, header):
        html = ''
        req = urllib.request.Request(url=urlStr)  # ,headers=header
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
        return html

    # 判断网络地址是否存在
    def TestWebPage(self, urlStr, header):
        html = ''
        req = urllib.request.Request(url=urlStr, method='HEAD')  # ,headers=header
        with  urllib.request.urlopen(req) as response:
            html = response.getcode()
        return html

    # 正则取文本
    def get_RegexGetText(self, Text, RegexText, Index):
        returnTxt = ""
        Regex = re.search(RegexText, Text, re.M | re.S)
        if Regex is None:
            returnTxt = ""
        else:
            returnTxt = Regex.group(Index)
        return returnTxt

    # 取集数
    def get_EpisodesList(self, jsonList):
        videos = []
        for vod in jsonList:
            url = vod['guid']
            title = vod['title']
            if len(url) == 0:
                continue
            videos.append(title + "$" + url)
        return videos

    # 取集数
    def get_EpisodesList_re(self, htmlTxt, patternTxt):
        ListRe = re.finditer(patternTxt, htmlTxt, re.M | re.S)
        videos = []
        for vod in ListRe:
            url = vod.group('url')
            title = vod.group('title')
            if len(url) == 0:
                continue
            videos.append(title + "$" + url)
        return videos

    # 取剧集区
    def get_lineList(self, Txt, mark, after):
        circuit = []
        origin = Txt.find(mark)
        while origin > 8:
            end = Txt.find(after, origin)
            circuit.append(Txt[origin:end])
            origin = Txt.find(mark, end)
        return circuit

    # 正则取文本,返回数组
    def get_RegexGetTextLine(self, Text, RegexText, Index):
        returnTxt = []
        pattern = re.compile(RegexText, re.M | re.S)
        ListRe = pattern.findall(Text)
        if len(ListRe) < 1:
            return returnTxt
        for value in ListRe:
            returnTxt.append(value)
        return returnTxt

    # 删除html标签
    def removeHtml(self, txt):
        soup = re.compile(r'<[^>]+>', re.S)
        txt = soup.sub('', txt)
        return txt.replace("&nbsp;", " ")

    # 取m3u8
    def get_m3u8(self, urlTxt):
        url = "https://vdn.apps.cntv.cn/api/getHttpVideoInfo.do?pid={0}".format(urlTxt)
        # htmlTxt = self.webReadFile(urlStr=url, header=self.header)
        htmlTxt = self.fetch(url).text
        jo = json.loads(htmlTxt)
        link = jo['hls_url'].strip()
        # 获取域名前缀
        urlPrefix = self.get_RegexGetText(Text=link, RegexText='(http[s]?://[a-zA-z0-9.]+)/', Index=1)
        # 域名前缀指定替换,然后可以获取到更高质量的视频列表
        new_link = link.replace(f'{urlPrefix}/asp/hls/', 'https://dh5.cntv.qcloudcdn.com/asp/h5e/hls/').split('?')[0]
        html = self.webReadFile(urlStr=new_link, header=self.header)
        content = html.strip()
        arr = content.split('\n')
        subUrl = arr[-1].split('/')
        # hdUrl = urlPrefix + arr[-1]

        # subUrl[3] = '2000'
        # subUrl[-1] = '2000.m3u8'
        # hdUrl = urlPrefix + '/'.join(subUrl)
        maxVideo = subUrl[-1].replace('.m3u8', '')
        hdUrl = link.replace('main', maxVideo)
        hdUrl = hdUrl.replace(urlPrefix, 'https://newcntv.qcloudcdn.com')
        hdRsp = self.TestWebPage(urlStr=hdUrl, header=self.header)
        if hdRsp == 200:
            url = hdUrl.split('?')[0]
            self.log(f'视频链接: {url}')
        else:
            url = ''
        return url

    # 搜索
    def get_list_search(self, html, tid):
        jRoot = json.loads(html)
        jsonList = jRoot['list']
        videos = []
        for vod in jsonList:
            url = vod['urllink']
            title = self.removeHtml(txt=vod['title'])
            img = vod['imglink']
            id = vod['id']
            brief = vod['channel']
            year = vod['uploadtime']
            if len(url) == 0:
                continue
            guids = [tid, title, url, img, id, year, '', brief]
            guid = "||".join(guids)
            videos.append({
                "vod_id": guid,
                "vod_name": title,
                "vod_pic": img,
                "vod_remarks": year
            })
        return videos

    def get_list1(self, html, tid):
        jRoot = json.loads(html)
        videos = []
        data = jRoot['response']
        if data is None:
            return []
        jsonList = data['docs']
        for vod in jsonList:
            id = vod['lastVIDE']['videoSharedCode']
            desc = vod['lastVIDE']['videoTitle']
            title = vod['column_name']
            url = vod['column_website']
            img = vod['column_logo']
            year = vod['column_playdate']
            brief = vod['column_brief']
            actors = ''
            if len(url) == 0:
                continue
            guids = [tid, title, url, img, id, year, actors, brief]
            guid = "||".join(guids)
            # print(vod_id)
            videos.append({
                "vod_id": guid,
                "vod_name": title,
                "vod_pic": img,
                "vod_remarks": desc.split('》')[1].strip() if '》' in desc else desc.strip()
            })
        # print(videos)
        return videos

    # 分类取结果
    def get_list(self, html, tid):
        jRoot = json.loads(html)
        videos = []
        data = jRoot['data']
        if data is None:
            return []
        jsonList = data['list']
        for vod in jsonList:
            url = vod['url']
            title = vod['title']
            img = vod['image']
            id = vod['id']
            try:
                brief = vod['brief']
            except:
                brief = ''
            try:
                year = vod['year']
            except:
                year = ''
            try:
                actors = vod['actors']
            except:
                actors = ''
            if len(url) == 0:
                continue
            guids = [tid, title, url, img, id, year, actors, brief]
            guid = "||".join(guids)
            # print(vod_id)
            videos.append({
                "vod_id": guid,
                "vod_name": title,
                "vod_pic": img,
                "vod_remarks": ''
            })
        return videos

    # 4k分类取结果
    def get_list_4k(self, html, tid):
        jRoot = json.loads(html)
        videos = []
        data = jRoot['data']
        if data is None:
            return []
        jsonList = data['list']
        for vod in jsonList:
            vod_remarks = vod['title']
            id = vod['id']
            vod = vod['last_video']
            img = vod['image']
            url = vod['url']
            title = vod['title']
            brief = vod.get('brief') or ''
            year = vod.get('year') or ''
            actors = vod.get('actors') or ''
            if len(url) == 0:
                continue
            guids = [tid, title, url, img, id, year, actors, brief]
            guid = "||".join(guids)
            # print(vod_id)
            videos.append({
                "vod_id": guid,
                "vod_name": title,
                "vod_pic": img,
                "vod_remarks": vod_remarks
            })
        return videos


if __name__ == '__main__':
    from t4.core.loader import t4_spider_init

    spider = Spider()
    t4_spider_init(spider)
    print(spider.homeVideoContent())
    # spider.init_api_ext_file()
    # url = 'https://api.cntv.cn/lanmu/columnSearch?&fl=&fc=%E6%96%B0%E9%97%BB&cid=&p=1&n=20&serviceId=tvcctv&t=jsonp&cb=Callback'
    # url = 'https://api.cntv.cn/lanmu/columnSearch?&fl=&fc=&cid=&p=1&n=20&serviceId=tvcctv&t=json&cb=ko'
    # r = spider.fetch(url)
    # print(r.text)
    # home_content = spider.homeContent(None)
    # print(home_content)
    # cate_content = spider.categoryContent('栏目大全', 1, {'cid': 'n'}, {})
    # print(cate_content)
    # vid = cate_content['list'][0]['vod_id']
    # print(vid)
    # detail_content = spider.detailContent([vid])
    # print(detail_content)
    #
    # vod_play_from = detail_content['list'][0]['vod_play_from']
    # vod_play_url = detail_content['list'][0]['vod_play_url']
    # print(vod_play_from, vod_play_url)
    # _url = vod_play_url.split('#')[0].split('$')[1]
    # print(_url)
    # play = spider.playerContent(vod_play_from, _url, None)
    # print(play)
