#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : 腾讯筛选.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/9/25


cates = 'choice&tv&movie&variety&cartoon&child&doco'.split('&')
fl_dict = {}

for cate in cates:
    fls = []
    fls.append({
        'key':'sort',
        'name':'排序',
        'value':[{'n':'最热','v':'18'},{'n':'最新','v':'19'},{'n':'好评','v':'16'},{'n':'高分好评','v':'21'}],
    })
    fls.append({
        'key': 'pay',
        'name': '资费',
        'value': [{'n': '全部', 'v': '-1'}, {'n': '免费', 'v': '867'}, {'n': '会员', 'v': '6'}],
    })
    year_value = [{'n': str(2022-i), 'v': str(2022-i)} for i in range(8)]
    year_value = [{'n': '全部', 'v': '-1'}]+year_value
    fls.append({
        'key': 'year',
        'name': '年代',
        'value': year_value,
    })
    fl_dict[cate] = fls
print(fl_dict)