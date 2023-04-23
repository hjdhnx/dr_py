#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : vod.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/9/6
import functools
import json

from flask import Blueprint,abort,request,render_template,render_template_string,jsonify,make_response,redirect,current_app
from time import time
from utils.web import getParmas,get_interval
from utils.cfg import cfg
from utils.env import get_env
from js.rules import getRuleLists,getJxs
from base.R import R
from utils.log import logger
from utils import parser
from controllers.cms import CMS
from base.database import db
from models.ruleclass import RuleClass
from models.playparse import PlayParse
from js.rules import getRules
from controllers.service import storage_service,rules_service
from concurrent.futures import ThreadPoolExecutor,as_completed,thread  # 引入线程池
from quickjs import Function,Context
import ujson
vod = Blueprint("vod", __name__)

def search_one_py(rule, wd, before: str = ''):
    t1 = time()
    if not before:
        with open('js/模板.js', encoding='utf-8') as f:
            before = f.read().split('export')[0]
    js_path = f'js/{rule}.js'
    try:
        ctx, js_code = parser.runJs(js_path, before=before)
        if not js_code:
            return None
        ruleDict = ctx.rule.to_dict()
        ruleDict['id'] = rule  # 把路由请求的id装到字典里,后面播放嗅探才能用
        logger.info(f'规则{rule}装载耗时:{get_interval(t1)}毫秒')
        cms = CMS(ruleDict, db, RuleClass, PlayParse, cfg)
        data = cms.searchContent(wd, show_name=True)
        return data
    except Exception as e:
        print(f'{rule}发生错误:{e}')
        return None

def search_one(rule, wd, before: str = '',env:dict=None,app=None):
    t1 = time()
    if not before:
        with open('js/模板.js', encoding='utf-8') as f:
            before = f.read().split('export')[0]
    end_code = """\nif (rule.模板 && muban.hasOwnProperty(rule.模板)) {rule = Object.assign(muban[rule.模板], rule);}"""
    js_path = f'js/{rule}.js'
    ctx = Context()
    try:
        with open(js_path, encoding='utf-8') as f2:
            jscode = f2.read()
        if env:
            # 渲染字符串文本 render_template_string 必须带 flask的上下文
            with app.app_context():
                for k in env:
                    # print(f'${k}', f'{env[k]}')
                    if f'${k}' in jscode:
                        jscode = jscode.replace(f'${k}', f'{env[k]}')
                # jscode = render_template_string(jscode, **env)
            # if '007' in rule:
            #     print(rule,jscode)
        jscode = before + jscode + end_code
        # print(jscode)
        ctx.eval(jscode)
        js_ret = ctx.get('rule')
        ruleDict = ujson.loads(js_ret.json())
        ruleDict['id'] = rule  # 把路由请求的id装到字典里,后面播放嗅探才能用
        logger.info(f'规则{rule}装载耗时:{get_interval(t1)}毫秒')
        cms = CMS(ruleDict, db, RuleClass, PlayParse, cfg)
        data = cms.searchContent(wd, show_name=True)
        return data
    except Exception as e:
        logger.info(f'{e}')
        return R.failed('爬虫规则加载失败')

