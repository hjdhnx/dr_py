#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : R.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/9/6

from flask import jsonify

class copy_utils:

    @staticmethod
    def obj_to_dic(obj):
        '''
        将传入的data对象转成字典
        '''
        result = {}
        for temp in obj.__dict__:
            if temp.startswith('_') or temp == 'metadata':
                continue
            result[temp] = getattr(obj, temp)
        return result

    @staticmethod
    def obj_to_list(list_obj):
        '''
        将传入的data对象转成List,list中的元素是字典
        '''
        result = []
        for obj in list_obj:
            result.append(copy_utils.obj_to_dic(obj))
        return result


class R(object):

    @classmethod
    def ok(self,msg='操作成功',data=None):
        if not data:
            data = []
        result = {"code": 200, "msg": msg, "data": data,"count":len(data)}
        return jsonify(result)

    @classmethod
    def error(self,msg="系统异常",code=404):
        result = {"code": code, "msg": msg}
        return jsonify(result)

    @classmethod
    def success(self,msg='操作成功', data=None):
        return self.ok(msg,data)

    @classmethod
    def failed(self,msg="系统异常", code=404):
        return self.error(msg,code)