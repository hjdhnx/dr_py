import requests
import execjs
from urllib.parse import quote
import json
import re


class qqmusic:
    def __init__(self, url):
        self.url = url
        self.vid = ""
        self.headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36¬"
        }
        self.js = execjs.compile(open("./js/qqmusic.js").read())
        self.get_vid()

    def get_vid(self):
        res = requests.get(self.url).text
        vid = re.findall('"songmid":"(.*?)",', res)[0]
        self.vid = vid

    def get_data(self):
        return json.dumps({"req": {"module": "CDN.SrfCdnDispatchServer", "method": "GetCdnDispatch",
                                   "param": {"guid": "12345678", "calltype": 0, "userip": ""}},
                           "req_0": {"module": "vkey.GetVkeyServer", "method": "CgiGetVkey",
                                     "param": {"guid": "12345678", "songmid": [self.vid], "songtype": [0],
                                               "loginflag": 1, "platform": "20"}},
                           "comm": {"format": "json", "ct": 24, "cv": 0}})

    def join_url_params(self):
        params = {
            "sign": self.js.call("getSign", self.get_data()),
            # "format": "json",
            # "inCharset": "utf8",
            # "outCharset": "utf-8",
            # "notice": "0",
            # "platform": "yqq.json",
            # "needNewCode": "0",
            "data": quote(str(self.get_data()))
        }
        return f'https://u.y.qq.com/cgi-bin/musics.fcg?sign={params["sign"]}&data={params["data"]}'

    def start(self):
        res = requests.get(self.join_url_params())
        print(res.text)
        return res.json()


if __name__ == '__main__':
    qqmusic().start()
