#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : log.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/9/6

import os
import logging
from logging import handlers
import sys

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
LOG_ROOT = dirname
print(LOG_ROOT)

# logging.basicConfig(
#                     # level=logging.INFO,  # 控制台打印的日志级别
#                     level=logging.DEBUG,  # 控制台打印的日志级别
#                     filename='dr.log',  # 将日志写入log_new.log文件中
#                     filemode='a',  # 模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志 a是追加模式，默认如果不写的话，就是追加模式
#                     # format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     format="%(asctime)s:%(levelname)s:%(name)s -- %(message)s", datefmt="%Y/%m/%d %H:%M:%S"  # 日志格式
#                     )

def get_logger(log_filename, level=logging.DEBUG, when='D', back_count=0):
    """
    https://blog.csdn.net/qq_39147299/article/details/124455632
    :brief  日志记录
    :param log_filename: 日志名称
    :param level: 日志等级 critical > error > warning > info > debug 当设置某个级别之后，把它低的不会被记录，例如级别设置为warning，则info和debug则会被丢弃
    :param when: 间隔时间:
        S:秒
        M:分
        H:小时
        D:天
        W:每星期（interval==0时代表星期一）
        midnight: 每天凌晨
    :param back_count: 备份文件的个数，若超过该值，就会自动删除
    :return: logger
    """
    # 创建一个日志器。提供了应用程序接口
    logger = logging.getLogger(log_filename)
    # 设置日志输出的最低等级,低于当前等级则会被忽略
    logger.setLevel(level)
    # 创建日志输出路径
    # log_path = os.path.join(LOG_ROOT, "logs")
    base_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))  # 上级目录
    log_path = os.path.join(base_path, f'logs')

    if not os.path.exists(log_path):
        os.mkdir(log_path)
    log_file_path = os.path.join(log_path, log_filename)
    # 创建格式器
    # formatter = logging.Formatter('%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',datefmt="%Y/%m/%d %H:%M:%S")
    formatter = logging.Formatter('%(asctime)s - %(pathname)s[line:%(lineno)d]:%(levelname)s:%(name)s -- %(message)s', datefmt="%Y-%m-%d %H:%M:%S")
    # 创建处理器：ch为控制台处理器，fh为文件处理器
    ch = logging.StreamHandler()
    ch.setLevel(level)
    # 输出到文件
    fh = logging.handlers.TimedRotatingFileHandler(
        filename=log_file_path,
        when=when,
        backupCount=back_count,
        encoding='utf-8')
    fh.setLevel(level)
    # 设置日志输出格式
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # 将处理器，添加至日志器中
    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger

logger = get_logger('dr.log',back_count=3)