#coding=utf-8
#!/usr/bin/python
import sys
sys.path.append('..') 
from base.spider import Spider
import requests
import json
import base64

class Spider(Spider):
	def getDependence(self):
		return ['py_ali']
	def getName(self):
		return "py_yunso"
	def init(self,extend):
		self.ali = extend[0]
		print("============py_yunso============")
		pass
	def isVideoFormat(self,url):
		pass
	def manualVideoCheck(self):
		pass
	def homeContent(self,filter):
		result = {}
		return result
	def homeVideoContent(self):
		result = {}
		return result

	def categoryContent(self,tid,pg,filter,extend):
		result = {}
		return result

	header = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 12; V2049A Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36",
		"origin": "https://www.upyunso.com/"
	}

	def detailContent(self,array):
		return self.ali.detailContent(array)

	def searchContent(self,key,quick):
		url = "https://api.upyunso.com/search?keyword={0}&page=1&s_type=2".format(key)
		rsp = requests.get(url=url, headers=self.header)
		vodList = json.loads(base64.b64decode(rsp.text))['result']['items']
		videos = []
		for vod in vodList:
			vid =vod['page_url']
			name = vod['title']
			if 'aliyundrive.com' in vid:
				videos.append({
					"vod_id": vid,
					"vod_name": name,
					"vod_pic": "https://inews.gtimg.com/newsapp_bt/0/13263837859/1000",
					"vod_remarks": vod['insert_time']
				})

		result = {
			'list':videos
		}
		return result

	def playerContent(self,flag,id,vipFlags):
		return self.ali.playerContent(flag,id,vipFlags)

	config = {
		"player": {},
		"filter": {}
	}
	header = {}

	def localProxy(self,param):
		return [200, "video/MP2T", action, ""]