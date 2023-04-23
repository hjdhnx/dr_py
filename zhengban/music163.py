from binascii import hexlify
import random
from Crypto.Cipher import AES
from base64 import b64encode
from Crypto.Util.Padding import pad
import requests


class music163:
    def __init__(self, url):
        self.url = url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36¬"
        }
        self.vid = self.url.split("id=")[-1]
        self.second_key = "".join(
            random.choices(list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'), k=16))

    def get_data(self, vid):
        return f'{{"ids":"[{vid}]","level":"standard","encodeType":"aac","csrf_token":""}}'

    def get_params(self, key, iv, data):
        cryptos = AES.new(key=key.encode(), mode=AES.MODE_CBC, iv=iv.encode())
        cryptos1 = AES.new(key=self.second_key.encode(), mode=AES.MODE_CBC, iv=iv.encode())
        first_data = b64encode(cryptos.encrypt(pad(data.encode(), 16)))
        second_data = cryptos1.encrypt(pad(first_data, 16))
        return b64encode(second_data).decode()

    def get_encSecKey(self, key):
        rs = pow(int(hexlify(key[::-1].encode('utf-8')), 16), 65537,
                 157794750267131502212476817800345498121872783333389747424011531025366277535262539913701806290766479189477533597854989606803194253978660329941980786072432806427833685472618792592200595694346872951301770580765135349259590167490536138082469680638514416594216629258349130257685001248172188325316586707301643237607)
        return hex(rs)[2:]

    def start(self):
        params = {
            "params": self.get_params("0CoJUm6Qyw8W8jud", "0102030405060708", self.get_data(self.vid)),
            "encSecKey": self.get_encSecKey(self.second_key)
        }
        res = requests.post("https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token=", data=params,
                            headers=self.headers)
        print(res.json())
        return res.json()


if __name__ == '__main__':
    music163().start()
