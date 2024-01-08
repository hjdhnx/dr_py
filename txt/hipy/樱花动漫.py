#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : 樱花动漫.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Author's Blog: https://blog.csdn.net/qq_32394351
# Date  : 2024/1/7

import sys

sys.path.append('..')
try:
    from base.spider import Spider as BaseSpider
except ImportError:
    from t4.base.spider import BaseSpider
import json
import time
import base64
import re
import io
import tokenize
from Crypto.Cipher import AES, PKCS1_v1_5 as PKCS1_cipher
from Crypto.Util.Padding import unpad
from Crypto.PublicKey import RSA

from cachetools import cached, TTLCache  # 可以缓存curd的函数，指定里面的key

"""
配置示例:
t4的配置里ext节点会自动变成api对应query参数extend,但t4的ext字符串不支持路径格式，比如./开头或者.json结尾
api里会自动含有ext参数是base64编码后的选中的筛选条件
 {
    "key":"hipy_t4_樱花动漫",
    "name":"樱花动漫(hipy_t4)",
    "type":4,
    "api":"http://192.168.31.49:5707/api/v1/vod/樱花动漫",
    "searchable":1,
    "quickSearch":1,
    "filterable":1,
    "ext":"https://jihulab.com/qiaoji/open/-/raw/main/yinghua"
}
"""


def envkey(self, url: str):
    return url


# 全局变量
gParam = {
    "HomeDict": {},
    "TypeDict": {},
}


