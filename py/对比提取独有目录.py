#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : 对比提取独有目录.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2023/1/6

import os
import shutil
from time import time

def getDirLists(path):
    files = os.listdir(path)
    print(len(files),files)
    return files

def get_extra(list1,list2):
    extra_list = set(list1) ^ set(list2)
    extra_list = list(extra_list)
    print(len(extra_list),extra_list)
    return extra_list

def get_interval(t):
    interval = time() - t
    interval = round(interval*1000,2)
    return interval

def copy_extra(compare_path,to_path,extra_list):
    t1 = time()
    total = len(extra_list)
    dir_total = 0
    for i in range(total):
        extra = extra_list[i]
        file_from = os.path.join(compare_path, extra)
        if os.path.isdir(file_from):  # 判断是否为文件夹
            dir_total += 1
            file_to = os.path.join(to_path, extra)
            print(f'开始提取第{i+1}/{total}项,复制{file_from}到{file_to}...')
            shutil.copytree(file_from, file_to, dirs_exist_ok=True)
        else:
            print(f'跳过提取非文件夹:{file_from}')
        # break
    print(f'全部文件夹提取完毕,共计{total}项,{dir_total}个文件夹,耗时{get_interval(t1)}毫秒')

if __name__ == '__main__':
    base_path = r'F:\odoo模块\odoo16c\addons'
    compare_path = r'F:\odoo模块\odoo16e20221019\odoo\addons'
    to_path = r'F:\odoo模块\odoo16ec\addons'
    base_files = getDirLists(base_path)
    compare_files = getDirLists(compare_path)
    extra_list = get_extra(base_files,compare_files)
    copy_extra(compare_path, to_path, extra_list)