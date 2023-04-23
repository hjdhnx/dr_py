#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : vipParse.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/10/31

from base.database import db
from datetime import datetime

class VipParse(db.Model):
    __tablename__ = 'vip_parse'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    url = db.Column(db.String(255),unique=True)
    state = db.Column(db.Integer, default=1)
    type = db.Column(db.Integer, default=0)
    order = db.Column(db.Integer, default=0)
    ext = db.Column(db.String(255))
    header = db.Column(db.String(255))
    create_date = db.Column(db.DateTime, index=True, default=datetime.now)
    write_date = db.Column(db.DateTime, index=True, default=datetime.now,onupdate=datetime.now)

    def __repr__(self):
        return "<VipParse(id='%s', name='%s', url='%s')>" % (
            self.id, self.name, self.url)

    @classmethod
    def hasItem(self, url):
        exists = db.session.query(self).filter(self.url == url).scalar() is not None
        if exists:
            return True
        else:
            return False