#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : cfg.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/9/10

from werkzeug.utils import import_string
from base import config
from easydict import EasyDict as edict

def get_conf(obj):
    new_conf = {}
    if isinstance(obj, str):
        obj = import_string(obj)
    for key in dir(obj):
        if key.isupper():
            new_conf[key] = getattr(obj, key)
    return new_conf

cfg = edict(get_conf(config))