class Spider(BaseSpider):  # 元类 默认的元类 type
    api_qj: str = 'https://jihulab.com/qiaoji/open/-/raw/main/yinghua'
    private_key: str = 'MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDA+5YTt3w1q/0WGw+TWyCSHTAeYiwBqAqDWot1u/1hoeANpED8gtW1AxB1mYNDQ+9eR8Ml+JC13+ME6RHjEbN4+n9V9OP90c81G0qSjBQ/DKQiMIFjbTH97RjVMtswf96tqwe4Rs/DT2ym6MP4P7QvJcxrFz5VVQXyOtUxhpMc9oktWuk0XKE8Mozu1FM879RknlM6WmJL85Wl/BnZrd+/AQbzziceELGrBfjbc1UOFAxYq2kA10H3o+Z4oOIODxUtXeh4R2oH3vHb4Ynnw6reXED5KsE3u1EO5HMQZyN16TZMTIps32bPe+vQlAT6V5nGcqXGT9fntjqIxJB0T9G3AgMBAAECggEBAKP6Yuh4BZP5g0CwV8jHKuLc6FE469mwdtZsLooo5cF68c3Fnu6xIXQAmZDDk3SpmhCLe7edASF5jwZSIL/H/68xcteQEdZP2/htKy1g16dHT4Q5oQfh9hOkznACGZuZW5ZH+HRNvyZfK5ybtkEPqERTouHwSyfo6feMpDDD/+cf3h1//7JKXKA7JPEU420YucsjQwjMuu5xdPa0TPqEc5mIbOBj753Pzn4GCScM+FRqJWr2x8e+KDPcPY8CUDLBSWxGLsB0A7+bEq/EiAQkbx09QKTwwxRLgVXjBbvyPB8BOuJpPM9BHx+vFcm5WSbkJdRI4qVFtEdsN/gDfFkwcjkCgYEA8Z8i/fTFRnzyvp9Pp8E+bSaYlvpTLUZ1KYNStaDg/BqlYGgGK1Jh90qjvRbBoiIjeBQd3IFLT4pFdd7Z9drLFdvqB22SNeVQU57kir/B6NY5G7yOjXB4qN17F4S3GubYIEcjF0W1tG/uOqqzb8FxrLJTK8WiFudbBt2ioCO4pJsCgYEAzHd8MctmD1Z1eM/xusvX1yCwGpxBuHT+ymThzLXyI6Ej0Q50jOQlf3cTyY/FgGbvAMz+oBybkEwE80gu7CPi0WPs+yCpAIB4+Th7afsrRylQI1ZWoRovaRmsyjnkIw0Mnj06VYNYPtkzm/OViRIqf4ESTTGas24bDm5DuwM9gxUCgYBwg4BR7gdnWYvYRGtdXNlrDowD0jGlZaftWt/LAE2EWAwmpooo5kYEV9eDl/M3QtptckCti++77FGIH+wzVl03op6KMvXg7xXGurkF+2GawRb62YUwS+2EBQ7q1rxFZLXD4hxvG+EPUwgGfbLtGZGLr8aXHYLrU3TJ769pDvlOfQKBgAFlAzzXtU9/eHele3GZuFQoTeswi6Y1bhN1UrDxwMALdlITtinL2JGg/0qNp3wzt4ea3lW7PDhkvFfocyF7MS3ab6Ba3aw6NBkHEJhtdSMcHgbPrPGWWyJtYWdTs8GlciOWKVKx/aUYGCkFJUz1CcMq3zQVlYeJxbd4ew/Iet/tAoGBAMRfvG1iLQAlS3AGaQeRwVxnvpciDn+7/sUCf8DEOk8Bqg4/ytJDTDrWufCtwmpsXmp6AUQig9mNKj7z26wSNbwYdzPsncK+sGRlS7eLAzzcv1a+1pghOOGDuQNzwlFOcauhkrcqjeKmu7OiKD48pvh3ZICiIWS1YL7LuMfUwHRJ'
    key: str = 'fQiG3YWTpQEYHNFTxJXCBaZrcCkkpfxH'
    iv: str = '1238389483762837'
    token: str = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJBcHBUbyIsImlhdCI6MTcwMDA3MTcwMiwiZXhwIjoxNzMxNjA3NzAyLCJuYmYiOjE3MDAwNzE3MDIsInN1YiI6IkFwcFRvIiwianRpIjoiYzRjNTAzOTQxYTM4NWI1MDMyMTAyYmY3Yzk1OGY4MzEiLCJkYXRhIjp7InVzZXJfaWQiOjI0ODc1NCwidXNlcl9jaGVjayI6ImUzYmQ3NmNhNTJhMGY4NjAwMTdjNjdkZGUwN2QzZTM3IiwidXNlcl9uYW1lIjoiaGV6aWh1aSJ9fQ.4LWs3rNL-os8_Pqa9LgKtvVG5f0aIxVyAjYIagvO1F4'
    ic: str = 'bmXes2xsCWvsSdfYav0s9D78Ly7w1o%2BOYXApKx6SUd4NWKsTsapbS52l7y%2FsTVCM2kcoLws2jryaDQlHLse5fxD2B2VXZXfaQo0eMTOv2Xq7CKoPa51uVt8WiIY2SPztc7wxGE89%2Fcw2Q3n85uUT3A%3D%3D'
    api: str = 'http://60.204.185.245:7090/appto/v1'
    api_cofig: str = api + '/config/get?p=android'
    api_home: str = api + '/home/cateData?id=1'
    api_cate: str = api + '/vod/getLists'
    api_search: str = api + '/vod/getVodSearch'
    api_detail: str = api + '/vod/getVod?__platform=android&__ic=' + ic
    api_parse: str = api + '/parsing/proxy'

    def getName(self):
        return "樱花动漫"

    @cached(cache=TTLCache(maxsize=3, ttl=3600), key=envkey)
    def get_init_api(self, url):
        try:
            print('get_init_api请求URL:', url)
            r = self.fetch(url)
            ret = self.decode_rsa(r.text[1:])
            return ret
        except Exception as e:
            print(f'get_init_api请求URL发生错误:{e}')
            return {}

    def init_extend(self, url):
        ret = self.get_init_api(url)
        if ret.get('key'):
            self.key = ret.get('key')
        if ret.get('ic'):
            self.ic = ret.get('ic')
        if ret.get('token'):
            self.token = ret.get('token')
        if ret.get('url') and ret.get('api'):
            api = ret.get('url') + ret.get('api')
            self.api = api
            self.api_cofig: str = api + '/config/get?p=android'
            self.api_home: str = api + '/home/cateData?id=1'
            self.api_cate: str = api + '/vod/getLists'
            self.api_search: str = api + '/vod/getVodSearch'
            self.api_detail: str = api + '/vod/getVod?__platform=android&__ic=' + self.ic
            self.api_parse: str = api + '/parsing/proxy'

    def init_api_ext_file(self):
        """
        这个函数用于初始化py文件对应的json文件，用于存筛选规则。
        执行此函数会自动生成筛选文件
        @return:
        """
        ext_file = __file__.replace('.py', '.json')
        print(f'ext_file:{ext_file}')
        ext_file_dict = self.homeContent(True)['filters']
        with open(ext_file, mode='w+', encoding='utf-8') as f:
            f.write(json.dumps(ext_file_dict, ensure_ascii=False))

    def init(self, extend=""):
        """
        初始化加载extend，一般与py文件名同名的json文件作为扩展筛选
        @param extend:
        @return:
        """
        # cipher_text = 'qebgGqODxKrWujD2TaoZoyh6aeYntZLsTaZW8MQvVNORiHLLi/o/cEEEXkSs1vfHEuiURxMTr9zL2Kwbffz2pDvLCamrK1tuxIcczsaI7cfsAh5gcgyzOOdZUszoU45ZgS9Bi4HZ3RDHZAWEqP0JyTaH32oDxgO9nx/xhe1xyVRyj9y5gkfPVt2AP94I8/DwDI9CEstcPzGfRNHYxlCuGMtnMvVwzonmkNDyOw+N5xr2ZI3P8O1cj04mCEAE6/d2tGSU/o+EOyWVLWWw0R3hoduHvjAtuMbBt6WNCcsL51zWceiTcsl34acqd9Pya3lA52ZFRojME/R4zdTzMbvwrOEF3Up0eB58//+NM6k4tW+cBNAHDGgO8t7hcfSG/TnJLQ7Gigrn899dGbFeQMCEQf0zxMxfgYBDkADs0aza9N2QIXChgEDVFDvw0vE2m6b+bJfswmbrhNEIM//95XpMv68HEP3jCTwFEehattwHjyYE4fJoH3OtPO++pDiZltaxdizfFD6WmTO+v4qub1QfpUEXWHzG6nqDA9MioigiTRdRAb4PEMioBCJS5/gel+PGRja1cR1NtBjl4RKpSPstwrmczG8qKQrn2Zjwkz8f4OdnEBKRLaWzb/hVDAQgqRfUyohEdnQyocaYsnB5lJoMSp93QCzwAuHYueyMh2fNpcemWGfs58wrZr5VFSBaQDYv/HjsNntoPaCDpoQIV9DJKiqQsiYMblsz/Mdbnlfd1vI5X69TVPvItzh26zXjgpFBKsiFDOtvd3bNe92XnTH3jiDgBQbqoL6jUbvhNQapqRUZxovWk30UQ0YTQnqODkorKdrEB1IeNhKt0epurJG/G7A6DQ6/6lZ7pAwlYVlfXzFgZOGNb1Hs52j2F+sGvgWY00BAH1eHtpHPPdckL25JMKai3QDQUAVBxAI8njCmcNUPfl9kDZe62QMNJwaZKD9eaOjNrdVsKjah9gkiWL8BnDxJeGErZyrvKhyqg0fwNvyn8wEfeUlwRzfDysrvjdBz3'
        # ret = self.decode_rsa(cipher_text[1:])
        # print(ret)
        # extend内容进行解密后可以获取key,iv,token等参数
        # print('gParam:',gParam)
        if extend.startswith('http'):
            self.init_extend(extend)
        else:
            self.init_extend(self.api_qj)

    def isVideoFormat(self, url):
        pass

    def manualVideoCheck(self):
        pass

    def homeContent(self, filterable=False):
        """
        获取首页分类及筛选数据
        @param filterable: 能否筛选，跟t3/t4配置里的filterable参数一致
        @return:
        """
        filter_names = {
            'area': '地区',
            'class': '分类',
            'director': '导演',
            'lang': '语言',
            'star': '明星',
            'state': '状态',
            'version': '版本',
            'year': '年份',
        }
        r = self.fetch(self.api_cofig)
        ret = r.json()
        data = self.decode(ret['data'])
        # print(data)
        result = {}
        classes = []
        filters = {}
        type_dict = {}
        for tp in data.get('get_type') or []:
            classes.append({
                'type_name': tp['type_name'],
                'type_id': tp['type_id']
            })
            type_dict[str(tp['type_id'])] = tp['type_name']
            tp_filters = []
            for key, value in tp['type_extend'].items():
                if value:
                    tp_filters.append({
                        'key': key,
                        'name': filter_names.get(key) or key,
                        'value': [{'n': '全部', 'v': ''}] + [{'n': i, 'v': i} for i in value.split(',') if i]
                    })
            filters[tp['type_id']] = tp_filters

        result['class'] = classes
        if filterable:
            result['filters'] = filters
        global gParam
        gParam['HomeDict'].update(result)
        gParam['TypeDict'].update(type_dict)
        return result

    def homeVideoContent(self):
        """
        首页推荐列表
        @return:
        """
        r = self.fetch(self.api_home)
        ret = r.json()
        data = self.decode(ret['data'])
        # print(data)
        d = []
        for section in data['sections']:
            items = section['items']
            for item in items:
                d.append({
                    'vod_name': item['vod_name'],
                    'vod_id': item['vod_id'],
                    'vod_pic': item['vod_pic'],
                    'vod_remarks': item['vod_remarks'],
                })
        result = {
            'list': d
        }
        return result

    def categoryContent(self, tid, pg, filterable, extend):
        """
        返回一级列表页数据
        @param tid: 分类id
        @param pg: 当前页数
        @param filterable: 能否筛选
        @param extend: 当前筛选数据
        @return:
        """
        page_count = 21  # 默认赋值一页列表21条数据
        fls = extend.keys()  # 哪些刷新数据
        # ?type_id=1&area=&lang=&year=&order=time&type_name=&page=1&pageSize=21
        params = {'page': pg, 'pageSize': page_count, 'tid': tid, 'type_name': gParam['TypeDict'].get(str(tid)) or ''}
        for fl in fls:
            params[fl] = extend[fl]
        r = self.fetch(self.api_cate, data=params)
        print(r.url)
        ret = r.json()
        data = self.decode(ret['data'])
        d = data['data']
        result = {
            'list': d,
            'page': pg,
            'pagecount': 9999 if len(d) >= page_count else pg,
            'limit': 90,
            'total': data['total'],
        }
        return result

    def detailContent(self, ids):
        """
        返回二级详情页数据
        @param ids: 一级传过来的vod_id列表
        @return:
        """
        # id=110102
        vod_id = ids[0]
        params = {'id': vod_id}
        r = self.fetch(self.api_detail, data=params)
        print(r.url)
        ret = r.json()
        data = self.decode(ret['data'])
        # print(data)

        vod = {"vod_id": vod_id,
               "vod_name": data['vod_name'],
               "vod_pic": data['vod_pic'],
               "type_name": data['vod_en'],
               "vod_year": data['vod_year'],
               "vod_area": data['vod_area'],
               "vod_remarks": data['vod_remarks'],
               "vod_actor": data['vod_actor'],
               "vod_director": data['vod_director'],
               "vod_content": data['vod_blurb'],
               "vod_play_from": data['vod_play_from'],
               }
        vod_play_list = data['vod_play_list']
        vod_play_urls = []
        for vod_play in vod_play_list:
            v_from = vod_play['player_info']['from']
            v_show = vod_play['player_info']['show']
            vod_play_url = '#'.join(
                [url['name'] + '$' + '&&'.join([url['url'], v_from, v_show]) for url in vod_play['urls']])
            vod_play_urls.append(vod_play_url)
        vod['vod_play_url'] = '$$$'.join(vod_play_urls)
        result = {
            'list': [vod]
        }
        # print(vod)
        return result

    def searchContent(self, wd, quick=False, pg=1):
        """
        返回搜索列表
        @param wd: 搜索关键词
        @param quick: 是否来自快速搜索。t3/t4配置里启用了快速搜索，在快速搜索在执行才会是True
        @param pg: 页数
        @return:
        """
        # ?wd=%E4%B8%89%E5%A4%A7%E9%98%9F&page=1&type=
        params = {'wd': wd, 'type': '', 'page': pg}
        r = self.fetch(self.api_search, data=params)
        print(r.url)
        ret = r.json()
        data = self.decode(ret['data'])
        # print(data)
        d = data['data']
        result = {
            'list': d
        }
        return result

    def playerContent(self, flag, id, vipFlags):
        """
        解析播放,返回json。壳子视情况播放直链或进行嗅探
        @param flag: vod_play_from 播放来源线路
        @param id: vod_play_url 播放的链接
        @param vipFlags: vip标识
        @return:
        """
        headers = {
            'Content-Type': 'multipart/form-data; boundary=--dio-boundary-1205762094',
            'token': self.token,
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
        }
        if '&&' in id:
            _v = id.split('&&')
            params = {'play_url': _v[0], 'label': _v[2], 'key': _v[1]}
        else:
            params = {'play_url': id, 'label': '主线', 'key': 'mp4'}
        # print(params)
        r = self.postBinary(self.api_parse, data=params, boundary='--dio-boundary-1205762094', headers=headers)
        # print(r.request.body.decode())
        ret = r.json()
        data = self.decode(ret['data'])
        # print(data)
        url = data['url']
        parse = 0
        result = {
            'parse': parse,  # 1=嗅探,0=播放
            'playUrl': '',  # 解析链接
            'url': url,  # 直链或待嗅探地址
            # 'header': headers,  # 播放UA
        }
        return result

    config = {
        "player": {},
        "filter": {}
    }
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36",
        "Host": "www.baidu.com",
        "Referer": "https://www.baidu.com/"
    }

    def localProxy(self, param):
        return [200, "video/MP2T", action, ""]

    # -----------------------------------------------自定义函数-----------------------------------------------
    def decode(self, text):
        return json.loads(self.aes_cbs_decode(text, self.key, self.iv))

    def decode_rsa(self, text):
        return json.loads(self.rsa_private_decode(text, self.private_key))

    def eval_computer(self, text):
        """
        自定义的字符串安全计算器
        @param text:字符串的加减乘除
        @return:计算后得到的值
        """
        localdict = {}
        self.safe_eval(f'ret={text.replace("=", "")}', localdict)
        ret = localdict.get('ret') or None
        return ret

    def safe_eval(self, code: str = '', localdict: dict = None):
        code = code.strip()
        if not code:
            return {}
        if localdict is None:
            localdict = {}
        builtins = __builtins__
        if not isinstance(builtins, dict):
            builtins = builtins.__dict__.copy()
        else:
            builtins = builtins.copy()
        for key in ['__import__', 'eval', 'exec', 'globals', 'dir', 'copyright', 'open', 'quit']:
            del builtins[key]  # 删除不安全的关键字
        # print(builtins)
        global_dict = {'__builtins__': builtins,
                       'json': json, 'print': print,
                       're': re, 'time': time, 'base64': base64
                       }  # 禁用内置函数,不允许导入包
        try:
            self.check_unsafe_attributes(code)
            exec(code, global_dict, localdict)
            return localdict
        except Exception as e:
            return {'error': f'执行报错:{e}'}

    # ==================== 静态函数 ======================
    @staticmethod
    def check_unsafe_attributes(string):
        """
        安全检测需要exec执行的python代码
        :param string:
        :return:
        """
        g = tokenize.tokenize(io.BytesIO(string.encode('utf-8')).readline)
        pre_op = ''
        for toktype, tokval, _, _, _ in g:
            if toktype == tokenize.NAME and pre_op == '.' and tokval.startswith('_'):
                attr = tokval
                msg = "access to attribute '{0}' is unsafe.".format(attr)
                raise AttributeError(msg)
            elif toktype == tokenize.OP:
                pre_op = tokval

    @staticmethod
    def aes_cbs_decode(ciphertext, key, iv):
        # 将密文转换成byte数组
        ciphertext = base64.b64decode(ciphertext)
        # 构建AES解密器
        decrypter = AES.new(key.encode(), AES.MODE_CBC, iv.encode())
        # 解密
        plaintext = decrypter.decrypt(ciphertext)
        # 去除填充
        plaintext = unpad(plaintext, AES.block_size)
        # 输出明文
        # print(plaintext.decode('utf-8'))
        return plaintext.decode('utf-8')

    @staticmethod
    def rsa_private_decode(ciphertext, private_key):
        # 计算需要添加的等号数
        b64_ciphertext = ciphertext
        num_padding = 4 - (len(b64_ciphertext) % 4)
        if num_padding < 4:
            b64_ciphertext += "=" * num_padding
        # print(len(ciphertext), ciphertext)
        # 将密文转换成byte数组
        # ciphertext = base64.b64decode(b64_ciphertext.encode("utf8"))
        ciphertext = base64.b64decode(b64_ciphertext)
        # print(len(ciphertext), ciphertext)
        # 构建RSA解密器
        private_key = f'-----BEGIN RSA PRIVATE KEY-----\n{private_key}\n-----END RSA PRIVATE KEY-----'
        pri_Key = RSA.importKey(private_key)
        decrypter = PKCS1_cipher.new(pri_Key)
        # 解密
        length = len(ciphertext)
        default_length = 256
        # 长度不用分段
        if length < default_length:
            plaintext = b''.join(decrypter.decrypt(ciphertext, b' '))
        else:
            # 需要分段
            offset = 0
            res = []
            while length - offset > 0:
                if length - offset > default_length:
                    res.append(decrypter.decrypt(ciphertext[offset:offset + default_length], b' '))
                else:
                    res.append(decrypter.decrypt(ciphertext[offset:], b' '))
                offset += default_length

            plaintext = b''.join(res)
        return plaintext.decode('utf-8')

    @staticmethod
    def rsa_public_encode(text, public_key):
        public_key = "-----BEGIN RSA PRIVATE KEY-----\n" + public_key + "\n-----END RSA PRIVATE KEY-----"
        pub_key = RSA.importKey(public_key)
        cipher = PKCS1_cipher.new(pub_key)
        text = text.encode("utf-8)")
        length = len(text)
        default_length = 256
        if length < default_length:
            rsa_text = base64.b64encode(cipher.encrypt(text))  # 加密并转为b64编码
        else:
            # 需要分段
            offset = 0
            res = []
            while length - offset > 0:
                if length - offset > default_length:
                    res.append(cipher.encrypt(text[offset:offset + default_length]))
                else:
                    res.append(cipher.encrypt(text[offset:]))
                offset += default_length
            byte_data = b''.join(res)

            rsa_text = base64.b64encode(byte_data)

        ciphertext = rsa_text.decode("utf8")
        return ciphertext


if __name__ == '__main__':
    # 在线aes测试 https://config.net.cn/tools/AES.html
    # 分类页:http://60.204.185.245:7090/appto/v1/home/cateData?id=1
    # 推荐页:http://60.204.185.245:7090/appto/v1/config/get?p=android
    spider = Spider()
    # spider.init('https://jihulab.com/qiaoji/open/-/raw/main/yinghua')
    spider.init()
    # spider.init_api_ext_file()  # 生成筛选对应的json文件

    # print(spider.homeContent(True))
    # print(spider.homeVideoContent())
    # print(spider.categoryContent('1', 1, True, {'year': '2024'}))
    # print(spider.detailContent([110078]))
    # print(spider.searchContent('斗罗大陆'))
    # print(spider.playerContent(None, 'f1d7d074f624e993e425f|11d1d091b0b28|31613145e4a7c|518737c8650978', None))
    # spider.searchContent('斗罗大陆')
