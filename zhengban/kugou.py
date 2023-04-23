import requests


class KuGou:
    def __init__(self, url):
        self.url = url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36¬"
        }
        self.base = url.split("#")[-1].split("&")
        self.hash = self.base[0].split("=")[-1]
        self.album_id = self.base[1].split("=")[-1]

    def start(self):
        params = {
            "r": "play/getdata",
            "hash": self.hash,
            "album_id": self.album_id,
            "mid": "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456"
        }
        res = requests.get("https://wwwapi.kugou.com/yy/index.php?", params=params, headers=self.headers)
        print(res.json())
        return res.json()


if __name__ == '__main__':
    KuGou().start()
