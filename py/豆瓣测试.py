#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : 豆瓣测试.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/9/16

import json

selected_categories = {
                        "类型": "",
                        "形式": "",
                        "地区": ""
                    }
print(selected_categories)
b = json.dumps(selected_categories, separators=(',', ':'), ensure_ascii=False)
print(b)