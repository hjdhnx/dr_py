import requests
import re


class kuaishou:
    def __init__(self, url):
        self.url = url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Mobile Safari/537.36",
            "Referer": self.url
        }

    def start(self):
        json_data = requests.get(self.url, headers=self.headers, allow_redirects=True).text
        res = re.findall('type="video/mp4" src="(.*?)"', json_data)[0]
        print(res)
        return res


if __name__ == '__main__':
    kuaishou().start()
