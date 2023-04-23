import requests

import re


class sohu:
    def __init__(self, url):
        self.url = url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36¬"
        }

    def get_vid(self):
        res = requests.get(self.url, headers=self.headers)
        vid = re.findall('var vid="(\d+)";', res.text)
        if len(vid) > 0:
            return vid[0]
        return re.findall('data-vid="(\d+)"', res.text)[0]

    def start(self):
        params = {
            "vid": self.get_vid(),
            "ver": "21",
            "ssl": "1",
            "pflag": "pch5",
        }
        res = requests.get("https://hot.vrs.sohu.com/vrs_flash.action", params=params, headers=self.headers)
        return res.json()


if __name__ == '__main__':
    sohu().start()
