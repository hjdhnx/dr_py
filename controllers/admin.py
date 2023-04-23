#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : admin.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/9/6
import os

import ujson
from flask import Blueprint,request,render_template,render_template_string,jsonify,make_response,redirect
from controllers.service import storage_service,rules_service,parse_service
from base.R import R
from base.database import db
from utils.log import logger
import shutil
from utils.update import getLocalVer,getOnlineVer,download_new_version,download_lives,copy_to_update
from utils import parser
from utils.env import get_env,update_env
from utils.web import getParmas,verfy_token
from js.rules import getRules,getCacheCount
from utils.parser import runJScode
from werkzeug.utils import secure_filename
from utils.web import md5
from utils.common_api import js_render

admin = Blueprint("admin", __name__)

# @admin.route("/",methods=['get'])
# def index():
#     return R.ok(msg='欢迎进入首页',data=None)

# @admin.route("/info",methods=['get'])
# def info_all():
#     data = storage_service.query_all()
#     return R.ok(data=data)

@admin.route('/')
def admin_index():  # 管理员界面
    if not verfy_token():
        return render_template('login.html')
    lsg = storage_service()
    live_url = lsg.getItem('LIVE_URL')
    use_py = lsg.getItem('USE_PY')
    js0_password = lsg.getItem('JS0_PASSWORD')
    # print(f'live_url:', live_url)
    rules = getRules('js')
    # print(rules)
    cache_count = getCacheCount()
    # print(cache_count)
    return render_template('admin.html',js0_password=js0_password, pystate=use_py,rules=rules,cache_count=cache_count, ver=getLocalVer(), live_url=live_url)

@admin.route('/settings')
def admin_settings():  # 管理员界面
    if not verfy_token():
        return render_template('login.html')
    lsg = storage_service()
    # conf_list = 'LIVE_URL|USE_PY|PLAY_URL|PLAY_DISABLE|LAZYPARSE_MODE|WALL_PAPER_ENABLE|WALL_PAPER|UNAME|PWD|LIVE_MODE|LIVE_URL|CATE_EXCLUDE|TAB_EXCLUDE'.split('|')
    conf_lists = lsg.getStoreConf()
    # print(conf_lists)
    return render_template('settings.html', conf_lists=conf_lists,ver=getLocalVer())

@admin.route('/save_conf',methods=['POST'])
def admin_save_conf():  # 管理员界面
    if not verfy_token():
        # return render_template('login.html')
        return R.error('请登录后再试')
    key = getParmas('key')
    value = getParmas('value')
    print(f'key:{key},value:{value}')
    lsg = storage_service()
    res_id = lsg.setItem(key,value)
    return R.success(f'修改成功,记录ID为:{res_id}')

@admin.route('/update_env',methods=['POST'])
def admin_update_env():  # 更新环境变量中的某个值
    if not verfy_token():
        # return render_template('login.html')
        return R.error('请登录后再试')
    key = getParmas('key')
    value = getParmas('value')
    print(f'key:{key},value:{value}')
    ENV = update_env(key,value)
    return R.success(f'修改成功,最新的完整ENV见data',data=ENV)


@admin.route("/view/<name>",methods=['GET'])
def admin_view_rule(name):
    return js_render(name)
    # if not name or not name.split('.')[-1] in ['js','txt','py','json']:
    #     return R.error(f'非法猥亵,未指定文件名。必须包含js|txt|json|py')
    # try:
    #     env = get_env()
    #     # print(env)
    #     if env.get('js_proxy'):
    #         js_proxy = env['js_proxy']
    #         burl = request.base_url
    #         if '=>' in js_proxy:
    #             oldsrc = js_proxy.split('=>')[0]
    #             if oldsrc in burl:
    #                     newsrc = js_proxy.split('=>')[1]
    #                     # print(f'js1源代理已启用,全局替换{oldsrc}为{newsrc}')
    #                     rurl = burl.replace(oldsrc, newsrc)
    #                     if burl != rurl:
    #                         jscode = parser.getJs(name, 'js')
    #                         # rjscode = render_template_string(jscode, env=env)
    #                         rjscode = jscode
    #                         for k in env:
    #                             # print(f'${k}', f'{env[k]}')
    #                             if f'${k}' in rjscode:
    #                                 rjscode = rjscode.replace(f'${k}', f'{env[k]}')
    #                         # rjscode = render_template_string(jscode, **env)
    #                         if rjscode.strip() == jscode.strip():  # 无需渲染才代理
    #                             return redirect(rurl)
    #                         else:
    #                             logger.info(f'{name}由于存在环境变量无法被依赖代理')
    #
    #     return parser.toJs(name,'js',env)
    # except Exception as e:
    #     return R.error(f'非法猥亵\n{e}')

