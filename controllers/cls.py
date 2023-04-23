#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : CLS.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/9/6

from flask import Blueprint
from controllers.classes import getClasses,getClassInfo
from base.R import R
from utils.log import logger
from base.database import db
from models.ruleclass import RuleClass

cls = Blueprint("cls", __name__)

@cls.route('/get/<cls>')
def getClassInfoApi(cls):
    info = getClassInfo(cls)
    return R.ok(info)

@cls.route('/clear/<cls>')
def clearClassApi(cls):
    logger.info(f'开始查询{cls}的分类详情')
    res = db.session.query(RuleClass).filter(RuleClass.name == cls)
    if res:
        res.delete()
        db.session.commit()
        return R.success(f'已清除{cls}的分类缓存')
    else:
        return R.failed(f'数据库不存在{cls}的分类缓存')