#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : index.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/9/6
import json
import ujson
import os
import re

from flask import Blueprint,abort,render_template,render_template_string,url_for,redirect,make_response,send_from_directory,request
from controllers.service import storage_service,rules_service,parse_service
from controllers.classes import getClasses,getClassInfo

from utils.files import getPics,custom_merge,getAlist,get_live_url,get_multi_rules,getCustonDict
from js.rules import getRules,getPys
from utils.encode import parseText,base64Encode,base64Decode
from base.R import R
from utils.system import getHost,is_linux
from utils.cfg import cfg
from utils import parser
from utils.ua import time,get_interval
from utils.log import logger
from utils.update import getLocalVer,getHotSuggest
from js.rules import getJxs
import random
from utils.web import getParmas,verfy_token
from utils.common_api import js_render
import functools


home = Blueprint("home", __name__,static_folder='/static')

@home.route('/')
def forbidden():  # put application's code here
    abort(403)

@home.route('/favicon.ico')  # 设置icon
def favicon():
    # return home.send_static_file('img/favicon.svg')
    return redirect('/static/img/favicon.svg')
    # 对于当前文件所在路径,比如这里是static下的favicon.ico
    # return send_from_directory(os.path.join(app.root_path, 'static'),  'img/favicon.svg', mimetype='image/vnd.microsoft.icon')

@home.route('/index')
def index():
    sup_port = cfg.get('SUP_PORT', 9001)
    lsg = storage_service()
    pid_url = lsg.getItem('PID_URL')
    manager0 = ':'.join(getHost(0).split(':')[0:2])
    manager1 = ':'.join(getHost(1).split(':')[0:2])
    manager2 = pid_url or ':'.join(getHost(2).split(':')[0:2]).replace('https','http')
    if sup_port:
        manager0 += f':{sup_port}'
        manager1 += f':{sup_port}'
        if not pid_url:
            manager2 += f':{sup_port}'
    # print(manager2)
    ver = getLocalVer()
    return render_template('index.html',ver=ver,getHost=getHost,manager0=manager0,manager1=manager1,manager2=manager2,is_linux=is_linux())

@home.route('/rules/clear')
def rules_to_clear():
    return render_template('rules_to_clear.html',rules=getRules(),classes=getClasses())

@home.route('/rules/view')
def rules_to_view():
    return render_template('rules_to_view.html',rules=getRules(),classes=getClasses())

@home.route('/pics')
def random_pics():
    id = getParmas('id')
    # print(f'id:{id}')
    pics = getPics()
    # print(pics)
    new_conf = cfg
    lsg = storage_service()
    store_conf_dict = lsg.getStoreConfDict()
    new_conf.update(store_conf_dict)
    if not new_conf.WALL_PAPER and len(pics) > 0:
        if id and f'images/{id}.jpg' in pics:
            pic = f'images/{id}.jpg'
        else:
            pic = random.choice(pics)
        file = open(pic, "rb").read()
        response = make_response(file)
        response.headers['Content-Type'] = 'image/jpeg'
        return response
    else:
        return redirect(new_conf.WALL_PAPER)

@home.route('/clear')
def clear_rule():
    rule = getParmas('rule')
    if not rule:
        return R.failed('规则字段必填')
    cache_path = os.path.abspath(f'cache/{rule}.js')
    if not os.path.exists(cache_path):
        return R.failed('服务端没有此规则的缓存文件!'+cache_path)
    os.remove(cache_path)
    return R.success('成功删除文件:'+cache_path)

@home.route("/plugin/<name>",methods=['GET'])
def plugin(name):
    # name=道长影视模板.js
    if not name or not name.split('.')[-1] in ['js','txt','py','json']:
        return R.failed(f'非法猥亵,未指定文件名。必须包含js|txt|json|py')
    try:
        return parser.toJs(name)
    except Exception as e:
        return R.failed(f'非法猥亵\n{e}')

@home.route('/files/<name>')
def get_files(name):
    base_path = 'base/files'
    os.makedirs(base_path,exist_ok=True)
    file_path = os.path.join(base_path, f'{name}')
    if not os.path.exists(file_path):
        return R.failed(f'{file_path}文件不存在')

    with open(file_path, mode='rb') as f:
        file_byte = f.read()
    response = make_response(file_byte)
    filename = name
    response.headers['Content-Type'] = 'application/octet-stream'
    response.headers['Content-Disposition'] = f'attachment;filename="{filename}"'
    return response

@home.route('/txt/<path:filename>')
def custom_static_txt(filename):
    # 自定义静态目录 {{ url_for('custom_static',filename='help.txt')}}
    # print(filename)
    return send_from_directory('txt', filename)

@home.route('/libs/<path:filename>')
def custom_static_libs(filename):
    # 自定义静态目录 {{ url_for('custom_static',filename='help.txt')}}
    # print(filename)
    return send_from_directory('libs', filename)

