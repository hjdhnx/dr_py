#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : 荐片筛选.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/10/22

def getFilters():
    fyyear = '全部&2022&2021&2020&2019&2018&2017&2016'.split('&')
    fyyeark = '0&101&118&16&7&2&3&22'.split('&')
    fysort = '热门&评分&更新'.split('&')
    fysortK = 'hot&rating&update'.split('&')
    fyclass='0&1&2&3&4'

    fy_dict = {}
    for i in fyclass.split('&'):
        fy_dict[i] = [{
                'key': 'year',
                'name': '年代',
                'value': [{'n':fyyear[j],'v':fyyeark[j]} for j in range(len(fyyear))]
            },{
                'key': 'sort',
                'name': '排序',
                'value': [{'n':fysort[k],'v':fysortK[k]} for k in range(len(fysort))]
            }]
    print(fy_dict)

if __name__ == '__main__':
    getFilters()
