import requests
import re


class KeQq:
    def __init__(self, url):
        self.url = url
        self.headers = {
            "Referer": "https://ke.qq.com/",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36¬",
            "Cookie": ""
        }
        self.taid = re.findall("taid=(\d+)", self.url)[0]
        self.vid = ""

    def getParams(self):
        vid = re.findall("vid=(\d+)", self.url)
        if vid:
            return self.url.split("#")[0].split("/")[-1], vid[0]
        html = requests.get(self.url, headers=self.headers)
        params = re.findall(f"data-tid=(\d+)\sdata-taid={self.taid}\sdata-vid=(\d+)", html.text)
        return params[0]

    def getSign(self):
        term_id, fileId = self.getParams()
        self.vid = fileId
        res = requests.get("https://ke.qq.com/cgi-bin/qcloud/get_token", params={"term_id": term_id, "fileId": fileId},
                           headers=self.headers).json()
        return res["result"]

    def start(self):
        params = self.getSign()
        res = requests.get(f"https://playvideo.qcloud.com/getplayinfo/v2/1258712167/{self.vid}",
                           params=params, headers=self.headers)
        print(res.text)
        return res.json()


if __name__ == '__main__':
    KeQq("").start()
