#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : vod.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/9/6
import functools
import json
import os
from urllib.parse import urljoin, unquote,quote
import requests
from flask import Blueprint, abort, request, render_template, send_from_directory, render_template_string, jsonify, \
    make_response, redirect, \
    current_app, url_for
from time import time
from utils.web import getParmas, get_interval
from utils.cfg import cfg
from utils.env import get_env
from js.rules import getRuleLists, getJxs
from base.R import R
from utils.log import logger
from utils import parser
from controllers.cms import CMS
from base.database import db
from models.ruleclass import RuleClass
from models.playparse import PlayParse
from js.rules import getRules
from controllers.service import storage_service, rules_service
from concurrent.futures import ThreadPoolExecutor, as_completed, thread  # 引入线程池
from quickjs import Function, Context
import ujson

# web = Blueprint("web", __name__, template_folder='templates/cmsV10/mxpro/html/index/')
web = Blueprint("web", __name__)


@web.route('/cms/<path:filename>')
def custom_static_cms(filename):
    # 自定义静态目录 {{ url_for('custom_static',filename='help.txt')}}
    # print(filename)
    return send_from_directory('templates/cms', filename)


@web.route('/player/<path:filename>')
def custom_static_player(filename):
    # 自定义静态目录 {{ url_for('custom_static',filename='help.txt')}}
    # print(filename)
    return send_from_directory('templates/player', filename)

@web.route('/player1')
def custom_player1():
    ctx = getParmas()
    return render_template('player/mui/index.html', ctx=ctx)

@web.route('/player2')
def custom_player2():
    ctx = getParmas()
    return render_template('player/p2p-media-loader/p2pm3u8.html', ctx=ctx)

@web.route('/player3')
def custom_player3():
    ctx = getParmas()
    return render_template('player/p2pplayer/index.htm', ctx=ctx)

@web.route('/<web_name>/<theme>')
def web_index(web_name, theme):
    ctx = {'web_name': web_name, 'key': '关键词', 'description': '描述'}
    lsg = storage_service()
    js0_password = lsg.getItem('JS0_PASSWORD')
    ctx['pwd'] = js0_password
    ctx['path'] = request.path
    ctx['url'] = request.url
    vod_id = getParmas('vod_id')
    vod_name = getParmas('vod_name')
    wd = getParmas('wd')
    pg = getParmas('pg') or '1'
    tid = getParmas('tid')
    tname = getParmas('tname')
    url = getParmas('url')
    fl = getParmas('f')
    player = getParmas('player') or 'mui'
    ctx['vod_id'] = vod_id
    ctx['vod_name'] = vod_name
    ctx['wd'] = wd
    ctx['pg'] = pg
    ctx['tid'] = tid
    ctx['tname'] = tname
    ctx['url'] = url
    ctx['fl'] = quote(fl)
    print('tid:', tid,'fl:',fl)
    # print('f:', fl)

    file_path = os.path.abspath(f'js/{web_name}.js')
    print(file_path)
    if not os.path.exists(file_path):
        return render_template('404.html', ctx=ctx, error=f'发生错误的原因可能是下面路径未找到:{file_path}')

    try:
        if url:
            return render_template(f'player/{player}/index.html', ctx=ctx)
        elif vod_id and vod_name:
            return render_template(f'cms/{theme}/detailContent.html', ctx=ctx)
        elif wd:
            return render_template(f'cms/{theme}/searchContent.html', ctx=ctx)
        elif tid:
            return render_template(f'cms/{theme}/categoryContent.html', ctx=ctx)
        else:
            return render_template(f'cms/{theme}/homeContent.html', ctx=ctx)
    except Exception as e:
        return render_template('404.html', ctx=ctx, error=f'发生错误的原因可能是下面路径未找到:{e}')


@web.route('/302redirect')
def get302UrlResponse():
    url = getParmas('url')
    if not url:
        abort(403)
    params = {}
    if not url.startswith('http'):
        url = urljoin(request.root_url, url)
        # url = urljoin('http://localhost:5705/',url)
        print(url)
        items = url.split('vod?')[1].split('&')
        for item in items:
            params[item.split('=')[0]] = item.split('=')[1]
        print(params)
        # abort(403)

    timeout = getParmas('timeout') or 5000
    rurl = url
    try:
        timeout = int(timeout)
        headers = {
            # 'referer': url,
            'user-agent': 'Mozilla/5.0'
        }
        logger.info(f'开始调用接口:{url}')
        r = requests.get(url, headers=headers, timeout=timeout, verify=False)
        rurl = r.url
        res_data = r.text
        try:
            res_data = r.json()
        except:
            pass

        # rurl = url_for('vod.vod_home', **params)
        # print(rurl)
        logger.info(f'结束调用接口:{rurl}')
        is_redirect = unquote(rurl) != unquote(url)
        return jsonify({
            'url': rurl,
            'redirect': is_redirect,
            'data': res_data,
        })

    except Exception as e:
        logger.info(f'发生了错误:{e}')
        return jsonify({
            'url': rurl,
            'redirect': False,
            'data': None,
            'error': f'{e}',
        })
