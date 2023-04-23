#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : system.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/9/6

from flask import request
import psutil
import sys
from utils.cfg import cfg

def get_wlan_info():
    info = psutil.net_if_addrs()
    # print(info)
    netcard_info = []
    ips = []
    for k, v in info.items():
        for item in v:
            if item[0] == 2:
                netcard_info.append((k, item[1]))
                ips.append(item[1])
    return netcard_info,ips

def get_host_ip(): # 获取局域网ip
    netcard_info,ips = get_wlan_info()
    # print(netcard_info)
    real_ips = list(filter(lambda x: x and x != '127.0.0.1', ips))
    jyw = list(filter(lambda x: str(x).startswith('192.168') and not str(x).endswith('.1'), real_ips))
    # print(jyw)
    return real_ips[-1] if len(jyw) < 1 else jyw[0]

def getHost(mode=0,port=None):
    port = port or request.environ.get('SERVER_PORT')
    # mode 为0是本地,1是局域网 2是线上
    try:
        mode = int(mode)
    except:
        mode = 2
    if mode == 0:
        host = f'http://localhost:{port}'
    elif mode == 1:
        REAL_IP = get_host_ip()
        ip = REAL_IP
        host = f'http://{ip}:{port}'
    else:
        from controllers.service import storage_service
        lsg = storage_service()
        # print(cfg.PLAY_URL) # 可能会报错: 'EasyDict' object has no attribute 'xxx'
        host = lsg.getItem('PLAY_URL',cfg.get('PLAY_URL',''))
    # print(mode,host)
    return host

def is_linux():
    return not 'win' in sys.platform