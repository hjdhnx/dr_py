#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : error.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/8/25

def failed(msg):
    return {
        'msg':msg,
        'code':404,
    }

def success(msg):
    return {
        'msg':msg,
        'code':200,
    }