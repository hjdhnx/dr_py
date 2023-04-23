#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : ruleclass.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/9/6

from base.database import db
from datetime import datetime

class RuleClass(db.Model):
    __tablename__ = 'rule_class'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), unique=True)
    class_name = db.Column(db.String(255))
    class_url = db.Column(db.String(255))
    cookie = db.Column(db.String(255))
    state = db.Column(db.Integer, default=1)
    order = db.Column(db.Integer, default=0)
    create_date = db.Column(db.DateTime, index=True, default=datetime.now)
    write_date = db.Column(db.DateTime, index=True, default=datetime.now,onupdate=datetime.now)

    def __repr__(self):
        return "<RuleClass(name='%s', class_name='%s', class_url='%s',cookie='%s')>" % (
            self.name, self.class_name, self.class_url, self.cookie)

    @classmethod
    def hasItem(self, key):
        exists = db.session.query(self).filter(self.name == key).scalar() is not None
        if exists:
            return True
        else:
            return False