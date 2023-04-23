import requests
import re
from base64 import b64decode
import json


class huya:
    def __init__(self, url):
        self.url = url

    def decodeStream(self, stream):
        return b64decode(stream).decode()

    def start(self):
        res = requests.get(self.url).text
        hyplay = re.findall('hyPlayerConfig\s=\s(.*?});', res, re.S)
        stream = json.loads(self.decodeStream(eval(hyplay[0])['stream']).replace("amp;", ""))
        print(stream)
        return stream


if __name__ == '__main__':
    huya().start()
