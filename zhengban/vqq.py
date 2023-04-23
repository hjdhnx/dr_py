#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : vqq.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/10/24

import requests
import re

time_out = 2
cookie = """
    pgv_pvid=5805499462; iip=0; RK=yQaYRyNLbG; ptcz=2a0d041daba2e1e3872184cd999e01bf90678c0e492c5900527c802251d224ad; tvfe_boss_uuid=53b5e88a3ebeba2c; video_platform=2; _tc_unionid=78fa72d7-2485-49f5-abf3-e72f7122cbb5; pgv_pvi=1381712896; logTrackKey=613d40c3fea04aafb45fc9642dd67b99; main_login=qq; vqq_appid=101483052; vqq_openid=406CA2296D6A3B970597D6CF1605B6B7; vqq_vuserid=1260982452; pgv_info=ssid=s1368217315; pac_uid=1_434857005; vversion_name=8.2.95; video_omgid=3419ca23530808d22bb278e881e46647; _qpsvr_localtk=0.710205836458567; vqq_access_token=88AEE1A8BC32318537BC7D81586E44A4; vqq_refresh_token=2D85975A29FB056EB6F9A338CB8F1EF5; o_cookie=434857005; video_guid=3419ca23530808d22bb278e881e46647; video_bucketid=4; fqm_pvqid=0a2a19f9-b09d-48d2-835a-cee916bdb63f; fqm_sessionid=a2c625f7-98e9-4d69-adb4-ad82846832bc; uin=o0434857005; skey=@rZMv3mYSR; vqq_vusession=Xd5bba2m9ByWls30Vi2FSQ.N; vqq_next_refresh_time=6530; vqq_login_time_init=1666665341; login_time_last=2022-10-25 10:35:44
    """.strip()

login_token = """
vqq_appid=101483052; vqq_openid=406CA2296D6A3B970597D6CF1605B6B7; vqq_vuserid=1260982452;vqq_vusession=Xd5bba2m9ByWls30Vi2FSQ.N; vqq_refresh_token=2D85975A29FB056EB6F9A338CB8F1EF5;vqq_next_refresh_time=6530;
""".strip()

auth_token = """
vqq_appid=101483052; vqq_openid=406CA2296D6A3B970597D6CF1605B6B7; vqq_vuserid=1260982452;vqq_vusession=
""".strip()

user_token = """
pgv_pvid=5805499462;video_platform=2;o_cookie=434857005;ptui_loginuin=434857005;uid=o0434857005;uin=o0434857005;vqq_vuserid=1260982452;vversion_name=8.2.95;vqq_next_refresh_time=6530;vqq_login_time_init=1666665341; login_time_last=2022-10-25 10:35:44
""".strip()
cookie = login_token
headers = {
        # "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36¬",
        "User-Agent": "qqlive",
        "cookie": cookie,
}
def get_vid(vipUrl):
    vid = None
    if vipUrl.find('v.qq.com/x/cover/') > -1:
        _type = vipUrl.split("v.qq.com/x/cover/")[1].split(".html")[0]
        if _type.find('/') > -1:
            vid = _type.split("/")[1]
        else:
            r = requests.get(vipUrl, headers=headers)
            html = r.text
            vid = html.split('<link rel="canonical" href="https://v.qq.com/x/cover/')[1].split('/')[1].split('.')[0]
    else:
        if re.search('/page/.*\.html', vipUrl):
            vid = vipUrl.split("/page/")[1].split(".html")[0]
        else:
            if vipUrl.find('&vid=') > -1:
                vid = vipUrl.split("&vid=")[1].split("&")[0]

    print(f'vid:{vid}')
    return vid

def vqq_jx_rx(url):
    # 1080P画质
    vid = get_vid(url)
    api = f"https://vv.video.qq.com/getinfo?defn=fhd&platform=10801&otype=ojson&sdtfrom=v4138&appVer=7&vid={vid}&newnettype=1&fhdswitch=1&show1080p=1&dtype=3&sphls=2"
    print(api)
    r = requests.get(api, headers=headers, timeout=time_out)
    ret = r.json()
    try:
        urls = ret["vl"]["vi"][0]['ul']['ui']
        # url = urls[-1]['url']
        url = urls[0]['url']
        realUrl = url
        print(realUrl)
    except:
        print(ret)

def vqq_jx(url):
    # 720P 画质
    vid = get_vid(url)
    api = f'https://vv.video.qq.com/getinfo?encver=2&defn=shd&platform=10801&otype=ojson&sdtfrom=v4138&appVer=7&dtype=3&vid={vid}&newnettype=1'
    print(api)
    r = requests.get(api,headers=headers,timeout=time_out)
    ret = r.json()
    try:
        urls = ret["vl"]["vi"][0]['ul']['ui']
        print(urls)
        url = urls[-1]['url']
        pt = urls[-1]['hls']['pt']
        realUrl = url + pt
        print(realUrl)
    except:
        print(ret)

if __name__ == '__main__':
    # 斗罗大陆
    url = 'https://v.qq.com/x/cover/m441e3rjq9kwpsc/c00442r6ry6.html'
    # 复仇者联盟
    # url = 'https://v.qq.com/x/cover/v2098lbuihuqs11/m00314jtw6k.html'
    # vqq_jx(url)
    vqq_jx_rx(url)