# @home.route('/js/<path:filename>')
# def custom_static_js(filename):
#     # 自定义静态目录 {{ url_for('custom_static',filename='help.txt')}}
#     # print(filename)
#     return send_from_directory('js', filename)

@home.route('/js/<path:name>',methods=['GET'])
def custom_static_js(name):
    # 自定义静态目录 {{ url_for('custom_static',filename='help.txt')}}
    # print(name)
    return js_render(name)

# @home.route('/txt/<name>')
# def get_txt_files(name):
#     base_path = 'txt'
#     os.makedirs(base_path,exist_ok=True)
#     file_path = os.path.join(base_path, f'{name}')
#     if not os.path.exists(file_path):
#         return R.failed(f'{file_path}文件不存在')
#
#     with open(file_path, mode='r',encoding='utf-8') as f:
#         file_byte = f.read()
#     response = make_response(file_byte)
#     response.headers['Content-Type'] = 'text/plain; charset=utf-8'
#     return response


@home.route('/lives')
def get_lives():
    # ?path=base/live.txt
    path = getParmas('path')
    live_path = path or 'base/直播.txt'
    if not re.search('(txt|json|conf)$',live_path,re.M|re.S) or not re.search('^(txt|base)',live_path,re.M|re.S):
        abort(403)
    if not os.path.exists(live_path):
        # with open(live_path,mode='w+',encoding='utf-8') as f:
        #     f.write('')
        return ''

    with open(live_path,encoding='utf-8') as f:
        live_text = f.read()
    if len(live_text) > 100 and live_text.find('http') < 0:
        try:
            live_text = base64Decode(live_text)
            logger.info(f'{path} base64解码完毕')
        except Exception as e:
            logger.info(f'{path} base64解码失败:{e}')
    response = make_response(live_text)
    response.headers['Content-Type'] = 'text/plain; charset=utf-8'
    return response

@home.route('/liveslib')
def get_liveslib():
    live_path = 'js/custom_spider.jar'
    if not os.path.exists(live_path):
        with open(live_path,mode='w+',encoding='utf-8') as f:
            f.write('')

    with open(live_path,mode='rb') as f:
        live_text = f.read()
    response = make_response(live_text)
    filename = 'custom_spider.jar'
    response.headers['Content-Type'] = 'application/octet-stream'
    response.headers['Content-Disposition'] = f'attachment;filename="{filename}"'
    return response

@home.route('/hotsugg')
def get_hot_search():
    s_from = getParmas('from')
    size = getParmas('size')
    data = getHotSuggest(s_from,size)
    return R.success('获取成功',data)

def merged_hide(merged_config):
    t1 = time()
    store_rule = rules_service()
    hide_rules = store_rule.getHideRules()
    hide_rule_names = list(map(lambda x: x['name'], hide_rules))
    # print(hide_rule_names)
    all_cnt = len(merged_config['sites'])

    def filter_show(x):
        name = x['api'].split('rule=')[1].split('&')[0] if 'rule=' in x['api'] else x['key'].replace('dr_','')
        # print(name)
        if not str(x['key']).startswith('dr_') and name == 'drpy':
            name = x['key']
        return name not in hide_rule_names

    merged_config['sites'] = list(filter(filter_show, merged_config['sites']))
    logger.info(f'数据库筛选隐藏规则耗时{get_interval(t1)}毫秒,共计{all_cnt}条规则,隐藏后可渲染{len(merged_config["sites"])}条规则')

