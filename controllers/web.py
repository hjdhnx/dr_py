#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : vod.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/9/6
import functools
import json
import os

from flask import Blueprint, abort, request, render_template, send_from_directory, render_template_string, jsonify, \
    make_response, redirect, \
    current_app
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
    player = getParmas('player') or 'mui'
    ctx['vod_id'] = vod_id
    ctx['vod_name'] = vod_name
    ctx['wd'] = wd
    ctx['pg'] = pg
    ctx['tid'] = tid
    ctx['tname'] = tname
    ctx['url'] = url
    print('tid:',tid)

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