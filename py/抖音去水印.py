#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : 抖音去水印.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2023/1/28

import requests
import re

MOBILE_UA = 'Mozilla/5.0 (Linux; Android 11; M2007J3SC Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045714 Mobile Safari/537.36'
PC_UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
UA = 'Mozilla/5.0'
UC_UA = 'Mozilla/5.0 (Linux; U; Android 9; zh-CN; MI 9 Build/PKQ1.181121.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.5.5.1035 Mobile Safari/537.36'
IOS_UA = 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
VIVO_UA = 'Mozilla/5.0 (Linux; Android 11; V1824A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/13.5.2.0'
headers = {
        'Referer': 'https://www.iesdouyin.com',
        'user-agent': VIVO_UA,
        'cookie':'ttwid=1%7CMW5dLoe75C1tpxkuQAkpRyycNJxsjOiOxfXpIOJfnss%7C1674880922%7Cb830b760a030f0fc32aa06d22d60a166540ed87be8a63abc663ea0455c58c41e;s_v_web_id=verify_ldfguvw1_WlKOQ6sh_pefT_4Bfi_ACxe_cWYKf0e69scc;_tea_utm_cache_2018={%22utm_source%22:%22copy_link%22%2C%22utm_medium%22:%22android%22%2C%22utm_campaign%22:%22client_share%22};msToken=JFS1K9RTk3HmNnjKLzDSP3Q44-ghPZipTGFWEeSrRPbVbjWhzdCH50jTlpHsrnMDU1lxzvOdslMY8o6M2EEs_HWSPcZ30-r3m61AJy6WgcJ-m__Inx1aZMzcswG2898=;__ac_signature=_02B4Z6wo00f01zYd0kQAAIDCewNHdokIx0c2PdbAAK5e20;_tea_utm_cache_1243={%22utm_source%22:%22copy%22%2C%22utm_medium%22:%22android%22%2C%22utm_campaign%22:%22client_share%22};msToken=PLm81i75pqzCZg1EaBc7BCpwr0xr1HbG87z_9CDKh5ppmg4uz5uXUzq7mxcjbaHG2KYMfFUvL0lHa60c48i8pwXWSGui9xv1snjD82GhMgXjx-BObdqUIk-yavvjDvk='
}

headers2 = {
    'user-agent':MOBILE_UA
}

def main(url):
    s = requests.session()
    r = s.get(url,headers=headers)
    lurl = r.url
    print(f'重定向地址:{lurl}')
    video_id = re.search(r'video/(\d+)',lurl,re.M).groups()[0]
    print(f'video_id:{video_id}')
    url2 = f'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={video_id}'
    print(f'访问接口:{url2}')
    r = s.get(url2,headers=headers)
    print(r.text)
    try:
        data = r.json()
        uri = data['item_list'][0]['video']['play_addr']['uri']
        print(f'uri:{uri}')
        url3 = f'https://aweme.snssdk.com/aweme/v1/play/?video_id={uri}'
        print(f'开始访问:{url3}')
        r = s.get(url3, headers=headers)
        print(f'得到真实去水印地址:{r.url}')
    except:
        print('获取接口数据失败...')

if __name__ == '__main__':
    # 分享的地址
    # share_url = 'https://v.douyin.com/BJmKbjb/'
    share_url = 'https://v.douyin.com/BJmKbjb/'
    main(share_url)