@home.route('/config/<int:mode>')
def config_render(mode):
    # print(dict(app.config))
    tt = time()
    UA = request.headers['User-Agent']
    ver = getParmas('ver')
    logger.info(f'ver:{ver},UA:{UA}')
    if ver not in ['1','2']:
        ISTVB = 'okhttp/3' in UA
    elif ver == '1':
        ISTVB = False
    elif ver == '2':
        ISTVB = True
    # print(ISTVB)
    if mode == 1:
        jyw_ip = getHost(mode)
        logger.info(jyw_ip)
    new_conf = cfg
    lsg = storage_service()
    store_conf_dict = lsg.getStoreConfDict()
    new_conf.update(store_conf_dict)
    # print(new_conf)
    # print(type(new_conf),new_conf)
    host = getHost(mode)
    # ali_token = lsg.getItem('ALI_TOKEN')
    ali_token = new_conf.ALI_TOKEN
    xr_mode = new_conf.XR_MODE
    js_proxy = new_conf.JS_PROXY
    js0_password = new_conf.JS0_PASSWORD
    js_mode = int(new_conf.JS_MODE or 0)
    print(f'{type(js_mode)} jsmode:{js_mode}')
    # print(ali_token)
    customConfig = getCustonDict(host,ali_token,js0_password)
    # print(customConfig)
    jxs = getJxs(host=host)
    use_py = lsg.getItem('USE_PY')
    pys = getPys() if use_py else []
    # print(pys)
    alists = getAlist()
    alists_str = json.dumps(alists, ensure_ascii=False)
    live_url = get_live_url(new_conf,mode)
    rules = getRules('js',js_mode)
    rules = get_multi_rules(rules)
    # html = render_template('config.txt',rules=getRules('js'),host=host,mode=mode,jxs=jxs,base64Encode=base64Encode,config=new_conf)
    html = render_template('config.txt',js0_password=js0_password,UA=UA,xr_mode=xr_mode,ISTVB=ISTVB,pys=pys,rules=rules,host=host,mode=mode,js_mode=js_mode,jxs=jxs,alists=alists,alists_str=alists_str,live_url=live_url,config=new_conf)
    merged_config = custom_merge(parseText(html),customConfig)
    # print(merged_config['sites'])
    merged_hide(merged_config)
    # response = make_response(html)
    # print(len(merged_config['sites']))
    print(merged_config['sites'])
    merged_config['sites'] = sort_sites_by_order(merged_config['sites'],js_mode)
    # print(merged_config['parses'])
    parses = sort_parses_by_order(merged_config['parses'],host)
    # print(parses)
    merged_config['parses'] = parses
    config_text = json.dumps(merged_config,ensure_ascii=False,indent=1)

    # 依赖代理逻辑修改,改为admin/view去动态代理
    # if js_proxy:
    #     # print('js_proxy:',js_proxy)
    #     if '=>' in js_proxy:
    #         oldsrc = js_proxy.split('=>')[0]
    #         newsrc = js_proxy.split('=>')[1]
    #         print(f'js1源代理已启用,全局替换{oldsrc}为{newsrc}')
    #         config_text = config_text.replace(oldsrc,newsrc)

    response = make_response(config_text)
    # response = make_response(str(merged_config))
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    logger.info(f'自动生成动态配置共计耗时:{get_interval(tt)}毫秒')
    return response

def comp(x, y):
    if x['order'] > y['order']:
        return 1
    elif x['order'] < y['order']:
        return - 1
    else:
        if x['write_date'] < y['write_date']:
            return 1
        elif x['write_date'] > y['write_date']:
            return -1
        else:
            return 0

def sort_sites_by_order(sites,js_mode=0):
    rules = rules_service()
    rule_list = rules.query_all()
    # print(rule_list)
    rule_names = list(map(lambda x: x['name'], rule_list))
    # print(rule_names)
    # print(sites)
    for i in range(len(sites)):
        # sites[i]['id'] = i+1
        site_name = sites[i]['api'].split('rule=')[1].split('&')[0] if 'rule=' in sites[i]['api'] else sites[i]['key']
        if js_mode and str(site_name).startswith('dr'):
            site_name = site_name.replace('dr_','')
        if not str(sites[i]['key']).startswith('dr_') and site_name == 'drpy':
            site_name = sites[i]['key']
            # print(sites[i])
        # print(site_name)
        if site_name in rule_names:
            site_rule = rule_list[rule_names.index(site_name)]
            sites[i]['state'] = 1 if site_rule['state'] is None else site_rule['state']
            sites[i]['order'] = 0 if site_rule['order'] is None else site_rule['order']
            sites[i]['write_date'] = 0 if site_rule['write_date'] is None else site_rule['write_date'].timestamp()
        else:
            sites[i]['state'] = 1
            sites[i]['order'] = 0
            sites[i]['write_date'] = 0
        # sites[i]['site_name'] = site_name
    # print(sites)
    # sites.sort(key=lambda x: x['order'], reverse=False)
    sites.sort(key=functools.cmp_to_key(comp), reverse=False)
    # print(sites)
    for site in sites:
        del site['state']
        del site['order']
        del site['write_date']
    return sites

def sort_parses_by_order(parses,host):
    t1 = time()
    parse = parse_service()
    parse_list = parse.query_all()
    parse_url_list = list(map(lambda x: x['url'], parse_list))
    new_parses = []
    new_parses_url = []
    for i in range(len(parses)):
        # parses[i]['id'] = i + 1
        # 去重
        if parses[i]['url'] in new_parses_url:
            # print(f"重复的解析:{parses[i]['name']},{parses[i]['url']}")
            continue
        if str(parses[i]['url']).startswith(host):
            parses[i]['url'] = parses[i]['url'].replace(host,'')
        if parses[i]['url'] in parse_url_list:
            parse_rule = parse_list[parse_url_list.index(parses[i]['url'])]
            parses[i]['state'] = 1 if parse_rule['state'] is None else parse_rule['state']
            parses[i]['order'] = 0 if parse_rule['order'] is None else parse_rule['order']
            parses[i]['write_date'] = 0 if parse_rule['write_date'] is None else parse_rule['write_date'].timestamp()
        else:
            parses[i]['state'] = 1
            parses[i]['order'] = 0
            parses[i]['write_date'] = 0

        if not parses[i].get('header'):
            parses[i]['header'] = {'User-Agent': 'Mozilla/5.0'}
        if str(parses[i]['url']).startswith('/'):
            parses[i]['url'] = host + parses[i]['url']
        new_parses.append(parses[i])
        new_parses_url.append(parses[i]['url'])
    new_parses.sort(key=functools.cmp_to_key(comp), reverse=False)
    # print(sites)
    for par in new_parses:
        del par['state']
        del par['order']
        del par['write_date']
    # print(new_parses)
    logger.info(f'{len(new_parses)}/{len(parses)}条解析解析排序耗时:{get_interval(t1)}毫秒')
    return new_parses