@admin.route('/clear/<name>')
def admin_clear_rule(name):
    if not name or not name.split('.')[-1] in ['js','txt','py','json']:
        return R.error(f'非法猥亵,未指定文件名。必须包含js|txt|json|py')
    if not verfy_token():
        return render_template('login.html')

    file_path = os.path.abspath(f'js/{name}')
    print(file_path)
    if not os.path.exists(file_path):
        return R.error('服务端没有此文件!'+file_path)
    os.remove(file_path)
    return R.ok('成功删除文件:'+file_path)

@admin.route('/get_ver')
def admin_get_ver():
    if not verfy_token():
        # return render_template('login.html')
        return R.error('请登录后再试')
    online_ver,msg = getOnlineVer()
    return jsonify({'local_ver':getLocalVer(),'online_ver':online_ver,'msg':msg})

@admin.route('/update_db')
def admin_update_db():
    if not verfy_token():
        # return render_template('login.html')
        return R.error('请登录后再试')
    old_dbfile = 'migrations'
    if os.path.exists(old_dbfile):
        logger.info(f'开始删除历史数据库迁移文件:{old_dbfile}')
        shutil.rmtree(old_dbfile)
    db.session.execute('drop table if exists alembic_version')
    cmd = 'flask db migrate && flask db upgrade'
    if not os.path.exists('migrations'):
        cmd = 'flask db init && '+cmd
    logger.info(f'开始执行cmd:{cmd}')
    result = os.system(cmd)
    logger.info(f'cmd执行结果:{result}')
    return R.success('数据库升级完毕')

@admin.route('/update_ver')
def admin_update_ver():
    if not verfy_token():
        return R.failed('请登录后再试')
    msg = download_new_version()
    return R.success(msg)

@admin.route('/rule_state/<int:state>',methods=['POST'])
def admin_rule_state(state=0):  # 管理员修改规则状态
    if not verfy_token():
        return R.error('请登录后再试')
    names = getParmas('names')
    if not names:
        return R.success(f'修改失败,没有传递names参数')
    rule_list = names.split(',')
    rules = rules_service()
    # print(rules.query_all())
    # print(rules.getState(rule_list[0]))
    # print(rule_list)
    success_list = []
    for rule in rule_list:
        try:
            res_id = rules.setState(rule,state)
            success_list.append(f'{rule}:{res_id}')
        except:
            success_list.append(rule)

    return R.success(f'修改成功,服务器反馈信息为:{success_list}')

@admin.route('/rule_order/<int:order>',methods=['POST'])
def admin_rule_order(order=0):  # 管理员修改规则顺序
    if not verfy_token():
        return R.error('请登录后再试')
    names = getParmas('names')
    if not names:
        return R.success(f'修改失败,没有传递names参数')
    rule_list = names.split(',')
    rules = rules_service()
    # print(rules.query_all())
    # print(rules.getState(rule_list[0]))
    # print(rule_list)
    success_list = []
    rule_list.reverse() # 倒序解决时间多重排序问题
    for rule in rule_list:
        try:
            res_id = rules.setOrder(rule,order)
            success_list.append(f'{rule}:{res_id}')
        except:
            success_list.append(rule)

    return R.success(f'修改成功,服务器反馈信息为:{success_list}')

@admin.route('/parse/save_data',methods=['POST'])
def admin_parse_save_data():  # 管理员保存拖拽排序后的解析数据
    if not verfy_token():
        return R.error('请登录后再试')
    data = getParmas('data')
    if not data:
        return R.success(f'修改失败,没有传递data参数')
    parse = parse_service()
    success_list = []
    data = ujson.loads(data)
    new_list = []
    new_data = []
    for nd in data:
        if not nd.get('url') and nd.get('name') != '🌐Ⓤ':
            continue
        if nd['url'] not in new_list:
            new_data.append(nd)
            new_list.append(nd['url'])

    print(f'去重前:{len(data)},去重后:{len(new_data)}')
    for i in range(len(new_data)):
        d = new_data[i]
        # if not d.get('url') and d.get('name') != '🌐Ⓤ':
        #     continue
        obj = {
            'name':d.get('name', ''),
            'url':d.get('url', ''),
            'state':d.get('state',1),
            'type': d.get('state',0),
            'order':i+1,
            'ext':d.get('ext',''),
            'header':d.get('header',''),
        }
        # print(obj)
        try:
            parse.saveData(obj)
            success_list.append(f'parse:{d["url"]}')
            # print(obj)
            # print(200,obj)
        except Exception as e:
            success_list.append(d["url"])
            print(f'{d["url"]}失败:{e}')
    # print(len(success_list))
    return R.success(f'修改成功,服务器反馈信息为:{success_list}')

