#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : 芒果筛选.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/9/25

cates = '2&3&1&50&51&115'.split('&')
fl_dict = {}

for cate in cates:
    fls = []
    fls.append({
        'key':'chargeInfo',
        'name':'付费类型',
        'value':[{'n':'全部','v':'all'},{'n':'免费','v':'b1'},{'n':'vip','v':'b2'},{'n':'VIP用券','v':'b3'},{'n':'付费点播','v':'b4'}],
    })
    fls.append({
        'key': 'sort',
        'name': '排序',
        'value': [{'n': '最新', 'v': 'c1'}, {'n': '最热', 'v': 'c2'}, {'n': '知乎高分', 'v': 'c4'}],
    })
    year_value = [{'n': str(2022-i), 'v': str(2022-i)} for i in range(19)]
    year_value = [{'n': '全部', 'v': 'all'}]+year_value
    fls.append({
        'key': 'year',
        'name': '年代',
        'value': year_value,
    })
    fl_dict[cate] = fls
print(fl_dict)