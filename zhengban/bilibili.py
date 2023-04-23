import requests
import re


class Bili:
    def __init__(self, url):
        self.url = url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36¬"
        }

    def start(self):
        res = requests.get(self.url)
        result = re.findall("window.__playinfo__=(.*?)</script>", res.text)
        print(result[0])
        return result[0]


if __name__ == '__main__':
    Bili().start()
