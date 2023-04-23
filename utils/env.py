#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : env.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/11/21

from utils.cfg import cfg
import ujson
from controllers.service import storage_service

def get_env():
    new_conf = cfg
    lsg = storage_service()
    store_conf_dict = lsg.getStoreConfDict()
    new_conf.update(store_conf_dict)
    # print(new_conf)
    env = {
        'ali_token': new_conf.ALI_TOKEN,
        'js_proxy':new_conf.JS_PROXY,
        'fl':'{{fl}}' # 防止被依赖代理
    }
    ENV = new_conf.ENV.strip()
    if ENV:
        # print(ENV)
        try:
            ENV = ujson.loads(ENV)
        except Exception as e:
            print(f'自定义环境变量有误,不是合法json:{e}')
            ENV = {}
    if ENV:
        env.update(ENV)
    # print(env)
    return env

def update_env(env_key:str,env_value:str):
    lsg = storage_service()
    env = lsg.getItem('ENV')
    ENV = {}
    try:
        ENV = ujson.loads(env)
    except:
        env = '{}'
    if env_key:
        ENV[env_key] = env_value
        new_env = ujson.dumps(ENV,ensure_ascii=False)
        print(new_env)
        lsg.setItem('ENV',new_env)
    return ENV