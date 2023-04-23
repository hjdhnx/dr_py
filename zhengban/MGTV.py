import base64
import requests
import uuid
import time


class MGTV:
    def __init__(self, url):
        self.url = url

    def get_video_id(self):
        return self.url.split("/", 5)[-1].split(".")[0]

    def get_pm2(self):
        did = "e6e13014-393b-43e7-b6be-2323e4960939"
        suuid = uuid.uuid4()
        pno = "1030"
        # tk2 = self.encode_tk2(did, pno)
        params = {
            "did": did,
            "suuid": suuid,
            "cxid": "",
            "tk2": self.encode_tk2(did, pno),
            "type": "pch5",
            "video_id": self.get_video_id(),
            "_support": "10000000",
            "auth_mode": "1",
            "src": "",
            "abroad": "",
        }
        res = requests.get("https://pcweb.api.mgtv.com/player/video", params=params).json()
        return res['data']['atc']['pm2']

    def encode_tk2(self, did="e6e13014-393b-43e7-b6be-2323e4960939", pno="1030"):
        tk2 = bytes(f"did={did}|pno={pno}|ver=0.3.0301|clit={int(time.time())}".encode())
        tk2 = base64.b64encode(tk2).decode().replace("/\+/g", "_").replace("/\//g", "~").replace("/=/g", "-")
        tk2 = list(' '.join(tk2).split())
        tk2.reverse()
        return "".join(tk2)

    def start(self):
        params = {
            "_support": "10000000",
            "tk2": self.encode_tk2(),
            "pm2": self.get_pm2(),
            "video_id": self.get_video_id(),
            "type": "pch5",
            "auth_mode": "1",
            "src": "",
            "abroad": "",
        }
        res = requests.get("https://pcweb.api.mgtv.com/player/getSource", params=params).json()
        print(res)
        return res


if __name__ == '__main__':
    MGTV().start()
