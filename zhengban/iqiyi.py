import requests
import execjs
import re
import time
from urllib.parse import quote, unquote


class iqiyi:
    def __init__(self, url):
        self.url = url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36¬"
        }
        self.authkey = self.load_auth_js()
        self.cmd5js = self.load_cmd5x_js()

    def load_auth_js(self):
        return execjs.compile(open("./js/iqiyi.js").read())

    def load_cmd5x_js(self):
        return execjs.compile(open("./js/cmd5x.js").read())

    def get_tvid(self):
        res = requests.get(self.url, headers=self.headers)
        # print(res.text)
        tvid = re.findall("tvid=(.*?)&aid", res.text)[0]
        vid = re.findall('"vid":"(.*?)",', res.text)[0]
        # print(tvid)
        return tvid, vid

    def join_params(self):
        tvid, vid = self.get_tvid()
        _time = int(time.time() * 1000)
        params = {
            "tvid": tvid,
            "bid": "300",
            "vid": vid,
            "src": "01080031010000000000",
            "vt": "0",
            "rs": "1",
            "uid": "",
            "ori": "pcw",
            "ps": "1",
            "k_uid": "1bf80ab6e72de7ab4a42f4db91bd530b",
            "pt": "0",
            "d": "0",
            "s": "",
            "lid": "",
            "cf": "",
            "ct": "",
            "authKey": self.authkey.call("auth", self.authkey.call("auth", "") + f"{_time}{tvid}"),
            "k_tag": "1",
            "ost": "undefined",
            "ppt": "undefined",
            "dfp": "a16da00a581aa149139fe169e3914993e4ff9cb705a50e3a41fc7927f988f2cb3e",
            "locale": "zh_cn",
            "prio": quote('{"ff":"f4v","code":2}'),
            "pck": "",
            "k_err_retries": "0",
            "up": "",
            "qd_v": "2",
            "tm": _time,
            "qdy": "a",
            "qds": "0",
            "k_ft1": "706436220846084",
            "k_ft4": "36283952406532",
            "k_ft5": "1",
            "bop": quote(
                '{"version":"10.0","dfp":"a16da00a581aa149139fe169e3914993e4ff9cb705a50e3a41fc7927f988f2cb3e"}'),
            "ut": "0"
        }
        temp = "/dash?"
        for k, v in params.items():
            temp += k + "=" + str(v) + "&"
        vf = self.cmd5js.call("parse_vf", temp[:-1])
        params['vf'] = vf
        # requests 会再次进行url编码，所以一开始怎么弄都不对！！！！这里要解码！！
        params["bop"] = unquote(params["bop"])
        params["prio"] = unquote(params["prio"])
        return params

    def start(self):
        params = self.join_params()
        res = requests.get("https://cache.video.iqiyi.com/dash", params=params, headers=self.headers)
        print(res.text)


if __name__ == '__main__':
    iqiyi().start()
