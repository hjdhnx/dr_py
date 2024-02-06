#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : base_java_loader.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Author's Blog: https://blog.csdn.net/qq_32394351
# Date  : 2024/1/11

import os
import sys

sys.path.append('..')
try:
    # from base.spider import Spider as BaseSpider
    from base.spider import BaseSpider
    from com.github.tvbox.osc.util import PyUtil
    from java import jbyte, jarray
    # https://chaquo.com/chaquopy/doc/current/python.html#java.jbyte
except ImportError:
    from t4.base.spider import BaseSpider

# 全局变量
gParam = {
    # JVM已经启用过某个jar文件
    "JVM": {'xx.jar': False},
}


class Spider(BaseSpider):  # 元类 默认的元类 type
    jar_path: str = ''
    jClass = None

    def _prepare_env(self, jpype):
        global gParam
        if gParam['JVM'].get(self.jar_path):
            return
        try:
            jpype.startJVM(classpath=[self.jar_path], convertStrings=False)
            gParam['JVM'][self.jar_path] = True
        except Exception as e:
            self.log(f'jpype.startJVM发生了错误:{e}')

    def init_jar(self, jar_path="./bdys.jar"):
        self.log(f'base_java_loader 初始化jar文件:{jar_path}')
        if not os.path.exists(jar_path):
            raise FileNotFoundError
        self.jar_path = jar_path
        if self.ENV.lower() == 't4':
            import jpype
            self._prepare_env(jpype)
            self.jClass = jpype.JClass
        elif self.ENV.lower() == 't3':
            PyUtil.load(jar_path)
            self.jClass = None

    def call_java(self, class_name, method_name, *args):
        if self.ENV.lower() == 't4':
            class1 = self.jClass(class_name)
            method = getattr(class1, method_name)
            # method = eval(f'class1.{method_name}', {'class1': class1})
            # print(method)
            return method(*args)
        elif self.ENV.lower() == 't3':
            return PyUtil.call(class_name, method_name, *args)

    @staticmethod
    def jarBytes(some_bytes: bytes):
        return jarray(jbyte)(some_bytes)

    def init(self, extend=""):
        pass

    def homeContent(self, filter):
        pass

    def homeVideoContent(self):
        pass

    def categoryContent(self, tid, pg, filter, extend):
        pass

    def detailContent(self, ids):
        pass

    def searchContent(self, key, quick, pg=1):
        pass

    def playerContent(self, flag, id, vipFlags):
        pass

    def localProxy(self, param):
        pass

    def isVideoFormat(self, url):
        pass

    def manualVideoCheck(self):
        pass

    def getName(self):
        pass
