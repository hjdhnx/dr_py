import requests


class DouYin:
    def __init__(self, url):
        self.url = url
        self.headers = {

            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/89.0.4389.114 Safari/537.36 "
        }

    def get_mid(self):
        res = requests.get(self.url, headers=self.headers)
        return res.url.split("/", 6)[-2]

    def start(self):
        url = f"https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={self.get_mid()}"
        res = requests.get(url, headers=self.headers)
        print(res.json())
        return res.json()


if __name__ == '__main__':
    DouYin().start()
