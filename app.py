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
from utils.system import get_wlan_info,getHost
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
    app.logger.name = "drLogger"
    # lsg = service.storage_service()
    logger.info(f"默认解析地址:{app.config.get('PLAY_URL')}")
    # logger.info(f"自定义播放解析地址:{lsg.getItem('PLAY_URL')}")
    logger.info(f'当前操作系统{sys.platform}')
    rule_list = getRuleLists()
    wlan_info,_ = get_wlan_info()
    logger.info(rule_list)
    logger.info(f'局域网: {getHost(1, app.config.get("HTTP_PORT"))}/index\n本地: {getHost(0, app.config.get("HTTP_PORT"))}/index\nwlan_info:{wlan_info}')
    db.init_app(app)
    db.app = app
    db.create_all(app=app)
    return app

app = create_flask_app()
migrate = Migrate(app, db)

now_python_ver = ".".join([str(i) for i in sys.version_info[:3]])
if sys.version_info < (3,9):
    from gevent.pywsgi import WSGIServer
    # from gevent import monkey
    # monkey.patch_socket() # 开启socket异步
    print(f'当前python版本{now_python_ver}为3.9.0及以下,支持gevent')
else:
    print(f'当前python版本{now_python_ver}为3.9.0及以上,不支持gevent')

if __name__ == "__main__":
    http_port = int(app.config.get('HTTP_PORT', 5705))
    http_host = app.config.get('HTTP_HOST', '0.0.0.0')
    if sys.version_info < (3, 9):
        # server = WSGIServer(('0.0.0.0', 5705), app, handler_class=WebSocketHandler,log=app.logger)
        # server = WSGIServer(('0.0.0.0', 5705), app, handler_class=WebSocketHandler,log=None)
        server = WSGIServer((http_host, http_port), app, log=logger)
        server.serve_forever()
    else:
        app.run(debug=False, host=http_host, port=http_port)