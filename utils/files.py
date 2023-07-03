#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : files.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/9/6

import os
import shutil

from utils.system import getHost
from controllers.service import storage_service
from utils.encode import base64Encode,parseText
from flask import render_template_string
from utils.log import logger

def getPics(path='images'):
    base_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))  # 上级目录
    img_path = os.path.join(base_path, f'{path}')
    os.makedirs(img_path,exist_ok=True)
    file_name = os.listdir(img_path)
    # file_name = list(filter(lambda x: str(x).endswith('.js') and str(x).find('模板') < 0, file_name))
    # print(file_name)
    pic_list = [img_path+'/'+file for file in file_name]
    # pic_list = file_name
    # print(type(pic_list))
    return pic_list

def get_live_url(new_conf,mode):
    host = getHost(mode)
    lsg = storage_service()
    # t1 = time()
    # live_url = host + '/lives' if new_conf.get('LIVE_MODE',1) == 0 else lsg.getItem('LIVE_URL',getHost(2)+'/lives')
    live_url = host + '/lives' if lsg.getItem('LIVE_MODE',1) == 0 else lsg.getItem('LIVE_URL',getHost(2)+'/lives')
    live_url = base64Encode(live_url)
    # print(f'{get_interval(t1)}毫秒')
    return live_url

def getAlist():
    base_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))  # 上级目录
    alist_path = os.path.join(base_path, 'js/alist.conf')
    alist_cpath = os.path.join(base_path, 'base/alist.conf')
    try:
        if not os.path.exists(alist_cpath):
            shutil.copy(alist_path, alist_cpath)  # 复制文件
        with open(alist_cpath,encoding='utf-8') as f:
            data = f.read().strip()
        alists = []
        for i in data.split('\n'):
            i = i.strip()
            dt = i.split(',')
            if not i.strip().startswith('#'):
                obj = {
                    'name': dt[0],
                    'server': dt[1],
                    'type':"alist",
                }
                if len(dt) > 2:
                    obj.update({
                        'password': dt[2]
                    })
                alists.append(obj)
        print(f'共计{len(alists)}条alist记录')
        return alists
    except Exception as e:
        print(f'获取alist列表失败:{e}')
        return []

def get_jar_list():
    base_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))  # 上级目录
    jar_path = os.path.join(base_path, 'libs/jar')
    if not os.path.exists(jar_path):
        os.makedirs(jar_path, exist_ok=True)
        logger.info(f'初始化{jar_path}目录')

    jars = os.listdir(jar_path)
    jars = list(filter(lambda x: str(x).endswith('.jar') and str(x).find('base') < 0, jars))
    # print(jars)
    # jar_list = [file.replace('.jar', '') for file in jars]
    return jars

def get_drop_js(jsd_list):
    base_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))  # 上级目录
    js_path = os.path.join(base_path, 'js')
    js_list = [os.path.join(js_path, jsd.replace('jsd','js')) for jsd in jsd_list]
    return js_list

def get_jsd_list():
    base_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))  # 上级目录
    js_path = os.path.join(base_path, 'js')
    if not os.path.exists(js_path):
        os.makedirs(js_path, exist_ok=True)
        logger.info(f'初始化{js_path}目录')

    jsds = os.listdir(js_path)
    jsds = list(filter(lambda x: str(x).endswith('.jsd'), jsds))
    return jsds

def custom_merge(original:dict,custom:dict):
    """
    合并用户配置
    :param original: 原始配置
    :param custom: 自定义配置
    :return:
    """
    if not custom or len(custom.keys()) < 1:
        return original
    new_keys = custom.keys()
    updateObj = {}
    extend_obj = {}
    for key in ['wallpaper','spider','homepage','lives','hotSearch','sniffer','recommend','rating','rules']:
        if key in new_keys:
            updateObj[key] = custom[key]

    for key in ['drives','sites','flags','ads','parses']:
        if key in new_keys:
            extend_obj[key] = custom[key]

    original.update(updateObj)
    for key in extend_obj.keys():
        # original[key].extend(extend_obj[key])
        # print(key,original.get(key))
        if original.get(key) and isinstance(original[key],list):
            original[key].extend(extend_obj[key])
        else:
            original[key] = extend_obj[key]
    logger.info(f'合并配置共有解析数量:{len(original.get("parses"))}')
    return original

def getCustonDict(host,ali_token='',js0_password=''):
    customFile = 'base/custom.conf'
    if not os.path.exists(customFile):
        with open(customFile, 'w+', encoding='utf-8') as f:
            f.write('{}')
    customConfig = False
    try:
        with open(customFile,'r',encoding='utf-8') as f:
            text = f.read()
            customConfig = parseText(render_template_string(text,host=host,ali_token=ali_token,js0_password=js0_password))
    except Exception as e:
        logger.info(f'用户自定义配置加载失败:{e}')
    return customConfig

def get_multi_rules(rules):
    lsg = storage_service()
    multi_mode = lsg.getItem('MULTI_MODE',0)
    fix_multi = ['drpy']
    if not multi_mode or str(multi_mode)=='0':
        rules['list'] = list(filter(lambda x: x['name'] in fix_multi or x.get('multi'), rules['list']))
        rules['count'] = len(rules['list'])
        # print(rules)
    return rules