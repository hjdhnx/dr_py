import requests
import re
import json


class haokan:
    def __init__(self, url):
        self.url = url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36¬",
        }

    def getJson(self, text):
        res = re.findall("PRELOADED_STATE__\s=\s(.*?);", text)[0]
        res = json.loads(res)
        return res

    def start(self):
        res = requests.get(self.url, headers=self.headers).text
        return self.getJson(res)


if __name__ == '__main__':
    haokan().start()
