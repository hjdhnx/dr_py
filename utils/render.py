#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : render.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2023/4/19

import re
from jinja2 import Environment, Template


def to_lower_camel_case(x):
    """转小驼峰法命名：下划线转驼峰且首字母小写"""
    s = re.sub('_([a-zA-Z])', lambda m: (m.group(1).upper()), x)
    return s[0].lower() + s[1:]


def render_template_string(source: str, **context):
    # 构造环境
    env = Environment()
    # 添加一个过滤器
    env.filters['to_lower_camel_case'] = to_lower_camel_case
    # 获取模板
    template: Template = env.from_string(source)
    # 渲染
    view = template.render(**context)
    return view
