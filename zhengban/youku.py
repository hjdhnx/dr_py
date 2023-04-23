import time
import requests
import re
from hashlib import md5
import json


class YouKu:
    def __init__(self, url):
        self.url = "https://acs.youku.com/h5/mtop.youku.play.ups.appinfo.get/1.1/"
        self.int_time = int(time.time()) * 1000
        # self.vid = "XNTQwMTgxMTE2"
        self.video_url = url
        # 用于存储show_id,videoId
        self.params = {}
        self.get_current_showid()
        self.cookie = ''
        self.cookie_dict = {}
        self.language = {
            "ja": "日语",
            "guoyu": "国语",
            "default": "默认",
            "yue": "粤语",
        }

    def get_current_showid(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
        }
        res = requests.get(self.video_url, headers=headers).text
        current_showid = re.findall("id_(.*?).html", res)[0]
        # video_id = re.findall("videoId: '(\d+)'", res)[0]
        self.params = {"show_id": current_showid}

    def get_steal_params(self):
        return json.dumps({
            "ccode": "0502",
            "client_ip": "192.168.1.1",
            "utid": re.findall("cna=(.*?);", self.cookie)[0],
            "client_ts": self.int_time,
            "version": "2.1.63",
            "ckey": "DIl58SLFxFNndSV1GFNnMQVYkx1PP5tKe1siZu/86PR1u/Wh1Ptd+WOZsHHWxysSfAOhNJpdVWsdVJNsfJ8Sxd8WKVvNfAS8aS8fAOzYARzPyPc3JvtnPHjTdKfESTdnuTW6ZPvk2pNDh4uFzotgdMEFkzQ5wZVXl2Pf1/Y6hLK0OnCNxBj3+nb0v72gZ6b0td+WOZsHHWxysSo/0y9D2K42SaB8Y/+aD2K42SaB8Y/+ahU+WOZsHcrxysooUeND",
        })

    def get_biz_params(self):
        return json.dumps({
            "vid": re.findall("id_(.*?).html", self.video_url)[0],
            "play_ability": "16782592",  # 写死在js里的
            "current_showid": self.params["show_id"],
            "preferClarity": "4",  # 貌似是清晰度
            "extag": "EXT-X-PRIVINF",  # 写死在js里的
            "master_m3u8": "1",
            "media_type": "standard,subtitle",
            "app_ver": "2.1.63",
            "drm_type": "19",
            "key_index": "web01",

        })

    def get_ad_params(self):
        return json.dumps({
            "vs": "1.0",
            "pver": "2.1.63",
            "sver": "2.0",
            "site": 1,
            "aw": "w",
            "fu": 0,
            "d": "0",
            "bt": "pc",
            "os": "mac",
            "osv": "",
            "dq": "auto",
            "atm": "",
            "partnerid": "null",
            "wintype": "interior",
            "isvert": 0,
            "vip": 0,
            "p": 1,
            "rst": "mp4",
            "needbf": 2,
            "avs": "1.0",
        })

    def get_data(self):
        return json.dumps({"steal_params": self.get_steal_params(), "biz_params": self.get_biz_params(),
                           "ad_params": self.get_ad_params()})

    def join_params(self):
        data = self.get_data()
        return {
            'jsv': '2.5.8',
            'appKey': '24679788',
            't': self.int_time,
            'sign': md5(str(
                re.findall("m_h5_tk=(.*?)_", self.cookie)[0] + "&" + str(self.int_time) + "&" + "24679788" + "&" + str(
                    data)).encode("utf8")).hexdigest(),
            'api': 'mtop.youku.play.ups.appinfo.get',
            'v': '1.1',
            'timeout': '20000',
            'YKPid': '20160317PLF000211',
            'YKLoginRequest': 'true',
            'AntiFlood': 'true',
            'AntiCreep': 'true',
            'type': 'jsonp',
            'dataType': 'jsonp',
            'callback': 'mtopjsonp3',
            "data": f"{data}"
        }

    def loads_jsonp(self, _jsonp):
        try:
            return json.loads(re.match(".*?({.*}).*", _jsonp, re.S).group(1))
        except:
            raise ValueError('Invalid Input')

    def start(self):
        headers = {
            "Accept": "*/*",
            "Host": "acs.youku.com",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
            "cookie": self.cookie,
            "Referer": "https://v.youku.com/"
        }
        res = requests.get(self.url, params=self.join_params(), headers=headers)
        print(res.text)


if __name__ == '__main__':
    YouKu().start()
