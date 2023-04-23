#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : 外部更新环境变量.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/12/6

import requests


class Drpy:
    def __init__(self, url, username='admin', password='drpy'):
        s = requests.session()
        data = {
            'username': username,
            'password': password,
        }
        print(data)
        login_api = f'{url.rstrip("/")}/admin/login'
        try:
            r = s.post(login_api, data=data)
            print(r.cookies)
            print(r.text)
            self.env_api = f'{url.rstrip("/")}/admin/update_env'
            self.s = s
            print('drpy连接成功')
        except:
            self.s = None
            print('drpy连接失败')

    def update_env(self, key, value):
        if not self.s:
            exit('drpy未连接，无法进行操作')
        else:
            data = {
                'key': key,
                'value': value,
            }
            r = self.s.post(self.env_api, data=data)
            jsonData = r.json()
            if jsonData.get('code') == 200:
                print('修改成功')
                print(jsonData['data'])
            else:
                print('修改失败')


if __name__ == '__main__':
    drpy = Drpy('http://localhost:5705/')
    drpy.update_env('test_env', '测试环境变量')