def multi_search2(wd):
    t1 = time()
    lsg = storage_service()
    try:
        timeout = round(int(lsg.getItem('SEARCH_TIMEOUT', 5000)) / 1000, 2)
    except:
        timeout = 5
    rules = getRules('js')['list']
    rule_names = list(map(lambda x: x['name'], rules))
    rules_exclude = ['drpy']
    new_rules = list(filter(lambda x: x.get('searchable', 0) and x.get('name', '') not in rules_exclude, rules))
    search_sites = [new_rule['name'] for new_rule in new_rules]
    nosearch_sites = set(rule_names) ^ set(search_sites)
    nosearch_sites.remove('drpy')
    # print(nosearch_sites)
    logger.info(f'开始聚搜{wd},共计{len(search_sites)}个规则,聚搜超时{timeout}秒')
    logger.info(f'不支持聚搜的规则,共计{len(nosearch_sites)}个规则:{",".join(nosearch_sites)}')
    # print(search_sites)
    res = []
    with open('js/模板.js', encoding='utf-8') as f:
        before = f.read().split('export')[0]
    logger.info(f'聚搜准备工作耗时:{get_interval(t1)}毫秒')
    t2 = time()
    thread_pool = ThreadPoolExecutor(len(search_sites))  # 定义线程池来启动多线程执行此任务
    obj_list = []
    try:
        for site in search_sites:
            obj = thread_pool.submit(search_one, site, wd, before)
            obj_list.append(obj)
        thread_pool.shutdown(wait=True)  # 等待所有子线程并行完毕
        vod_list = [obj.result() for obj in obj_list]
        for vod in vod_list:
            if vod and isinstance(vod, dict) and vod.get('list') and len(vod['list']) > 0:
                res.extend(vod['list'])
        result = {
            'list': res
        }
        logger.info(f'drpy聚搜{len(search_sites)}个源耗时{get_interval(t2)}毫秒,含准备共计耗时{get_interval(t1)}毫秒')
    except Exception as e:
        result = {
            'list': []
        }
        logger.info(f'drpy聚搜{len(search_sites)}个源耗时{get_interval(t2)}毫秒,含准备共计耗时:{get_interval(t1)}毫秒,发生错误:{e}')
    return jsonify(result)


def merged_hide(merged_rules):
    t1 = time()
    store_rule = rules_service()
    hide_rules = store_rule.getHideRules()
    hide_rule_names = list(map(lambda x: x['name'], hide_rules))
    # print('隐藏:',hide_rule_names)
    all_cnt = len(merged_rules)
    # print(merged_rules)

    def filter_show(x):
        # name = x['api'].split('rule=')[1].split('&')[0] if 'rule=' in x['api'] else x['key'].replace('dr_','')
        name = x
        # print(name)
        return name not in hide_rule_names

    merged_rules = list(filter(filter_show, merged_rules))
    # print('隐藏后:',merged_rules)
    logger.info(f'数据库筛选隐藏规则耗时{get_interval(t1)}毫秒,共计{all_cnt}条规则,隐藏后可渲染{len(merged_rules)}条规则')
    # merged_rules = []
    return merged_rules

def disable_exit_for_threadpool_executor():
    import atexit
    import concurrent.futures
    atexit.unregister(concurrent.futures.thread._python_exit)

def sort_lsg_rules(sites:list):
    """
     查询结果按order和write_date 联合排序
    :param sites:
    :return:
    """
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

    sites.sort(key=functools.cmp_to_key(comp), reverse=False)
    return sites

def sort_lsg_rules2(sites:list,lsg_rule_names:list):
    """
     查询结果按order和write_date 联合排序
    :param sites:
    :return:
    """
    def comp(x, y):
        try:
            x1 = lsg_rule_names.index(x)
        except:
            x1 = 999

        try:
            y1 = lsg_rule_names.index(y)
        except:
            y1 = 999

        if x1 >= y1:
            return 1
        elif x1 < y1:
            return - 1

    sites.sort(key=functools.cmp_to_key(comp), reverse=False)
    return sites

def getSearchSites():
    val = {}
    lsg = storage_service()
    try:
        timeout = round(int(lsg.getItem('SEARCH_TIMEOUT',5000))/1000,2)
    except:
        timeout = 5
    val['timeout'] = timeout
    rules = getRules('js')['list']
    rule_names = list(map(lambda x: x['name'], rules))
    rules_exclude = ['drpy']
    new_rules = list(filter(lambda x: x.get('searchable', 0) and x.get('name', '') not in rules_exclude, rules))
    total_search = [new_rule['name'] for new_rule in new_rules]
    nosearch_sites = set(rule_names) ^ set(total_search)
    nosearch_sites.remove('drpy')
    val['total_search'] = total_search
    val['nosearch_sites'] = list(nosearch_sites)
    search_sites = merged_hide(total_search)
    lsg_rules = rules_service()
    lsg_rule_list = lsg_rules.query_all()
    lsg_rule_list = list(filter(lambda x: x['name'] in search_sites, lsg_rule_list))
    lsg_rule_names = list(map(lambda x: x['name'], lsg_rule_list))

    search_sites = sort_lsg_rules2(search_sites, lsg_rule_names)
    search_limit = lsg.getItem('SEARCH_LIMIT', 24)
    try:
        search_limit = int(search_limit)
    except:
        search_limit = 0
    if search_limit < 1:
        search_limit = 0
    search_sites = search_sites[:search_limit]
    val['search_limit'] = search_limit
    val['search_sites'] = search_sites
    return val

