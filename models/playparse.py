#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : playparse.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/9/6

from base.database import db

class PlayParse(db.Model):
    __tablename__ = 'play_parse'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    play_url = db.Column(db.String(255))
    real_url = db.Column(db.String(255))

    def __repr__(self):
        return "<PlayParse(play_url='%s', real_url='%s')>" % (
            self.play_url, self.real_url)