# coding=utf-8
# !/usr/bin/python
import sys

sys.path.append('..')
try:
    # from base.spider import Spider as BaseSpider
    from base.spider import BaseSpider
except ImportError:
    from t4.base.spider import BaseSpider
import time
import re
from urllib import request, parse
import urllib
import urllib.request
from xml.etree.ElementTree import fromstring, ElementTree as et

"""
配置示例:
t4的配置里ext节点会自动变成api对应query参数extend,但t4的ext字符串不支持路径格式，比如./开头或者.json结尾
api里会自动含有ext参数是base64编码后的选中的筛选条件
 {
    "key":"hipy_t4_新浪资源",
    "name":"新浪资源(hipy_t4)",
    "type":4,
    "api":"http://192.168.31.49:5707/api/v1/vod/新浪资源",
    "searchable":1,
    "quickSearch":0,
    "filterable":1,
    "ext":""
},
{
    "key": "hipy_t3_新浪资源",
    "name": "新浪资源(hipy_t3)",
    "type": 3,
    "api": "{{host}}/txt/hipy/新浪资源.py",
    "searchable": 1,
    "quickSearch": 0,
    "filterable": 1,
    "ext": ""
},
"""


class Spider(BaseSpider):  # 元类 默认的元类 type
    def getName(self):
        return "新浪资源"  # 除去少儿不宜的内容

    filterate = False

    def init(self, extend=""):
        print("============{0}============".format(extend))
        pass

    def isVideoFormat(self, url):
        pass

    def manualVideoCheck(self):
        pass

    def homeContent(self, filter):
        result = {}
        timeClass = time.localtime(time.time())
        cateManual = {
            '动漫': '3',
            '动漫电影': '17',
            '综艺': '4',
            '纪录片': '5',
            '动作片': '6',
            '爱情片': '7',
            '科幻片': '8',
            '战争片': '9',
            '剧情片': '10',
            '恐怖片': '11',
            '喜剧片': '12',
            '大陆剧': '13',
            '港澳剧': '14',
            '台湾剧': '15',
            '欧美剧': '16',
            '韩剧': '18',
            '日剧': '20',
            '泰剧': '21',
            '体育': '23'
        }
        # if timeClass.tm_hour>22:
        # 	cateManual['伦理片']='22'
        # 	self.filterate=False
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
        xmlTxt = self.custom_webReadFile(
            urlStr='https://api.xinlangapi.com/xinlangapi.php/provide/vod/from/xlyun/at/xml/?ac=list&h=24')
        tree = et(fromstring(xmlTxt))
        root = tree.getroot()
        listXml = root.iter('list')
        videos = self.custom_list(html=listXml)
        result = {
            'list': videos
        }
        return result

    def categoryContent(self, tid, pg, filter, extend):
        result = {}
        videos = []
        pagecount = 1
        limit = 20
        total = 9999
        Url = 'https://api.xinlangapi.com/xinlangapi.php/provide/vod/from/xlyun/at/xml/?ac=list&t={0}&pg={1}'.format(
            tid, pg)
        xmlTxt = self.custom_webReadFile(urlStr=Url)
        tree = et(fromstring(xmlTxt))
        root = tree.getroot()
        listXml = root.iter('list')
        for vod in listXml:
            pagecount = vod.attrib['pagecount']
            limit = vod.attrib['pagesize']
            total = vod.attrib['recordcount']
        videos = self.custom_list(html=root.iter('list'))
        result['list'] = videos
        result['page'] = pg
        result['pagecount'] = pagecount
        result['limit'] = limit
        result['total'] = total
        return result

    def detailContent(self, array):
        result = {}
        aid = array[0].split('###')
        id = aid[1]
        logo = aid[2]
        title = aid[0]
        vod_play_from = ['播放线路', ]
        vod_year = ''
        vod_actor = ''
        vod_content = ''
        vod_director = ''
        type_name = ''
        vod_area = ''
        vod_lang = ''
        vodItems = []
        vod_play_url = []
        try:
            url = 'https://api.xinlangapi.com/xinlangapi.php/provide/vod/from/xlyun/at/xml/?ac=detail&ids=' + id
            xmlTxt = self.custom_webReadFile(urlStr=url)
            jRoot = et(fromstring(xmlTxt))
            xmlList = jRoot.iter('list')
            for vod in xmlList:
                for x in vod:
                    for v in x:
                        if v.tag == 'actor':
                            vod_actor = v.text
                        if v.tag == 'director':
                            vod_director = v.text
                        if v.tag == 'des':
                            vod_content = v.text
                        if v.tag == 'area':
                            vod_area = v.text
                        if v.tag == 'year':
                            vod_year = v.text
                        if v.tag == 'type':
                            type_name = v.text
                        if v.tag == 'lang':
                            vod_lang = v.text

            temporary = self.custom_RegexGetText(Text=xmlTxt, RegexText=r'<dd flag="xlyun">(.+?)</dd>', Index=1)
            temporary = temporary.replace('<![CDATA[', '').replace(']]>', '')
            vodItems = self.custom_EpisodesList(temporary)
            joinStr = "#".join(vodItems)
            vod_play_url.append(joinStr)
        except:
            pass
        vod = {
            "vod_id": array[0],
            "vod_name": title,
            "vod_pic": logo,
            "type_name": type_name,
            "vod_year": vod_year,
            "vod_area": vod_area,
            "vod_remarks": vod_lang,
            "vod_actor": vod_actor,
            "vod_director": vod_director,
            "vod_content": vod_content
        }
        vod['vod_play_from'] = "$$$".join(vod_play_from)
        vod['vod_play_url'] = "$$$".join(vod_play_url)
        result = {
            'list': [
                vod
            ]
        }
        if self.filterate == True and self.custom_RegexGetText(Text=type_name, RegexText=r'(伦理|倫理|福利)',
                                                               Index=1) != '':
            result = {'list': []}
        return result

    def searchContent(self, key, quick, pg=1):
        Url = 'https://api.xinlangapi.com/xinlangapi.php/provide/vod/from/xlyun/at/xml/?ac=list&wd={0}&pg={1}'.format(
            urllib.parse.quote(key), '1')
        xmlTxt = self.custom_webReadFile(urlStr=Url)
        tree = et(fromstring(xmlTxt))
        root = tree.getroot()
        listXml = root.iter('list')
        videos = self.custom_list(html=listXml)
        result = {
            'list': videos
        }
        return result

    def playerContent(self, flag, id, vipFlags):
        result = {}
        parse = 1
        url = id
        htmlTxt = self.custom_webReadFile(urlStr=url, header=self.header)
        url = self.custom_RegexGetText(Text=htmlTxt, RegexText=r'(https{0,1}://.+?\.m3u8)', Index=1)
        if url.find('.m3u8') < 1:
            url = id
            parse = 0
        result["parse"] = parse  # 0=直接播放、1=嗅探
        result["playUrl"] = ''
        result["url"] = url
        result['jx'] = 0  # VIP解析,0=不解析、1=解析
        result["header"] = ''
        return result

    config = {
        "player": {},
        "filter": {}
    }
    header = {}

    def localProxy(self, params):
        return [200, "video/MP2T", ""]

    # -----------------------------------------------自定义函数-----------------------------------------------
    # 正则取文本
    def custom_RegexGetText(self, Text, RegexText, Index):
        returnTxt = ""
        Regex = re.search(RegexText, Text, re.M | re.S)
        if Regex is None:
            returnTxt = ""
        else:
            returnTxt = Regex.group(Index)
        return returnTxt

    # 分类取结果
    def custom_list(self, html):
        ListRe = html
        videos = []
        temporary = []
        for vod in ListRe:
            for value in vod:
                for x in value:

                    if x.tag == 'name':
                        title = x.text
                    if x.tag == 'id':
                        id = x.text
                    if x.tag == 'type':
                        tid = x.text
                    if x.tag == 'last':
                        last = x.text
                temporary.append({
                    "name": title,
                    "id": id,
                    "last": last
                })

        if len(temporary) > 0:
            idTxt = ''
            for vod in temporary:
                idTxt = idTxt + vod['id'] + ','
            if len(idTxt) > 1:
                idTxt = idTxt[0:-1]
                url = 'https://api.xinlangapi.com/xinlangapi.php/provide/vod/from/xlyun/at/xml/?ac=detail&ids=' + idTxt
                xmlTxt = self.custom_webReadFile(urlStr=url)
                jRoot = et(fromstring(xmlTxt))
                xmlList = jRoot.iter('list')
                for vod in xmlList:
                    for x in vod:
                        for v in x:
                            if v.tag == 'name':
                                title = v.text
                            if v.tag == 'id':
                                vod_id = v.text
                            if v.tag == 'pic':
                                img = v.text
                            if v.tag == 'note':
                                remarks = v.text
                            if v.tag == 'year':
                                vod_year = v.text
                            if v.tag == 'type':
                                type_name = v.text
                        if self.filterate == True and self.custom_RegexGetText(Text=type_name,
                                                                               RegexText=r'(伦理|倫理|福利)',
                                                                               Index=1) != '':
                            continue
                        vod_id = '{0}###{1}###{2}'.format(title, vod_id, img)
                        # vod_id='{0}###{1}###{2}###{3}###{4}###{5}###{6}###{7}###{8}###{9}###{10}'.format(title,vod_id,img,vod_actor,vod_director,'/'.join(type_name),'/'.join(vod_time),'/'.join(vod_area),vod_lang,vod_content,vod_play_url)
                        # print(vod_id)
                        videos.append({
                            "vod_id": vod_id,
                            "vod_name": title,
                            "vod_pic": img,
                            "vod_year": vod_year,
                            "vod_remarks": remarks
                        })
        return videos

    # 访问网页
    def custom_webReadFile(self, urlStr, header=None, codeName='utf-8'):
        html = ''
        if header == None:
            header = {
                "Referer": urlStr,
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36',
                "Host": self.custom_RegexGetText(Text=urlStr, RegexText='https*://(.*?)(/|$)', Index=1)
            }
        # import ssl
        # ssl._create_default_https_context = ssl._create_unverified_context#全局取消证书验证
        req = urllib.request.Request(url=urlStr, headers=header)  # ,headers=header
        with  urllib.request.urlopen(req) as response:
            html = response.read().decode(codeName)
        return html

    # 取剧集区
    def custom_lineList(self, Txt, mark, after):
        circuit = []
        origin = Txt.find(mark)
        while origin > 8:
            end = Txt.find(after, origin)
            circuit.append(Txt[origin:end])
            origin = Txt.find(mark, end)
        return circuit

    # 正则取文本,返回数组
    def custom_RegexGetTextLine(self, Text, RegexText, Index):
        returnTxt = []
        pattern = re.compile(RegexText, re.M | re.S)
        ListRe = pattern.findall(Text)
        if len(ListRe) < 1:
            return returnTxt
        for value in ListRe:
            returnTxt.append(value)
        return returnTxt

    # 取集数
    def custom_EpisodesList(self, html):
        ListRe = html.split('#')
        videos = []
        for vod in ListRe:
            t = vod.split('$')
            url = t[1]
            title = t[0]
            if len(url) == 0:
                continue
            videos.append(title + "$" + url)
        return videos

    # 取分类
    def custom_classification(self):
        xmlTxt = self.custom_webReadFile(
            urlStr='https://api.xinlangapi.com/xinlangapi.php/provide/vod/from/xlyun/at/xml/')
        tree = et(fromstring(xmlTxt))
        root = tree.getroot()
        classXml = root.iter('class')
        temporaryClass = {}
        for vod in classXml:
            for value in vod:
                if self.custom_RegexGetText(Text=value.text, RegexText=r'(福利|倫理片|伦理片)', Index=1) != '':
                    continue
                temporaryClass[value.text] = value.attrib['id']
                print("'{0}':'{1}',".format(value.text, value.attrib['id']))
        return temporaryClass


if __name__ == '__main__':
    from t4.core.loader import t4_spider_init

    spider = Spider()
    t4_spider_init(spider)
    print(spider.homeContent(True))
    print(spider.homeVideoContent())

# T=Spider()
# T. homeContent(filter=False)
# T.custom_classification()
# l=T.homeVideoContent()
# l=T.searchContent(key='柯南',quick='')
# l=T.categoryContent(tid='22',pg='1',filter=False,extend={})
# for x in l['list']:
# 	print(x['vod_name'])
# mubiao= l['list'][2]['vod_id']
# # print(mubiao)
# playTabulation=T.detailContent(array=[mubiao,])
# # print(playTabulation)
# vod_play_from=playTabulation['list'][0]['vod_play_from']
# vod_play_url=playTabulation['list'][0]['vod_play_url']
# url=vod_play_url.split('$$$')
# vod_play_from=vod_play_from.split('$$$')[0]
# url=url[0].split('$')
# url=url[1].split('#')[0]
# # print(url)
# m3u8=T.playerContent(flag=vod_play_from,id=url,vipFlags=True)
# print(m3u8)