def multi_search(wd):
    t1 = time()
    val = getSearchSites()
    timeout = val['timeout']
    total_search = val['total_search']
    nosearch_sites = val['nosearch_sites']
    search_limit = val['search_limit']
    search_sites = val['search_sites']

    env = get_env()
    logger.info(f'开始聚搜{wd},共计{len(total_search)}个规则,聚搜超时{timeout}秒')
    logger.info(f'不支持聚搜的规则,共计{len(nosearch_sites)}个规则:{",".join(nosearch_sites)}')
    msearch_msg = f'搜索限制条数:{search_limit}/{len(search_sites)} {search_sites}'
    logger.info(msearch_msg)
    print(msearch_msg)
    # search_sites = []
    res = []
    if len(search_sites) > 0:
        with open('js/模板.js', encoding='utf-8') as f:
            before = f.read().split('export')[0]
        with ThreadPoolExecutor(max_workers=len(search_sites)) as executor:
            to_do = []
            for site in search_sites:
                future = executor.submit(search_one, site, wd, before,env,current_app._get_current_object())
                to_do.append(future)
            try:
                for future in as_completed(to_do, timeout=timeout):  # 并发执行
                    ret = future.result()
                    # print(ret)
                    if ret and isinstance(ret,dict) and ret.get('list'):
                        res.extend(ret['list'])
            except Exception as e:
                print(f'发生错误:{e}')
                import atexit
                atexit.unregister(thread._python_exit)
                executor.shutdown = lambda wait: None

                # disable_exit_for_threadpool_executor()
    logger.info(f'drpy聚搜{len(search_sites)}个源共计耗时{get_interval(t1)}毫秒')
    return jsonify({
        "list": res
    })

@vod.route('/vods')
def vods_search():
    val = getSearchSites()
    print(val)

    # return jsonify(val)
    return render_template('show_search.html',val=val)

