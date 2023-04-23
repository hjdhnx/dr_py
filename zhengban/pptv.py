import base64
import time
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA
import math
import random
import execjs
import uuid
import requests
import re


class PPTV:
    def __init__(self,url):
        self.url = "https://oneplay.api.pptv.com/ups-service/play"
        self.video_url = url
        self.pk = '\n'.join([
            '-----BEGIN PUBLIC KEY-----',
            'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqe6XLQF2JmXWgfh09t8TTZsOb6bnj+duiWw4G7pd5Uo1/DN7Xij3Tys9E7XBX0gdXKYI9j+6Fr45bM28fzl4AxUxnhzmbExRt1NJarDGMKo49ViRg1VbL+Wh9kRi+rAxBisdRiP2JEAL+Awqu80chZxxdyoI1k3fSLoZsv/PGkwolE71qsEM4BO1J9RWNp0wlNGqgR+bTwLKkoe7oiZaKaMsSBWNIBDkwgGKFJZzXMXMnqGsDmfbdi32j6hW9DdrxjCx/i9Nzahd1TWVnw9O1AHL5PD5kM3HzqkAewBu38sZxw8DSGYqG0fgVAQtiLHhlD/19F4NKxqL8IVCinMBHQIDAQAB',
            '-----END PUBLIC KEY-----'
        ])
        self.publicKey = RSA.importKey(self.pk)
        self.js = execjs.compile(open("./js/pptv.js").read())
        self.headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "no-cache",
            "referer": "https://v.pptv.com/",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
        }

    def getRamNumber(self, e):
        t = ""
        for i in range(e):
            t += str(hex(math.floor(16 * random.random()))[2:])
        return t.upper()

    def encrypt(self, message):
        cipher = Cipher_pkcs1_v1_5.new(self.publicKey)
        cipher_text = base64.b64encode(cipher.encrypt(message))
        return cipher_text

    def get_cipher(self):
        t = self.getRamNumber(48)
        i = self.getRamNumber(16)
        res = self.encrypt(f"{t},{i}".encode('utf8'))
        encryptParams = self.get_3des(self.get_msg(), t, i)
        return {"cipher": res.decode(), "encryptParams": encryptParams}

    def get_3des(self, msg, key, iv):
        return self.js.call("encrypted", msg, key, iv)

    def get_msg(self):
        js_result = self.js.call("get3rdKeyRandom")
        type = 'mhpptv'
        appId = 'pptv.web.h5'
        appPlt = 'web'
        appVer = '1.0.4'
        channel = 'sn.cultural'
        sdkVer = '1.5.0'
        cid = self.get_cid()
        allowFt = '0,1,2,3'
        rf = '0'
        ppi = '302c393939'
        o = 'www.google.com'
        ahl_ver = '1'
        ahl_random = js_result['random_hex']
        ahl_signa = js_result['signature_hex']
        vvId = uuid.uuid4()
        version = '1'
        https = 'true'
        streamFormat = 3
        result = f"type={type}&appId={appId}&appPlt={appPlt}&appVer={appVer}&channel={channel}&sdkVer={sdkVer}&cid={cid}&allowFt={allowFt}&rf={rf}&ppi={ppi}&o={o}&ahl_ver={ahl_ver}&ahl_random={ahl_random}&ahl_signa={ahl_signa}&vvId={vvId}&version={version}&https={https}&streamFormat={streamFormat}"
        return result

    def get_cid(self):
        res = requests.get(self.video_url, headers=self.headers).text
        cid = re.findall('var webcfg = {"id":(.*?),', res)
        return cid[0]

    def get_sign(self):
        return self.js.call("get3rdKeyRandom")

    def start(self):
        result = self.get_cipher()
        params = {
            "cipher": result.get("cipher"),
            "encryptParams": result.get("encryptParams"),
            "format": "jsonp",
            "cb": f"getPlayEncode_{int(time.time())}"

        }

        res = requests.get(self.url, params=params, headers=self.headers)
        print(res.text)


if __name__ == '__main__':
    PPTV().start()
