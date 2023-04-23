#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : 批量重命名.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/12/12

import os

def main(path):
    # base_path = os.path.dirname(os.path.abspath(__file__))  # 当前文件所在目录
    # print(base_path)
    files = os.listdir(path)
    print(files)
    for file in files:
        if file.endswith('2.js'):
            print(file)
            os.rename(path+'/'+file,path+'/'+file.replace('2.js','.js'))
        elif file.endswith('2[飞].js'):
            print(file)
            os.rename(path+'/'+file,path+'/'+file.replace('2[飞].js','[飞].js'))


if __name__ == '__main__':
    path = r'F:\drpy源\js'
    main(path)