@vod.route('/vod')
def vod_home():
    lsg = storage_service()
    js0_disable = lsg.getItem('JS0_DISABLE',cfg.get('JS0_DISABLE',0))
    if js0_disable:
        abort(403)
    js0_password = lsg.getItem('JS0_PASSWORD', cfg.get('JS0_PASSWORD', ''))
    # print('js0_password:',js0_password)
    if js0_password:
        pwd = getParmas('pwd')
        if pwd != js0_password:
            abort(403)
    t0 = time()
    rule = getParmas('rule')
    ac = getParmas('ac')
    ids = getParmas('ids')
    if ac and ids and ids.find('#') > -1:  # 聚搜的二级
        id_list = ids.split(',')
        rule = id_list[0].split('#')[1]
        # print(rule)

    ext = getParmas('ext')
    filters = getParmas('f')
    tp = getParmas('type')
    # print(f'type:{tp}')
    # if not ext.startswith('http') and not rule:
    if not rule:
        return R.failed('规则字段必填')
    rule_list = getRuleLists()
    # if not ext.startswith('http') and not rule in rule_list:
    if not ext and not rule in rule_list:
        msg = f'服务端本地仅支持以下规则:{",".join(rule_list)}'
        return R.failed(msg)
    # logger.info(f'检验耗时:{get_interval(t0)}毫秒')
    t1 = time()
    # js_path = f'js/{rule}.js' if not ext.startswith('http') else ext
    js_path = f'js/{rule}.js' if not ext else ext
    with open('js/模板.js', encoding='utf-8') as f:
        before = f.read().split('export')[0]
    # logger.info(f'js读取耗时:{get_interval(t1)}毫秒')
    end_code = """\nif (rule.模板 && muban.hasOwnProperty(rule.模板)) {rule = Object.assign(muban[rule.模板], rule);}"""
    logger.info(f'参数检验js读取共计耗时:{get_interval(t0)}毫秒')
    t2 = time()


    # ctx, js_code = parser.runJs(js_path,before=before)
    # if not js_code:
    #     return R.failed('爬虫规则加载失败')
    # # rule = ctx.eval('rule')
    # # print(type(ctx.rule.lazy()),ctx.rule.lazy().toString())
    # ruleDict = ctx.rule.to_dict()

    ctx = Context()
    try:
        with open(js_path,encoding='utf-8') as f2:
            jscode = f2.read()
        env = get_env()
        for k in env:
            # print(f'${k}',f'{env[k]}')
            if f'${k}' in jscode:
                jscode = jscode.replace(f'${k}',f'{env[k]}')
        # print(env)
        # if env:
        #     jscode = render_template_string(jscode,**env)
        # print(jscode)
        jscode = before + jscode + end_code
        # print(jscode)
        ctx.eval(jscode)
        js_ret = ctx.get('rule')
        ruleDict = ujson.loads(js_ret.json())
    except Exception as e:
        logger.info(f'{e}')
        return R.failed('爬虫规则加载失败')

    # print(type(ruleDict))
    # print(ruleDict)
    # print(ruleDict)
    ruleDict['id'] = rule  # 把路由请求的id装到字典里,后面播放嗅探才能用
    # print(ruleDict)
    # print(rule)
    # print(type(rule))
    # print(ruleDict)
    logger.info(f'js装载耗时:{get_interval(t2)}毫秒')
    # print(ruleDict)
    # print(rule)
    cms = CMS(ruleDict,db,RuleClass,PlayParse,cfg,ext)
    wd = getParmas('wd')
    quick = getParmas('quick')
    play = getParmas('play') # 类型为4的时候点击播放会带上来
    flag = getParmas('flag') # 类型为4的时候点击播放会带上来
    # myfilter = getParmas('filter')
    t = getParmas('t')
    pg = getParmas('pg','1')
    pg = int(pg)
    q = getParmas('q')
    play_url = getParmas('play_url')

    if play:
        jxs = getJxs()
        play_url = play.split('play_url=')[1]
        play_url = cms.playContent(play_url, jxs,flag)
        if isinstance(play_url, str):
            # return redirect(play_url)
            # return jsonify({'parse': 0, 'playUrl': play_url, 'jx': 0, 'url': play_url})
            # return jsonify({'parse': 0, 'playUrl': play_url, 'jx': 0, 'url': ''})
            return jsonify({'parse': 0, 'playUrl': '', 'jx': 0, 'url': play_url})
        elif isinstance(play_url, dict):
            return jsonify(play_url)
        else:
            return play_url

    if play_url:  # 播放
        jxs = getJxs()
        play_url = cms.playContent(play_url,jxs)
        if isinstance(play_url,str):
            return redirect(play_url)
        elif isinstance(play_url,dict):
            return jsonify(play_url)
        else:
            return play_url

    if ac and t:  # 一级
        fl = {}
        if filters and filters.find('{') > -1 and filters.find('}') > -1:
            fl = json.loads(filters)
        # print(filters,type(filters))
        # print(fl,type(fl))
        data = cms.categoryContent(t,pg,fl)
        # print(data)
        return jsonify(data)
    if ac and ids: # 二级
        id_list = ids.split(',')
        show_name = False
        if ids.find('#') > -1:
            id_list = list(map(lambda x:x.split('#')[0],id_list))
            show_name = True
        # print('app:377',len(id_list))
        # print(id_list)
        data = cms.detailContent(pg,id_list,show_name)
        # print(data)
        return jsonify(data)
    if wd: # 搜索
        if rule == 'drpy':
            print(f'准备单独处理聚合搜索:{wd}')
            return multi_search(wd)
            # return multi_search2(wd)
        else:
            data = cms.searchContent(wd)
            # print(data)
            return jsonify(data)
    # return jsonify({'rule':rule,'js_code':js_code})
    home_data = cms.homeContent(pg)
    return jsonify(home_data)