@admin.route('/force_update')
def admin_force_update():
    if not verfy_token():
        return R.failed('请登录后再试')
    ret = copy_to_update()
    if ret:
        msg = '升级成功'
        return R.success(msg)
    else:
        msg = '升级失败。具体原因只能去看实时日志(通过9001端口)'
        return R.failed(msg)

@admin.route('/update_lives')
def admin_update_lives():
    url = getParmas('url')
    if not url:
        return R.failed('未提供被同步的直播源远程地址!')
    if not verfy_token():
        return R.failed('请登录后再试')
    live_url = url
    success = download_lives(live_url)
    if success:
        return R.success(f'直播源{live_url}同步成功')
    else:
        return R.failed(f'直播源{live_url}同步失败')

@admin.route('/write_live_url')
def admin_write_live_url():
    url = getParmas('url')
    if not url:
        return R.failed('未提供修改后的直播源地址!')
    if not verfy_token():
        return R.failed('请登录后再试')
    lsg = storage_service()
    id = lsg.setItem('LIVE_URL',url)
    msg = f'已修改的配置记录id为:{id}'
    return R.success(msg)

@admin.route('/change_use_py')
def admin_change_use_py():
    if not verfy_token():
        return R.failed('请登录后再试')
    lsg = storage_service()
    use_py = lsg.getItem('USE_PY')
    new_use_py = '' if use_py else '1'
    state = '开启' if new_use_py else '关闭'
    id = lsg.setItem('USE_PY', new_use_py)
    msg = f'已修改的配置记录id为:{id},结果为{state}'
    return R.success(msg)

# @admin.route('/get_use_py')
# def admin_get_use_py():
#     if not verfy_token():
#         return R.failed('请登录后再试')
#     lsg = storage_service()
#     use_py = lsg.getItem('USE_PY')
#     state = 1 if use_py else 0
#     return R.success(state)

@admin.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if not verfy_token():
        return render_template('login.html')
    if request.method == 'POST':
        try:
            file = request.files['file']
            filename = secure_filename(file.filename)
            print(f'推荐安全文件命名:{filename}')
            savePath = f'js/{file.filename}'
            if os.path.exists(savePath):
                return R.failed(f'上传失败,文件已存在,请先查看删除再试')
            with open('js/模板.js', encoding='utf-8') as f2:
                before = f2.read().split('export')[0]
            upcode = file.stream.read().decode('utf-8')
            check_to_run = before + upcode
            # print(check_to_run)
            try:
                loader, _ = runJScode(check_to_run)
                rule = loader.eval('rule')
                if not rule:
                    return R.failed('文件上传失败,检测到上传的文件不是drpy框架支持的源代码')
            except:
                return R.failed('文件上传失败,检测到上传的文件不是drpy框架支持的源代码')
            print(savePath)
            file.seek(0) # 读取后变成空文件,重新赋能
            file.save(savePath)
            return R.success('文件上传成功')
        except Exception as e:
            return R.failed(f'文件上传失败!{e}')
    else:
        # return render_template('upload.html')
        return R.failed('文件上传失败')

@admin.route('/login',methods=['GET','POST'])
def login_api():
    username = getParmas('username')
    password = getParmas('password')
    autologin = getParmas('autologin')
    if not all([username,password]):
        return R.failed('账号密码字段必填')
    token = md5(f'{username};{password}')
    check = verfy_token(token=token)
    if check:
        # response = make_response(redirect('/admin'))
        response = make_response(R.success('登录成功'))
        response.set_cookie('token', token)
        return response
    else:
        return R.failed('登录失败,用户名或密码错误')

@admin.route('/logtail')
def admin_logtail():
    if not verfy_token():
        return R.failed('请登录后再试')
    return render_template('logtail.html')

@admin.route('/lives')
def admin_lives():
    if not verfy_token():
        return R.failed('请登录后再试')
    # print(dir(request))
    # 完整地址: request.base_url url
    # 带http的前缀 host_url root_url
    # 不带http的前缀 host
    # 当前路径 path
    host_url = request.host_url
    def get_lives():
        base_path = os.path.dirname(os.path.abspath(__file__))  # 当前文件所在目录
        # print(base_path)
        live_path = os.path.join(base_path, '../txt/lives')
        # print(live_path)
        files = os.listdir(live_path)
        # print(files)
        # files = list(filter(lambda x: str(x).endswith('.txt') and str(x).find('模板') < 0, files))
        files = list(filter(lambda x: str(x).split('.')[-1] in ['txt','json','m3u'] and str(x).find('模板') < 0, files))
        files = [f'{host_url}lives?path=txt/lives/{file}' for file in files]
        return files

    files = '\n'.join(get_lives())
    response = make_response(files)
    response.headers['Content-Type'] = 'text/plain; charset=utf-8'
    return response