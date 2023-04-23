#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : flaskOcrDz.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2021/11/1
import json

from flask import Flask, jsonify, request,Response
import requests
import ddddocr
ocr = ddddocr.DdddOcr()

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # jsonify返回的中文正常显示

@app.route("/",methods=['GET'])
def index():
    return '欢迎使用简单验证码文字识别,海阔视界道长专用'

def hexStringTobytes(str):
    str = str.replace(" ", "")
    print(str)
    return bytes.fromhex(str)

def bytesToHexString(bs):
    return ''.join(['%02X ' % b for b in bs])

class LocalOcr:
    def __init__(self,file=None,url='http://127.0.0.1:10000'):
        self.file = file
        self.url = url
        self.yzm = self.yzm_ocr(0)

    def read(self):
        return self.yzm

    def yzm_ocr(self,count=0):
        try:
            r = requests.post(self.url, data=self.file,timeout=(0.5,2))
            yzm = r.text
            return yzm
        except:
            if count < 3:
                count += 1
                return self.yzm_ocr(count)
            else:
                return ""

def ocr2(hex):
    if type(hex) == list:
        hex = ''.join(hex)
    img_bytes = hexStringTobytes(hex)
    # print(img_bytes)
    # with open('1.png','wb+') as f:
    #     f.write(img_bytes)

    dm_url = 'http://dm.mudery.com:10000'
    im_ocr = LocalOcr(img_bytes, dm_url)
    yzm = im_ocr.read()
    ret = {'msg': 'ok','ret':yzm,'code':0,'detail':'验证码识别成功'}
    print(ret)
    return jsonify(ret)

def docr(hex):
    if type(hex) == list:
        hex = ''.join(hex)
    img_bytes = hexStringTobytes(hex)
    try:
        img_str = img_bytes.decode("latin1")
        if img_str.find('html') > -1:
            ret = {'msg': '拜托,我收到你传过来的数据是个网页而不是图片,麻烦解密后把图片的hex给我', 'ret': img_str[:500], 'code': -1, 'detail': '图片识别失败'}
            return jsonify(ret)
        else:
            res = ocr.classification(img_bytes)
            ret = {'msg': 'ok', 'ret': res, 'code': 0, 'detail': '图片识别成功'}
            # print(ret)
            return jsonify(ret)
    except Exception as e:
        # print(f'{e}')
        ret = {'msg': 'error', 'ret': f'{e}', 'code': -2, 'detail': '发生了意外的错误'}
        return ret

@app.route("/api/ocr",methods=['GET', 'POST'])
def ocr_fast():
    args = {}
    try:
        ctp = request.content_type
        if request.method == 'POST':
            if ctp.find('application/json') > -1:
                try:
                    args = request.json
                except Exception as e:
                    # args = request.get_data(as_text=True)
                    args = {}
            else:
                args = request.form
        elif request.method == 'GET':
            args = request.args
        if not args.get('hex'):
            return '缺少必传参数:hex!'
    except Exception as e:
        return jsonify({'msg':'非法调用','code':'-1'})
    # print(args.get('hex'))
    # return ocr2(args.get('hex'))
    return docr(args.get('hex'))

@app.route("/api/hex2img",methods=['GET'])
def ocr_hex2img():
    try:
        args = request.args
        if not args.get('hex'):
            return '缺少必传参数:hex!'
    except Exception as e:
        return jsonify({'msg':'非法调用','code':'-1'})
    # print(args.get('hex'))
    # return ocr2(args.get('hex'))
    hex = args.get('hex')
    if type(hex) == list:
        hex = ''.join(hex)
    img_bytes = hexStringTobytes(hex)
    resp = Response(img_bytes, mimetype='image/jpeg')
    return resp

@app.route("/api/ocr_img",methods=['POST'])
def ocr_img_fast():
    # print(request.values)
    # print(request.files)
    # print(request.data)
    try:
        img_bytes = request.data
        ret = ocr.classification(img_bytes)
        return ret
        # return jsonify({'ret':ret,'code':0,'msg':'识别完毕'})
    except Exception as e:
        return ''
        # return jsonify({'msg':'请求出错','code':-1,'detail':f'{e}'})

def test():
    pic = 'yzm1.png'
    # pic = '2.png'
    with open(pic, 'rb') as f:
        img_bytes = f.read()
    res = ocr.classification(img_bytes)
    print(res)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9000)
    # test()