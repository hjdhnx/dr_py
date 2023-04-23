#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : storage.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/9/6

from base.database import db
from functools import lru_cache

class Storage(db.Model):
    __tablename__ = 'storage'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    key = db.Column(db.String(20), unique=True)
    value = db.Column(db.UnicodeText())
    # value = db.Column(db.Text())

    def __repr__(self):
        return "<Storage(key='%s', value='%s')>" % (
            self.key, self.value)

    @classmethod
    def setItem(self, key, value=None):
        res = db.session.query(self).filter(self.key == key).first()
        if res:
            res.value = value
            db.session.add(res)
        else:
            res = Storage(key=key, value=value)
            db.session.add(res)
            db.session.flush()
        try:
            db.session.commit()
            self.clearCache()
            return res.id
        except Exception as e:
            print(f'发生了错误:{e}')
            return None

    @classmethod
    @lru_cache(maxsize=200)
    def getItem(self, key, value=''):
        res = db.session.query(self).filter(self.key == key).first()
        if res:
            return res.value or value
        else:
            return value

    @classmethod
    @lru_cache(maxsize=200)
    def hasItem(self, key):
        exists = db.session.query(self).filter(self.key == key).scalar() is not None
        # res = db.session.query(self).filter(self.key == key).
        if exists:
            return True
        else:
            return False

    @classmethod
    def clearItem(self, key):
        self.clearCache()
        res = db.session.query(self).filter(self.key == key).first()
        if res:
            res.delete()
            ret = db.session.commit()
            self.clearCache()
            return ret
        else:
            return True

    @classmethod
    def clearCache(self):
        self.getItem.cache_clear()
        self.hasItem.cache_clear()