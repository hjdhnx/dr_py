#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : app.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/9/6

from flask.app import Flask
from flask_migrate import Migrate
from base import config
from base.database import db
from utils.log import logger
from utils.system import get_wlan_info, getHost
from controllers import *
from js.rules import getRuleLists
import sys


def create_flask_app():
    app = Flask(__name__, static_folder='static', static_url_path='/static')
    app.config.from_object(config)  # 单独的配置文件里写了，这里就不用弄json中文显示了
    app.register_blueprint(home.home, url_prefix='')
    app.register_blueprint(admin.admin, url_prefix='/admin')
    app.register_blueprint(vod.vod, url_prefix='')
    app.register_blueprint(cls.cls, url_prefix='/cls')
    app.register_blueprint(layui.layui, url_prefix='/layui')
    app.register_blueprint(parse.parse, url_prefix='/parse')
    # app.register_blueprint(web.web, url_prefix='/web',template_folder='templates/cmsV10/mxpro/html/index/')
    app.register_blueprint(web.web, url_prefix='/web')
    app.logger.name = "drLogger"
    # lsg = service.storage_service()
    logger.info(f"默认解析地址:{app.config.get('PLAY_URL')}")
    # logger.info(f"自定义播放解析地址:{lsg.getItem('PLAY_URL')}")
    logger.info(f'当前操作系统{sys.platform}')
    rule_list = getRuleLists()
    wlan_info, _ = get_wlan_info()
    logger.info(rule_list)
    logger.info(
        f'局域网: {getHost(1, app.config.get("HTTP_PORT"))}/index\n本地: {getHost(0, app.config.get("HTTP_PORT"))}/index\nwlan_info:{wlan_info}')
    db.init_app(app)
    db.app = app
    db.create_all(app=app)
    return app


app = create_flask_app()
migrate = Migrate(app, db)
max_version = (3, 11)  # 小于3.11的版本(3.6-3.10)
max_version_str = ".".join([str(i) for i in max_version])
now_python_ver = ".".join([str(i) for i in sys.version_info[:3]])
no_error = True
if sys.version_info < max_version:
    try:
        from gevent.pywsgi import WSGIServer

        # from gevent import monkey
        # monkey.patch_all()  # 多线程,只能放在最开头,import其它包之前

        from gevent import monkey

        monkey.patch_socket()  # 开启socket异步
        print(f'当前python版本{now_python_ver}为{max_version_str}及以下,支持gevent')

    except Exception as e:
        print(f'gevent使用过程中发生了错误:{e}')
        no_error = False
else:
    print(f'当前python版本{now_python_ver}为{max_version_str}及以上,不支持gevent')

if __name__ == "__main__":
    http_port = int(app.config.get('HTTP_PORT', 5705))
    http_host = app.config.get('HTTP_HOST', '0.0.0.0')
    threaded = app.config.get('THREAD')
    GEVENT = app.config.get('GEVENT')
    print(GEVENT)
    if threaded is None:
        threaded = True
    if GEVENT is None:
        debug = False
    # https://www.zhihu.com/question/64096559
    print(f'threaded:{threaded},GEVENT:{GEVENT}')
    # if sys.version_info < (3, 9) and not sys.platform.startswith('win'):
    use_gevent = sys.version_info < max_version  # 是否使用协程
    is_debug = (not GEVENT) and sys.platform.startswith('win')  # windows开调试模式
    print(f'开启调试模式:{is_debug}')
    if use_gevent and no_error and not is_debug:
        # server = WSGIServer(('0.0.0.0', 5705), app, handler_class=WebSocketHandler,log=app.logger)
        # server = WSGIServer(('0.0.0.0', 5705), app, handler_class=WebSocketHandler,log=None)
        server = WSGIServer((http_host, http_port), app, log=logger)
        server.serve_forever()
    else:
        app.run(debug=False, host=http_host, port=http_port, threaded=threaded)
