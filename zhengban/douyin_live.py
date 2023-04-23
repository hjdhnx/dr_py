import requests
import re


class douYinLive:
    def __init__(self, url):
        self.url = url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36¬"
        }

    def parse(self, html):
        return re.findall('flv_pull_url":(.*?})', html)[0]

    def start(self):
        res = requests.get(self.url, headers=self.headers)
        print(self.parse(res.text))


if __name__ == '__main__':
    douYinLive().start()
