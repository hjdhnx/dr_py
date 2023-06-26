#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : config.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/9/6

DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'gp'
PASSWORD = '123456'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'pira'
# DB_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)
# DB_URI = 'sqlite:///models/rules.db?charset=utf8&check_same_thread=False'
DB_URI = 'sqlite:///base/rules.db?charset=utf8&check_same_thread=False'
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = False  # 打印sql语句
JSON_AS_ASCII = False  # jsonify返回的中文正常显示
PLAY_URL = 'http://cms.nokia.press'  # 匹配远程解析服务器链接 远程接口主页地址，后面不能有/
PLAY_URL = PLAY_URL.rstrip('/')
PID_URL = ''  # 自定义的9001进程管理快捷方式
PID_URL = PID_URL.rstrip('/')
HTTP_HOST = '0.0.0.0'
HTTP_PORT = '5705'
PLAY_DISABLE = False  # 全局禁用播放解析
LAZYPARSE_MODE = 1  # 播放解析模式(0 本地 1 局域网 2远程 仅在全局禁用为False的时候生效)
WALL_PAPER_ENABLE = True  # 启用自定义壁纸
# WALL_PAPER = "https://picsum.photos/1280/720/?blur=10"  # 自定义壁纸,可注释
WALL_PAPER = "https://tuapi.eees.cc/api.php?category=fengjing&type=302"  # 自定义壁纸,可注释
SUP_PORT = 9001  # supervisord 服务端口
RETRY_CNT = 3  # 验证码重试次数
# OCR_API = 'http://192.168.3.224:9000/api/ocr_img' # 验证码识别接口,传参数data
# OCR_API = 'http://dm.mudery.com:10000' # 验证码识别接口,传参数data
OCR_API = 'https://api.nn.ci/ocr/b64/text'  # 验证码识别接口,传参数data
UNAME = 'admin'  # 管理员账号
PWD = 'drpy'  # 管理员密码
USE_PY = 0  # 开启py源
JS0_DISABLE = 0  # 禁用js0
JS0_PASSWORD = ''  # js0密码
JS_MODE = 0  # js模式 0 drpy服务器解析 1 pluto本地解析
MAX_CONTENT_LENGTH = 1 * 1024 * 100  # 100 kB
LIVE_MODE = 0  # 0 本地 1外网
# LIVE_URL = 'https://gitcode.net/bd/v/-/raw/main/live/zb.txt'  # 初始化外网直播地址(后续在管理界面改)
# LIVE_URL = 'https://agit.ai/hu/hcr/raw/commit/f8e9c10309a533e5b06df133f859c45cb91f4731/0ER.txt'  # 月光直播接口
LIVE_URL = 'https://raw.fastgit.org/zhanghong1983/TVBOXZY/main/TV/live.txt'  # 初始化外网直播地址(后续在管理界面改)
CATE_EXCLUDE = '首页|留言|APP|下载|资讯|新闻|动态|明星|专题|最新|排行|解析'  # 动态分类过滤
TAB_EXCLUDE = '猜你|喜欢|下载|剧情|简介|排序'  # 动态线路名过滤
# {% if config.WALL_PAPER %}"wallpaper":"{{ config.WALL_PAPER }}",{% endif %}
SEARCH_TIMEOUT = 5000  # 聚搜超时毫秒
SEARCH_LIMIT = 24  # 聚搜限制条数
MULTI_MODE = 0  # 多源模式
XR_MODE = 1  # 仙人模式
JS_PROXY = 'http://localhost:5705/admin/view/=>https://ghproxy.net/https://raw.githubusercontent.com/hjdhnx/dr_py/main/js/'  # 源代理
ALI_TOKEN = ''  # 适用于初始配置的阿里云token
ENV = '{"bili_cookie":""}'  # 自定义环境变量
UPDATE_PROXY = 'https://ghproxy.net/'  # 检测升级代理
THREAD = True  # 开启windows多线程调用
GEVENT = False  # windows开启此参数就不走gevent,方便调试
SPECIAL = '腾云驾雾:腾讯&奇珍异兽:爱奇艺&百忙无果:芒果&优酷&哔哩影视&Alist'  # 特殊优选
