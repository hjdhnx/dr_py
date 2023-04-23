#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : test_time.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/12/29

import datetime
from datetime import timedelta

if __name__ == '__main__':
    # a = datetime.datetime.now().now().replace(hour=0, minute=1)).strftime('%Y-%m-%d %H:%M:%S')
    # print(a)
    print(datetime)
    print(datetime.datetime.now())
    print(datetime.datetime.now().replace(hour=0, minute=1).strftime('%Y-%m-%d %H:%M:%S'))
    print((datetime.datetime.now().replace(hour=0, minute=0, second=0)+ timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S'))