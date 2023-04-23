#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : chatgpt调用.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2023/2/7
import json
import time

# 文档地址: https://platform.openai.com/docs/api-reference/completions/create

import requests

API_KEY = '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'
AUTH = f'Bearer {API_KEY}'

def ask_chatpgt(word):
    """
    问chatgpt得到答案
    """
    headers = {
        'Content-Type':'application/json',
        'Authorization':AUTH,
    }
    # print(headers)
    pdata = {
        "model": "text-davinci-003",
        "prompt": word,
        "temperature": 0.9,
        "max_tokens": 1000,
        "top_p": 1,
        "frequency_penalty": 0.0,
        "presence_penalty": 0.6,
        "stop": [" AI:"]
    }
    # print(pdata)
    t1 = time.time()
    ret = ''
    try:
        r = requests.post('https://api.openai.com/v1/completions',data=json.dumps(pdata),headers=headers)
        ret = r.json()
        answer = ret['choices'][0]['text']
    except Exception as e:
        answer = f'发生了错误:{e} {ret}'
    # print(ret)
    # print(answer)
    t2 = time.time()
    sec = round((t2 - t1)*1000,2)
    print(f'共计耗时:{sec}毫秒,{answer}')
    return [answer,sec]

if __name__ == '__main__':
    print(ask_chatpgt('1+1等于几'))
    # https://chat.openai.com/auth/login
    # http://fastapi.frp.mudery.com/other_request/chatgpt
    # http://spider.scwinbao.com:8274/other_request/chatgpt
    # print(ask_chatpgt('假如我处于一个荒岛，现在我来扮演玩家，你来扮演电脑，你给我选项，我们玩一个荒岛求生的游戏'))
    # print(ask_chatpgt('以 背影为题，写一篇400字的作文'))