@home.route('/configs')
def config_gen():
    if not verfy_token():
        return R.failed('请登录后再试')
    # 生成文件
    os.makedirs('txt',exist_ok=True)
    new_conf = cfg
    lsg = storage_service()
    store_conf_dict = lsg.getStoreConfDict()
    new_conf.update(store_conf_dict)
    try:
        use_py = lsg.getItem('USE_PY')
        js_mode = int(new_conf.JS_MODE or 0)
        js0_password = new_conf.JS0_PASSWORD
        pys = getPys() if use_py else False
        alists = getAlist()
        alists_str = json.dumps(alists,ensure_ascii=False)
        rules = getRules('js',js_mode)
        rules = get_multi_rules(rules)
        host0 = getHost(0)
        jxs = getJxs(host=host0)
        set_local = render_template('config.txt',js0_password=js0_password,pys=pys,rules=rules,alists=alists,alists_str=alists_str,live_url=get_live_url(new_conf,0),mode=0,js_mode=js_mode,host=host0,jxs=jxs)
        # print(set_local)
        host1 = getHost(1)
        jxs = getJxs(host=host1)
        set_area = render_template('config.txt',js0_password=js0_password,pys=pys,rules=rules,alists=alists,alists_str=alists_str,live_url=get_live_url(new_conf,1),mode=1,js_mode=js_mode,host=host1,jxs=jxs)
        host2 = getHost(2) or host1
        # print('远程地址:'+host2)
        jxs = getJxs(host=host2)
        set_online = render_template('config.txt',js0_password=js0_password,pys=pys,rules=rules,alists=alists,alists_str=alists_str,live_url=get_live_url(new_conf,2),mode=1,js_mode=js_mode,host=host2,jxs=jxs)
        ali_token = new_conf.ALI_TOKEN
        # parses = []
        with open('txt/pycms0.json','w+',encoding='utf-8') as f:
            customConfig = getCustonDict(host0,ali_token,js0_password)
            set_dict = custom_merge(parseText(set_local), customConfig)
            merged_hide(set_dict)
            set_dict['sites'] = sort_sites_by_order(set_dict['sites'], js_mode)
            # if not parses:
            #     print('生成静态配置时初始化排序parses')
            #     parses = sort_parses_by_order(set_dict['parses'])
            # set_dict['parses'] = parses
            set_dict['parses'] = sort_parses_by_order(set_dict['parses'],host0)
            # set_dict = json.loads(set_local)
            f.write(json.dumps(set_dict,ensure_ascii=False,indent=4))
        with open('txt/pycms1.json','w+',encoding='utf-8') as f:
            customConfig = getCustonDict(host1,ali_token,js0_password)
            set_dict = custom_merge(parseText(set_area), customConfig)
            merged_hide(set_dict)
            set_dict['sites'] = sort_sites_by_order(set_dict['sites'], js_mode)
            set_dict['parses'] = sort_parses_by_order(set_dict['parses'],host1)
            # set_dict = json.loads(set_area)
            f.write(json.dumps(set_dict,ensure_ascii=False,indent=4))

        with open('txt/pycms2.json','w+',encoding='utf-8') as f:
            customConfig = getCustonDict(host2,ali_token,js0_password)
            set_dict = custom_merge(parseText(set_online), customConfig)
            merged_hide(set_dict)
            set_dict['sites'] = sort_sites_by_order(set_dict['sites'], js_mode)
            set_dict['parses'] = sort_parses_by_order(set_dict['parses'],host2)
            # set_dict = json.loads(set_online)
            f.write(json.dumps(set_dict,ensure_ascii=False,indent=4))
        files = [os.path.abspath(rf'txt\pycms{i}.json') for i in range(3)]
        # print(files)
        return R.success('猫配置生成完毕，文件位置在:\n'+'\n'.join(files))
    except Exception as e:
        return R.failed(f'配置文件生成错误:\n{e}')

@home.route("/info",methods=['get'])
def info_all():
    data = storage_service.query_all()
    return R.ok(data=data)