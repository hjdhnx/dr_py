import execjs
import requests
import re
import time


class DouYu:
    def __init__(self, room_id):
        self.room_id = room_id
        self.int_time = int(time.time())
        self.did = "3966acse00dd10qer895bdca00031601"

    def get_ub98484234(self):
        res = requests.get(f"https://www.douyu.com/{self.room_id}").text
        ub98484234 = re.findall("(function ub98484234.*?})var", res)[0]
        var = re.findall("var\sv\s=\s(.*?)[.]slice", ub98484234)[0]
        var1 = re.findall(f"(var {var}=.*?);", res)[0]
        return f"var CryptoJS = require('crypto-js');{var1};{ub98484234}"

    def get_sign(self):
        js = execjs.compile(self.get_ub98484234())
        res = js.call("ub98484234", self.room_id, self.did, self.int_time)
        return res.split("sign=")[-1]

    def get_params(self):
        return {
            'v': f'2201{time.strftime("%Y%m%d", time.localtime())}',
            'did': self.did,
            'tt': self.int_time,
            'sign': self.get_sign(),
            'cdn': "tct-h5",
            'rate': '0',
            'ver': 'Douyu_221041305',
            'iar': '0',
            'ive': '1',
            'hevc': '0',
            'fa': '1',
        }

    def start(self):
        res = requests.post(f"https://www.douyu.com/lapi/live/getH5Play/{self.room_id}", data=self.get_params()).json()
        print(res)


if __name__ == '__main__':
    DouYu().start()
