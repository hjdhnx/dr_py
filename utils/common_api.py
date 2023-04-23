#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : common_api.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Author's Blog: https://blog.csdn.net/qq_32394351
# Date  : 2023/3/22

from utils import parser
from utils.env import get_env
from base.R import R
from flask import request,redirect
from utils.log import logger

def js_render(name):
    if not name or not name.split('.')[-1] in ['js','txt','py','json']:
        return R.error(f'非法猥亵,未指定文件名。必须包含js|txt|json|py')
    try:
        env = get_env()
        # print(env)
        if env.get('js_proxy'):
            js_proxy = env['js_proxy']
            burl = request.base_url
            if '=>' in js_proxy:
                oldsrc = js_proxy.split('=>')[0]
                if oldsrc in burl:
                        newsrc = js_proxy.split('=>')[1]
                        # print(f'js1源代理已启用,全局替换{oldsrc}为{newsrc}')
                        rurl = burl.replace(oldsrc, newsrc)
                        if burl != rurl:
                            jscode = parser.getJs(name, 'js')
                            # rjscode = render_template_string(jscode, env=env)
                            rjscode = jscode
                            for k in env:
                                # print(f'${k}', f'{env[k]}')
                                if f'${k}' in rjscode:
                                    rjscode = rjscode.replace(f'${k}', f'{env[k]}')
                            # rjscode = render_template_string(jscode, **env)
                            if rjscode.strip() == jscode.strip():  # 无需渲染才代理
                                return redirect(rurl)
                            else:
                                logger.info(f'{name}由于存在环境变量无法被依赖代理')

        return parser.toJs(name,'js',env)
    except Exception as e:
        return R.error(f'非法猥亵\n{e}')