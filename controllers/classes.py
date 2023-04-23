#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : classes.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/9/6

from base.database import db
from utils.log import logger
from models.ruleclass import RuleClass

def getClasses():
    if not db:
        msg = '未提供数据库连接'
        logger.info(msg)
        return []
    res = db.session.query(RuleClass).all()
    return [rc.name for rc in res]

def getClassInfo(cls):
    if not db:
        msg = f'未提供数据库连接,获取{cls}详情失败'
        logger.info(msg)
        return None
    logger.info(f'开始查询{cls}的分类详情')
    res = db.session.query(RuleClass).filter(RuleClass.name == cls).first()
    if res:
        logger.info(str(res))
        return str(res)
    else:
        return f'数据库不存在{cls}的分类缓存'