import requests
import execjs
import re


class xigua:
    def __init__(self, url):
        self.url = url
        if "wid_try=1" not in self.url:
            self.url = self.url + "&wid_try=1"
        self.headers = {
            "referer": self.url,
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
        }
        self.nonce = self.getNonce()

    def getNonce(self):
        res = requests.get(self.url, headers=self.headers)
        return res.cookies.get("__ac_nonce")

    def getSign(self):
        jscode = execjs.compile(open("./js/xigua.js").read())
        ctx = jscode.call("getSign", self.nonce, self.url)
        return f"__ac_nonce={self.nonce};__ac_signature={ctx};__ac_referer={self.url}"

    def start(self):
        self.headers.update({"cookie": self.getSign()})
        html = requests.get(self.url, headers=self.headers)
        res = re.findall("window._SSR_HYDRATED_DATA=(.*?)</script>", html.text)[0].replace("undefined", 'null')
        print(res)
        return res


if __name__ == '__main__':
    xigua().start()
