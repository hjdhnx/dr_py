import re, os, stat, gzip, time, hmac, queue, base64, random, hashlib, hashlib, itertools, datetime, calendar, \
    threading, tkinter, socket, struct
import execjs  # JS模块，需要安装pyexecjs
import requests  # 网页请求模块，需要安装requests
import pymysql  # Mysql模块，需要安装PyMysql
from urllib import parse
from tkinter import messagebox
from pypinyin import Style, pinyin  # 需要安装拼音库 pypinyin
from requests.packages.urllib3.exceptions import InsecureRequestWarning

文件打开方式_只读 = 'r'
文件打开方式_二进制_只读 = 'rb'
文件打开方式_读写 = 'r+'
文件打开方式_二进制_读写 = 'rb+'
文件打开方式_覆盖写入 = 'w'  # 文件不存在会创建新文件
文件打开方式_二进制_覆盖写入 = 'wb'  # 文件不存在会创建新文件
文件打开方式_覆盖读写 = 'w+'  # 文件不存在会创建新文件
文件打开方式_二进制_覆盖读写 = 'wb+'  # 文件不存在会创建新文件
文件打开方式_追加写入 = 'a'  # 文件不存在会创建新文件
文件打开方式_二进制_追加写入 = 'ab'  # 文件不存在会创建新文件
文件打开方式_追加读写 = 'a+'  # 文件不存在会创建新文件
文件打开方式_二进制_追加读写 = 'ab+'  # 文件不存在会创建新文件

time_时间格式_取简化星期名称 = '%a'  # 本地(local) 简化星期名称
time_时间格式_取完整星期名称 = '%A'  # 本地完整星期名称
time_时间格式_取简化月份名称 = '%b'  # 本地简化月份名称
time_时间格式_取整月份名称 = '%B'  # 本地完整月份名称
time_时间格式_取日期和时间 = '%c'  # 本地相应的日期和时间表示
time_时间格式_取日 = '%d'  # 一个月中的第几天（01-31）
time_时间格式_取时24 = '%H'  # 一天中的第几个小时（24小时制00-23）
time_时间格式_取时12 = '%I'  # 第几个小时（12小时制01-12）
time_时间格式_取一年中的第几天 = '%j'  # 一年中的第几天（001-366）
time_时间格式_取月份 = '%m'  # 月份（01-12）
time_时间格式_取分钟 = '%M'  # 分钟数（00-59）
time_时间格式_取am或pm相应符 = '%p'  # 本地am或pm的相应符
time_时间格式_取秒 = '%S'  # 秒（01-60）
time_时间格式_取年中第几星期U = '%U'  # 一年中的星期数。（00-53 星期天是一个星期的开始）第一个星期天之前的所有天数都放在第0周
time_时间格式_取星期几 = '%w'  # 一个星期中的第几天（0-6 0是星期天）
time_时间格式_取年中第几星期W = '%W'  # 和%U基本相同，不同的是%W以星期一为一个星期的开始
time_时间格式_取日月年 = '%x'  # 本地相应日期
time_时间格式_取时分秒 = '%X'  # 本地相应时间
time_时间格式_取年份 = '%y'  # 去掉世纪的年份（00-99）
time_时间格式_取完整年份 = '%Y'  # 完整的年份
time_时间格式_取时区 = '%z'  # 时区的名字

讯代理_代理地址 = 'forward.xdaili.cn:80'
电脑UA = [
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv,2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv,2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4094.1 Safari/537.36",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)"
]
手机UA = [
    "Mozilla/5.0 (iPhone 84; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.8.0 Mobile/14G60 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 7.0; STF-AL10 Build/HUAWEISTF-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 V1_AND_SQ_7.2.0_730_YYB_D QQ/7.2.0.3270 NetType/4G WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.18 NetType/WIFI Language/en",
    "Mozilla/5.0 (Linux; Android 5.1.1; vivo Xplay5A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.0.10 (Baidu; P1 5.1.1)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; STF-AL00 Build/HUAWEISTF-AL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; LEX626 Build/HEXCNFN5902606111S) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/7.4 baiduboxapp/8.3.1 (Baidu; P1 6.0)",
    "Mozilla/5.0 (iPhone 92; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.7.2 Mobile/14F89 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; ZUK Z2121 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.8.952 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A372 MicroMessenger/6.5.17 NetType/WIFI Language/zh_HK",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; SM-C7000 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.2.948 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92 MicroMessenger/6.5.16 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; MI 4S Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.1.3",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; SM-G9550 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.0.953 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1; m3 note Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.0.10 (Baidu; P1 5.1)",
    "Mozilla/5.0 (iPhone 92; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 MQQBrowser/7.7.2 Mobile/15A372 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 6.0; MX6 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_0_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13A405 MicroMessenger/6.5.15 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.1.1; OPPO R11 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; PRA-AL00 Build/HONORPRA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.0.953 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; FRD-AL00 Build/HUAWEIFRD-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 V1_AND_SQ_7.1.0_0_TIM_D TIM2.0/1.2.0.1692 QQ/6.5.5  NetType/2G WebP/0.3.0 Pixel/1080 IMEI/869953022249635",
    "Mozilla/5.0 (Linux; Android 5.1; OPPO R9tm Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.0.10 (Baidu; P1 5.1)",
    "Mozilla/5.0 (Linux; Android 7.0; VTR-AL00 Build/HUAWEIVTR-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 wxwork/2.1.3 MicroMessenger/6.3.22",
    "Mozilla/5.0 (Linux; Android 7.0; Infinix X572 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 lite baiduboxapp/2.3.2 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; Android 6.0.1; SM-A7100 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/7.4 baiduboxapp/8.1 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (iPhone 91; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.8.0 Mobile/14C92 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 5.1.1; vivo X7 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 wxwork/2.1.3 MicroMessenger/6.3.22",
    "Mozilla/5.0 (Linux; Android 5.1; m3 note Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 wxwork/2.1.3 MicroMessenger/6.3.22",
    "Mozilla/5.0 (Linux; Android 6.0; MX6 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 wxwork/2.1.3 MicroMessenger/6.3.22",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 wxwork/2.1.5 MicroMessenger/6.3.22",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; MX5 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.8 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; C106 Build/ZAXCNFN5902606201S) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.0.953 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; KIW-TL00H Build/HONORKIW-TL00H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.0.953 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.0.10 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; Android 7.0; EVA-AL00 Build/HUAWEIEVA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_1 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A402 MicroMessenger/6.5.16 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; SM-G9500 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.0.953 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; NX531J Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/6.8 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_1 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A402 wxwork/2.1.5 MicroMessenger/6.3.22",
    "Mozilla/5.0 (Linux; U; Android 7.1.2; zh-cn; MI 5X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.2",
    "Mozilla/5.0 (iPhone 6; CPU iPhone OS 9_3_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/6.0 MQQBrowser/6.6.1 Mobile/13E238 Safari/8536.25",
    "Mozilla/5.0 (Linux; Android 7.1.1; OPPO R11 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.1; vivo X6D Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 MicroMessenger/6.5.16 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; EVA-DL00 Build/HUAWEIEVA-DL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.0.2; vivo X6A Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.0.10 (Baidu; P1 5.0.2)",
    "Mozilla/5.0 (Linux; Android 5.1.1; MX4 Pro Build/LMY48W; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.0.10 (Baidu; P1 5.1.1)",
    "Mozilla/5.0 (Linux; Android 4.4.4; HM NOTE 1LTE Build/KTU84P; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 V1_AND_SQ_6.6.9_482_YYB_D QQ/6.6.9.3060 NetType/WIFI WebP/0.3.0 Pixel/720",
    "Mozilla/5.0 (Linux; Android 7.0; MIX Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 V1_AND_SQ_7.2.0_730_YYB_D QQ/7.2.0.3270 NetType/WIFI WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; Android 5.1; OPPO R9m Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 V1_AND_SQ_7.2.0_730_YYB_D QQ/7.2.0.3270 NetType/4G WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; Android 7.1.1; NX563J Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 V1_AND_SQ_7.2.0_730_YYB_D QQ/7.2.0.3270 NetType/4G WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; Android 7.0; EVA-AL10 Build/HUAWEIEVA-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.1; vivo X6Plus D Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 V1_AND_SQ_7.2.0_730_YYB_D QQ/7.2.0.3270 NetType/4G WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; Android 6.0; ALE-TL00 Build/HuaweiALE-TL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; ZUK Z2121 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 V1_AND_SQ_7.2.0_730_YYB_D QQ/7.2.0.3270 NetType/4G WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; PLK-AL10 Build/HONORPLK-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.0.953 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; WAS-AL00 Build/HUAWEIWAS-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone 6p; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.8.0 Mobile/14G60 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 7.0; DUK-AL20 Build/HUAWEIDUK-AL20; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.0.10 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; SM-G9550 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.8 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; Redmi Note 4X Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 rabbit/1.0 baiduboxapp/7.1 (Baidu; P1 6.0)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Mobile/14E277 MicroMessenger/6.5.16 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; EVA-DL00 Build/HUAWEIEVA-DL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.0.953 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.17 NetType/WIFI Language/en",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A372 MicroMessenger/6.5.15 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_2_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13D15 search%2F1.0 baiduboxapp/0_0.1.1.7_enohpi_8022_2421/1.2.9_1C2%257enohPi/1099a/088D84D1E9A6AEE91798B97AAA03690B96CFCB638FGIMSINMHB/1",
    "Mozilla/5.0 (Linux; Android 5.1.1; OPPO R7sPlus Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.0.10 (Baidu; P1 5.1.1)",
    "Mozilla/5.0 (iPhone 6sp; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 MQQBrowser/7.8.0 Mobile/15A372 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (iPhone 6p; CPU iPhone OS 8_1_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 MQQBrowser/7.8.0 Mobile/12B436 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 6.0.1; OPPO A57 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 V1_AND_SQ_7.2.0_730_YYB_D QQ/7.2.0.3270 NetType/WIFI WebP/0.3.0 Pixel/720",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; KIW-CL00 Build/HONORKIW-CL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; MI 4LTE Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 V1_AND_SQ_7.1.5_708_YYB_D QQ/7.1.5.3215 NetType/4G WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; Android 4.4.2; Coolpad 8675 Build/KOT49H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.3.18.800 NetType/cmnet Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0.1; vivo X9i Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; VIE-AL10 Build/HUAWEIVIE-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.0.953 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; Redmi Note 4 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; Redmi 3 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.1.3",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; Redmi Note 4 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.0.953 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; SM-G9550 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.2 baiduboxapp/9.2.0.10 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; Android 6.0.1; Redmi Note 3 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile Safari/537.36 Maxthon/3047",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; Redmi 4 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.3",
    "Mozilla/5.0 (Linux; Android 6.0.1; MI 5s Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 V1_AND_SQ_7.2.0_730_YYB_D QQ/7.2.0.3270 NetType/WIFI WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; Android 7.0; HUAWEI CAZ-AL10 Build/HUAWEICAZ-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 V1_AND_SQ_7.1.0_692_YYB_D QQ/7.1.0.3175 NetType/WIFI WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; Android 5.1; OPPO A37m Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.0.10 (Baidu; P1 5.1)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A372 MicroMessenger/6.5.17 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.7 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; M5 Note Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/7.4 baiduboxapp/8.1 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (Linux; Android 7.1.1; ONEPLUS A3000 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 8.0; G8342 Build/47.1.A.2.324; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.14.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A372 MicroMessenger/6.5.17 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; EVA-TL00 Build/HUAWEIEVA-TL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.16 NetType/4G Language/zh_TW",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.5.16 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; EVA-TL00 Build/HUAWEIEVA-TL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0.1; SM-C5000 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OD105 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.0.953 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Mobile/14D27 MicroMessenger/6.5.15 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone 6s; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 MQQBrowser/7.8.0 Mobile/13F69 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-CN; N5209 Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.0.953 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; FRD-AL00 Build/HUAWEIFRD-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0.1; vivo X9Plus Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 MicroMessenger/6.5.16 NetType/3G Language/zh_CN",
    "Mozilla/5.0 (iPhone 6s; CPU iPhone OS 10_1_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/6.0 MQQBrowser/6.9 Mobile/14B100 Safari/8536.25 MttCustomUA/2",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.1.3",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; PRO 6 Plus Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.0.953 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone 92; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 MQQBrowser/7.2.1 Mobile/15A372 Safari/8536.25 MttCustomUA/2 QBWebViewType/1",
    "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; HUAWEI MT7-CL00 Build/HuaweiMT7-CL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.3 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone 92; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 MQQBrowser/7.8.0 Mobile/15A372 Safari/8536.25 MttCustomUA/2 QBWebViewType/1",
    "Mozilla/5.0 (Linux; Android 7.0; PRA-AL00X Build/HONORPRA-AL00X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/7.4 baiduboxapp/8.3.1 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; Android 7.0; MI 5 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.1.1; M631 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.0.10 (Baidu; P1 5.1.1)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; PRA-AL00X Build/HONORPRA-AL00X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.0.953 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; HTC A9w Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OPPO R11 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.0.953 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Mobile/14D27 MicroMessenger/6.5.17 NetType/3G Language/en",
    "Mozilla/5.0 (Linux; Android 5.1.1; Redmi Note 3 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 4.2.2; Lenovo A708t Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/7.4 baiduboxapp/8.2.5 (Baidu; P1 4.2.2)",
    "Mozilla/5.0 (Linux; Android 7.0; PRA-AL00X Build/HONORPRA-AL00X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0.1; SM-C5000 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A372 MicroMessenger/6.5.15 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; MI 4LTE Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.2",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; ZUK Z2121 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.2.948 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.1.1; vivo X9i Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; MHA-AL00 Build/HUAWEIMHA-AL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.8 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.1.1; vivo X7 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.4.1000 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A372 MicroMessenger/6.5.16 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A372 wxwork/2.1.5 MicroMessenger/6.3.22",
    "Mozilla/5.0 (Linux; Android 4.4.4; SM-N935F Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Safari/537.36 baidubrowser/7.13.13.0 (Baidu; P1 4.4.4)",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; HUAWEI VNS-TL00 Build/HUAWEIVNS-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.2.5.884 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; vivo Y67A Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/7.4 baiduboxapp/8.5 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; Redmi 3 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.0.953 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MI 5s Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.0.953 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; SM-G9300 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.0.10 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; WAS-AL00 Build/HUAWEIWAS-AL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.8 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1; OPPO A59s Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.0.10 (Baidu; P1 5.1)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; WAS-TL10 Build/HUAWEIWAS-TL10) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.8 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; ZUK Z2151 Build/MXB48T) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.6.951 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; MI 4LTE Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.0.953 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; H60-L01 Build/HDH60-L01) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.2 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; NEM-AL10 Build/HONORNEM-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; EVA-AL10 Build/HUAWEIEVA-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.0.953 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.1.1; vivo X9i Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.1.1; OPPO R11 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.0.10 (Baidu; P1 7.1.1)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92 MicroMessenger/6.5.10 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.13.1080 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; Redmi Note 4X Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.8 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; EVA-TL00 Build/HUAWEIEVA-TL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.0.10 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; PLK-TL01H Build/HONORPLK-TL01H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.0.953 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; HUAWEI CAZ-AL10 Build/HUAWEICAZ-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.4.950 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; Redmi Note 3 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043507 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; HUAWEI VNS-DL00 Build/HUAWEIVNS-DL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.8 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; ONEPLUS A3010 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.0.953 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; FRD-AL10 Build/HUAWEIFRD-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.0.10 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; Android 5.1; OPPO R9m Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.0.10 (Baidu; P1 5.1)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.17 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0.1; Redmi Note 3 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043507 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0.1; OPPO R9st Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.1 baiduboxapp/9.1.5.10 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (Linux; Android 5.1.1; Redmi Note 3 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.15 NetType/4G Language/en",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 search%2F1.0 baiduboxapp/0_0.0.2.7_enohpi_8022_2421/3.3.01_2C2%258enohPi/1099a/E45349801E2DA062C66A2B67D1063CCA3F80520CDORHQTBKLEQ/1",
    "Mozilla/5.0 (Linux; Android 6.0.1; 1605-A01 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.1 baidubrowser/7.15.15.0 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (Linux; Android 7.0; MHA-AL00 Build/HUAWEIMHA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone 5SGLOBAL; CPU iPhone OS 9_0_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 MQQBrowser/7.2 Mobile/13A404 Safari/8536.25 MttCustomUA/2 QBWebViewType/1",
    "Mozilla/5.0 (Linux; Android 6.0.1; Redmi Note 3 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.0.10 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (Linux; Android 6.0.1; SM-C9000 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.1 baidubrowser/7.15.15.0 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (Linux; Android 6.0.1; MI 5s Plus Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.1.1; OPPO R7sm Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.0.10 (Baidu; P1 5.1.1)",
    "Mozilla/5.0 (iPhone 6s; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 MQQBrowser/7.7.2 Mobile/15A372 Safari/8536.25 MttCustomUA/2 QBWebViewType/1",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; MIX Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.2",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.16 NetType/2G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; EVA-AL10 Build/HUAWEIEVA-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.0.953 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; vivo Y66L Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.7 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; Redmi Note 4X Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.1.3",
    "Mozilla/5.0 (Linux; Android 6.0; Letv X500 Build/DBXCNOP5902605181S; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.1 baidubrowser/7.15.15.0 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; vivo Y67 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.2 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; Redmi Note 3 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.8 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; Lenovo K32c36 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.8 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; EVA-AL00 Build/HUAWEIEVA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.0.953 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-hk; SM-C7000 Build/MMB29M) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/1.0.0.100 U3/0.8.0 Mobile Safari/534.30 AliApp(TB/6.2.0) WindVane/8.0.0 1080X1920 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; Android 6.0.1; OPPO R9s Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.0.10 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (iPhone 6; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.7.2 Mobile/14F89 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_2_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13D15 MicroMessenger/6.5.16 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; FRD-AL10 Build/HUAWEIFRD-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043507 Safari/537.36 MicroMessenger/6.5.10.1060 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92 MicroMessenger/6.5.16 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92 MicroMessenger/6.5.16 NetType/4G Language/zh_HK",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OPPO R11 Pluskt Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.8.952 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; MIX Build/MXB48T) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.8 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.0.2; vivo X6A Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.2 baiduboxapp/9.2.0.10 (Baidu; P1 5.0.2)",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; SM-G925P Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.1.949 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 rabbit%2F1.0 baiduboxapp/0_7.0.5.7_enohpi_6311_046/3.3.01_1C2%256enohPi/1099a/6A4B957D5B5BA4F869CF7610DFF0C1BD1DD4480AFFRLQMDDDIP/1",
    "Mozilla/5.0 (Linux; Android 6.0; MI 5 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.1; CUN-TL00 Build/HUAWEICUN-TL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; PRO 6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.8 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; PLK-AL10 Build/HONORPLK-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043507 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.16 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; KING 7S Build/PP6000_230I) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/6.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; MI 5 Build/MXB48T) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.17 Mobile Safari/537.36 AliApp(TB/6.11.2) WindVane/8.0.0 1080X1920 GCanvas/1.4.2.21",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 rabbit%2F1.0 baiduboxapp/0_0.0.8.6_enohpi_4331_057/3.3.01_1C2%258enohPi/1099a/4CA0E6CD6CBF0560D540380FF2290A37ED902FFACORCNFARAST/1",
    "Mozilla/5.0 (Linux; U; Android 5.0.2; zh-CN; PLK-AL10 Build/HONORPLK-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.8.952 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; SM-G9300 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.2 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone 5; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.7.2 Mobile/14G60 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; MI NOTE LTE Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.0.3",
    "Mozilla/5.0 (Linux; Android 5.1.1; vivo Y51A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.0.10 (Baidu; P1 5.1.1)",
    "Mozilla/5.0 (Linux; Android 6.0; 1503-A01 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.2 baiduboxapp/9.2.0.10 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MHA-TL00 Build/HUAWEIMHA-TL00) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.1.5.871 U3/0.8.0 Mobile Safari/534.30",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.8.952 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; NX549J Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.8.952 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; m3 note Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.8.952 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; EDI-AL10 Build/HUAWEIEDISON-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.2 baiduboxapp/9.2.0.10 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; HUAWEI CAZ-AL10 Build/HUAWEICAZ-AL10) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.8 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone 6p; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 MQQBrowser/7.7.2 Mobile/13G36 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Windows NT 6.1; Android) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.9.2.1000",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; MI 6 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.1",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.8 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; HUAWEI CAZ-TL10 Build/HUAWEICAZ-TL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/7.4 baiduboxapp/8.3.1 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; DUK-AL20 Build/HUAWEIDUK-AL20) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.8 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.4.1 Mobile/14E277 Safari/8536.25 MttCustomUA/2 QBWebViewType/1",
    "Mozilla/5.0 (iPad; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.4.1 Mobile/14F89 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (iPad; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.4.1 Mobile/14F89 Safari/8536.25",
    "Mozilla/5.0 (iPad; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.4.1 Mobile/14F89 Safari/8536.25 MttCustomUA/2 QBWebViewType/1",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; MI NOTE LTE Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.1",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; lephone W7 Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.8 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; Le X620 Build/HEXCNFN5601405171S; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.2 baiduboxapp/9.2.0.10 (Baidu; P1 6.0)",
    "Mozilla/5.0 (iPhone 5SGLOBAL; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.7.2 Mobile/14G60 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (iPad; CPU iPhone OS 10_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.4.1 Mobile/14B72 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 7.1.1; OPPO R11t Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPad; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.4.1 Mobile/14C92 Safari/8536.25 MttCustomUA/2 QBWebViewType/1",
    "Mozilla/5.0 (iPad; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 MQQBrowser/7.4.1 Mobile/13F69 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 search%2F1.0 baiduboxapp/0_0.0.2.7_enohpi_8022_2421/2.3.01_2C2%258enohPi/1099a/E45349801E2DA062C66A2B67D1063CCA3F80520CDORHQTBKLEQ/1",
    "Mozilla/5.0 (Linux; Android 6.0.1; OPPO R9s Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043507 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.1.1; vivo X7 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.0.10 (Baidu; P1 5.1.1)",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; MI 4LTE Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.1.3",
    "Mozilla/5.0 (iPhone 91; CPU iPhone OS 10_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.2.1 Mobile/14A346 Safari/8536.25 MttCustomUA/2 QBWebViewType/1",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; MI 5 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.1",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; A311 Build/MOB30D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/42.0.2311.153 Mobile Safari/537.36 XiaoMi/MiuiBrowser/2.1.1",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; HM NOTE 1LTE Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.1",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; HM NOTE 1LTE Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/42.0.2311.153 Mobile Safari/537.36 XiaoMi/MiuiBrowser/2.1.1",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; PE-CL00 Build/HuaweiPE-CL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/6.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; MI 5s Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.2",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; HUAWEI MLA-AL10 Build/HUAWEIMLA-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.8.952 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Mobile/14E304 MicroMessenger/6.5.15 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; HUAWEI TAG-TL00 Build/HUAWEITAG-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.8.952 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; MHA-AL00 Build/HUAWEIMHA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043507 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13E238 MicroMessenger/6.5.15 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; 1505-A01 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043507 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12F70 MicroMessenger/6.5.5 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.1; CUN-TL00 Build/HUAWEICUN-TL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone 6sp; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.7.2 Mobile/14F89 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 6.0.1; SM-C5000 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043507 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.1.2; zh-CN; MI 5C Build/N2G47J) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.8.952 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1; HUAWEI TIT-TL00 Build/HUAWEITIT-TL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.2 baiduboxapp/9.2.0.10 (Baidu; P1 5.1)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36 MicroMessenger/6.5.16 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.0.2; HTC_E9x Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/3G Language/zh_CN",
    "Mozilla/5.0 (iPhone 92; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.4.1 Mobile/14G60 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.16 NetType/4G Language/en",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; HUAWEI NXT-TL00 Build/HUAWEINXT-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.4.950 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_0_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13A452 MicroMessenger/6.5.15 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0.1; Mi Note 2 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043507 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; EVA-AL00 Build/HUAWEIEVA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043507 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0.1; MI 5s Plus Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.1; OPPO R9tm Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043507 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; SM-G9200 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.0.907 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; SM-A7108 Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/6.3 rabbit/1.0 baiduboxapp/7.2 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (Linux; Android 6.0; PRO 6 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; KNT-AL10 Build/HUAWEIKNT-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; EVA-DL00 Build/HUAWEIEVA-DL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; FRD-AL10 Build/HUAWEIFRD-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.1 baidubrowser/7.15.15.0 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; vivo X7 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.8.952 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1; HUAWEI TIT-AL00 Build/HUAWEITIT-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.2 baiduboxapp/9.2.0.10 (Baidu; P1 5.1)",
    "Mozilla/5.0 (Linux; Android 6.0.1; SM-C5000 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043507 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_2_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13D15 MicroMessenger/6.5.16 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; MI 4LTE Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.1.949 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; G8232 Build/41.2.A.7.53) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.4.950 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; Redmi Pro Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.7.7",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; EVA-AL00 Build/HUAWEIEVA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.8.952 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; EDI-AL10 Build/HUAWEIEDISON-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.1 baiduboxapp/9.1.5.10 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; Android 7.0; MHA-AL00 Build/HUAWEIMHA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043507 Safari/537.36 MicroMessenger/6.5.3.980 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; MI 5s Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.1",
    "Mozilla/5.0 (Linux; Android 6.0; Le X620 Build/HEXCNFN5902606111S; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043507 Safari/537.36 V1_AND_SQ_7.1.8_718_YYB_D QQ/7.1.8.3240 NetType/WIFI WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; Android 5.0.2; vivo Y51A Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.1 baiduboxapp/9.1.5.10 (Baidu; P1 5.0.2)",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; 1505-A01 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.2.948 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; EVA-AL10 Build/HUAWEIEVA-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.8.952 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone 92; CPU iPhone OS 10_1_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.7.2 Mobile/14B100 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; Redmi Pro Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.1.3",
    "Mozilla/5.0 (Linux; Android 5.1.1; vivo X7 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043507 Safari/537.36 MicroMessenger/6.5.4.1000 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.13 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; vivo Y67 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OPPO R11 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.8.952 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; STF-AL00 Build/HUAWEISTF-AL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.8 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1.1; vivo X6SPlus A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 5.1.1)",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; KIW-CL00 Build/HONORKIW-CL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.8 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 baiduboxapp/0_11.0.1.8_enohpi_4331_057/3.3.01_1C2%259enohPi/1099a/1FC7DAA4975A1AC9FBCC5B172A4AE8FCEC3D8D836FCIMFHREQI/1",
    "Mozilla/5.0 (Linux; Android 5.1; MX5 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043507 Safari/537.36 V1_AND_SQ_7.1.8_718_YYB_D QQ/7.1.8.3240 NetType/WIFI WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; Redmi Note 3 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.1.3",
    "Mozilla/5.0 (Linux; Android 5.0.2; Redmi Note 3 Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043507 Safari/537.36 V1_AND_SQ_7.1.8_718_YYB_D QQ/7.1.8.3240 NetType/WIFI WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 baiduboxapp/0_01.0.4.8_enohpi_8022_2421/3.3.01_2C2%259enohPi/1099a/7512D55B6AA7C2A4D7ACF770BDFA942E203403DA5FRLASRAEMH/1",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; OPPO A57 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.8 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; MI 5 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 Maxthon/3048",
    "Mozilla/5.0 (Linux; Android 7.1.1; ONEPLUS A3000 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043507 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone 6s; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 MQQBrowser/7.7.2 Mobile/13G36 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; MI NOTE LTE Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.8.952 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; JD-PLUS Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.1.949 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; NEM-AL10 Build/HONORNEM-AL10) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.6 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043507 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.1; m1 note Build/LMY47D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.2 baiduboxapp/9.2.0.10 (Baidu; P1 5.1)",
    "Mozilla/5.0 (Linux; Android 6.0.1; OPPO R9s Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.2 baiduboxapp/9.2.0.10 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; Redmi 4X Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.8.952 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-CN; Coolpad 8675-FHD Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.8.952 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-TW; MI 5s Build/MXB48T) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.5.1005 U3/0.8.0 Mobile Safari/534.30",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; MI 5s Plus Build/MXB48T) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.8 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_2_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13D15 MicroMessenger/6.5.15 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0.1; ATH-AL00 Build/HONORATH-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043507 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; 1503-M02 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.7.1041 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; HUAWEI MLA-AL10 Build/HUAWEIMLA-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043507 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Mobile/14D27 MicroMessenger/6.5.15 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 4.3; SM-G7108V Build/JLS36C; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 4.3)",
    "Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043507 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0.1; X900+ Build/CEXCNFN5902605111S; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.2 baiduboxapp/9.2.0.10 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12H143 MicroMessenger/6.5.8 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone 91; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.7.2 Mobile/14D27 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (iPhone 6s; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.4.1 Mobile/14G60 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043507 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.8.952 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; HUAWEI GRA-UL00 Build/HUAWEIGRA-UL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.1 baiduboxapp/9.1.0.12 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; MI 4LTE Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.8.952 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 4.4.2; HUAWEI MT2-L01 Build/HuaweiMT2-L01; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.4.1000 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone 6; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.7.2 Mobile/14D27 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 6.0.1; MI 5s Plus Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043507 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12F70 MicroMessenger/6.5.15 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; SM-G9200 Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.6 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 MicroMessenger/6.5.13 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; EVA-TL00 Build/HUAWEIEVA-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.8.952 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12A365 MicroMessenger/6.5.14 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.1.1; OPPO R11 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.2 baiduboxapp/9.2.0.10 (Baidu; P1 7.1.1)",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; Redmi Note 4 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.8.952 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 MicroMessenger/6.5.13 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; Letv X500 Build/DBXCNOP5902605181S; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; Redmi Note 4X Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.8 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone 91; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.7.2 Mobile/14F89 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; Redmi 3 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.8 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; MI 6 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.0",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; FRD-AL10 Build/HUAWEIFRD-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.8.952 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; M836 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.1 baiduboxapp/9.1.5.10 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (Linux; Android 6.0; Le X620 Build/HEXCNFN5900001151E) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/7.4 baiduboxapp/8.5 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; vivo X6D Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.4.950 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android; unknown; zh-CN) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.8.822 U3/0.8.0 Mobile Safari/534.30",
    "Mozilla/5.0 (Linux; Android 7.0; DUK-AL20 Build/HUAWEIDUK-AL20; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.2 baiduboxapp/9.2.0.10 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; Android 5.1.1; vivo X7 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone 6sp; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 MQQBrowser/7.7.2 Mobile/13F69 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 6.0.1; MI 5s Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; Mi-4c Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12F70 baiduboxapp/0_31.1.3.8_enohpi_8022_2421/3.8_1C2%257enohPi/1099a/A54801DC5E0712EDEF5E6D7D64624EE0C94C217FCOCTFGGAGPK/1",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; OPPO R9s Plus Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.1.939 UCBS/2.10.1.10 Mobile Safari/537.36 AliApp(TB/6.10.10) WindVane/8.0.0 1080X1920 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; PRA-AL00X Build/HONORPRA-AL00X) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.8 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; 1605-A01 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.8.952 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.0.3",
    "Mozilla/5.0 (Linux; Android 5.0.2; F103 Build/LRX21M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 5.0.2)",
    "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; H60-L02 Build/HDH60-L02) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.8 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; TA-1000 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043507 Safari/537.36 MicroMessenger/6.5.7.1041 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 rabbit%2F1.0 baiduboxapp/0_0.0.8.6_enohpi_8022_2421/3.3.01_2C2%259enohPi/1099a/468449D259991E6F99D3894A30C12B948E9EA6E2AFCTOGIIHJA/1",
    "Mozilla/5.0 (Linux; Android 7.0; EVA-AL00 Build/HUAWEIEVA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.2 baiduboxapp/9.2.0.10 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; vivo Y51A Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.8.952 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; PE-CL00 Build/HuaweiPE-CL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.2 baiduboxapp/9.2.0.10 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; Android 7.1.1; vivo X9s Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.2 baiduboxapp/9.2.0.10 (Baidu; P1 7.1.1)",
    "Mozilla/5.0 (Linux; Android 7.0; SM-G9350 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/56.0.2924.87 Mobile Safari/537.36 baiduboxapp/8.1 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; Android 7.1.1; vivo X9s L Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.2 baiduboxapp/9.2.0.10 (Baidu; P1 7.1.1)",
    "Mozilla/5.0 (Linux; Android 6.0; HUAWEI VNS-DL00 Build/HUAWEIVNS-DL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.15 NetType/3G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; FRD-AL10 Build/HUAWEIFRD-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.2 baiduboxapp/9.2.0.10 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; Android 7.1.1; vivo X9i Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043507 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; FRD-AL10 Build/HUAWEIFRD-AL10) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.8 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; M5 Note Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone 6s; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.7.2 Mobile/14F89 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 5.0.2; PLK-TL00 Build/HONORPLK-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/7.4 baiduboxapp/8.2.5 (Baidu; P1 5.0.2)",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; HUAWEI C199s Build/HuaweiC199s) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/6.5 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1; vivo X6Plus D Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.2 baiduboxapp/9.2.0.10 (Baidu; P1 5.1)",
    "Mozilla/5.0 (Linux; Android 7.0; FRD-AL10 Build/HUAWEIFRD-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_1_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Mobile/14B100 MicroMessenger/6.5.15 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0.1; KIW-UL00 Build/HONORKIW-UL00) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.0.0 MQQBrowser/6.6 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; Redmi 3X Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.1",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; R7Plusm Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.8.952 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone 92; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.2.1 Mobile/14G60 Safari/8536.25 MttCustomUA/2 QBWebViewType/1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13C75 MicroMessenger/6.5.15 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36 MicroMessenger/6.5.15 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; KNT-AL20 Build/HUAWEIKNT-AL20; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.2 baiduboxapp/9.2.0.10 (Baidu; P1 7.0)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_1_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12B436 baiduboxapp/0_0.1.1.7_enohpi_8022_2421/1.1.8_1C2%257enohPi/1099a/D389E26599B2D1BE2F75CA2D0220FEBD5DB46D543FRDELPHMEN/1",
    "Mozilla/5.0 (Linux; Android 7.0; VKY-AL00 Build/HUAWEIVKY-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.2 baiduboxapp/9.2.0.10 (Baidu; P1 7.0)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_1_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12B436 search%2F1.0 baiduboxapp/0_0.1.1.7_enohpi_8022_2421/1.1.8_1C2%257enohPi/1099a/D389E26599B2D1BE2F75CA2D0220FEBD5DB46D543FRDELPHMEN/1",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; Redmi Note 3 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.0.3",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A403 MicroMessenger/6.5.15 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.2 baiduboxapp/9.2.0.10 (Baidu; P1 7.1.1)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; EVA-AL10 Build/HUAWEIEVA-AL10) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.1 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; EVA-AL10 Build/HUAWEIEVA-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 V1_AND_SQ_6.6.9_482_YYB_D QQ/6.6.9.3060 NetType/WIFI WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; Android 7.0; EVA-AL10 Build/HUAWEIEVA-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; EVA-TL00 Build/HUAWEIEVA-TL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.2 baiduboxapp/9.2.0.10 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; Android 7.1.1; 1607-A01 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 V1_AND_SQ_7.1.5_708_YYB_D PA QQ/7.1.5.3215 NetType/4G WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; Android 6.0; PLK-TL01H Build/HONORPLK-TL01H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.4.1000 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; PLK-TL01H Build/HONORPLK-TL01H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 V1_AND_SQ_6.6.9_482_YYB_D QQ/6.6.9.3060 NetType/WIFI WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (iPhone 6sp; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.7.2 Mobile/14C92 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; MI 5s Plus Build/MXB48T) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.8.952 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; EVA-AL10 Build/HUAWEIEVA-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; vivo Xplay5A Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.8 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; VTR-AL00 Build/HUAWEIVTR-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.8.952 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; BLN-AL40 Build/HONORBLN-AL40) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.8.952 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; KNT-AL20 Build/HUAWEIKNT-AL20) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.8.952 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; M5 Note Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; STF-AL10 Build/HUAWEISTF-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.8.952 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; vivo Y55A Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.2 baiduboxapp/9.2.0.10 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; MI 5s Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.0",
    "Mozilla/5.0 (iPhone 6p; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.7.2 Mobile/14D27 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 6.0; vivo Y67 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.2 baiduboxapp/9.2.0.10 (Baidu; P1 6.0)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.5.15 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; VTR-AL00 Build/HUAWEIVTR-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 MicroMessenger/6.5.15 NetType/WIFI Language/zh_HK",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; HUAWEI GRA-TL00 Build/HUAWEIGRA-TL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.8 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; VKY-AL00 Build/HUAWEIVKY-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.8.952 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043507 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.15 NetType/4G Language/zh_TW",
    "Mozilla/5.0 (Linux; Android 5.1; m1 metal Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 baidubrowser/7.8.12.0 (Baidu; P1 5.1)",
    "Mozilla/5.0 (Linux; U; Android 5.0.2; zh-CN; Letv X501 Build/DBXCNOP5501304131S) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.800 U3/0.8.0 Mobile Safari/534.30",
    "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043507 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; PRA-TL10 Build/HONORPRA-TL10) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.8 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; MI 5 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 baidubrowser/7.14.14.0 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; EVA-AL00 Build/HUAWEIEVA-AL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.8 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; Mi Note 2 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.0",
    "Mozilla/5.0 (iPhone 91; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.7.2 Mobile/14C92 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 7.1.1; OD105 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.1.1; MI MAX 2 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043507 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; Mi-4c Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0.1; Mi Note 2 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043507 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0.1; MI 4C Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/7.4 baiduboxapp/8.3.1 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; EVA-DL00 Build/HUAWEIEVA-DL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.8 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; KIW-UL00 Build/HONORKIW-UL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/6.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; KIW-AL10 Build/HONORKIW-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone 91; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.7.2 Mobile/14G60 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; VKY-AL00 Build/HUAWEIVKY-AL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.8 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; SM919 Build/MXB48T) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.4.950 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1.1; KIW-UL00 Build/HONORKIW-UL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/7.1 rabbit/1.0 baiduboxapp/7.6.1 (Baidu; P1 5.1.1)",
    "Mozilla/5.0 (Linux; Android 7.0; BLN-AL20 Build/HONORBLN-AL20; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.2 baiduboxapp/9.2.0.10 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; Redmi Note 4 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.8 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MI MAX Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.6.951 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; Letv X500 Build/DAXCNCU5801810201S; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 4.4.2; CHM-UL00 Build/HonorCHM-UL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.3.23.840 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MHA-AL00 Build/HUAWEIMHA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.6.951 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; PLK-AL10 Build/HONORPLK-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; KNT-AL10 Build/HUAWEIKNT-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.6.951 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; LON-L29 Build/HUAWEILON-L29) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.7 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92 MicroMessenger/6.5.15 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13E233 MicroMessenger/6.5.15 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone 6sp; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.7.2 Mobile/14G60 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 5.1.1; vivo X7 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; HUAWEI MLA-AL10 Build/HUAWEIMLA-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 4.4.2; Che2-TL00 Build/HonorChe2-TL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.13.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; SM-G9280 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.2.942 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; EVA-TL00 Build/HUAWEIEVA-TL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; FRD-AL10 Build/HUAWEIFRD-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.10.1060 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12D508 MicroMessenger/6.5.7 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Mobile/14E277 MicroMessenger/6.5.15 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; OPPO R9m Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.8 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Mobile/14E304 MicroMessenger/6.5.15 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.1.1; vivo X9i Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.2 baiduboxapp/9.2.0.10 (Baidu; P1 7.1.1)",
    "Mozilla/5.0 (Linux; Android 5.1; m2 note Build/LMY47D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043313 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0.1; SM-C5000 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0.1; SM-C5000 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; HUAWEI NXT-CL00 Build/HUAWEINXT-CL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; Android 7.0; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043507 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone 6; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.7.2 Mobile/14G60 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 7.1.1; OPPO R11 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; CAM-AL00 Build/HONORCAM-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.2 baiduboxapp/9.2.0.10 (Baidu; P1 6.0)",
    "Mozilla/5.0 (iPhone 84; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.7.2 Mobile/14E304 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; NX549J Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.4 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MI MAX 2 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.6.951 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone 6; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.6.0 Mobile/14G60 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; MI MAX Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.8 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; Redmi Note 4 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.2 baiduboxapp/9.2.0.10 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; Android 5.1; vivo X6D Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.2 baiduboxapp/9.2.0.10 (Baidu; P1 5.1)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; MI 4S Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.1.3",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36 MicroMessenger/6.5.9 NetType/2G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; OPPO A59s Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.6.951 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; Le X620 Build/HEXCNFN5902606111S; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.1 baiduboxapp/9.1.0.12 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; vivo X6Plus D Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.6.951 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.1.2; zh-cn; MI 5X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.0",
    "Mozilla/5.0 (Linux; Android 7.0; SM-G9350 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 baidubrowser/7.14.14.0 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 7.1.2; zh-CN; MI 5X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.6.951 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OPPO R11 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.6.951 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; PRA-AL00X Build/HONORPRA-AL00X) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.6 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; Redmi Note 4X Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.6 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone 5SGLOBAL; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/6.0 MQQBrowser/6.9.1 Mobile/13G36 Safari/8536.25 MttCustomUA/2",
    "Mozilla/5.0 (Linux; Android 4.4.2; PE-TL00M Build/HuaweiPE-TL00M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.2 baiduboxapp/9.2.0.10 (Baidu; P1 4.4.2)",
    "Mozilla/5.0 (iPhone 6s; CPU iPhone OS 9_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 MQQBrowser/7.7.2 Mobile/13C75 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 7.0; EVA-AL10 Build/HUAWEIEVA-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.2 baiduboxapp/9.2.0.10 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; MI 6 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.8 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; 1505-A01 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.7 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone 6p; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.7.2 Mobile/14G60 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4X Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.5.14 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; HUAWEI MLA-AL10 Build/HUAWEIMLA-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.2 baiduboxapp/9.2.0.10 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; Android 6.0; MI 5 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0.1; vivo X9 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.15 NetType/WIFI Language/en",
    "Mozilla/5.0 (iPhone 6s; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.7.2 Mobile/14E304 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_2_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13D15 MicroMessenger/6.5.14 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MI 6 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.8.952 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1.1; A51 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.2 baiduboxapp/9.2.0.10 (Baidu; P1 5.1.1)",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; OPPO R9s Plus Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.8 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; HTC D10w Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.4.950 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.14 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; MI 5 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 Maxthon/3047",
    "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; VKY-AL00 Build/HUAWEIVKY-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.6.951 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.8 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; HUAWEI MT7-CL00 Build/HuaweiMT7-CL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13C75 MicroMessenger/6.5.15 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; DUK-AL20 Build/HUAWEIDUK-AL20) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.1 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; Redmi Note 4 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; VTR-AL00 Build/HUAWEIVTR-AL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.8 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; HUAWEI NXT-CL00 Build/HUAWEINXT-CL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.2 baiduboxapp/9.2.0.10 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; OPPO R9s Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.8 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.2 baiduboxapp/9.2.0.10 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; Android 6.0.1; ZTE A2018 Build/MXB48T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.0.0 MQQBrowser/6.6 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-TW; MI 5s Build/MXB48T) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.2.995 U3/0.8.0 Mobile Safari/534.30",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; ATH-CL00 Build/HONORATH-CL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/6.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; SM-A9000 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; FRD-AL00 Build/HUAWEIFRD-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.2.948 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 7.1.1)",
    "Mozilla/5.0 (Linux; Android 4.4.4; OPPO R7s Build/KTU84P; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.1; F100 Build/LMY47D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 5.1)",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; GN5003 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.6 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; vivo X9 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.1.939 UCBS/2.10.1.10 Mobile Safari/537.36 AliApp(TB/6.10.3) WindVane/8.0.0 1080X1920 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; BLN-AL10 Build/HONORBLN-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.2.948 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 2.3.3; en-us ; LS670 Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1/UCBrowser/8.6.1.262/145/355",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; vivo Y66 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.7 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone 6s; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.7.1 Mobile/14E304 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 6.0.1; vivo X9 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone 5SGSM; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.7.1 Mobile/14F89 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 7.0; TRT-AL00A Build/HUAWEITRT-AL00A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 baiduboxapp/8.6.5 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; Android 6.0.1; ZTE A2017 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (iPhone 6; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.7.1 Mobile/14F89 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; LEX720 Build/WAXCNFN5902304261S) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.7 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 4.4.2; HONOR H30-L01M Build/HonorH30-L01M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043313 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; Mi Note 2 Build/MXB48T) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.7.7",
    "Mozilla/5.0 (iPhone 5SGSM; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 MQQBrowser/7.3 Mobile/11D257 Safari/8536.25 MttCustomUA/2 QBWebViewType/1",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; ONEPLUS A3000 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.2.948 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; Le X620 Build/HEXCNFN5902606111S) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/7.4 baiduboxapp/8.4 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; vivo V3 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.7 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1.1; KIW-AL10 Build/HONORKIW-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.76 Mobile Safari/537.36 MQQBrowser/6.1",
    "Mozilla/5.0 (Linux; Android 5.0.2; vivo Y37 Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 5.0.2)",
    "Mozilla/5.0 (Linux; Android 4.4.2; PE-TL20 Build/HuaweiPE-TL20; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; DUK-AL20 Build/HUAWEIDUK-AL20) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.2.948 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A456 MicroMessenger/6.5.12 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; PLK-AL10 Build/HONORPLK-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043313 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.12 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.1; m1 metal Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043313 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone 6sp; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.7.1 Mobile/14F89 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; Redmi Note 4 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.0.3",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 MicroMessenger/6.5.12 NetType/2G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4X Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; Android 4.4.2; HONOR H30-L01 Build/HonorH30-L01; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; SCL-AL00 Build/HonorSCL-AL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.5 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; TRT-AL00A Build/HUAWEITRT-AL00A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043313 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0.1; SM-G9280 Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043313 Safari/537.36 MicroMessenger/6.3.16.49_r03ae324.780 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; 8692-A00 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.7 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; KNT-AL10 Build/HUAWEIKNT-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.2.948 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; VKY-AL00 Build/HUAWEIVKY-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043313 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; GEM-703L Build/HUAWEIGEM-703L; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; HUAWEI GRA-CL10 Build/HUAWEIGRA-CL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043313 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; STF-AL10 Build/HUAWEISTF-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043313 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; SM-N9200 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 4.4.2; L50t Build/17.1.E.2.67; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 4.4.2)",
    "Mozilla/5.0 (Linux; Android 7.0; VTR-AL00 Build/HUAWEIVTR-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043313 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; OPPO R9m Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.7 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; PE-TL10 Build/HuaweiPE-TL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043313 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; BLN-AL40 Build/HONORBLN-AL40; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043313 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; FRD-AL10 Build/HUAWEIFRD-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043313 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.0.2; SM-G9200 Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.1; GN5001 Build/LMY47D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.7.1041 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; KNT-AL20 Build/HUAWEIKNT-AL20; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043313 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; KNT-AL20 Build/HUAWEIKNT-AL20; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043313 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; MI NOTE LTE Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.7 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; MI 5s Plus Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 4.4.2; H60-L01 Build/HDH60-L01; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043313 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 4.4.4; dazen X7 Build/KTU84P; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.3.23.840 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.1.1; vivo Y51e Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043313 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 4.1.2; ZTE N919 Build/JZO54K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043313 Safari/537.36 MicroMessenger/6.5.4.1000 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.1; OPPO R9m Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043313 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; ZTE C2016 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043313 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; DUK-AL20 Build/HUAWEIDUK-AL20; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; Android 5.0.2; vivo Y937 Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 5.0.2)",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; Redmi 3S Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.0.3",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 search%2F1.0 baiduboxapp/0_0.0.0.7_enohpi_4331_057/2.3.9_1C2%258enohPi/1099a/EA5690B80317F655CC46FCE0F4BDB31F0A7D420E8FRRMPKDKNE/1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92 MicroMessenger/6.5.12 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; MI 6 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.0.3",
    "Mozilla/5.0 (iPhone 6sp; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.7.1 Mobile/14C92 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; vivo X7Plus Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.0.947 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; Le X620 Build/HBXCNCU5902606112S; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; Redmi Note 4X Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.0.3",
    "Mozilla/5.0 (Linux; Android 6.0; Redmi Note 4 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043313 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; MI MAX Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2891.650 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.8.7",
    "Mozilla/5.0 (Linux; Android 6.0.1; vivo X9Plus Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; MI NOTE LTE Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/42.0.2311.153 Mobile Safari/537.36 XiaoMi/MiuiBrowser/2.1.1",
    "Mozilla/5.0 (Linux; Android 6.0; vivo Y67A Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043313 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; MI 5 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.0.3",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; NCE-AL00 Build/HUAWEINCE-AL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.7 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; N958St Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/6.3 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; vivo X9Plus Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.1.949 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1.1; NX508J Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 5.1.1)",
    "Mozilla/5.0 (Linux; Android 7.0; STF-AL10 Build/HUAWEISTF-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/7.4 baiduboxapp/8.1 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; Android 6.0; MI 5 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043313 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; ONEPLUS A3010 Build/MXB48T) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.5.937 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; MI 5s Plus Build/MXB48T) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.0.3",
    "Mozilla/5.0 (Linux; Android 4.4.4; N5207 Build/KTU84P; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043313 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-CN; GT-I9500 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.7.0.634 U3/0.8.0 Mobile Safari/534.30",
    "Mozilla/5.0 (iPhone 91; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.7.0 Mobile/14F89 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 7.0; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; Redmi Note 4 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043313 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MHA-AL00 Build/HUAWEIMHA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.2.948 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 4.3; zh-CN; SM-N7506V Build/JLS36C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.8.945 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; CAM-UL00 Build/HONORCAM-UL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/6.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; MI NOTE LTE Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (Linux; Android 7.0; FRD-AL10 Build/HUAWEIFRD-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; Android 7.0; MI MAX Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043313 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Mobile/14E304 MicroMessenger/6.5.12 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; PRO 5 Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.1.949 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 4.4.4; R7c Build/KTU84P; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 4.4.4)",
    "Mozilla/5.0 (iPhone 6p; CPU iPhone OS 8_1_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 MQQBrowser/7.7.1 Mobile/12B436 Safari/8536.25 MttCustomUA/2 QBWebViewType/1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.5.12 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; PLK-TL01H Build/HONORPLK-TL01H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043313 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.1; OPPO A37m Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043408 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; PLK-AL10 Build/HONORPLK-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043313 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; MI MAX Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.0.3",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; MHA-AL00 Build/HUAWEIMHA-AL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.7 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; Che1-CL10 Build/Che1-CL10) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.7 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone 6; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.31 (KHTML, like Gecko) Version/11.0 MQQBrowser/7.7.0 Mobile/15A5327g Safari/8536.25 MttCustomUA/2 QBWebViewType/1",
    "Mozilla/5.0 (Linux; Android 4.4.4; 3007 Build/KTU84P; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 4.4.4)",
    "Mozilla/5.0 (Linux; Android 6.0; HUAWEI MT7-TL10 Build/HuaweiMT7-TL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; FRD-AL10 Build/HUAWEIFRD-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.1.949 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; FRD-DL00 Build/HUAWEIFRD-DL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.7 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone 91; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.5.1 Mobile/14F89 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 4.4.2; SM-G3568V Build/KOT49H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone 92; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.7.0 Mobile/14C92 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 5.1; OPPO R9tm Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0.1; vivo X9Plus Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043408 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; Redmi Note 4 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; HUAWEI CAZ-AL10 Build/HUAWEICAZ-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; VKY-AL00 Build/HUAWEIVKY-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.2.948 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone 6; CPU iPhone OS 10_1_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.6.1 Mobile/14B100 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 6.0.1; MI 5s Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36 MicroMessenger/6.5.12 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; Le X620 Build/HBXCNCU5902606112S; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; SM-G920K Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; Android 7.0; KNT-AL20 Build/HUAWEIKNT-AL20; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; BLN-AL10 Build/HONORBLN-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.2.936 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; HUAWEI MLA-AL10 Build/HUAWEIMLA-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043313 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; HUAWEI MLA-AL10 Build/HUAWEIMLA-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043313 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/NON_NETWORK Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; STF-AL10 Build/HUAWEISTF-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.1.949 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; vivo X9 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043313 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.1.1; vivo X7 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.1.1; OPPO A53 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/56.0.2785.49 Mobile MQQBrowser/6.2 TBS/043220 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 5.0.1; zh-cn; HUAWEI GRA-TL00 Build/HUAWEIGRA-TL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/31.0.0.0 MQQBrowser/7.5 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; MI 5 Build/MXB48T) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.9.5",
    "Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/7.4 baiduboxapp/8.5 (Baidu; P1 7.1.1)",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; HM 1S Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.9.5",
    "Mozilla/5.0 (Linux; Android 7.1.1; OD105 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043313 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; CAM-TL00H Build/HONORCAM-TL00H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.0.947 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MI 5 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.1.949 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; C106-9 Build/ZCXCNCT5902606201S) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.1.949 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; MI 5s Plus Build/MXB48T) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.1.949 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; PLK-UL00 Build/HONORPLK-UL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 V1_AND_SQ_7.1.5_708_YYB_D QQ/7.1.5.3215 NetType/4G WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (iPhone 6s; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/6.0 MQQBrowser/6.6 Mobile/13B143 Safari/8536.25",
    "Mozilla/5.0 (iPhone 6s; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.7.0 Mobile/14G60 Safari/8536.25 MttCustomUA/2 QBWebViewType/1",
    "Mozilla/5.0 (Linux; Android 6.0; HUAWEI MLA-AL10 Build/HUAWEIMLA-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043313 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; BLN-AL10 Build/HONORBLN-AL10) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.7 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1; OPPO R9m Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 5.1)",
    "Mozilla/5.0 (Linux; Android 6.0.1; vivo X9i Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; Mi Note 2 Build/MXB48T) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.9.5",
    "Mozilla/5.0 (Linux; Android 5.0.2; vivo Y37 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/7.4 baiduboxapp/8.3.1 (Baidu; P1 5.0.2)",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; MI NOTE LTE Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.1.949 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; OPPO R9 Plustm A Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.1 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; H60-L12 Build/HDH60-L12) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/23.0.1654.15 UCBrowser/9.2.1.416 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; HUAWEI GRA-TL00 Build/HUAWEIGRA-TL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.7 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; vivo X7 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.1.939 UCBS/2.10.1.10 Mobile Safari/537.36 AliApp(TB/6.10.1) WindVane/8.0.0 1080X1920 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; Android 7.0; KNT-AL20 Build/HUAWEIKNT-AL20; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MI 6 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.1.949 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.1.1; TA-1000 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 7.1.1)",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; Redmi 3 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.9.5",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_1_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12B466 search%2F1.0 baiduboxapp/0_0.0.3.7_enohpi_4331_057/3.1.8_2C2%257enohPi/1099a/363BA7CF28EB37E48AB129155575900C8AD6AF124OCSMIGJABF/1",
    "Mozilla/5.0 (Linux; Android 5.1.1; vivo X7 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.4.1000 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 rabbit/1.0 baiduboxapp/7.1 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; Android 6.0; M5 Note Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; OPPO R9s Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.1.949 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 MicroMessenger/6.5.12 NetType/4G Language/zh_TW",
    "Mozilla/5.0 (iPhone 6p; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.6.1 Mobile/14E304 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; vivo X9L Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.7 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.0.1; zh-cn; HUAWEI GRA-TL00 Build/HUAWEIGRA-TL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.3 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1.1; vivo X7 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043408 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; OPPO R9s Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.7 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; Redmi 3 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.5 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1.1; vivo V3 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 5.1.1)",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; HM 2A Build/KTU84Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.9.1",
    "Mozilla/5.0 (iPhone 6sp; CPU iPhone OS 9_3_4 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 MQQBrowser/7.6.1 Mobile/13G35 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (iPhone 6p; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.6.1 Mobile/14F89 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (iPhone 92; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.6.1 Mobile/14F89 Safari/8536.25 MttCustomUA/2 QBWebViewType/1",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; MI NOTE LTE Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.0.3",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; OPPO A57 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.7 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; ZTE A2017 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 4.1.2; zh-cn; GT-N5100 Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.6 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; KNT-AL10 Build/HUAWEIKNT-AL10) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.7 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B329 MicroMessenger/5.0.1",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; 2014812 Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.5.7",
    "Mozilla/5.0 (Linux; Android 6.0.1; SM-G9208 Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (Linux; Android 7.0; BLN-TL10 Build/HONORBLN-TL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; SM-G9250 Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.7 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-CN; MI 3 Build/KTU84P) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.2.1.550 U3/0.8.0 Mobile Safari/534.30",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; PRO 5 Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.7 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone 6s; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.7.0 Mobile/14F89 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; HM NOTE 1LTE Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.9.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/11B554a rabbit%2F1.0 baiduboxapp/0_0.0.5.6_enohpi_6311_046/4.0.7_2C2%256enohPi/1099a/67FBE25DB85CC0234D4749F47A0C832C37D9EF0B5OGKHDDIEFP/1",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; Redmi 4 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.85 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.2.15",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; vivo X9Plus L Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.8.945 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; Redmi 3 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.7 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; Che2-TL00 Build/HonorChe2-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.5.943 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; HM 2A Build/KTU84Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.9.5",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; DUK-AL20 Build/HUAWEIDUK-AL20) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.7 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 7.1.1)",
    "Mozilla/5.0 (iPhone 6p; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.7.0 Mobile/14F89 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 5.1; vivo X6D Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 5.1)",
    "Mozilla/5.0 (Linux; Android 6.0.1; vivo X9Plus L Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; OPPO R9m Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.1.949 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; vivo X9 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.1.939 UCBS/2.10.1.10 Mobile Safari/537.36 AliApp(TB/6.9.7) WindVane/8.0.0 1080X1920 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; Redmi Note 4X Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.6.946 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1.1; vivo X7 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 5.1.1)",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; OPPO R9 Plustm A Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.7 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; ONEPLUS A3010 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.6.946 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1; m1 note Build/LMY47D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 5.1)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; DUK-AL20 Build/HUAWEIDUK-AL20) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.1.949 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; SM-N9008S Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.8.945 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1; OPPO A37m Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 5.1)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; VIE-AL10 Build/HUAWEIVIE-AL10) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.7 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; FRD-AL00 Build/HUAWEIFRD-AL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.7 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; vivo Y67A Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; PRA-AL00 Build/HONORPRA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043307 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13B143 MicroMessenger/6.5.12 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0.1; vivo X9 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Mobile Safari/537.36 MicroMessenger/6.5.6.1020 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.0.2; vivo X6A Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 5.0.2)",
    "Mozilla/5.0 (Linux; Android 6.0; NEM-AL10 Build/HONORNEM-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043408 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_1_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Mobile/14B100 MicroMessenger/6.5.12 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; N9180 Build/KVT49L) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.6 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; HUAWEI MLA-AL10 Build/HUAWEIMLA-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; Android 7.0; SM-G9300 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/56.0.2924.87 Mobile Safari/537.36 baiduboxapp/8.1 (Baidu; P1 7.0)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13E234 MicroMessenger/6.5.12 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; M5 Note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.6 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1.1; OPPO R11 Plus Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 V1_AND_SQ_7.1.5_708_YYB_D QQ/7.1.5.3215 NetType/WIFI WebP/0.3.0 Pixel/720",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; CHM-UL00 Build/HonorCHM-UL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.2.942 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_0 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13A342 MicroMessenger/6.5.12 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; EDI-AL10 Build/HUAWEIEDISON-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.5.943 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; M5 Note Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; EVA-TL00 Build/HUAWEIEVA-TL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; Android 4.4.4; 6plus Build/KTU84P; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 4.4.4)",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-CN; Coolpad 8675-A Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.1.949 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 4.4.4; Coolpad 8675-A Build/KTU84P; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Xiaomi_2016112_TD-LTE/V1 Linux/3.18.24 Android/6.0 Release/8.8.2016 Browser/AppleWebKit537.36 Mobile Safari/537.36 System/Android 6.0 XiaoMi/MiuiBrowser/2.4.9",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; MI 4W Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.9.5",
    "Mozilla/5.0 (Linux; Android 4.2.2; GT-I9158 Build/JDQ39; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043408 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; Coolpad 8675 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.6 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_0_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13A452 MicroMessenger/6.3.30 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; WAS-TL10 Build/HUAWEIWAS-TL10) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.7 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone 6p; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.6.1 Mobile/14D27 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (iPhone 6s; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.6.1 Mobile/14F89 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; SM-N9005 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1.1; vivo X7 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043408 Safari/537.36 MicroMessenger/6.5.6.1020 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 5.0.2; zh-CN; SM-A7000 Build/LRX22G) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.9.9.739 U3/0.8.0 Mobile Safari/534.30",
    "Mozilla/5.0 (Linux; Android 4.4.4; OPPO R7s Build/KTU84P; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone 6; CPU iPhone OS 9_2_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 MQQBrowser/7.1 Mobile/13D15 Safari/8536.25 MttCustomUA/2",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_0_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13A452 MicroMessenger/6.3.30 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; KNT-AL20 Build/HUAWEIKNT-AL20) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.1.949 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone 6p; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 MQQBrowser/7.6.1 Mobile/13B143 Safari/8536.25 MttCustomUA/2 QBWebViewType/1",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; NX549J Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.5 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1; OPPO A59s Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 5.1)",
    "Mozilla/5.0 (iPhone 92; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.6.1 Mobile/14F89 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13C75 MicroMessenger/6.5.12 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; VTR-AL00 Build/HUAWEIVTR-AL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.7 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; Redmi Note 4X Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.9.5",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; vivo Y55A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.7 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12H321 MicroMessenger/6.5.12 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; en-us; ONEPLUS A3000 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.6 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; KIW-AL10 Build/HONORKIW-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.1.949 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; PLK-CL00 Build/HONORPLK-CL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.6 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; vivo Y67 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92 MicroMessenger/6.5.12 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 search%2F1.0 baiduboxapp/0_0.0.3.7_enohpi_8022_2421/2.3.01_1C2%257enohPi/1099a/EDD42046AD981A416AF22FEA7C88D4AB11692BFC6ORSGTPPOJP/1",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.7 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; SM-G9280 Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.2.942 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; ZTE A2017 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; vivo X7 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.7 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; PRO 6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.7 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 4.4.4; R8205 Build/KTU84P; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 4.4.4)",
    "Mozilla/5.0 (Linux; Android 6.0; HUAWEI VNS-DL00 Build/HUAWEIVNS-DL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 V1_AND_SQ_7.0.0_676_YYB_D QQ/7.0.0.3135 NetType/WIFI WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; m3 note Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.6 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; EVA-AL10 Build/HUAWEIEVA-AL10) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.7 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1.1; vivo V3Max A Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/7.1 rabbit/1.0 baiduboxapp/7.5.1 (Baidu; P1 5.1.1)",
    "Mozilla/5.0 (iPhone 6; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.6.1 Mobile/14F89 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92 MicroMessenger/6.5.12 NetType/2G Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 MicroMessenger/6.5.12 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone 6sp; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.6.1 Mobile/14C92 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; VKY-AL00 Build/HUAWEIVKY-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.1.949 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Mobile/14D27 MicroMessenger/6.5.12 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; HUAWEI MT7-TL10 Build/HuaweiMT7-TL10) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.6 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone 6; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.28 (KHTML, like Gecko) Version/11.0 MQQBrowser/7.6.1 Mobile/15A5318g Safari/8536.25 MttCustomUA/2 QBWebViewType/1",
    "Mozilla/5.0 (Linux; Android 7.0; MHA-TL00 Build/HUAWEIMHA-TL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 rabbit/1.0 baiduboxapp/7.1 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; NCE-AL10 Build/HUAWEINCE-AL10) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.6.0.771 U3/0.8.0 Mobile Safari/534.30",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 MicroMessenger/6.3.31 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; KIW-CL00 Build/HONORKIW-CL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.7 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; SM-G9350 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043307 Safari/537.36 MicroMessenger/6.5.7.1041 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; EDI-AL10 Build/HUAWEIEDISON-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043307 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; ZUK Z2121 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043408 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; ALE-TL00 Build/HuaweiALE-TL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; EVA-TL00 Build/HUAWEIEVA-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.1.949 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 MicroMessenger/6.5.12 NetType/WIFI Language/en",
    "Mozilla/5.0 (Linux; Android 7.0; VKY-AL00 Build/HUAWEIVKY-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043408 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; vivo X6S A Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.1.949 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; BLN-AL10 Build/HONORBLN-AL10) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.6 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 baiduboxapp/0_31.1.3.8_enohpi_8022_2421/2.3.01_2C2%258enohPi/1099a/C0E87667138CBB7295D3D850AD1FAF9474453CBC5FRRKIBGLHA/1",
    "Mozilla/5.0 (Linux; Android 4.4.4; OPPO R7 Build/KTU84P; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 4.4.4)",
    "Mozilla/5.0 (Linux; Android 7.0; MHA-AL00 Build/HUAWEIMHA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043408 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; HUAWEI GRA-UL10 Build/HUAWEIGRA-UL10) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.6 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; HM NOTE 1LTE Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.9.5",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; Redmi Note 3 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.85 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.1.4",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; vivo X6S A Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.6 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; PIC-AL00 Build/HUAWEIPIC-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; M3s Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.1.949 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; MI 4LTE Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.9.5",
    "Mozilla/5.0 (Linux; Android 5.1; OPPO R9tm Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 5.1)",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; PLK-TL01H Build/HONORPLK-TL01H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.1.949 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Mobile/14E304 MicroMessenger/6.5.10 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone 92; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.6.1 Mobile/14E304 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; U20 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.1.949 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1.1; R7Plusm Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 5.1.1)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MHA-AL00 Build/HUAWEIMHA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.1.949 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; BLN-AL10 Build/HONORBLN-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; Android 4.4.2; PE-TL20 Build/HuaweiPE-TL20; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043408 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/7.1 baiduboxapp/8.0 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; NEM-AL10 Build/HONORNEM-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.1.949 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OPPO R11t Build/NMF26X) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.6.1.717 U3/0.8.0 Mobile Safari/534.30",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 MicroMessenger/6.5.11 NetType/3G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.1.1; vivo Y51A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 5.1.1)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; EVA-AL00 Build/HUAWEIEVA-AL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.2 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; HUAWEI NXT-TL00 Build/HUAWEINXT-TL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 baidubrowser/7.14.14.0 (Baidu; P1 7.0)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 MicroMessenger/6.5.6 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.1.949 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; vivo X9 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; HUAWEI MLA-AL10 Build/HUAWEIMLA-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.1.949 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; vivo X9Plus Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; ZTE BA610C Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.1.949 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 MicroMessenger/6.5.12 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 4.4.2; Che2-UL00 Build/HonorChe2-UL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 4.4.2)",
    "Mozilla/5.0 (Linux; Android 7.0; EVA-AL00 Build/HUAWEIEVA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; Android 6.0; CAM-TL00 Build/HONORCAM-TL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 baiduboxapp/8.6.5 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; Android 5.1; OPPO R9m Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.1.1; SM-A8000 Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/7.4 baiduboxapp/8.2.5 (Baidu; P1 5.1.1)",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; OPPO R9s Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.1.939 UCBS/2.10.1.10 Mobile Safari/537.36 AliApp(TB/6.9.5) WindVane/8.0.0 1080X1920 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; Android 6.0.1; OPPO R9s Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (Linux; Android 6.0; M5 Note Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; Android 5.1; vivo X6D Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 V1_AND_SQ_7.1.0_692_YYB_D QQ/7.1.0.3175 NetType/WIFI WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 MicroMessenger/6.5.2 NetType/2G Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A456 MicroMessenger/6.3.27 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 MicroMessenger/6.5.4 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 MicroMessenger/6.5.4 NetType/2G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; HUAWEI VNS-TL00 Build/HUAWEIVNS-TL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/2G Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A403 MicroMessenger/6.5.9 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; XT1650-05 Build/NCC25.106-15) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.0.947 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.1.1; MI MAX 2 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043307 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-CN; 4G Build/KTU84P) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.4.1.576 U3/0.8.0 Mobile Safari/534.30",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; SM-A7100 Build/LMY47X) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.9.2.712 U3/0.8.0 Mobile Safari/534.30",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; MI 5s Plus Build/MXB48T) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.9.5",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; KNT-AL10 Build/HUAWEIKNT-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.1.949 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 4.3; zh-cn; HM 1SC Build/JLS36C) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/6.5 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; SM-G9350 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.6 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone 6s; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.6.1 Mobile/14E304 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 baiduboxapp/0_21.0.6.7_enohpi_4331_057/2.3.01_1C2%259enohPi/1099a/CB3044BC838EF3B069420FBE5519E2DC918D563D1FCKBCBEHHA/1",
    "Mozilla/5.0 (Linux; U; Android 4.3; zh-cn; R831S Build/JLS36C) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baidubrowser/4.5.19.14 (Baidu; P1 4.3)",
    "Mozilla/5.0 (Linux; Android 7.0; EVA-AL10 Build/HUAWEIEVA-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; Android 7.0; DUK-AL20 Build/HUAWEIDUK-AL20; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 baiduboxapp/8.1 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; Android 7.0; TRT-AL00A Build/HUAWEITRT-AL00A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; Android 6.0; BLN-AL10 Build/HONORBLN-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 MicroMessenger/6.5.10.1080 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.0.1; HUAWEI GRA-CL00 Build/HUAWEIGRA-CL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0.1; OPPO A57 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; WAS-AL00 Build/HUAWEIWAS-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043307 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13E238 MicroMessenger/6.5.10 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 MicroMessenger/6.5.11 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0.1; SM-G9280 Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; EVA-TL00 Build/HUAWEIEVA-TL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043307 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; TRT-AL00A Build/HUAWEITRT-AL00A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043307 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.1.1; OPPO R11t Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043307 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; MI 4LTE Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.8.7",
    "Mozilla/5.0 (Linux; Android 5.1; vivo X6D Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.6.1020 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; HUAWEI GRA-TL00 Build/HUAWEIGRA-TL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; SM-G9200 Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.0.907 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone 5; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.5.1 Mobile/14F89 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 7.0; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043408 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; FRD-AL10 Build/HUAWEIFRD-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043307 Safari/537.36 V1_AND_SQ_7.1.0_692_YYB_D QQ/7.1.0.3175 NetType/WIFI WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; H60-L03 Build/HDH60-L03) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.4.0.558 U3/0.8.0 Mobile Safari/534.30",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; vivo X9 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.1.939 UCBS/2.10.1.10 Mobile Safari/537.36 AliApp(TB/6.9.5) WindVane/8.0.0 1080X1920 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; PRO 5 Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.8.945 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; NCE-AL10 Build/HUAWEINCE-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.0.947 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; MHA-AL00 Build/HUAWEIMHA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043307 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.0.2; vivo X6Plus A Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/7.4 baiduboxapp/8.5 (Baidu; P1 5.0.2)",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; FRD-AL00 Build/HUAWEIFRD-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.1.939 UCBS/2.10.1.10 Mobile Safari/537.36 AliApp(TB/6.9.5) WindVane/8.0.0 1080X1812 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; Android 6.0.1; MI MAX Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/7.2 baidubrowser/7.2.4.204 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (Linux; Android 7.0; PRA-AL00X Build/HONORPRA-AL00X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043307 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 rabbit%2F1.0 baiduboxapp/0_21.0.6.7_enohpi_4331_057/2.3.01_1C2%259enohPi/1099a/CB3044BC838EF3B069420FBE5519E2DC918D563D1FCKBCBEHHA/1",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 5.1.1)",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OPPO R11 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.8.945 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; SM-A8000 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.0.2; PLK-AL10 Build/HONORPLK-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 5.0.2; zh-cn; Redmi Note 3 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.9.5",
    "Mozilla/5.0 (Linux; Android 6.0; EVA-AL00 Build/HUAWEIEVA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.7.1041 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 MicroMessenger/6.3.30 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.5.7 NetType/2G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; m1 metal Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.8.945 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; ZTE BA610C Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.6 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 4.4.2; H60-L02 Build/HDH60-L02; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.3.980 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; FRD-AL10 Build/HUAWEIFRD-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043307 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; MHA-AL00 Build/HUAWEIMHA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043307 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.1.1; SM801 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.0.2; Redmi Note 2 Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; TRT-AL00A Build/HUAWEITRT-AL00A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043307 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 MicroMessenger/6.5.11 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; HUAWEI VNS-AL00 Build/HUAWEIVNS-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.8.945 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 4.4.4; vivo Y29L Build/KTU84P; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 4.4.2; CHM-TL00 Build/HonorCHM-TL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 4.4.4; A31 Build/KTU84P; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 4.4.2; CHM-TL00H Build/HonorCHM-TL00H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone 6; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 MQQBrowser/7.3 Mobile/12H143 Safari/8536.25 MttCustomUA/2 QBWebViewType/1",
    "Mozilla/5.0 (iPhone 6; CPU iPhone OS 9_3_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 MQQBrowser/7.2.1 Mobile/13E238 Safari/8536.25 MttCustomUA/2 QBWebViewType/1",
    "Mozilla/5.0 (Linux; Android 6.0; HUAWEI GRA-CL00 Build/HUAWEIGRA-CL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; Android 6.0; PLK-AL10 Build/HONORPLK-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.1; CUN-TL00 Build/HUAWEICUN-TL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 V1_AND_SQ_6.5.0_390_YYB_D QQ/6.5.0.2835 NetType/4G WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; Android 6.0; Redmi Pro Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 baiduboxapp/8.6.5 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; SM919 Build/MXB48T) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.8.945 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 baiduboxapp/0_01.0.4.8_enohpi_8022_2421/2.3.01_2C2%259enohPi/1099a/FC6C4B0788C416054CAC03E5668904CE8F62AFDA3ORIAPLJSND/1",
    "Mozilla/5.0 (Linux; Android 5.1; OPPO A59m Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 baiduboxapp/8.6.5 (Baidu; P1 5.1)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13C75 MicroMessenger/6.5.10 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; MHA-AL00 Build/HUAWEIMHA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043307 Safari/537.36 V1_AND_SQ_7.1.0_692_YYB_D QQ/7.1.0.3175 NetType/WIFI WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; Android 6.0; BLN-AL10 Build/HONORBLN-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 V1_AND_SQ_7.1.0_692_YYB_D QQ/7.1.0.3175 NetType/4G WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; FRD-AL00 Build/HUAWEIFRD-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.8.945 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; MHA-AL00 Build/HUAWEIMHA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; ONEPLUS A3010 Build/MXB48T) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.2.5.884 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; FRD-AL10 Build/HUAWEIFRD-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.8.945 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12H143 MicroMessenger/6.5.10 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; EVA-AL10 Build/HUAWEIEVA-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 V1_AND_SQ_7.1.0_692_YYB_D QQ/7.1.0.3175 NetType/WIFI WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; Android 6.0.1; LG-H868 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 V1_AND_SQ_7.1.0_692_YYB_D QQ/7.1.0.3175 NetType/WIFI WebP/0.3.0 Pixel/1440",
    "Mozilla/5.0 (Linux; Android 7.0; HUAWEI MLA-AL00 Build/HUAWEIMLA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043307 Safari/537.36 V1_AND_SQ_6.6.2_450_YYB_D QQ/6.6.2.2980 NetType/WIFI WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; Android 7.0; PRA-TL10 Build/HONORPRA-TL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043307 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; Mi-4c Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.9.6",
    "Mozilla/5.0 (Linux; U; Android 5.0.2; zh-CN; Redmi Note 3 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.8.945 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.5.7 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.0.2; vivo Y35A Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 baiduboxapp/8.6.5 (Baidu; P1 5.0.2)",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; ONEPLUS A3000 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.1.944 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; KIW-CL00 Build/HONORKIW-CL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.6 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A403 baiduboxapp/0_9.1.0.8_enohpi_4331_057/1.0.01_1C2%258enohPi/1099a/31408F69DAEBFE9F751CFBEDA7FF01906186CE1FDFRCHOICHMB/1",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.8.945 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; Mi-4c Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.8.945 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; CHM-TL00 Build/HonorCHM-TL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.6 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.9.5",
    "Mozilla/5.0 (iPhone 6sp; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.6.0 Mobile/14C92 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; LG-H819 Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.8.945 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; Redmi Note 3 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.9.5",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; NEM-TL00H Build/HONORNEM-TL00H) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/6.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; Redmi Note 4 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; MI 5s Build/MXB48T) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.6 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; PE-TL00M Build/HuaweiPE-TL00M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.4 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; Nexus 6P Build/N4F26I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.8.945 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone 84; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 MQQBrowser/7.6.0 Mobile/13F69 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 5.0.2; zh-cn; Redmi Note 2 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.9.5",
    "Mozilla/5.0 (iPhone 6; CPU iPhone OS 10_1_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.6.0 Mobile/14B100 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 MicroMessenger/6.5.10 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.1.1; YQ607 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 baiduboxapp/8.6.5 (Baidu; P1 5.1.1)",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; MI 6 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.6 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; HUAWEI MLA-AL10 Build/HUAWEIMLA-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; MI 5s Build/MXB48T) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.9.5",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; HUAWEI MLA-AL10 Build/HUAWEIMLA-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.8.945 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; PLK-AL10 Build/HONORPLK-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.0.2; vivo X6Plus A Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 baiduboxapp/8.6.5 (Baidu; P1 5.0.2)",
    "Mozilla/5.0 (Linux; Android 7.0; PIC-AL00 Build/HUAWEIPIC-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 baiduboxapp/8.6.5 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; MI 5 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.7.7",
    "Mozilla/5.0 (Linux; Android 5.0.2; Redmi Note 2 Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 baiduboxapp/8.6.5 (Baidu; P1 5.0.2)",
    "Mozilla/5.0 (iPhone 6p; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.6.0 Mobile/14F89 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36 MicroMessenger/6.5.9 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 MicroMessenger/6.5.10 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; PLK-AL10 Build/HONORPLK-AL10) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.6 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; SM-G9280 Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 baiduboxapp/8.6.5 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; Le X620 Build/HEXCNFN5902606111S) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.6 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; Letv X501 Build/DBXCNOP5902605181S; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 baiduboxapp/8.6.5 (Baidu; P1 6.0)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_1_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12B440 baiduboxapp/0_0.0.8.3_enohpi_6311_046/2.1.8_1C2%257enohPi/1099a/e3f5536a141811db40efd6400f1d0a4e/1",
    "Mozilla/5.0 (iPhone 84; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.6.0 Mobile/14F89 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 6.0; PE-TL20 Build/HuaweiPE-TL20; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.0.2; vivo Y51A Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 baiduboxapp/8.6.5 (Baidu; P1 5.0.2)",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; Redmi Pro Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.9.5",
    "Mozilla/5.0 (Linux; Android 6.0; M1 E Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 baiduboxapp/8.6.5 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; Android 7.0; KNT-AL10 Build/HUAWEIKNT-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 baidubrowser/7.14.14.0 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; Android 7.0; EVA-AL10 Build/HUAWEIEVA-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043307 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone 6sp; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 MQQBrowser/7.6.0 Mobile/13G36 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 7.0; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043307 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.1; CUN-AL00 Build/HUAWEICUN-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 rabbit/1.0 baiduboxapp/7.1 (Baidu; P1 5.1)",
    "Mozilla/5.0 (Linux; Android 7.0; MI MAX Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 baiduboxapp/8.6.5 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; Redmi Note 3 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.8.7",
    "Mozilla/5.0 (iPhone 5SGLOBAL; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 MQQBrowser/7.1 Mobile/13F69 Safari/8536.25 MttCustomUA/2",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; EVA-AL00 Build/HUAWEIEVA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.8.945 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1; OPPO R9tm Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; vivo X5S L Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.6 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 4.4.2; HONOR H30-L01 Build/HonorH30-L01; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; Redmi 3S Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.9.5",
    "Mozilla/5.0 (Linux; Android 6.0; MI 5 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Mobile/14B72 MicroMessenger/6.5.9 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; OPPO R9m Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 baiduboxapp/8.6.5 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; Android 5.1.1; OPPO A33 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 baiduboxapp/8.6.5 (Baidu; P1 5.1.1)",
    "Mozilla/5.0 (Linux; U; Android 6.0; en-gb; PLK-UL00 Build/HONORPLK-UL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/6.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 4.4.2; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; HUAWEI G750-T01 Build/HuaweiG750-T01) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.7 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone 6sp; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.4.1 Mobile/14A456 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; VKY-AL00 Build/HUAWEIVKY-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.8.945 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; MI 5s Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.9.6",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; HUAWEI MT7-CL00 Build/HuaweiMT7-CL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.6 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 4.4.2; PE-UL00 Build/HuaweiPE-UL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 baiduboxapp/8.6.5 (Baidu; P1 4.4.2)",
    "Mozilla/5.0 (Linux; Android 7.0; MI MAX Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043307 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; Redmi Note 4 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13E233 search%2F1.0 baiduboxapp/0_0.1.1.7_enohpi_6311_046/3.9_2C2%256enohPi/1099a/5D1C827E3FFF1113EB8C5DA7380B50F20325F881FOCMEACTITQ/1",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; HUAWEI GRA-TL00 Build/HUAWEIGRA-TL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.6 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; vivo Y55A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.8.945 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; SM-G9200 Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Mobile Safari/537.36 rabbit/1.0 baiduboxapp/7.1 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (Linux; Android 4.4.4; N5207 Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/6.3 rabbit/1.0 baiduboxapp/7.4 (Baidu; P1 4.4.4)",
    "Mozilla/5.0 (Linux; Android 7.0; VTR-AL00 Build/HUAWEIVTR-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043307 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 search%2F1.0 baiduboxapp/0_21.0.6.7_enohpi_8022_2421/2.3.01_1C2%257enohPi/1099a/B2A2B05D606E466813533D82AAF61095345B0B941FRGIIOBOJK/1",
    "Mozilla/5.0 (Linux; Android 7.0; SM-G9308 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/7.4 baiduboxapp/8.5 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; VIE-AL10 Build/HUAWEIVIE-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.8.945 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; Redmi 4X Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.8.945 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 4.4.4; SM-G7200 Build/KTU84P; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; Le X620 Build/HEXCNFN5902606111S; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_4 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G35 MicroMessenger/6.5.9 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13E238 MicroMessenger/6.5.9 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0.1; vivo Y55A Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 baiduboxapp/8.6.5 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; MI 5 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.9.6",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; EVA-AL10 Build/HUAWEIEVA-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.8.945 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone 5SGLOBAL; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 MQQBrowser/7.6.0 Mobile/12H143 Safari/8536.25 MttCustomUA/2 QBWebViewType/1",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; VIE-AL10 Build/HUAWEIVIE-AL10) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.6 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; M571C Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/6.7 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1; HUAWEI TIT-AL00 Build/HUAWEITIT-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.4.1000 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.0.2; vivo Y37A Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 baiduboxapp/8.6.5 (Baidu; P1 5.0.2)",
    "Mozilla/5.0 (Linux; Android 6.0; HUAWEI GRA-TL00 Build/HUAWEIGRA-TL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 baiduboxapp/8.6.5 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; MI 5 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.9.5",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MI 5 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.8.945 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 4.4.4; R7c Build/KTU84P; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/ctlte Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_1_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Mobile/14B100 MicroMessenger/6.5.9 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0.1; vivo X9Plus L Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_4 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G35 MicroMessenger/6.5.9 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Mobile/14D27 MicroMessenger/6.3.22 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.0.2; vivo X6A Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 4.4.4) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36 XiaoMi/MiuiBrowser/2.1.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Mobile/14D27 MicroMessenger/6.5.9 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; MI 6 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.9.5",
    "Mozilla/5.0 (Linux; Android 6.0.1; OPPO R9s Plus Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 baiduboxapp/8.6.5 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; PLK-TL01H Build/HONORPLK-TL01H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.8.945 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; ZUK Z2131 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.6 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; ONEPLUS A3000 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.8.945 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; SM-C7000 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.8.945 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; SM-G9250 Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 baiduboxapp/6.3.1 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; HUAWEI CRR-CL00 Build/HUAWEICRR-CL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.6 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13C75 MicroMessenger/6.3.27 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0.1; SM-A9000 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 baiduboxapp/6.3.1 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; Redmi Note 4 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.9.5",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 MicroMessenger/6.5.9 NetType/WIFI Language/zh_TW",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; OPPO R9s Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.6 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; vivo X7 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.1.939 UCBS/2.10.1.8 Mobile Safari/537.36 AliApp(TB/6.8.6) WindVane/8.0.0 1080X1920 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; Android 5.1.1; OPPO A53m Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 4.1.2; en-US; GT-S7278U Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.5.809 U3/0.8.0 Mobile Safari/534.30",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; vivo X9 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.1.939 UCBS/2.10.1.8 Mobile Safari/537.36 AliApp(TB/6.9.1) WindVane/8.0.0 1080X1920 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; Android 6.0; HUAWEI GRA-UL10 Build/HUAWEIGRA-UL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 baiduboxapp/6.3.1 (Baidu; P1 6.0)",
    "Mozilla/5.0 (iPhone 6; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.6.0 Mobile/14E304 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92 MicroMessenger/6.5.9 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; PE-TL20 Build/HuaweiPE-TL20) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.8.945 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; OPPO A59s Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.6 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; HUAWEI eH880 Build/HUAWEINXT-XD00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 baiduboxapp/8.6.5 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; Android 4.4.4; MI 3W Build/KTU84P; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 wxwork/2.0.0 MicroMessenger/6.3.22",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; MI MAX Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.9.5",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; SM-N9100 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.8.945 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1; m1 metal Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; vivo Y67 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.6.946 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1.1; vivo V3Max A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 baiduboxapp/8.6.5 (Baidu; P1 5.1.1)",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; MI NOTE LTE Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.9.5",
    "Mozilla/5.0 (Linux; Android 5.1.1; vivo X7Plus Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/7.1 baiduboxapp/8.0 (Baidu; P1 5.1.1)",
    "Mozilla/5.0 (Linux; Android 5.1.1; vivo Xplay5A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 baiduboxapp/8.6.5 (Baidu; P1 5.1.1)",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; LEX622 Build/HBXCNCU5902606112S) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.6 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1; CUN-TL00 Build/HUAWEICUN-TL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.7.1041 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0.1; MI NOTE LTE Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 wxwork/2.0.0 MicroMessenger/6.3.22",
    "Mozilla/5.0 (Linux; Android 4.4.2; Che2-UL00 Build/HonorChe2-UL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 baiduboxapp/8.6.5 (Baidu; P1 4.4.2)",
    "Mozilla/5.0 (Linux; Android 4.4.4; MI 3W Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 wxwork/1.3.5 MicroMessenger/6.3.22",
    "Mozilla/5.0 (Linux; Android 7.0; BLN-AL40 Build/HONORBLN-AL40; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043307 Safari/537.36 wxwork/2.0.0 MicroMessenger/6.3.22",
    "Mozilla/5.0 (Linux; Android 5.1.1; Redmi 3 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 V1_AND_SQ_7.1.0_692_YYB_D QQ/7.1.0.3175 NetType/WIFI WebP/0.3.0 Pixel/720",
    "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 V1_AND_SQ_7.1.0_692_YYB_D QQ/7.1.0.3175 NetType/WIFI WebP/0.3.0 Pixel/720",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A456 wxwork/2.0.1 MicroMessenger/6.3.22",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MI 6 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.8.945 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 MicroMessenger/6.5.2 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.1; OPPO A37m Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 baiduboxapp/8.6.5 (Baidu; P1 5.1)",
    "Mozilla/5.0 (iPhone 6sp; CPU iPhone OS 9_3_4 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 MQQBrowser/7.6.0 Mobile/13G35 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13E234 MicroMessenger/6.5.9 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; vivo Y67A Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; Redmi Pro Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; HM NOTE 1W Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.4 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12D508 baiduboxapp/0_11.0.0.8_enohpi_4331_057/2.8_2C2%257enohPi/1099a/87F9802A5B1122A65A6C9B4E437B35215C10388BAOCGNDTGGFD/1",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; NEM-AL10 Build/HONORNEM-AL10) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/6.6 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.6 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone 6; CPU iPhone OS 8_1_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 MQQBrowser/7.6.0 Mobile/12B466 Safari/8536.25 MttCustomUA/2 QBWebViewType/1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_1_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Mobile/14B100 MicroMessenger/6.5.9 NetType/4G Language/en",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MHA-AL00 Build/HUAWEIMHA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.8.945 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone 5SGLOBAL; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.6.0 Mobile/14F89 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; 2014813 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.8.6",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; Redmi 3S Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.8.7 tae_sdk_a_2.1.0 AliApp(BC/2.1.0)",
    "Mozilla/5.0 (Linux; Android 5.1.1; OPPO R7sPlus Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 baiduboxapp/8.6.5 (Baidu; P1 5.1.1)",
    "Mozilla/5.0 (Linux; Android 6.0.1; OPPO R9s Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 V1_AND_SQ_7.1.0_692_YYB_D QQ/7.1.0.3175 NetType/4G WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; Android 7.0; MI MAX Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043307 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 5.0; zh-cn; SM-N9008V Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/6.4 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; HUAWEI NXT-DL00 Build/HUAWEINXT-DL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.8.945 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; SM-G9500 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 baiduboxapp/8.6.5 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; 2014813 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.8.7",
    "Mozilla/5.0 (Linux; Android 5.1; OPPO R9tm Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; ONEPLUS A3000 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.8.945 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 4.4.4; OPPO R7 Build/KTU84P; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.1.1; vivo X7 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043305 Safari/537.36 MicroMessenger/6.5.6.1020 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Mobile/14D27 MicroMessenger/6.3.28 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; DUK-AL20 Build/HUAWEIDUK-AL20; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043307 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_1_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Mobile/14B100 MicroMessenger/6.5.9 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; VIE-AL10 Build/HUAWEIVIE-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043307 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 baiduboxapp/8.6.5 (Baidu; P1 5.1)",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; ONEPLUS A3010 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.6 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1; SM-J7008 Build/LMY47O) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/7.4 baiduboxapp/8.2.5 (Baidu; P1 5.1)",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-CN; OPPO R7s Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.3.3) WindVane/8.0.0 1080X1800",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; OPPO R7sm Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 1080X1800",
    "Mozilla/5.0 (Linux; U; Android 5.0.2; zh-CN; vivo X6Plus A Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MP1503 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; SM-A7100 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.1.939 UCBS/2.10.1.10 Mobile Safari/537.36 AliApp(TB/6.10.3) WindVane/8.0.0 1080X1920 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; FRD-AL00 Build/HUAWEIFRD-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1794",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; LA-S31 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 720X1280",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-CN; CHM-CL00 Build/CHM-CL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 720X1280",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; VTR-TL00 Build/HUAWEIVTR-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 7.0; MHA-AL00 Build/HUAWEIMHA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060133) NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.6.1 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.6.0 NetType/3G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 1080X1776",
    "Mozilla/5.0 (Linux; Android 5.1; vivo V3M A Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1200(0x26060031) NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.1; vivo V3M A Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1200(0x26060031) NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; m1 note Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.1 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; FRD-DL00 Build/HUAWEIFRD-DL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 1080X1794",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; Redmi Note 4X Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.1 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 8.0.0; zh-CN; ALP-AL00 Build/HUAWEIALP-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; Redmi Note 3 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; Redmi Note 4X Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.10",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; Le X620 Build/HEXCNFN5902012151S) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.25 Mobile Safari/537.36 AliApp(TB/7.1.3) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; GN8003 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; HUAWEI MT7-CL00 Build/HuaweiMT7-CL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; PLK-AL10 Build/HONORPLK-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1.44) WindVane/8.3.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 8.0.0; zh-CN; BKL-AL20 Build/HUAWEIBKL-AL20) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 1080X2160",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; vivo Xplay5A Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3.4) WindVane/8.0.0 1440X2560",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_2 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; vivo X20Plus A Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 1080X2040",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; NEM-AL10 Build/HONORNEM-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 5.0; zh-CN; R7Plust Build/LRX21M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.1.939 UWS/2.11.0.7 Mobile Safari/537.36 AliApp(TB/6.11.0) UCBS/2.11.1.1 WindVane/8.0.0 1080X1800 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; PLK-TL01H Build/HONORPLK-TL01H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 1080X1812",
    "Mozilla/5.0 (Linux; Android 6.0; M5 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.1 baidubrowser/7.17.12.0 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-CN; CHM-CL00 Build/CHM-CL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 720X1280",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; M1 E Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.1 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; TA-1000 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.1.939 UCBS/2.10.1.10 Mobile Safari/537.36 AliApp(TB/6.10.3) WindVane/8.0.0 1080X1920 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.85 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.2.15",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_2 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B202 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; vivo X9i Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; vivo X6L Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; OPPO R9m Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-CN; OPPO R7s Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 1080X1800",
    "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.1 baidubrowser/7.17.12.0 (Baidu; P1 7.1.1)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; FRD-AL00 Build/HUAWEIFRD-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 1080X1794",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; vivo X9s Plus Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; VIE-AL10 Build/HUAWEIVIE-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 1080X1812",
    "Mozilla/5.0 (Linux; Android 5.1.1; OPPO R9 Plusm A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1200(0x26060031) NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; VIE-AL10 Build/HUAWEIVIE-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 1080X1815",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MIX 2 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 1080X2030",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; MHA-AL00 Build/HUAWEIMHA-AL00) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/1.0.0.100 U3/0.8.0 Mobile Safari/534.30 AliApp(TB/6.3.0) WindVane/8.0.0 1080X1812 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OPPO R11 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.6) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; GN9011 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HTC D816t Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.8.2.962 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; VTR-AL00 Build/HUAWEIVTR-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.3.0 720X1280",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OPPO R11t Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 8.0.0; zh-cn; BKL-AL20 Build/HUAWEIBKL-AL20) AppleWebKit/537.36 (KHTML, like Gecko) MQQBrowser/7.3 Chrome/37.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; vivo X7Plus Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; SM-G9350 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 1440X2560",
    "Mozilla/5.0 (Linux; Android 7.1.1; OPPO R11 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1200(0x26060031) NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 8.0.0; zh-cn; STF-AL10 Build/HUAWEISTF-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.0.0 MQQBrowser/7.3 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; SM-G9009D Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.8.952 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; PIC-AL00 Build/HUAWEIPIC-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1200(0x26060031) NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; OPPO R9m Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.1 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; LON-AL00 Build/HUAWEILON-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.8.2.962 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; PRA-AL00X Build/HONORPRA-AL00X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 1080X1812",
    "Mozilla/5.0 (Linux; Android 6.0.1; OPPO R9sk Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1200(0x26060031) NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; OPPO R9sk Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 5.0.2; vivo X6Plus A Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 5.0.2)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_2 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A421 MicroMessenger/6.6.0 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MI MAX 2 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.8.2.962 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; NX595J Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; SM-G9350 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.8.2.962 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; HUAWEI NXT-DL00 Build/HUAWEINXT-DL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.1 baiduboxapp/10.1.0.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; EVA-AL10 Build/HUAWEIEVA-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 1080X1794",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1776",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_1 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C153 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; Mi Note 2 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.4.3",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; vivo X7Plus Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 7.0; MI 5 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.1 baiduboxapp/10.1.0.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Mobile/14B72 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; vivo X9Plus Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (iPhone 6sp; CPU iPhone OS 11_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0 MQQBrowser/8.0.2 Mobile/15B87 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (iPhone 6s; CPU iPhone OS 11_1_2 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/6.0 MQQBrowser/6.7.2 Mobile/15B202 Safari/8536.25 MttCustomUA/2",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MI 5s Plus Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.8.2.962 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; FRD-AL00 Build/HUAWEIFRD-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1200(0x26060031) NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone 6p; CPU iPhone OS 11_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0 MQQBrowser/8.0.2 Mobile/15B87 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; WAS-AL00 Build/HUAWEIWAS-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; HUAWEI NXT-TL00 Build/HUAWEINXT-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.8.2.962 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1200(0x26060031) NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MI 6 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.8.2.962 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.0.2; zh-CN; Redmi Note 3 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OPPO R11 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; HUAWEI TIT-AL00 Build/HUAWEITIT-AL00) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.8.822 U3/0.8.0 Mobile Safari/534.30",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-CN; Meitu M4s Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 720X1280",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; Mi-4c Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.7.7",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; CPN-AL00 Build/HUAWEICPN-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.1.961 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MI 5 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; EVA-TL00 Build/HUAWEIEVA-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 1080X1794",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; HUAWEI VNS-AL00 Build/HUAWEIVNS-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; FRD-AL10 Build/HUAWEIFRD-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 1080X1794",
    "Mozilla/5.0 (Linux; Android 7.1.1; MI MAX 2 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1200(0x26060031) NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MHA-AL00 Build/HUAWEIMHA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-CN; A0001 Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.1.961 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.10",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; OPPO R9tm Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; vivo Y55A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 720X1280",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; vivo X7 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.25 Mobile Safari/537.36 AliApp(TB/7.1.3) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MIX 2 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.8.2.962 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; EVA-AL00 Build/HUAWEIEVA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 baiduboxapp/8.6.5 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; Android 7.0; SM-G9280 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.1 baiduboxapp/10.1.0.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92 MicroMessenger/6.6.0 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MI MAX Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; vivo X20 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 1080X2160",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.9 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; SM-G9350 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.4 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.1.1; Mi Note 3 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043804 Mobile Safari/537.36 MicroMessenger/6.6.1200(0x26060031) NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; HUAWEI NXT-TL00 Build/HUAWEINXT-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.21 Mobile Safari/537.36 AliApp(TB/7.1.1) WindVane/8.0.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; OPPO A59s Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 720X1280",
    "Mozilla/5.0 (Linux; Android 7.0; VKY-AL00 Build/HUAWEIVKY-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5 Build/M4B30X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.5.11 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (iPhone 6; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.0 MQQBrowser/8.0.2 Mobile/14G60 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 6.0.1; vivo X9Plus Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043804 Mobile Safari/537.36 MicroMessenger/6.6.1200(0x26060031) NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_3 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A432 MicroMessenger/6.5.17 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12H143 MicroMessenger/6.6.0 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0.1; vivo X9 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043804 Mobile Safari/537.36 MicroMessenger/6.6.1200(0x26060031) NetType/WIFI Language/en",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; MHA-AL00 Build/HUAWEIMHA-AL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; EVA-AL10 Build/HUAWEIEVA-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile MQQBrowser/6.2 TBS/043722 Safari/537.36 MicroMessenger/6.6.1200(0x26060031) NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone 6s; CPU iPhone OS 10_1_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0 MQQBrowser/8.0.2 Mobile/14B150 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (iPhone 91; CPU iPhone OS 11_2_1 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0 MQQBrowser/7.9.0 Mobile/15C153 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-CN; DOOV L1 Build/DOOVL1) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.21 Mobile Safari/537.36 AliApp(TB/7.1.0) WindVane/8.0.0 720X1280",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A372 MicroMessenger/6.5.23 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; OPPO R9sk Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone 6p; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 MQQBrowser/7.2.1 Mobile/13G36 Safari/8536.25 MttCustomUA/2 QBWebViewType/1",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; OPPO R9s Plus Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; HUAWEI NXT-TL00 Build/HUAWEINXT-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OPPO R11s Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 1080X2016",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MI 5 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.8.2.962 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; vivo X7 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; vivo X20A Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X2160",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-CN; MI PAD Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1536X2048",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; Le X620 Build/HBXCNCU5902606112S) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.1.939 UCBS/2.10.1.8 Mobile Safari/537.36 AliApp(TB/6.8.6) WindVane/8.0.0 1080X1920 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; DUK-AL20 Build/HUAWEIDUK-AL20) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; OPPO R9s Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; SM-G9350 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; OPPO R9 Plustm A Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (iPhone 92; CPU iPhone OS 11_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0 MQQBrowser/8.0.2 Mobile/15B87 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; HUAWEI GRA-UL00 Build/HUAWEIGRA-UL00) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/1.0.0.100 U3/0.8.0 Mobile Safari/534.30 AliApp(TB/6.7.6) WindVane/8.0.0 1080X1812 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; KNT-AL20 Build/HUAWEIKNT-AL20) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 1440X2408",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; VTR-AL00 Build/HUAWEIVTR-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; vivo X7 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.3.2.21) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 7.0; HUAWEI NXT-CL00 Build/HUAWEINXT-CL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.1 baiduboxapp/10.1.0.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; vivo X9L Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; vivo X20 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone 6; CPU iPhone OS 11_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0 MQQBrowser/8.0.2 Mobile/15B87 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 5.0.2; zh-cn; Redmi Note 3 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.10",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MHA-TL00 Build/HUAWEIMHA-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1812",
    "Mozilla/5.0 (Linux; Android 5.1.1; vivo X7 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043804 Mobile Safari/537.36 MicroMessenger/6.6.1200(0x26060031) NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; MHA-AL00 Build/HUAWEIMHA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_2 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B202 MicroMessenger/6.6.0 NetType/4G Language/zh_TW",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; KIW-CL00 Build/HONORKIW-CL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.7.957 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.0.2; zh-CN; vivo X6A Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 UWS/2.10.2.11 Mobile Safari/537.36 AliApp(DingTalk/4.2.1) com.alibaba.android.rimet/0 Channel/10003993 language/zh-CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; DUK-AL20 Build/HUAWEIDUK-AL20) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.8.0.960 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; MI PAD 3 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Safari/537.36 T7/10.1 baiduboxapp/10.1.0.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; SM-C5000 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1; OPPO R9tm Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1200(0x26060031) NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; vivo Y67A Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; VKY-AL00 Build/HUAWEIVKY-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.1 baiduboxapp/10.1.0.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; Android 6.0; OPPO A59st Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1200(0x26060031) NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; LON-AL00 Build/HUAWEILON-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 1440X2560",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; Redmi Note 4 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.8.2.962 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; DUK-AL20 Build/HUAWEIDUK-AL20) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.8.2.962 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MI MAX 2 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.1.961 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; MI 6 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.11",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; FRD-AL10 Build/HUAWEIFRD-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.1.939 UCBS/2.10.1.10 Mobile Safari/537.36 AliApp(TB/6.9.7) WindVane/8.0.0 1080X1794 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; PE-TL20 Build/HuaweiPE-TL20) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1776",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; PRA-AL00X Build/HONORPRA-AL00X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; Redmi Note 3 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; OPPO R9km Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 5.1; OPPO R9m Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.0.2; vivo Y51A Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043804 Mobile Safari/537.36 MicroMessenger/6.5.22.1160 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1200(0x26060030) NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_1 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C153 MicroMessenger/6.5.3 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A372 MicroMessenger/6.5.23 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_1 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C153 MicroMessenger/6.5.3 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.1.1; MX6 Build/NMF26O; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1200(0x26060030) NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0.1; SM-C9000 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043804 Mobile Safari/537.36 MicroMessenger/6.5.23.1180 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 5.0.2; zh-CN; Redmi Note 2 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; DUK-AL20 Build/HUAWEIDUK-AL20) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2.15) WindVane/8.3.0 1080X1812",
    "Mozilla/5.0 (Linux; Android 7.1.1; MI MAX 2 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A372 MicroMessenger/6.6.0 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 5.0.2; zh-CN; vivo X5Pro D Build/LRX21M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_1 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C153 MicroMessenger/6.5.15 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0.1; vivo X9 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043804 Mobile Safari/537.36 MicroMessenger/6.6.1200(0x26060030) NetType/4G Language/en",
    "Mozilla/5.0 (Linux; Android 7.1.1; OPPO R11 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1200(0x26060030) NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone1 03; CPU iPhone OS 11_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0 MQQBrowser/8.0.2 Mobile/15B87 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; PE-UL00 Build/HuaweiPE-UL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.5.937 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Mobile/14E304 MicroMessenger/6.6.0 NetType/WIFI Language/zh_HK",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; HUAWEI MT7-TL10 Build/HuaweiMT7-TL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; M2 E Build/MMB29U) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.8.2.962 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.1.1; OPPO R11 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.1 baiduboxapp/10.1.0.11 (Baidu; P1 7.1.1)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Mobile/14B72 MicroMessenger/6.6.0 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 4.3; zh-CN; A0001 Build/JLS36C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.6.951 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; MI 5s Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.1.1; OPPO R11 Pluskt Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1200(0x26060030) NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; VTR-AL00 Build/HUAWEIVTR-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36 lite baiduboxapp/2.5.0.10 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; Mi Note 3 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; M5 Note Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1200(0x26060030) NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; vivo Xplay6 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.1.2; zh-cn; Redmi 5 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; OPPO R9s Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.8.2.962 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; FRD-AL00 Build/HUAWEIFRD-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.1.961 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; MI 5 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.5",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.8.2.962 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; STF-AL10 Build/HUAWEISTF-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.1 baiduboxapp/10.1.0.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-CN; ZTE Q802C Build/KTU84P) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.5.811 U3/0.8.0 Mobile Safari/534.30",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; SM-N9200 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.1.961 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; HUAWEI MLA-AL10 Build/HUAWEIMLA-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.1 baiduboxapp/10.1.0.11 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; SM-G9280 Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1440X2560",
    "Mozilla/5.0 (Linux; Android 7.0; VTR-AL00 Build/HUAWEIVTR-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.1 baiduboxapp/10.1.0.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 7.1.2; zh-cn; Redmi 4X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.10",
    "Mozilla/5.0 (Linux; Android 7.1.1; vivo X20Plus A Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.1 baiduboxapp/10.1.0.11 (Baidu; P1 7.1.1)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; EVA-AL10 Build/HUAWEIEVA-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1794",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; LA-S31 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 720X1280",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MI 6 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_1 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A403 MicroMessenger/6.5.21 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.1.2; zh-cn; MI 5X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MI 6 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.5.955 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.1.2; zh-cn; Redmi 4X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.5",
    "Mozilla/5.0 (iPhone 6; CPU iPhone OS 11_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/6.0 MQQBrowser/6.1.1 Mobile/15C114 Safari/8536.25",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; Redmi Note 4X Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; VKY-AL00 Build/HUAWEIVKY-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 5.1; OPPO R9tm Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1200(0x26060030) NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; MI NOTE Pro Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.10",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; Best sonny LT918 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.0.960 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; Mi Note 2 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; MHA-AL00 Build/HUAWEIMHA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile MQQBrowser/6.2 TBS/043722 Safari/537.36 MicroMessenger/6.6.1200(0x26060030) NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MI 5s Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.1.961 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.1.2; zh-cn; MI 5X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.10",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; OPPO R7s Build/KTU84P) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/1.0.0.100 U3/0.8.0 Mobile Safari/534.30 AliApp(TB/6.7.6) WindVane/8.0.0 1080X1800 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; ONEPLUS A3010 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.1.961 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; LEX720 Build/WAXCNFN5902606012S) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.1.961 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; KNT-AL10 Build/HUAWEIKNT-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile MQQBrowser/6.2 TBS/043722 Safari/537.36 V1_AND_SQ_7.3.2_762_YYB_D QQ/7.3.2.3350 NetType/WIFI WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; Android 6.0.1; vivo X9 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043804 Mobile Safari/537.36 MicroMessenger/6.6.1200(0x26060030) NetType/WIFI Language/en",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; HUAWEI MLA-AL10 Build/HUAWEIMLA-AL10) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; Redmi Note 4 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.1.961 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; EVA-AL10 Build/HUAWEIEVA-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.1 baiduboxapp/10.1.0.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; Android 7.0; BLN-AL40 Build/HONORBLN-AL40; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.1 baiduboxapp/10.1.0.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-CN; OPPO R7 Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.3.9) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 7.0; FRD-AL00 Build/HUAWEIFRD-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1200(0x26060030) NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; HUAWEI CRR-UL00 Build/HUAWEICRR-UL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.20 Mobile Safari/537.36 AliApp(TB/7.0.2) WindVane/8.0.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; MI NOTE LTE Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 6.0.1; OPPO R9s Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.1 baiduboxapp/10.1.0.11 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MP1512 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; VTR-AL00 Build/HUAWEIVTR-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.21 Mobile Safari/537.36 AliApp(TB/7.1.1) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MHA-AL00 Build/HUAWEIMHA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; MI 5 Build/MXB48T) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-CN; OPPO R7s Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1800",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; OPPO R9s Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2.5) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MI 5 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; HUAWEI TAG-TL00 Build/HUAWEITAG-TL00) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/1.0.0.100 U3/0.8.0 Mobile Safari/534.30 AliApp(TB/5.10.7) WindVane/8.0.0 720X1184 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; 1605-A01 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.8 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; vivo Xplay5A Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1440X2560",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; vivo X9Plus L Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; vivo X9Plus Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 7.0; PIC-AL00 Build/HUAWEIPIC-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043630 Safari/537.36 V1_AND_SQ_7.3.2_762_YYB_D QQ/7.3.2.3350 NetType/WIFI WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; Android 6.0; NEM-AL10 Build/HONORNEM-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; TRT-AL00A Build/HUAWEITRT-AL00A) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 720X1208",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; OPPO R9s Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; NCE-AL00 Build/HUAWEINCE-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 720X1208",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; Mi Note 2 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; SM-C9000 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; SM-C5000 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; STF-AL10 Build/HUAWEISTF-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 6.0; NEM-AL10 Build/HONORNEM-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; OPPO A59s Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 720X1280",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; vivo X9 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.3.9) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MI 5s Plus Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.1.961 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.1.1; vivo X9 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.0.11 (Baidu; P1 7.1.1)",
    "Mozilla/5.0 (Linux; U; Android 7.1.2; zh-CN; M6 Note Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MHA-AL00 Build/HUAWEIMHA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3.2) WindVane/8.0.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; BLN-AL10 Build/HONORBLN-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; vivo X20 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X2034",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; VIE-AL10 Build/HUAWEIVIE-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.25 Mobile Safari/537.36 AliApp(TB/7.1.3.1) WindVane/8.0.0 1080X1804",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; BTV-W09 Build/HUAWEIBEETHOVEN-W09) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1600X2560",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; HM NOTE 1LTE Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.2",
    "Mozilla/5.0 (Linux; U; Android 5.0.2; zh-CN; vivo X5M Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 720X1280",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; FRD-AL10 Build/HUAWEIFRD-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1794",
    "Mozilla/5.0 (Linux; Android 7.0; JMM-AL10 Build/HONORJMM-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.1 baiduboxapp/10.1.0.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; vivo V3Max A Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; SM-G9350 Build/NRD90M) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/1.0.0.100 U3/0.8.0 Mobile Safari/534.30 AliApp(TB/6.7.2) WindVane/8.0.0 1080X1920 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; SM-G9550 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.8.0.960 UWS/2.12.0.1 Mobile Safari/537.36 AliApp(TB/7.3.2.2) UCBS/2.11.1.1 WindVane/8.3.0 1080X2094",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; Redmi Note 3 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 8.0; ALP-AL00 Build/HUAWEIALP-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.1 baiduboxapp/10.1.0.11 (Baidu; P1 8.0.0)",
    "Mozilla/5.0 (Linux; U; Android 5.0.2; zh-CN; vivo Y35 Build/LRX21M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.0.9) WindVane/8.3.0 720X1280",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MI 5 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.8.958 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; vivo X9 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.4) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; MI 5s Plus Build/MXB48T) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OPPO R11 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 7.1.1; OPPO A73t Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 lite baiduboxapp/2.5.0.10 (Baidu; P1 7.1.1)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; DUK-AL20 Build/HUAWEIDUK-AL20) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; M5 Note Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.0 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0.0; zh-cn; PRO 6 Plus Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.1 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; EVA-TL00 Build/HUAWEIEVA-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1794",
    "Mozilla/5.0 (Linux; U; Android 5.0.2; zh-CN; SM-A5000 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 720X1280",
    "Mozilla/5.0 (Linux; U; Android 5.0; zh-CN; SM-N9008 Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; OPPO R9tm Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 4.4.4; OPPO R7s Build/KTU84P; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1200(0x26060030) NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MI MAX Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.0.960 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; OPPO R9st Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 5.0.1; zh-CN; HUAWEI GRA-TL00 Build/HUAWEIGRA-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1794",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; HUAWEI MLA-AL10 Build/HUAWEIMLA-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.1.961 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; VTR-AL00 Build/HUAWEIVTR-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2.15) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 6.0; HUAWEI CAZ-AL10 Build/HUAWEICAZ-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0.1; OPPO R9s Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043804 Mobile Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0.1; OPPO R9s Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0.1; vivo X9Plus Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043804 Mobile Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; PLK-AL10 Build/HONORPLK-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; vivo X7Plus Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.20 Mobile Safari/537.36 AliApp(TB/7.0.2) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-TW; STV100-3 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.0.1015 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1; OPPO R9m Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.1 baiduboxapp/10.1.0.11 (Baidu; P1 5.1)",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; OPPO R7sm Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1800",
    "Mozilla/5.0 (Linux; U; Android 5.0; zh-CN; PLK-TL01H Build/HONORPLK-TL01H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.21 Mobile Safari/537.36 AliApp(TB/7.1.1) WindVane/8.0.0 1080X1794",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; vivo Xplay6 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; vivo X7Plus Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; PLK-TL01H Build/HONORPLK-TL01H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; EVA-AL00 Build/HUAWEIEVA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.8.0.960 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; Le X620 Build/HEXCNFN5902606111S) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.3 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12H143 MicroMessenger/6.5.3 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; PRA-AL00X Build/HONORPRA-AL00X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043507 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Mobile/14E304 MicroMessenger/6.5.12 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; STF-AL10 Build/HUAWEISTF-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.16 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.1.2; M6 Note Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.1 baiduboxapp/10.1.0.11 (Baidu; P1 7.1.2)",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; Redmi 4 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.10",
    "Mozilla/5.0 (iPhone 6s; CPU iPhone OS 11_2_1 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0 MQQBrowser/8.0.2 Mobile/15C153 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; BND-AL10 Build/HONORBND-AL10) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; Redmi Note 4X Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile MQQBrowser/6.2 TBS/043722 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; MI 5 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.4.1",
    "Mozilla/5.0 (Linux; Android 5.1.1; MX4 Pro Build/LMY48W; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.1 baiduboxapp/10.1.0.11 (Baidu; P1 5.1.1)",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; Le X620 Build/HEXCNFN5902606111S) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.9.959 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone 91; CPU iPhone OS 11_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0 MQQBrowser/8.0.2 Mobile/15B87 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 6.0.1; SM-A5000 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; OPPO A57 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 720X1280",
    "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; WAS-AL00 Build/HUAWEIWAS-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.1 baiduboxapp/10.1.0.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OD105 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.7.8.958 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OPPO R11s Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X2016",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; BAC-AL00 Build/HUAWEIBAC-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1812",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B93 MicroMessenger/6.6.0 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; SM-C7010 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; vivo Y67 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 720X1280",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; M1 E Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; Le X620 Build/HEXCNFN5902606111S) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; SM-C7000 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; PIC-TL00 Build/HUAWEIPIC-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.6) WindVane/8.0.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; EVA-TL00 Build/HUAWEIEVA-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.20 Mobile Safari/537.36 AliApp(TB/6.11.3) WindVane/8.0.0 1080X1812 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; SM-G9350 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1.3) WindVane/8.3.0 1440X2560",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; 1505-A01 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 5.0.1; zh-CN; HUAWEI GRA-UL10 Build/HUAWEIGRA-UL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1794",
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; CVK350C Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 8.0.0; zh-CN; ALP-AL00 Build/HUAWEIALP-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.1.961 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone 6; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Version/10.0 MQQBrowser/8.0.2 Mobile/14D27 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; SM-C7000 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone 6sp; CPU iPhone OS 9_2_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 MQQBrowser/8.0.2 Mobile/13D15 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; GIONEE S10 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; ZUK Z2131 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.1.961 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.1.1; OD105 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile MQQBrowser/6.2 TBS/043722 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; vivo X7 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 6.0.1; OPPO R9s Plus Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.1 baiduboxapp/10.1.0.11 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; OPPO R9 Plusm A Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; OPPO A57 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 720X1280",
    "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; PLK-AL10 Build/HONORPLK-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.1.961 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; Coolpad 8737A Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone1 02; CPU iPhone OS 11_2_1 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0 MQQBrowser/8.0.2 Mobile/15C153 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; Le X820 Build/FEXCNFN5902812081S) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1440X2560",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1812",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_1 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C153 MicroMessenger/6.6.0 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; STF-AL10 Build/HUAWEISTF-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; vivo X9i Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MP1603 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; vivo X5L Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 720X1280",
    "Mozilla/5.0 (Linux; Android 6.0; HUAWEI VNS-TL00 Build/HUAWEIVNS-TL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.3.31.940 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.1.2; zh-CN; MI 5X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (iPhone1 02; CPU iPhone OS 11_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0 MQQBrowser/8.0.2 Mobile/15B87 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; PRO 6s Build/NMF26O) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; vivo X9s Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 7.0; MIX Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043630 Safari/537.36 V1_AND_SQ_7.3.2_762_YYB_D QQ/7.3.2.3350 NetType/WIFI WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; OPPO R9s Plus Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; HUAWEI GRA-UL10 Build/HUAWEIGRA-UL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1812",
    "Mozilla/5.0 (Linux; Android 6.0.1; OPPO R9s Plust Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B93 MicroMessenger/6.6.0 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.1 baiduboxapp/10.1.0.11 (Baidu; P1 5.1.1)",
    "Mozilla/5.0 (Linux; Android 7.1.1; OPPO R11t Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile MQQBrowser/6.2 TBS/043722 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; SM-C9000 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 5.1; OPPO R9tm Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; MI 5s Plus Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MI 5 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.1.961 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92 MicroMessenger/6.6.0 NetType/4G Language/zh_HK",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; OPPO A57t Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 720X1280",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; VTR-AL00 Build/HUAWEIVTR-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 7.1.1; vivo X9 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043630 Safari/537.36 V1_AND_SQ_7.3.2_762_YYB_D QQ/7.3.2.3350 NetType/WIFI WebP/0.3.0 Pixel/1920",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_3 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A432 baiduboxapp/0_31.1.3.8_enohpi_4331_057/3.0.11_2C2%257enohPi/1099a/1104AAA74194F3A2B88C4AF76930A0914370CA23EOCNBKLTOMJ/1",
    "Mozilla/5.0 (Linux; Android 6.0.1; SM-A7100 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; VIE-AL10 Build/HUAWEIVIE-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; vivo X9 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1.1; vivo V3Max A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.1 baiduboxapp/10.1.0.11 (Baidu; P1 7.1.1)",
    "Mozilla/5.0 (Linux; Android 5.1; H8S Build/LMY47D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4X Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043804 Mobile Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; EVA-TL00 Build/HUAWEIEVA-TL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; M5 Note Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; SM-G9350 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; Android 8.0; MHA-AL00 Build/HUAWEIMHA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 3S Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.1; CUN-AL00 Build/HUAWEICUN-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13C75 MicroMessenger/6.6.0 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4X Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.19.1140 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.1.1; OPPO R11t Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.1.1; vivo X7 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.1 baiduboxapp/10.1.0.11 (Baidu; P1 5.1.1)",
    "Mozilla/5.0 (Linux; Android 7.1.1; vivo X9 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043630 Safari/537.36 V1_AND_SQ_7.3.2_762_YYB_D QQ/7.3.2.3350 NetType/4G WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; U; Android 5.0.2; zh-CN; vivo X6A Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 7.0; MHA-AL00 Build/HUAWEIMHA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.1 baiduboxapp/10.1.0.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; MI 4LTE Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.7 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; M5 Note Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.1; vivo X6D Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.1 baiduboxapp/10.1.0.11 (Baidu; P1 5.1)",
    "Mozilla/5.0 (Linux; Android 7.0; MI 5s Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile MQQBrowser/6.2 TBS/043722 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; STF-AL10 Build/HUAWEISTF-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1.7) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; VIE-AL10 Build/HUAWEIVIE-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1794",
    "Mozilla/5.0 (iPhone 6; CPU iPhone OS 11_1_2 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0 MQQBrowser/8.0.2 Mobile/15B202 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; EVA-TL00 Build/HUAWEIEVA-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.1.961 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.0.2; zh-CN; vivo X6Plus A Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; vivo X9s Plus Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (iPhone1 03; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.2 (KHTML, like Gecko) Version/11.0 MQQBrowser/8.0.2 Mobile/15D5046b Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 7.0; SM-G9350 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.1 baiduboxapp/10.1.0.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; Android 5.1.1; vivo Xplay5A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.1 baiduboxapp/10.1.0.11 (Baidu; P1 5.1.1)",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MX6 Build/NMF26O) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.3.9) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; MI 5s Plus Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.4.1",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; vivo X9 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0.0; zh-CN; PRO 6 Plus Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.1.961 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; MI 5s Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/1.0.0.100 U3/0.8.0 Mobile Safari/534.30 AliApp(TB/6.5.1) WindVane/8.0.0 1080X1812 GCanvas/1.4.2.21",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Mobile/14D27 MicroMessenger/6.6.0 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; OPPO R9m Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_1 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C153 MicroMessenger/6.6.0 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92 MicroMessenger/6.6.0 NetType/WIFI Language/zh_HK",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 MicroMessenger/6.5.23 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; PIC-AL00 Build/HUAWEIPIC-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; vivo X7Plus Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MX6 Build/NMF26O) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; vivo X6D Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; OPPO R9sk Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; vivo X20A Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.2) WindVane/8.3.0 1080X2034",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_1_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Mobile/14B100 MicroMessenger/6.6.0 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; VIE-AL10 Build/HUAWEIVIE-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1080X1800",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; WAS-AL00 Build/HUAWEIWAS-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.2.954 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 4.4.4; OPPO R7s Build/KTU84P; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.6.0 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 8.0.0; zh-cn; STF-AL10 Build/HUAWEISTF-AL10) AppleWebKit/537.36 (KHTML, like Gecko) MQQBrowser/7.3 Chrome/37.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; DUK-AL20 Build/HUAWEIDUK-AL20) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.1.961 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; ZUK Z2121 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.8 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone 6s; CPU iPhone OS 9_2_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 MQQBrowser/8.0.1 Mobile/13D15 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; TRT-TL10A Build/HUAWEITRT-TL10A) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.0.960 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; OPPO R9 Plustm A Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 7.0; MI 5s Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.1 baiduboxapp/10.1.0.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; SM-G9500 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1080X2076",
    "Mozilla/5.0 (Linux; Android 6.0.1; vivo X9 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043804 Mobile Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/en",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; m1 metal Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 6.0; HUAWEI VNS-TL00 Build/HUAWEIVNS-TL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/45.0.2454.95 Mobile Safari/537.36 baiduboxapp/6.3.1 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MHA-AL00 Build/HUAWEIMHA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.1.961 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; STF-AL10 Build/HUAWEISTF-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; vivo X9 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 7.0; EVA-AL00 Build/HUAWEIEVA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.1 baiduboxapp/10.1.0.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; HUAWEI VNS-TL00 Build/HUAWEIVNS-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.5.955 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 8.0.0; zh-CN; BKL-AL20 Build/HUAWEIBKL-AL20) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1080X2160",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; OPPO R9m Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1.3) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 7.0; Mi-4c Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; BND-AL10 Build/HONORBND-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.0.960 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1; OPPO R9m Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile MQQBrowser/6.2 TBS/043722 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; STV100-3 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1440X2392",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; MI MAX Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 5.0.2; vivo X5Pro D Build/LRX21M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; vivo X9Plus Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.1.961 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; DUK-AL20 Build/HUAWEIDUK-AL20) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; PRO 6s Build/NMF26O) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; OPPO R9s Plus Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 6.0.1; Redmi Note 3 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MHA-TL00 Build/HUAWEIMHA-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1080X1812",
    "Mozilla/5.0 (iPhone 6p; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/6.0 MQQBrowser/6.8 Mobile/13G36 Safari/8536.25 MttCustomUA/2",
    "Mozilla/5.0 (Linux; Android 6.0; vivo Y67A Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; 1501_M02 Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.25 Mobile Safari/537.36 AliApp(TB/7.1.3) WindVane/8.0.0 720X1280",
    "Mozilla/5.0 (Linux; U; Android 7.1.2; zh-CN; MI 5X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OD103 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.1.961 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; vivo X9Plus Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; VKY-AL00 Build/HUAWEIVKY-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.1.961 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.1.961 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone 91; CPU iPhone OS 11_2_1 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0 MQQBrowser/8.0.2 Mobile/15C153 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; OD103 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1; OPPO R9t Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.1 baiduboxapp/10.1.0.11 (Baidu; P1 5.1)",
    "Mozilla/5.0 (Linux; Android 7.0; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; HUAWEI GRA-UL00 Build/HUAWEIGRA-UL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; HUAWEI CAZ-AL10 Build/HUAWEICAZ-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1080X1788",
    "Mozilla/5.0 (Linux; Android 6.0.1; HUAWEI ALE-CL00 Build/HuaweiALE-CL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 lite baiduboxapp/2.5.0.10 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; NX569H Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; 1505-A02 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.1.961 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 8.0.0; zh-cn; DUK-AL20 Build/HUAWEIDUK-AL20) AppleWebKit/537.36 (KHTML, like Gecko) MQQBrowser/7.3 Chrome/37.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.1.1; MIX 2 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 7.1.1)",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; ONEPLUS A5000 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; FRD-AL00 Build/HUAWEIFRD-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1080X1794",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; SM-G9280 Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1440X2560",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; MX6 Build/NMF26O) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; 1505-A01 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; Le X620 Build/HEXCNFN5902606111S) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; MI NOTE LTE Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OPPO R11s Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1080X2016",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; SM-G9250 Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1440X2560",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; Redmi Note 4 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; OPPO R9m Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.1.939 UCBS/2.10.1.8 Mobile Safari/537.36 AliApp(TB/6.8.5) WindVane/8.0.0 1080X1920 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; EVA-AL10 Build/HUAWEIEVA-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1080X1812",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_4 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G35 MicroMessenger/6.5.21 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; EVA-TL00 Build/HUAWEIEVA-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.4.950 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; OPPO R9m Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.14 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; Mi Note 3 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; SM-N9200 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_2 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B202 MicroMessenger/6.5.23 NetType/WIFI Language/en",
    "Mozilla/5.0 (Linux; Android 6.0.1; SM-A7100 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.5.11 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; Che1-CL10 Build/Che1-CL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.8.0.960 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; BLN-AL20 Build/HONORBLN-AL20) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; vivo X9s Plus Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; vivo Xplay5A Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1440X2560",
    "Mozilla/5.0 (iPhone 6p; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 MQQBrowser/8.0.2 Mobile/13B143 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; HUAWEI MLA-AL10 Build/HUAWEIMLA-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3.1) WindVane/8.0.0 1080X1800",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; OPPO R9tm Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OD103 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; m3 note Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.1.961 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; FRD-AL10 Build/HUAWEIFRD-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; EVA-AL00 Build/HUAWEIEVA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-CN; OPPO R7 Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; MI 5s Plus Build/MXB48T) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0.0.3723 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.0 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; EVA-TL00 Build/HUAWEIEVA-TL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; vivo X9 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.1.961 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; WAS-AL00 Build/HUAWEIWAS-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; EVA-AL10 Build/HUAWEIEVA-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Mobile/14E304 MicroMessenger/6.6.0 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.1; m1 note Build/LMY47D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.1 baiduboxapp/10.1.0.11 (Baidu; P1 5.1)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; FRD-AL10 Build/HUAWEIFRD-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.0.960 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; GN9010 Build/LMY47D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/1.0.0.100 U3/0.8.0 Mobile Safari/534.30 AliApp(TB/6.8.0) WindVane/8.0.0 720X1280 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1080X1821",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; Redmi Note 4X Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.10",
    "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; vivo Xplay3S Build/KVT49L) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1440X2560",
    "Mozilla/5.0 (Linux; Android 8.0; BKL-AL20 Build/HUAWEIBKL-AL20; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 8.0.0)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; PRA-AL00X Build/HONORPRA-AL00X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.0.960 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; PRO 6s Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; ATH-AL00 Build/HONORATH-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.21 Mobile Safari/537.36 AliApp(TB/7.1.0) WindVane/8.0.0 1080X1776",
    "Mozilla/5.0 (Linux; Android 5.1; OPPO A37m Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; HUAWEI CAZ-AL10 Build/HUAWEICAZ-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; Android 7.1.1; OPPO R11 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_3 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A432 MicroMessenger/6.6.0 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; EVA-AL10 Build/HUAWEIEVA-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; VKY-AL00 Build/HUAWEIVKY-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92 MicroMessenger/6.6.0 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.1; vivo X6D Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; MI 4LTE Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.10",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; 1605-A01 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.5.937 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1.1; 2014813 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_2 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B202 MicroMessenger/6.6.0 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.1.1; OPPO R9 Plusm A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 4.4.2; PE-TL20 Build/HuaweiPE-TL20; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile MQQBrowser/6.2 TBS/043722 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; WAS-AL00 Build/HUAWEIWAS-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043409 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; M1 E Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.9.959 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1; MX5 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile MQQBrowser/6.2 TBS/043722 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043803 Mobile Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; LON-AL00 Build/HUAWEILON-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; Mi-4c Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.10",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; SM-C7000 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.0.960 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; SM-C9000 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.8.0.960 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; KNT-AL20 Build/HUAWEIKNT-AL20) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1440X2408",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; vivo X7Plus Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OPPO R11 Plus Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.0.9) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 7.1.1; ONEPLUS A5000 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.1 baiduboxapp/10.1.0.11 (Baidu; P1 7.1.1)",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OPPO R11 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12D508 MicroMessenger/6.6.0 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; FRD-AL00 Build/HUAWEIFRD-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; FRD-AL00 Build/HUAWEIFRD-AL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; MI 5 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.1.1; vivo Xplay5A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 5.1.1)",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; PLK-TL01H Build/HONORPLK-TL01H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.0.960 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; MX5 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; PLK-TL01H Build/HONORPLK-TL01H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile MQQBrowser/6.2 TBS/043722 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_4 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G35 MicroMessenger/6.5.21 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 5.0; zh-CN; SM-N9009 Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.7.8.958 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; MI NOTE LTE Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.10",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; ZUK Z2131 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.21 Mobile Safari/537.36 AliApp(TB/7.1.0) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; vivo X9 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 UWS/2.10.2.11 Mobile Safari/537.36 AliApp(DingTalk/4.1.0) com.alibaba.android.rimet/0 Channel/700513 language/zh-CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; VIE-AL10 Build/HUAWEIVIE-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 UWS/2.10.2.11 Mobile Safari/537.36 AliApp(DingTalk/4.2.0) com.alibaba.android.rimet/0 Channel/227200 language/zh-CN",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; vivo X7 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 UWS/2.10.2.11 Mobile Safari/537.36 AliApp(DingTalk/4.1.5) com.alibaba.android.rimet/0 Channel/700513 language/zh-CN",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; vivo X9 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 UWS/2.10.2.11 Mobile Safari/537.36 AliApp(DingTalk/4.1.5) com.alibaba.android.rimet/0 Channel/700513 language/zh-CN",
    "Mozilla/5.0 (Linux; U; Android 5.0.2; zh-CN; vivo X6A Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 UWS/2.10.2.11 Mobile Safari/537.36 AliApp(DingTalk/4.1.5) com.alibaba.android.rimet/0 Channel/10003993 language/zh-CN",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; m3 note Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 UWS/2.10.2.11 Mobile Safari/537.36 AliApp(DingTalk/4.2.0) com.alibaba.android.rimet/0 Channel/228200 language/zh-CN",
    "Mozilla/5.0 (Linux; Android 6.0; PLK-AL10 Build/HONORPLK-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; PLK-AL10 Build/HONORPLK-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; vivo X9 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 7.1.1; vivo X9s Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; vivo X7 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; MI NOTE LTE Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (iPhone1 01; CPU iPhone OS 11_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0 MQQBrowser/8.0.2 Mobile/15B87 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; OPPO R9 Plusm A Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; FRD-AL00 Build/HUAWEIFRD-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1794",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; SM-C9000 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MHA-AL00 Build/HUAWEIMHA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; ZTE BA910 Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 720X1200",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C114 MicroMessenger/6.6.0 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; MI MAX 2 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.10",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; VTR-AL00 Build/HUAWEIVTR-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; BAC-AL00 Build/HUAWEIBAC-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.4) WindVane/8.3.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 5.0.2; zh-CN; vivo X6A Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; OPPO R9sk Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; OPPO R9tm Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.1.939 UCBS/2.10.1.10 Mobile Safari/537.36 AliApp(TB/6.10.3) WindVane/8.0.0 1080X1920 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; MIX Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.10",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; OPPO R9s Plus Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.4) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; HUAWEI MLA-AL10 Build/HUAWEIMLA-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1080X1800",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; vivo X20A Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.21 Mobile Safari/537.36 AliApp(TB/7.1.0) WindVane/8.0.0 1080X2034",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; PIC-AL00 Build/HUAWEIPIC-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1080X1812",
    "Mozilla/5.0 (Linux; Android 6.0.1; vivo X9 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/en",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; LON-AL00 Build/HUAWEILON-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1440X2560",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; C106 Build/ZAXCNFN5902606201S) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; VKY-AL00 Build/HUAWEIVKY-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.0.960 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; MI NOTE LTE Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/42.0.0.0 Mobile Safari/537.36 XiaoMi/MiuiBrowser/2.1.1",
    "Mozilla/5.0 (Linux; Android 6.0.1; SM-G9250 Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/7.1 baiduboxapp/8.0 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (Linux; Android 6.0; GEM-703LT Build/HUAWEIGEM-703LT; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.5.11 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; DUK-AL20 Build/HUAWEIDUK-AL20) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.0.960 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; ZUK Z2131 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.0.960 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.1.2; zh-CN; Redmi 4X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.0.960 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; MI 5 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.10",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MX6 Build/NMF26O) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; OPPO R9s Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.1) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; BAC-TL00 Build/HUAWEIBAC-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.0.9) WindVane/8.3.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; PRO 6s Build/NMF26O) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; vivo X9L Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.4) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A456 MicroMessenger/6.5.23 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; MIX 2 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; EVA-AL00 Build/HUAWEIEVA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.4) WindVane/8.3.0 1080X1794",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; MI 6 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.10 tae_sdk_a_2.1.0 AliApp(BC/2.1.0)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; EVA-TL00 Build/HUAWEIEVA-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.0.960 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; SM-G9350 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.20 Mobile Safari/537.36 AliApp(TB/7.0.2) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MHA-AL00 Build/HUAWEIMHA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.4) WindVane/8.3.0 1080X1812",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92 MicroMessenger/6.5.23 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 5.0.2; zh-CN; MI 2S Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.0.960 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; SM-G7200 Build/KTU84P) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/1.0.0.100 U3/0.8.0 Mobile Safari/534.30 AliApp(TB/6.4.3) WindVane/8.0.0 720X1280 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; SM-G9280 Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.5.943 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MX6 Build/NMF26O) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.4) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; PLK-TL01H Build/HONORPLK-TL01H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.4) WindVane/8.3.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MI MAX Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.4) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 6.0; PLK-AL10 Build/HONORPLK-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; HUAWEI RIO-UL00 Build/HUAWEIRIO-UL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1776",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; VTR-AL00 Build/HUAWEIVTR-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.8.0.960 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; EVA-AL10 Build/HUAWEIEVA-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; Mi Note 3 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.10",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; PLK-AL10 Build/HONORPLK-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.4) WindVane/8.3.0 1080X1812",
    "Mozilla/5.0 (Linux; Android 7.1.1; vivo X9 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043630 Safari/537.36 V1_AND_SQ_7.3.2_762_YYB_D QQ/7.3.2.3350 NetType/WIFI WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; Mi Note 3 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.4) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 7.0; SM-G9350 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.116 Mobile Safari/537.36 baiduboxapp/8.1 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 8.0.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; EVA-AL10 Build/HUAWEIEVA-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.4) WindVane/8.3.0 1080X1794",
    "Mozilla/5.0 (iPhone 92; CPU iPhone OS 11_0_1 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 MQQBrowser/7.6.1 Mobile/15A402 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 5.0.2; zh-cn; CHE-TL00 Build/HonorCHE-TL00) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/1.0.0.100 U3/0.8.0 Mobile Safari/534.30 AliApp(TB/6.6.4) WindVane/8.0.0 720X1280 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 7.1.2)",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; vivo X9s L Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.0.960 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1.1; OPPO R7sm Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 5.1.1)",
    "Mozilla/5.0 (Linux; Android 6.0; PLK-AL10 Build/HONORPLK-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 baiduboxapp/0_11.0.1.8_enohpi_4331_057/2.3.01_1C2%258enohPi/1099a/3E65BABDBCB50931241270A030F6C91B65A8FD4BEFCIPTCFBAK/1",
    "Mozilla/5.0 (Linux; Android 7.0; STF-AL00 Build/HUAWEISTF-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; Android 7.1.1; vivo X9i Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MHA-AL00 Build/HUAWEIMHA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.21 Mobile Safari/537.36 AliApp(TB/7.1.1) WindVane/8.0.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MI 5 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.0.960 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; vivo X20Plus A Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.4) WindVane/8.3.0 1080X2160",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; 1605-A01 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.9.959 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; OPPO R9m Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.4) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (iPhone 6p; CPU iPhone OS 8_1_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 MQQBrowser/7.4.1 Mobile/12B440 Safari/8536.25 MttCustomUA/2 QBWebViewType/1",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; MI 4LTE Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.0.960 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.0.2; en-us; PLK-AL10 Build/HONORPLK-AL10) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.3 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 8.0.0; zh-CN; ALP-AL00 Build/HUAWEIALP-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.4) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; PRO 7-S Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.4) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; MI 4LTE Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36 XiaoMi/MiuiBrowser/2.1.1",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; PLK-AL10 Build/HONORPLK-AL10) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; ONEPLUS A3000 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; SM-N950N Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.4) WindVane/8.3.0 1080X2220",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; OPPO A57 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.4) WindVane/8.3.0 720X1280",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OPPO R11 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.4) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; OPPO A57 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.3.0 720X1280",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MI NOTE Pro Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.0.960 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; FRD-AL10 Build/HUAWEIFRD-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.4) WindVane/8.3.0 1080X1794",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; vivo X9Plus Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.4) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; NX549J Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.4) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 7.0; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; Android 7.0; MHA-AL00 Build/HUAWEIMHA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile MQQBrowser/6.2 TBS/043722 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; VKY-TL00 Build/HUAWEIVKY-TL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-CN; HUAWEI G7-TL00 Build/HuaweiG7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.4) WindVane/8.3.0 720X1184",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; MIX 2 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.10",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; OPPO A59m Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.1.1; OD105 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.23 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; Mi Note 2 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.10",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; SM-G8508S Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.2 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.23 NetType/3G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13E234 MicroMessenger/6.5.23 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; FRD-AL00 Build/HUAWEIFRD-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; HUAWEI MT7-TL10 Build/HuaweiMT7-TL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 6.0)",
    "Mozilla/5.0 (iPhone 5SGLOBAL; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.0 MQQBrowser/8.0.1 Mobile/14G60 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_2 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B202 MicroMessenger/6.6.0 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Mobile/14B72 MicroMessenger/6.6.0 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; vivo V3Max A Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.4) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; VTR-AL00 Build/HUAWEIVTR-AL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; vivo X9 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 lite baiduboxapp/2.5.0.10 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (Linux; Android 7.0; MHA-AL00 Build/HUAWEIMHA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile MQQBrowser/6.2 TBS/043722 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; VTR-AL00 Build/HUAWEIVTR-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; Android 7.1.1; ONEPLUS A5000 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 7.1.1)",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; Mi-4c Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.8",
    "Mozilla/5.0 (Linux; Android 5.1; OPPO A37m Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.0.11 (Baidu; P1 5.1)",
    "Mozilla/5.0 (Linux; Android 7.0; SM-C7000 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043657 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.1.1; OPPO R11 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.1; HUAWEI TIT-AL00 Build/HUAWEITIT-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 5.1)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.0.960 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1; vivo X6D Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; HUAWEI MLA-AL10 Build/HUAWEIMLA-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.4) WindVane/8.3.0 1080X1800",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; vivo X20A Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.4) WindVane/8.3.0 1080X2160",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; MI 5 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; MI 5 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.11",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; vivo X7Plus Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.4) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; OPPO R9s Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.4) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 7.0; DLI-AL10 Build/HONORDLI-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; M5 Note Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.0.960 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; HUAWEI CAZ-AL10 Build/HUAWEICAZ-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.1.939 UCBS/2.10.1.10 Mobile Safari/537.36 AliApp(TB/6.9.7) WindVane/8.0.0 1080X1788 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.1; OPPO R9m Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 5.1)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; MI 5s Plus Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.10",
    "Mozilla/5.0 (Linux; Android 7.1.1; OPPO R11 Pluskt Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone 92; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.2.1 Mobile/14A456 Safari/8536.25 MttCustomUA/2 QBWebViewType/1",
    "Mozilla/5.0 (Linux; Android 7.1.1; OPPO R11 Pluskt Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; MI 5 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; Redmi 3S Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.10",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; Redmi 4X Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.10",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; MI 5s Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.10",
    "Mozilla/5.0 (Linux; U; Android 8.0.0; zh-cn; ONEPLUS A3010 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; HUAWEI MT7-CL00 Build/HuaweiMT7-CL00) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.2.0.661 U3/0.8.0 Mobile Safari/534.30",
    "Mozilla/5.0 (Linux; Android 6.0.1; SM-C5000 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (Linux; Android 5.0.2; vivo X6A Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 5.0.2)",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; OPPO R7sm Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.4) WindVane/8.3.0 1080X1800",
    "Mozilla/5.0 (iPhone1 02; CPU iPhone OS 11_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0 MQQBrowser/8.0.1 Mobile/15B87 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; Redmi Note 3 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.10",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; HM NOTE 1LTE Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.7.7",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; ONEPLUS A3010 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; HUAWEI CAZ-AL10 Build/HUAWEICAZ-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; BAC-AL00 Build/HUAWEIBAC-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.19.1140 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; Redmi Note 4X Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.10",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; vivo X6Plus D Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; SBM302SH Build/S0014) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; MI MAX Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.10",
    "Mozilla/5.0 (Linux; Android 5.1.1; vivo X6SPlus D Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.2 baiduboxapp/9.2.0.10 (Baidu; P1 5.1.1)",
    "Mozilla/5.0 (Linux; Android 7.1.1; vivo X9i Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone 6s; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.0 MQQBrowser/8.0.1 Mobile/14G60 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 7.0; FRD-AL00 Build/HUAWEIFRD-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.23.1180 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; WAS-AL00 Build/HUAWEIWAS-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; Android 6.0.1; MI MAX Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.4) WindVane/8.3.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; Coolpad 8297 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; Redmi Note 4 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.10",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; SM-G6100 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.4) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 5.1; ZTE Q806T Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36 baiduboxapp/5.3.5 (Baidu; P1 5.1)",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; OPPO A59s Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.4) WindVane/8.3.0 720X1280",
    "Mozilla/5.0 (Linux; Android 7.0; SM-G9500 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; EVA-AL10 Build/HUAWEIEVA-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.4) WindVane/8.3.0 1080X1812",
    "Mozilla/5.0 (Linux; Android 5.1; HUAWEI TIT-AL00 Build/HUAWEITIT-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 baiduboxapp/8.6.5 (Baidu; P1 5.1)",
    "Mozilla/5.0 (Linux; Android 6.0; CAM-TL00H Build/HONORCAM-TL00H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.0.10 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; Android 7.0; MI MAX Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 V1_AND_SQ_7.3.0_758_YYB_D QQ/7.3.0.3340 NetType/WIFI WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; LG-H961N Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.1.939 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; MI 5 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; PE-CL00 Build/HuaweiPE-CL00) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/1.0.0.100 U3/0.8.0 Mobile Safari/534.30 AliApp(TB/6.6.4) WindVane/8.0.0 1080X1776 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; Android 6.0; FRD-AL10 Build/HUAWEIFRD-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; Android 6.0; HUAWEI NXT-CL00 Build/HUAWEINXT-CL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 V1_AND_SQ_7.3.0_758_YYB_D QQ/7.3.0.3340 NetType/4G WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; MI 6 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; ZUG 5S Build/KVT49L) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.4.950 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92 MicroMessenger/6.5.23 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; Mi-4c Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; vivo X9 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.4) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; SM-G9550 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.4) WindVane/8.3.0 1080X2094",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MI 5s Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.0.960 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; HUAWEI MT7-CL00 Build/HuaweiMT7-CL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; M3X Build/MMB29U; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; vivo X6D Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.4) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (iPhone 6; CPU iPhone OS 9_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 MQQBrowser/8.0.1 Mobile/13C75 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; WAS-AL00 Build/HUAWEIWAS-AL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; EVA-AL00 Build/HUAWEIEVA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.0.960 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; NX529J Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.5 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; M5 Note Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 baiduboxapp/0_9.1.0.8_enohpi_1002_5211/2.3.9_1C2%257enohPi/1099a/8911065B8760AD22EBA1435F2B68B9E51C20FCFE9OCCRPRKPLJ/1",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; EVA-AL10 Build/HUAWEIEVA-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.7.8.958 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone 92; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.3 Mobile/14C92 Safari/8536.25 MttCustomUA/2 QBWebViewType/1",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MI 6 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.4) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; vivo X9Plus Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.0.960 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; M5 Note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; HUAWEI RIO-TL00 Build/HuaweiRIO-TL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 lite baiduboxapp/2.4.0.10 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (Linux; Android 7.0; KNT-AL20 Build/HUAWEIKNT-AL20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.0.0 MQQBrowser/6.6 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; FRD-AL00 Build/HUAWEIFRD-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.1.0.870 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; m1 metal Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.6) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; MI 6 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.8",
    "Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 5.1.1)",
    "Mozilla/5.0 (iPhone 92; CPU iPhone OS 11_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0 MQQBrowser/8.0.1 Mobile/15B87 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 7.1.1; vivo X9Plus Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 7.1.1)",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; vivo X9 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.0.960 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; PLK-AL10 Build/HONORPLK-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; vivo X9 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.0.960 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; EVA-TL00 Build/HUAWEIEVA-TL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.8 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; m3 note Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.0.960 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; vivo X7 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.4) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; vivo Y67A Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.3.7) WindVane/8.3.0 720X1280",
    "Mozilla/5.0 (Linux; Android 6.0; HUAWEI NXT-CL00 Build/HUAWEINXT-CL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 V1_AND_SQ_7.3.0_758_YYB_D QQ/7.3.0.3340 NetType/WIFI WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_3 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A432 MicroMessenger/6.5.23 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; MI MAX Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 baidubrowser/7.11.3.3 (Baidu/HAOPassion; P1 7.0)",
    "Mozilla/5.0 (Linux; Android 6.0; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043610 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; PE-UL00 Build/HuaweiPE-UL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.4) WindVane/8.3.0 1080X1776",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A456 MicroMessenger/6.5.22 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0.1; OPPO R9s Plus Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; OPPO R9 Plusm A Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.4) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; SM-G9250 Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1440X2560",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; vivo X9 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.9.959 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; VIE-AL10 Build/HUAWEIVIE-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.0.960 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 8.0; BLA-AL00 Build/HUAWEIBLA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 8.0.0)",
    "Mozilla/5.0 (Linux; Android 6.0; Redmi Note 4X Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-CN; R8107 Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.4) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 7.0; MI 5 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; HUAWEI CAZ-AL10 Build/HUAWEICAZ-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.4) WindVane/8.3.0 1080X1788",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; m3 note Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.8.0.960 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; G0215D Build/MMB29M) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.9.5.729 U3/0.8.0 Mobile Safari/534.30",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12D508 MicroMessenger/6.5.23 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; DUK-AL20 Build/HUAWEIDUK-AL20) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.4) WindVane/8.3.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; 1607-A01 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.4) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 5.1.1; vivo X7 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.4.1000 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.1.1; vivo Xplay6 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 7.1.1)",
    "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 7.1.1)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Mobile/14D27 MicroMessenger/6.5.23 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.1.1; vivo X9 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043630 Safari/537.36 V1_AND_SQ_7.3.0_758_YYB_D QQ/7.3.0.3340 NetType/WIFI WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.23 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; OPPO R9sk Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.4) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; OPPO R9s Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.0.960 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.4) WindVane/8.3.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; PRO 6s Build/NMF26O) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.0.960 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; KNT-AL10 Build/HUAWEIKNT-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.0.960 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_3 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G34 MicroMessenger/6.5.23 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 5.0.2; zh-CN; vivo X6A Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.4) WindVane/8.3.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; SM-G9350 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.1.1; MI MAX 2 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; FRD-AL10 Build/HUAWEIFRD-AL10) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 4.4.4; OPPO R7s Build/KTU84P; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.5.23 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; vivo X9 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.9.959 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; OPPO R9sk Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.21 Mobile Safari/537.36 AliApp(TB/7.1.1) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 5.1; vivo X6D Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 5.1)",
    "Mozilla/5.0 (Linux; Android 5.1; vivo X6D Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.1.1; vivo X7 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.4.1000 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.1.1; OPPO R11 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.1.1; MI MAX 2 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OPPO R11s Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.2.4) WindVane/8.3.0 1080X2016",
    "Mozilla/5.0 (iPhone 6sp; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0 MQQBrowser/8.0.1 Mobile/14C92 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (iPhone1 01; CPU iPhone OS 11_1_2 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0 MQQBrowser/8.0.0 Mobile/15B202 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 5.1; OPPO R9t Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 5.1)",
    "Mozilla/5.0 (Linux; Android 7.0; SM-G9350 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36 MicroMessenger/6.5.23 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MI 6 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.8.0.960 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; MI 6 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.10",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; KIW-TL00 Build/HONORKIW-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1776",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; vivo X6D Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 7.1.1; OPPO R11s Plus Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 lite baiduboxapp/2.5.0.10 (Baidu; P1 7.1.1)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_2 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B202 MicroMessenger/6.5.14 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_2 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B202 MicroMessenger/6.5.14 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.5.23 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; SM-G9550 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X2094",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; OPPO R11 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; Mi Note 2 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.5",
    "Mozilla/5.0 (Linux; Android 7.1.1; OPPO R11 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-CN; OPPO R7s Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1800",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; OPPO R9tm Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.9.959 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone 91; CPU iPhone OS 11_1_2 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0 MQQBrowser/7.9.0 Mobile/15B202 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; SM-N9200 Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.20 Mobile Safari/537.36 AliApp(TB/6.11.3) WindVane/8.0.0 1440X2560 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; VKY-AL00 Build/HUAWEIVKY-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 5.0.2; GN9006 Build/LRX21M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 5.0.2)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; DUK-AL20 Build/HUAWEIDUK-AL20) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.8",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; Redmi 3 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.9.959 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone 91; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.0 MQQBrowser/8.0.1 Mobile/14G60 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 6.0.1; MI NOTE LTE Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone 91; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.2.1 Mobile/14C92 Safari/8536.25 MttCustomUA/2 QBWebViewType/1",
    "Mozilla/5.0 (Linux; Android 4.4.4; SM-G5309W Build/KTU84P; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.5.11 (Baidu; P1 4.4.4)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; MIX Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.8",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; EVA-AL10 Build/HUAWEIEVA-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.9.959 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; EVA-AL10 Build/HUAWEIEVA-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.1; OPPO A59s Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 V1_AND_SQ_7.2.0_730_YYB_D QQ/7.2.0.3270 NetType/WIFI WebP/0.3.0 Pixel/720",
    "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 V1_AND_SQ_7.3.0_758_YYB_D QQ/7.3.0.3340 NetType/WIFI WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 3S Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 V1_AND_SQ_7.3.0_758_YYB_D QQ/7.3.0.3340 NetType/WIFI WebP/0.3.0 Pixel/720",
    "Mozilla/5.0 (Linux; Android 6.0.1; MI 4LTE Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 V1_AND_SQ_7.2.5_744_YYB_D QQ/7.2.5.3305 NetType/WIFI WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12D508 baiduboxapp/0_7.0.2.8_enohpi_069_046/2.8_1C2%254enohPi/1099a/A2A3CEE02CCCA22C0AEB53520AD5C8D7728947654ONLJAHGSCP/1",
    "Mozilla/5.0 (Linux; Android 6.0; M5 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.7.1041 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B93 MicroMessenger/6.5.22 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; VIE-AL10 Build/HUAWEIVIE-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C114 MicroMessenger/6.5.23 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; MHA-AL00 Build/HUAWEIMHA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile MQQBrowser/6.2 TBS/043722 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0.1; vivo Y66 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_2 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B202 MicroMessenger/6.5.23 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_2 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B202 MicroMessenger/6.5.9 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; HUAWEI CAZ-AL10 Build/HUAWEICAZ-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1788",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_2 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B202 MicroMessenger/6.5.23 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; OPPO R9s Plus Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 8.0.0; zh-CN; ONEPLUS A3000 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.6.946 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.1.2; zh-cn; Redmi 5A Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.5",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; PRA-AL00 Build/HONORPRA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.9.959 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.22 NetType/2G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; HUAWEI GRA-UL10 Build/HUAWEIGRA-UL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; Android 6.0; M621C Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; EVA-AL00 Build/HUAWEIEVA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1794",
    "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-CL00 Build/HuaweiMT7-CL00) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 UCBrowser/9.4.1.362 U3/0.8.0 Mobile Safari/533.1",
    "Mozilla/5.0 (iPhone 84; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.0 MQQBrowser/8.0.1 Mobile/14G60 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; WAS-AL00 Build/HUAWEIWAS-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; Le X620 Build/HEXCNFN5902606111S) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; vivo X9i Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; Redmi Note 4 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; Redmi Note 4X Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 V1_AND_SQ_7.3.0_758_YYB_D QQ/7.3.0.3340 NetType/WIFI WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MI 6 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-CN; R8107 Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; MI 5 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.8",
    "Mozilla/5.0 (iPhone1 01; CPU iPhone OS 11_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0 MQQBrowser/8.0.1 Mobile/15B87 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 6.0; EVA-TL00 Build/HUAWEIEVA-TL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.7.1041 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; OPPO R9m Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.1.939 UCBS/2.10.1.10 Mobile Safari/537.36 AliApp(TB/6.10.3) WindVane/8.0.0 1080X1920 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; vivo Xplay5S Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1440X2560",
    "Mozilla/5.0 (Linux; Android 6.0.1; OPPO R9s Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (Linux; Android 6.0; PLK-TL01H Build/HONORPLK-TL01H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.1.2; zh-cn; Redmi 4X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.8",
    "Mozilla/5.0 (Linux; U; Android 5.0; zh-CN; SM-N9008V Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; OPPO R9m Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3.1) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; MP1512 Build/MRA58K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/1.0.0.100 U3/0.8.0 Mobile Safari/534.30 AliApp(TB/6.8.0) WindVane/8.0.0 1080X1920 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; Android 7.0; ZUK Z2121 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; vivo X20A Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X2034",
    "Mozilla/5.0 (Linux; Android 7.1.1; OD105 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; EVA-AL10 Build/HUAWEIEVA-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1794",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; HUAWEI M2-801W Build/HUAWEIM2-801W) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.7.957 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; vivo X9 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; PRA-AL00X Build/HONORPRA-AL00X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 720X1184",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; DOOV L525 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 720X1280",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; Redmi 4 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; Le X620 Build/HEXCNFN5601304221S) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; MI 5s Plus Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.8",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; A51 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 720X1280",
    "Mozilla/5.0 (Linux; Android 6.0.1; vivo X9 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; vivo Y67L Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 720X1280",
    "Mozilla/5.0 (Linux; Android 7.0; SM-C7000 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043657 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0.1; vivo X9Plus Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; HUAWEI CAZ-TL10 Build/HUAWEICAZ-TL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.1.939 UCBS/2.10.1.8 Mobile Safari/537.36 AliApp(TB/6.8.5) WindVane/8.0.0 1080X1788 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MIX 2 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.9.959 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.0.2; zh-CN; vivo X5Pro V Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; vivo X9i Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.9.959 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.1.2; zh-cn; MI 5X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.8",
    "Mozilla/5.0 (Linux; Android 5.1.1; vivo Y51A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 5.1.1)",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; HUAWEI CAZ-TL10 Build/HUAWEICAZ-TL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1788",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; VKY-AL00 Build/HUAWEIVKY-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; MI 5s Plus Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.5",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; EVA-DL00 Build/HUAWEIEVA-DL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1794",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; ONEPLUS A3010 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; SM-G9300 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 5.1.1; SM-G9280 Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.0.10 (Baidu; P1 5.1.1)",
    "Mozilla/5.0 (Linux; Android 7.0; KNT-AL20 Build/HUAWEIKNT-AL20; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; BAC-AL00 Build/HUAWEIBAC-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 720X1208",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; FRD-AL10 Build/HUAWEIFRD-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1794",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MHA-AL00 Build/HUAWEIMHA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.9.959 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; LON-AL00 Build/HUAWEILON-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1440X2560",
    "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; HUAWEI MT7-CL00 Build/HuaweiMT7-CL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-CN; CHM-CL00 Build/CHM-CL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.21 Mobile Safari/537.36 AliApp(TB/7.1.0) WindVane/8.0.0 720X1280",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; MI 4LTE Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 6.0; EVA-AL10 Build/HUAWEIEVA-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; OPPO R9tm Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MP1602 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; OPPO R9sk Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; HUAWEI NXT-TL00 Build/HUAWEINXT-TL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; DUK-AL20 Build/HUAWEIDUK-AL20) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.9.959 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; HUAWEI VNS-AL00 Build/HUAWEIVNS-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.2.936 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; EVA-AL10 Build/HUAWEIEVA-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; MI NOTE LTE Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 7.1.1; MIX 2 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 lite baiduboxapp/2.5.0.10 (Baidu; P1 7.1.1)",
    "Mozilla/5.0 (iPhone 6s; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 MQQBrowser/8.0.1 Mobile/14E304 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; m2 note Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; ZTE BV0720T Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 720X1280",
    "Mozilla/5.0 (Linux; U; Android 5.0.2; zh-CN; vivo X6Plus A Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 6.0; DIG-AL00 Build/HUAWEIDIG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; SM-G9508 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X2076",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OPPO R11 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; MI MAX Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.5",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MI 5 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; HM 2A Build/KTU84Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.8",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; M5 Note Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.9.959 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A456 MicroMessenger/6.5.22 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; VTR-AL00 Build/HUAWEIVTR-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.9.959 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92 MicroMessenger/6.5.23 NetType/WIFI Language/zh_HK",
    "Mozilla/5.0 (Linux; U; Android 8.0.0; zh-CN; ALP-AL00 Build/HUAWEIALP-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.9.959 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone 6; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 MQQBrowser/8.0.1 Mobile/12H143 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 7.1.1; OPPO R11 Pluskt Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; OPPO A59m Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 720X1280",
    "Mozilla/5.0 (Linux; Android 7.0; VKY-AL00 Build/HUAWEIVKY-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; SM-A9000 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; ONEPLUS A3000 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.9.959 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.1.939 UCBS/2.10.1.10 Mobile Safari/537.36 AliApp(TB/6.10.10) WindVane/8.0.0 720X1184 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; SLA-AL00 Build/HUAWEISLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.9.959 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1.1; NX523J_V1 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.1 baidubrowser/7.16.12.0 (Baidu; P1 5.1.1)",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; vivo X20A Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X2160",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12A365 MicroMessenger/6.5.23 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MP1603 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MHA-AL00 Build/HUAWEIMHA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; NX512J Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.8.958 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; PRO 6 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 V1_AND_SQ_7.2.5_744_YYB_D QQ/7.2.5.3305 NetType/WIFI WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; Android 6.0.1; SM-C7010 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 V1_AND_SQ_6.7.0_496_YYB_D QQ/6.7.0.3095 NetType/WIFI WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; Android 7.1.1; GIONEE M7L Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043630 Safari/537.36 V1_AND_SQ_7.2.5_744_YYB_D QQ/7.2.5.3305 NetType/WIFI WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; Android 5.1.1; vivo X7Plus Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.0.11 (Baidu; P1 5.1.1)",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; vivo Xplay6 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.1.939 UCBS/2.10.1.8 Mobile Safari/537.36 AliApp(TB/6.8.6) WindVane/8.0.0 1080X1920 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; vivo X9Plus Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MP1503 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.21 Mobile Safari/537.36 AliApp(TB/7.1.1) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; OPPO R9s Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; DUK-AL20 Build/HUAWEIDUK-AL20) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 5.0.2; zh-CN; MI 2S Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.7.8.958 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.0.2; zh-CN; vivo X5Pro D Build/LRX21M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.25 Mobile Safari/537.36 AliApp(TB/7.1.3) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1812",
    "Mozilla/5.0 (Linux; Android 7.0; BLN-AL20 Build/HONORBLN-AL20; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; EVA-AL10 Build/HUAWEIEVA-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (iPhone 6; CPU iPhone OS 11_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0 MQQBrowser/8.0.1 Mobile/15B87 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; vivo V3Max A Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (iPhone 91; CPU iPhone OS 11_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0 MQQBrowser/8.0.1 Mobile/15B87 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 6.0; Le X620 Build/HEXCNFN5902606111S; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 V1_AND_SQ_7.1.5_708_YYB_D QQ/7.1.5.3215 NetType/WIFI WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; Android 6.0.1; MI 5s Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (Linux; Android 6.0; HUAWEI MLA-AL10 Build/HUAWEIMLA-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.2 baiduboxapp/9.2.0.10 (Baidu; P1 6.0)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92 MicroMessenger/6.5.22 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; LG-H990 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.25 Mobile Safari/537.36 AliApp(TB/7.1.3) WindVane/8.0.0 1440X2392",
    "Mozilla/5.0 (Linux; Android 5.1.1; Redmi Note 3 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; HUAWEI GRA-UL00 Build/HUAWEIGRA-UL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.1.1; OPPO R9 Plustm A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 5.1.1)",
    "Mozilla/5.0 (iPhone 6p; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.0 MQQBrowser/8.0.1 Mobile/14G60 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 7.0; FRD-AL00 Build/HUAWEIFRD-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; PRA-AL00X Build/HONORPRA-AL00X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; Pixel 2 XL Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.8.958 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1; vivo X6Plus D Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.16.1120 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.1.1; vivo X7 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36 MicroMessenger/6.5.22 NetType/2G Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B93 MicroMessenger/6.5.22 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone 92; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0 MQQBrowser/8.0.1 Mobile/14C92 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 6.0; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.3.27.880 NetType/ctlte Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_2_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13D15 MicroMessenger/6.5.22 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; F100S Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.3.23.840 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.0.2; vivo Y51A Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; DIG-AL00 Build/HUAWEIDIG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.16.1120 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; MP1512 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; MI 5s Plus Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (iPhone 6; CPU iPhone OS 9_0_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 MQQBrowser/7.1 Mobile/13A404 Safari/8536.25 MttCustomUA/2",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; MI 5s Plus Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; VIE-AL10 Build/HUAWEIVIE-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.8.958 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 4.4.2; CHM-TL00H Build/HonorCHM-TL00H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 V1_AND_SQ_7.2.5_744_YYB_D QQ/7.2.5.3305 NetType/4G WebP/0.3.0 Pixel/720",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13E234 baiduboxapp/0_9.1.0.8_enohpi_1002_5211/3.9_2C2%258enohPi/1099a/CC0A181123A1A7924AAB7534622EBF207830F0566OCRKQDHAKQ/1",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; VTR-AL00 Build/HUAWEIVTR-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 7.1.1; XT1650-05 Build/NCC26.118-31-1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 V1_AND_SQ_7.1.0_692_YYB_D QQ/7.1.0.3175 NetType/4G WebP/0.3.0 Pixel/1440",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; LEX626 Build/HEXCNFN5902606111S) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; vivo X6S A Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; ONEPLUS A5000 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 5.0.2; zh-cn; MI 2SC Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.8",
    "Mozilla/5.0 (iPhone 91; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0 MQQBrowser/8.0.1 Mobile/14C92 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 6.0; KNT-UL10 Build/HUAWEIKNT-UL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; Android 7.0; FRD-AL00 Build/HUAWEIFRD-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.0.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; NX563J Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.20 Mobile Safari/537.36 AliApp(TB/6.11.3) WindVane/8.0.0 1080X1920 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; EVA-AL10 Build/HUAWEIEVA-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1812",
    "Mozilla/5.0 (Linux; Android 5.1.1; vivo Y51t L Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; SM-G9300 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 5.0.2; zh-CN; Redmi Note 2 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; VTR-AL00 Build/HUAWEIVTR-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 720X1280",
    "Mozilla/5.0 (Linux; Android 6.0.1; vivo X9 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 4.4.2; PE-TL20 Build/HuaweiPE-TL20; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; PLK-TL01H Build/HONORPLK-TL01H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 UWS/2.10.2.11 Mobile Safari/537.36 AliApp(DingTalk/4.1.0) com.alibaba.android.rimet/0 Channel/227200 language/zh-CN",
    "Mozilla/5.0 (iPhone 6s; CPU iPhone OS 11_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0 MQQBrowser/8.0.1 Mobile/15B87 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OPPO R11 Plus Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; OPPO R9m Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; ONEPLUS A5000 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.8 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1776",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MP1602 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.20 Mobile Safari/537.36 AliApp(TB/6.11.3) WindVane/8.0.0 1080X1920 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; Android 7.0; STF-AL10 Build/HUAWEISTF-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.0.0 MQQBrowser/6.6 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; FRD-AL10 Build/HUAWEIFRD-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; HUAWEI MLA-AL10 Build/HUAWEIMLA-AL10) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; BAC-AL00 Build/HUAWEIBAC-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 7.1.2; zh-cn; M6 Note Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; vivo V3Max A Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (iPhone 6sp; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 MQQBrowser/8.0.1 Mobile/13G36 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; vivo X20A Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X2034",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; HUAWEI M2-A01L Build/HUAWEIM2-A01L) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.9.959 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone 6p; CPU iPhone OS 11_0_3 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 MQQBrowser/8.0.0 Mobile/15A432 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-CN; HM 2A Build/KTU84Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.20 Mobile Safari/537.36 AliApp(TB/7.0.2) WindVane/8.0.0 720X1280",
    "Mozilla/5.0 (Linux; Android 6.0; NEM-AL10 Build/HONORNEM-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; H60-L01 Build/HDH60-L01) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/1.0.0.100 U3/0.8.0 Mobile Safari/534.30 AliApp(TB/6.2.4) WindVane/8.0.0 1080X1776 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; U; Android 5.0.2; zh-CN; vivo Y35 Build/LRX21M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 720X1280",
    "Mozilla/5.0 (Linux; Android 5.1; OPPO R9km Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 5.1)",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; Mi Note 3 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.8.958 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; Redmi Note 4X Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 7.0; BAC-AL00 Build/HUAWEIBAC-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; SUGAR S9 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.1.939 UCBS/2.10.1.8 Mobile Safari/537.36 AliApp(TB/6.8.6) WindVane/8.0.0 1080X1812 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; KNT-AL10 Build/HUAWEIKNT-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.0.953 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-CN; OPPO R7 Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 6.0.1; vivo X9 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/en",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; OPPO A53m Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; HUAWEI CRR-CL00 Build/HUAWEICRR-CL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; VKY-AL00 Build/HUAWEIVKY-AL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; EVA-TL00 Build/HUAWEIEVA-TL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; vivo X7 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0.0; zh-cn; PRO 6 Plus Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; HUAWEI NXT-TL00 Build/HUAWEINXT-TL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MHA-AL00 Build/HUAWEIMHA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.3) WindVane/8.0.0 1080X1821",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; SM-G9006V Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 5.0.2; zh-CN; vivo Y51 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 540X960",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; Redmi 3X Build/MMB29M) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.9.3.727 U3/0.8.0 Mobile Safari/534.30",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; SLA-AL00 Build/HUAWEISLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 720X1208",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; OPPO R9sk Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; HUAWEI GRA-TL00 Build/HUAWEIGRA-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1812",
    "Mozilla/5.0 (iPhone 6; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.0 MQQBrowser/8.0.1 Mobile/14F89 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; x600 Build/ABXCNOP5902605181S) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; vivo Y66 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 720X1280",
    "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; vivo Xplay3S Build/KVT49L) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1440X2560",
    "Mozilla/5.0 (iPhone 6sp; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.0 MQQBrowser/8.0.0 Mobile/14G60 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; KIW-UL00 Build/HONORKIW-UL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.1.939 UCBS/2.10.1.10 Mobile Safari/537.36 AliApp(TB/6.10.3) WindVane/8.0.0 1080X1776 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; Android 7.0; MHA-AL00 Build/HUAWEIMHA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.5.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; SM-G9200 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1440X2560",
    "Mozilla/5.0 (Linux; Android 6.0; NEM-AL10 Build/HONORNEM-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; BLN-AL10 Build/HONORBLN-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; WAS-AL00 Build/HUAWEIWAS-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.27 Mobile Safari/537.36 AliApp(TB/7.2.1.8) WindVane/8.0.0 1080X1812",
    "Mozilla/5.0 (iPhone 6sp; CPU iPhone OS 11_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0 MQQBrowser/8.0.1 Mobile/15B87 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A456 baiduboxapp/0_11.0.0.8_enohpi_6311_046/2.0.01_2C2%256enohPi/1099a/E31908639055967BD5F95388314C057E49F72F6E5FCFRJDEECQ/1",
    "Mozilla/5.0 (Linux; Android 7.0; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.1 baidubrowser/7.16.12.0 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; vivo X6SPlus D Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.8.958 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; vivo X20A Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X2160",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; 1605-A01 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.1.939 UCBS/2.10.1.10 Mobile Safari/537.36 AliApp(TB/6.9.7) WindVane/8.0.0 1080X1920 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; HUAWEI MLA-AL10 Build/HUAWEIMLA-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1800",
    "Mozilla/5.0 (Linux; U; Android 5.0.2; zh-cn; vivo Y51A Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; OPPO A57 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.0.11 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.9.959 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; PIC-AL00 Build/HUAWEIPIC-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1812",
    "Mozilla/5.0 (iPhone 6sp; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.7.1 Mobile/14G60 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; VIE-AL10 Build/HUAWEIVIE-AL10) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_1_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Mobile/14B100 MicroMessenger/6.5.22 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OPPO R11 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.21 Mobile Safari/537.36 AliApp(TB/7.1.1) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; OPPO R7sm Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1800",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; OPPO R11t Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; FRD-AL00 Build/HUAWEIFRD-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; MHA-AL00 Build/HUAWEIMHA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.0.10 (Baidu; P1 7.0)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A456 MicroMessenger/6.5.19 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; FRD-AL10 Build/HUAWEIFRD-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.9.959 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; F105 Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.6 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1; vivo X6D Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/en",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_2 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B202 MicroMessenger/6.5.22 NetType/4G Language/zh_TW",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; OPPO A57t Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 720X1280",
    "Mozilla/5.0 (Linux; Android 7.1.1; vivo X9 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; vivo X9i Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 5.1.1; OPPO R9 Plusm A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 V1_AND_SQ_7.2.5_744_YYB_D QQ/7.2.5.3305 NetType/WIFI WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; Android 6.0; Redmi Note 4 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.0.11 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; Android 6.0; Redmi Note 4 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 V1_AND_SQ_7.2.5_744_YYB_D QQ/7.2.5.3305 NetType/WIFI WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; Android 7.0; PIC-AL00 Build/HUAWEIPIC-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.5.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-CN; vivo Y27 Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 720X1280",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; vivo Y67 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.21 Mobile Safari/537.36 AliApp(TB/7.1.0) WindVane/8.0.0 720X1280",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; SM-G9200 Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.0) WindVane/8.0.0 1440X2560",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_1_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12B436 MicroMessenger/6.5.22 NetType/3G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; HUAWEI CAZ-TL10 Build/HUAWEICAZ-TL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1788",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; MI NOTE LTE Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI P7-L07 Build/HuaweiP7-L07) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.20 Mobile Safari/537.36 AliApp(TB/6.11.3) WindVane/8.0.0 1080X1776 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; Android 6.0; PLK-TL01H Build/HONORPLK-TL01H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.1.1; vivo X9i Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.1.1; vivo X9 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043630 Safari/537.36 V1_AND_SQ_7.2.5_744_YYB_D QQ/7.2.5.3305 NetType/WIFI WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; vivo X9Plus Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.9.959 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.1.1; OPPO R11 Pluskt Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.1.1; ONEPLUS A5000 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.0.0 MQQBrowser/6.6 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone 6sp; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/6.0 MQQBrowser/6.8.1 Mobile/14G60 Safari/8536.25 MttCustomUA/2",
    "Mozilla/5.0 (Linux; Android 6.0; M5 Note Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; OPPO R9s Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.9.959 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; EVA-AL10 Build/HUAWEIEVA-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-CN; vivo Y27 Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TM/7.2.0) WindVane/8.0.0 T-UA=android_7.2.0_720x1280_600129 TMANDROID/600129@tmall_android_7.2.0",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; Mi Note 2 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.8",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; Letv X501 Build/DAXCNCU5902605181S) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; PRA-AL00X Build/HONORPRA-AL00X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.9.959 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; MI 5s Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_2 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A421 MicroMessenger/6.5.22 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; FRD-AL10 Build/HUAWEIFRD-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.1.939 UCBS/2.10.1.8 Mobile Safari/537.36 AliApp(TB/6.8.5) WindVane/8.0.0 1080X1794 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; Android 6.0.1; vivo X9i Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.0.12 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (Linux; Android 7.0; MI 5s Plus Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.0.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; Redmi 4X Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 720X1280",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; Redmi Note 4X Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; DUK-AL20 Build/HUAWEIDUK-AL20; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; vivo X7Plus Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.1.939 UCBS/2.10.1.10 Mobile Safari/537.36 AliApp(TB/6.10.10) WindVane/8.0.0 1080X1920 GCanvas/1.4.2.21",
    "Mozilla/5.0 (iPhone 6sp; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Version/10.0 MQQBrowser/8.0.1 Mobile/14D27 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 7.0.0; zh-CN; PRO 6 Plus Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1440X2560",
    "Mozilla/5.0 (Linux; Android 7.0; PRA-AL00X Build/HONORPRA-AL00X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 baiduboxapp/5.0 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; PRO 5 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MP1603 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.1.939 UCBS/2.10.1.10 Mobile Safari/537.36 AliApp(TB/6.10.2) WindVane/8.0.0 1080X1920 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MI MAX Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OPPO R11 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1.1) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 6.0.1; vivo X9 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.16.1120 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone 6s; CPU iPhone OS 11_1_2 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0 MQQBrowser/8.0.0 Mobile/15B202 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 7.0; FRD-AL10 Build/HUAWEIFRD-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.1.1; vivo V3Max A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/1.0.0.100 U3/0.8.0 Mobile Safari/534.30 AliApp(TB/6.7.6) WindVane/8.0.0 1080X1776 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; EVA-AL10 Build/HUAWEIEVA-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1794",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; SM-C5000 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; ONEPLUS A5000 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; vivo Xplay6 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1440X2560",
    "Mozilla/5.0 (Linux; Android 7.1.1; OPPO R11s Plus Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/4G Language/en",
    "Mozilla/5.0 (Linux; Android 7.0; MI 5s Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; HUAWEI CAZ-AL10 Build/HUAWEICAZ-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1788",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; F100L Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.1.939 UWS/2.11.0.7 Mobile Safari/537.36 AliApp(TB/6.11.0) UCBS/2.11.1.1 WindVane/8.0.0 720X1280 GCanvas/1.4.2.21",
    "Mozilla/5.0 (iPhone 6p; CPU iPhone OS 8_1_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 MQQBrowser/8.0.1 Mobile/12B436 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 5.0; zh-CN; vivo X5Pro D Build/LRX21M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 5.0.1; zh-CN; HUAWEI GRA-CL10 Build/HUAWEIGRA-CL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1794",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; vivo X6S A Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; SM-G9300 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; BLN-AL40 Build/HONORBLN-AL40) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1812",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_2 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B202 baiduboxapp/0_01.5.2.8_enohpi_4331_057/2.1.11_1C2%259enohPi/1099a/42A2BCE504692B8B5FAEA6243671EE417BEFE9FD3FCNNTFTJAK/1",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; LON-AL00 Build/HUAWEILON-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1440X2560",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MHA-AL00 Build/HUAWEIMHA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; m3 note Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.9.959 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; OPPO R9km Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Mobile/14E304 baiduboxapp/0_01.0.4.8_enohpi_8022_2421/1.3.01_1C2%257enohPi/1099a/28A011AE63362CBFC8B227A1EB56F6215CDDBBBE2FRKQFLPIQE/1",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OPPO R11 Plus Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (iPhone 99; CPU iPhone OS 99 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.6.0 Mobile/14E304 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; vivo X7 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; ONEPLUS A3000 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.3 Mobile Safari/537.36",
    "Xiaomi_MAT136_TD-LTE/V1 Linux/3.18.24 Android/6.0 Release/3.3.2017 Browser/AppleWebKit537.36 Mobile Safari/537.36 System/Android 6.0 XiaoMi/MiuiBrowser/2.4.9",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; MI 5 Build/MXB48T) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 5.0; zh-cn; SM-N9008 Build/LRX21V) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/1.0.0.100 U3/0.8.0 Mobile Safari/534.30 AliApp(TB/6.5.3) WindVane/8.0.0 1080X1920 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; Redmi 3 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OPPO R11t Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; PLK-TL01H Build/HONORPLK-TL01H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; OPPO R9s Plus Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; TRT-AL00 Build/HUAWEITRT-AL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; vivo X9 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; VTR-AL00 Build/HUAWEIVTR-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MX5 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; HUAWEI MLA-AL00 Build/HUAWEIMLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1800",
    "Mozilla/5.0 (Linux; Android 7.1.1; vivo X9i Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; TRT-AL00A Build/HUAWEITRT-AL00A) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; OPPO R9m Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; MI 4LTE Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; VTR-AL00 Build/HUAWEIVTR-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; vivo X9Plus L Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 7.0; KNT-AL10 Build/HUAWEIKNT-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; KIW-UL00 Build/HONORKIW-UL00) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/1.0.0.100 U3/0.8.0 Mobile Safari/534.30 AliApp(TB/6.5.3) WindVane/8.0.0 1080X1776 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; U; Android 5.0; zh-CN; SM-N9008 Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; VIE-AL10 Build/HUAWEIVIE-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1794",
    "Mozilla/5.0 (Linux; Android 6.0; DIG-AL00 Build/HUAWEIDIG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MI 6 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; PRO 5 Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; EVA-AL10 Build/HUAWEIEVA-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.9.959 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; SM-A9000 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.21 Mobile Safari/537.36 AliApp(TB/7.1.1) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; Redmi Note 3 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.5",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; SM-A9000 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; EVA-DL00 Build/HUAWEIEVA-DL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.1.939 UCBS/2.10.1.10 Mobile Safari/537.36 AliApp(TB/6.10.8) WindVane/8.0.0 1080X1794 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; U; Android 5.0.2; zh-CN; vivo X5Pro D Build/LRX21M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.20 Mobile Safari/537.36 AliApp(TB/7.0.2) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; OPPO A57 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 720X1280",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; vivo X7Plus Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-CN; OPPO R7t Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.0.953 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OPPO R11 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.9.959 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; M5 Note Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; EVA-DL00 Build/HUAWEIEVA-DL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1794",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; SM-G9350 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.0) WindVane/8.0.0 1440X2560",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OPPO A77 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MI 5s Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MIX 2 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X2030",
    "Mozilla/5.0 (iPhone 91; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.0 MQQBrowser/8.0.0 Mobile/14G60 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; vivo X9 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; vivo V3 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; vivo X9 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-CN; A0001 Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.7.957 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MP1701 Build/NMF26O) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; PRA-TL10 Build/HONORPRA-TL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; CAM-AL00 Build/HONORCAM-AL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; BAC-AL00 Build/HUAWEIBAC-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1812",
    "Mozilla/5.0 (Linux; Android 7.1.2; MI 5X Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.5.19.1140 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MHA-AL00 Build/HUAWEIMHA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.0) WindVane/8.0.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MI 6 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.0) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; 1607-A01 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 4.4.2; PE-TL10 Build/HuaweiPE-TL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.19.1140 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; vivo X6L Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OPPO R11 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; OPPO R9s Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; M5 Note Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; SM-G9350 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.1.939 UCBS/2.10.1.10 Mobile Safari/537.36 AliApp(TB/6.10.10) WindVane/8.0.0 1080X1920 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; STF-AL10 Build/HUAWEISTF-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; VKY-AL00 Build/HUAWEIVKY-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.9.959 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; SLA-AL00 Build/HUAWEISLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 720X1208",
    "Mozilla/5.0 (Linux; Android 7.1.1; OPPO R11 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; KNT-UL10 Build/HUAWEIKNT-UL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.0) WindVane/8.0.0 1080X1806",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; OPPO A59s Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 720X1280",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; SM-C7000 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; Redmi 4 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; OPPO R9st Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 5.0.2; zh-CN; HTC D826w Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1776",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; NX549J Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.9.959 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 4.4.2; PE-TL10 Build/HuaweiPE-TL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.19.1140 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone 91; CPU iPhone OS 11_1_2 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0 MQQBrowser/8.0.0 Mobile/15B202 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; SM-G9300 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.5 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; HUAWEI CRR-UL00 Build/HUAWEICRR-UL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 V1_AND_SQ_7.1.8_718_YYB_D QQ/7.1.8.3240 NetType/4G WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-CN; R8207 Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 720X1280",
    "Mozilla/5.0 (Linux; U; Android 7.1.2; zh-CN; M6 Note Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.6) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 7.0; MHA-AL00 Build/HUAWEIMHA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; MI 5 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.2",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OPPO R11st Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X2016",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; vivo X6Plus D Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; vivo X9 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.1.939 UCBS/2.10.1.10 Mobile Safari/537.36 AliApp(TB/6.10.10) WindVane/8.0.0 1080X1920 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; vivo Y66 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 720X1280",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; FRD-AL10 Build/HUAWEIFRD-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1794",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; vivo X6S A Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; VKY-AL00 Build/HUAWEIVKY-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.0) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 2.3; zh-CN; MI-ONEPlus) AppleWebKit/534.13 (KHTML, like Gecko) UCBrowser/8.6.0.199 U3/0.8.0 Mobile Safari/534.13",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; VKY-AL00 Build/HUAWEIVKY-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 5.0.2; zh-cn; vivo Y51A Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; SM-G9200 Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.9.959 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.0.2; zh-CN; vivo Y35 Build/LRX21M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 720X1280",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; vivo V3Max A Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; PRA-AL00X Build/HONORPRA-AL00X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1812",
    "Mozilla/5.0 (Linux; Android 6.0; HUAWEI MLA-AL10 Build/HUAWEIMLA-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; MI 6 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.2",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; OPPO R9tm Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.1) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; MP1709 Build/NMF26O) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Mobile/14E277 MicroMessenger/6.5.14 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0.1; SM-C5000 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; HUAWEI P8max Build/HUAWEIDAV-703L; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; Redmi 4 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.2.0) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; OPPO R9tm Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; Redmi 4 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.2",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_2 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B202 baiduboxapp/0_71.0.3.8_enohpi_1002_5211/2.1.11_2C2%259enohPi/1099a/C773022FBD7E74DD145F10CD98885F4E43045A16EOCAJSCFSIG/1",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; HLJ6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 720X1280",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; vivo X20A Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7.10) WindVane/8.0.0 1080X2034",
    "Mozilla/5.0 (Linux; Android 5.1.1; PLE-703L Build/HuaweiMediaPad; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.0.11 (Baidu; P1 5.1.1)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.22 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.1.2; zh-CN; MI 5X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.8.958 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; SM-G9550 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X2076",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; ATH-AL00 Build/HONORATH-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.5.1) WindVane/8.0.0 1080X1776",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_2 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B202 MicroMessenger/6.5.22 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 4.4.4; OPPO R7s Build/KTU84P; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0.1; vivo X9Plus Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0.1; vivo X9Plus Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; EVA-AL00 Build/HUAWEIEVA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1794",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; Redmi Note 4X Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; PRA-AL00X Build/HONORPRA-AL00X) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; MI PAD Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.7.7",
    "Mozilla/5.0 (iPhone 92; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0 MQQBrowser/8.0.0 Mobile/15B150 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (iPhone 6p; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 MQQBrowser/8.0.0 Mobile/14E304 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.5.11 (Baidu; P1 5.1)",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; Redmi 4X Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; OPPO A59m Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 720X1280",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-CN; OPPO R7s Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1800",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; EDI-AL10 Build/HUAWEIEDISON-AL10) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-CN; SM-E7000 Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.8.958 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Mobile/14D27 MicroMessenger/6.5.14 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0.1; vivo X9 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/en",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; ZTE A2017 Build/NMF26V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone 5; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 MQQBrowser/7.2.1 Mobile/11D257 Safari/8536.25",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; HUAWEI MLA-AL10 Build/HUAWEIMLA-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1800",
    "Mozilla/5.0 (Linux; U; Android 7.1.2; zh-cn; MI 5X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.1 tae_sdk_a_2.1.0 AliApp(BC/2.1.0)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_2 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B202 MicroMessenger/6.5.13 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; Redmi Note 4X Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.8",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; vivo X9s L Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.5.955 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; MI MAX 2 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.2",
    "Mozilla/5.0 (Linux; Android 7.1.1; MI MAX 2 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 V1_AND_SQ_7.1.0_0_TIM_D TIM2.0/2.0.1.1720 QQ/6.5.5  NetType/WIFI WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; U; Android 7.1.2; zh-cn; MI 5X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.1",
    "Mozilla/5.0 (Linux; Android 6.0; M5 Note Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.19.1140 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 V1_AND_SQ_7.2.5_744_YYB_D QQ/7.2.5.3305 NetType/WIFI WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; Android 6.0; PLK-AL10 Build/HONORPLK-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 8.0.0; zh-CN; ALP-AL00 Build/HUAWEIALP-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.2.954 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone 6p; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 MQQBrowser/8.0.0 Mobile/13B143 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 5.1; m1 note Build/LMY47D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 V1_AND_SQ_7.2.0_730_YYB_D QQ/7.2.0.3270 NetType/4G WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; Android 7.1.1; ONEPLUS A5000 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.1 baidubrowser/7.16.12.0 (Baidu; P1 7.1.1)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; DUK-AL20 Build/HUAWEIDUK-AL20) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.8.958 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.1.1; ONEPLUS A5000 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 V1_AND_SQ_7.1.8_718_YYB_D QQ/7.1.8.3240 NetType/WIFI WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_3 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A432 search%2F1.0 baiduboxapp/0_0.0.2.7_enohpi_8022_2421/3.0.11_2C2%258enohPi/1099a/E45349801E2DA062C66A2B67D1063CCA3F80520CDORHQTBKLEQ/1",
    "Mozilla/5.0 (Linux; Android 7.0; SM-G9300 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 V1_AND_SQ_7.2.5_744_YYB_D QQ/7.2.5.3305 NetType/4G WebP/0.3.0 Pixel/1440",
    "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 V1_AND_SQ_7.2.5_744_YYB_D QQ/7.2.5.3305 NetType/4G WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; Android 5.0.2; Redmi Note 3 Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 V1_AND_SQ_7.2.5_744_YYB_D QQ/7.2.5.3305 NetType/WIFI WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; Android 6.0.1; OPPO R9s Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 V1_AND_SQ_7.2.5_744_YYB_D QQ/7.2.5.3305 NetType/WIFI WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.22 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; FRD-AL00 Build/HUAWEIFRD-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 V1_AND_SQ_7.2.5_744_YYB_D QQ/7.2.5.3305 NetType/4G WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; U; Android 7.1.2; zh-cn; MI 5C Build/N2G47J) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.8",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; PLK-TL01H Build/HONORPLK-TL01H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.21 Mobile Safari/537.36 AliApp(TB/7.1.0) WindVane/8.0.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; Redmi 4 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 7.0; PRA-AL00X Build/HONORPRA-AL00X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.0.0 MQQBrowser/6.6 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; VTR-AL00 Build/HUAWEIVTR-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 720X1280",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; HTC_M8x Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1776",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; BAC-AL00 Build/HUAWEIBAC-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.20 Mobile Safari/537.36 AliApp(TB/7.0.2) WindVane/8.0.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; vivo X9 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 7.0; PIC-TL00 Build/HUAWEIPIC-TL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.0.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; M5 Note Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; OPPO R9s Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.8.958 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; BAC-AL00 Build/HUAWEIBAC-AL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; MI 5s Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.2",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A403 rabbit%2F1.0 baiduboxapp/0_0.0.0.7_enohpi_4331_057/1.0.01_1C2%258enohPi/1099a/FC9BC311FDAD46E5DA4454B9E670A2B1AE3ED2126ORRLCFABJM/1",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; PRO 6 Build/NMF26O) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; EVA-TL00 Build/HUAWEIEVA-TL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.0.11 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; Android 6.0; FRD-AL10 Build/HUAWEIFRD-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.0.11 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; vivo X9 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.6.956 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; ASUS_X018DC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.5.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; SM-G9200 Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1440X2560",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; M578CE Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.7 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone 92; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.9.0 Mobile/14G60 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; ONEPLUS A3010 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 5.0.2; zh-CN; vivo X6A Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OPPO R11 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; FRD-AL10 Build/HUAWEIFRD-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.8.958 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; EVA-AL10 Build/HUAWEIEVA-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.0.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; Android 6.0.1; SM-G9250 Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.19.1140 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; MI MAX 2 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.8",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; VKY-AL00 Build/HUAWEIVKY-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.8.958 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.0.2; zh-CN; Redmi Note 3 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.8.958 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; VKY-AL00 Build/HUAWEIVKY-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.0.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92 MicroMessenger/6.5.22 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.1; HUAWEI TIT-AL00 Build/HUAWEITIT-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.0.11 (Baidu; P1 5.1)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.22 NetType/4G Language/zh_TW",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12H143 MicroMessenger/6.5.18 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.5.22 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; VIE-AL10 Build/HUAWEIVIE-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.19.1140 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; vivo X7 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; ATH-AL00 Build/HONORATH-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.8.958 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; VIE-AL10 Build/HUAWEIVIE-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.0.11 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; Android 7.1.1; OPPO R11 Pluskt Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OPPO R11t Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; SM-C5000 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; EVA-DL00 Build/HUAWEIEVA-DL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.1.939 UCBS/2.10.1.10 Mobile Safari/537.36 AliApp(TB/6.9.5) WindVane/8.0.0 1080X1812 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; Android 6.0; M5 Note Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.22.1140 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; EVA-TL00 Build/HUAWEIEVA-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.8.958 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; VIE-AL10 Build/HUAWEIVIE-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.2 baiduboxapp/9.2.0.10 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; Android 6.0; KNT-UL10 Build/HUAWEIKNT-UL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.0.11 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; Android 6.0; NEM-AL10 Build/HONORNEM-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92 MicroMessenger/6.5.22 NetType/WIFI Language/zh_HK",
    "Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.0.11 (Baidu; P1 5.1.1)",
    "Mozilla/5.0 (Linux; Android 7.0; BAC-AL00 Build/HUAWEIBAC-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.0.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_2 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B202 MicroMessenger/6.5.22 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; VKY-AL00 Build/HUAWEIVKY-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.19.1140 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; vivo Y67 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; vivo X7Plus Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1.1; vivo Y51A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.0.11 (Baidu; P1 5.1.1)",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; MI NOTE LTE Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.8",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; OPPO R7sm Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1800",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MHA-AL00 Build/HUAWEIMHA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; OPPO R9s Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.25 Mobile Safari/537.36 AliApp(TB/7.1.3.2) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; MI 5s Build/MXB48T) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 5.0.2; zh-CN; vivo X6Plus A Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.5.955 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; vivo X7Plus Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.5.1) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MI 6 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; vivo X20A Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X2034",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; BAC-AL00 Build/HUAWEIBAC-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.21 Mobile Safari/537.36 AliApp(TB/7.1.1) WindVane/8.0.0 1080X1812",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; VIE-AL10 Build/HUAWEIVIE-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1794",
    "Mozilla/5.0 (Linux; Android 4.4.2; HM NOTE 1TD Build/KOT49H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 V1_AND_SQ_7.1.8_718_YYB_D QQ/7.1.8.3240 NetType/WIFI WebP/0.3.0 Pixel/720",
    "Mozilla/5.0 (Linux; Android 7.0; STF-AL00 Build/HUAWEISTF-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.19.1140 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; PRA-AL00X Build/HONORPRA-AL00X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.19.1140 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; PRA-AL00X Build/HONORPRA-AL00X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.0.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; Le X620 Build/HEXCNFN5902606111S) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.4.8) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; vivo Y51A Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 540X960",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; OPPO A37m Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.6) WindVane/8.0.0 720X1280",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 rabbit%2F1.0 baiduboxapp/0_0.1.1.7_enohpi_4331_057/2.3.9_2C2%257enohPi/1099a/9F1BE02FBB400C7CA1FD0E70F54EFDED8772E75C9FRMTQJJFKA/1",
    "Mozilla/5.0 (Linux; Android 6.0.1; OPPO R9s Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.0.11 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; ATH-AL00 Build/HONORATH-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1776",
    "Mozilla/5.0 (Linux; Android 7.0; STF-AL10 Build/HUAWEISTF-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.5.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; PLK-TL01H Build/HONORPLK-TL01H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1812",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_2 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B202 MicroMessenger/6.5.7 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.1.2; zh-cn; OPPO R11 Plus Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.11",
    "Mozilla/5.0 (Linux; U; Android 7.1.2; zh-CN; OPPO R11 Plus Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.8.958 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; U20 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.19.1140 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; ONEPLUS A5000 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.1.2; M6 Note Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.19.1140 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.1.2; zh-CN; M6 Note Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (iPhone 91; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.6.0 Mobile/14G60 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; PRA-AL00X Build/HONORPRA-AL00X) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 4.4.4; SM-G5309W Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/7.0 baidubrowser/7.0.26.205 (Baidu; P1 4.4.4)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; MI 5s Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; OPPO R9m Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-CN; OPPO R7 Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.1.939 UCBS/2.10.1.10 Mobile Safari/537.36 AliApp(TB/6.10.3) WindVane/8.0.0 1080X1920 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; U; Android 8.0.0; zh-CN; ALP-AL00 Build/HUAWEIALP-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.8.958 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone1 01; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0 MQQBrowser/7.9.0 Mobile/15B150 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 7.1.2; zh-cn; Redmi 4X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.8",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; MI NOTE LTE Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1812",
    "Mozilla/5.0 (Linux; Android 6.0; HUAWEI CAZ-AL10 Build/HUAWEICAZ-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 5.0.2; zh-CN; vivo X6Plus A Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 4.4.2; H60-L01 Build/HDH60-L01; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.5.11 (Baidu; P1 4.4.2)",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; OPPO R9 Plusm A Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MHA-AL00 Build/HUAWEIMHA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.8.958 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; MP1602 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.0.10 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; Android 7.1.1; vivo X9s Plus L Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.0.11 (Baidu; P1 7.1.1)",
    "Mozilla/5.0 (Linux; Android 6.0; M5 Note Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.19.1140 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.1.2; zh-CN; Redmi 4X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.8.958 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13B143 search%2F1.0 baiduboxapp/0_21.0.6.7_enohpi_8022_2421/1.9_2C2%258enohPi/1099a/3AE9D7C067B01211B3CB7EB8C57BCC73933E2D5B0FCBHSRHDCA/1",
    "Mozilla/5.0 (Linux; Android 7.1.2; MI 5X Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 lite baiduboxapp/2.5.0.10 (Baidu; P1 7.1.2)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.8.958 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; MI MAX Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.2",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12B411 MicroMessenger/6.5.22 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone 6; CPU iPhone OS 8_1_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 MQQBrowser/7.6.1 Mobile/12B440 Safari/8536.25 MttCustomUA/2 QBWebViewType/1",
    "Mozilla/5.0 (Linux; Android 7.0; BLN-AL10 Build/HONORBLN-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.1 baidubrowser/7.16.12.0 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; Android 7.0; KNT-UL10 Build/HUAWEIKNT-UL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.0.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; KNT-UL10 Build/HUAWEIKNT-UL10) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone 6p; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0 MQQBrowser/7.9.0 Mobile/15B150 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 MicroMessenger/6.5.21 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; HUAWEI MT7-TL10 Build/HuaweiMT7-TL10) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.5.22 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; PLK-AL10 Build/HONORPLK-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.19.1140 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.5.22 NetType/3G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.0.11 (Baidu; P1 7.1.1)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; PRA-TL10 Build/HONORPRA-TL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.0.953 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; FRD-AL00 Build/HUAWEIFRD-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.19.1140 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 MicroMessenger/6.5.22 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 baiduboxapp/0_01.5.2.8_enohpi_6311_046/2.3.01_1C2%259enohPi/1099a/6352308ACA4574E687E28C854F5D613ACADD05EF5FRTOJKMFFD/1",
    "Mozilla/5.0 (iPhone 6p; CPU iPhone OS 11_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0 MQQBrowser/7.9.0 Mobile/15B93 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_3 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A432 MicroMessenger/6.5.22 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.5.22 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone 6; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.9.0 Mobile/14G60 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 7.0; HUAWEI MLA-AL10 Build/HUAWEIMLA-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 lite baiduboxapp/2.5.0.10 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; Android 5.1; OPPO R9m Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.0.11 (Baidu; P1 5.1)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; TRT-AL00A Build/HUAWEITRT-AL00A) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.6.4) WindVane/8.0.0 720X1208",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.5.22 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone 91; CPU iPhone OS 11_0_2 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 MQQBrowser/7.9.0 Mobile/15A421 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; OPPO R9s Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 6.0.1; MIX Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 V1_AND_SQ_7.2.5_744_YYB_D QQ/7.2.5.3305 NetType/WIFI WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.5.21 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; STF-AL00 Build/HUAWEISTF-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.6) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Mobile/14D27 MicroMessenger/6.5.22 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; MP1611 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 lite baiduboxapp/2.4.0.10 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; Android 6.0; HUAWEI NXT-TL00 Build/HUAWEINXT-TL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.1 baiduboxapp/9.1.0.12 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; Android 7.1.1; OPPO R11 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.19.1140 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone 6p; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 MQQBrowser/7.9.0 Mobile/13B143 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (iPhone 92; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.9.0 Mobile/14D27 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 6.0.1; MI 5s Plus Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.0.11 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (iPhone 5; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.9.0 Mobile/14G60 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; EVA-TL00 Build/HUAWEIEVA-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.7.957 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.0.2; zh-cn; Letv X500 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.5.7",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-TW; A31 Build/KTU84P) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.0.8.855 U3/0.8.0 Mobile Safari/534.30",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; vivo X9 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.8 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; Redmi Note 4X Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; vivo Y67A Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Mobile Safari/537.36 lite baiduboxapp/2.2.1 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.7.957 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; vivo X9Plus Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.7.957 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MX6 Build/NMF26O) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.7.957 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; MHA-AL00 Build/HUAWEIMHA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.19.1140 NetType/WIFI Language/zh_CN",
    "Xiaomi_MDT2_TD-LTE/V1 Linux/3.18.31 Android/7.1 Release/5.15.2017 Browser/AppleWebKit537.36 Mobile Safari/537.36 System/Android 7.1 XiaoMi/MiuiBrowser/8.7.7",
    "Mozilla/5.0 (Linux; Android 6.0.1; SM-G9250 Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/7.4 baiduboxapp/8.1 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; SM-C5000 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.8 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; SM-G9209 Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.5.955 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1; OPPO A59s Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.1 baidubrowser/7.16.12.0 (Baidu; P1 5.1)",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; HUAWEI CRR-UL00 Build/HUAWEICRR-UL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/6.6 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; MIX Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 V1_AND_SQ_7.2.5_744_YYB_D QQ/7.2.5.3305 NetType/4G WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; Android 6.0; KNT-AL10 Build/HUAWEIKNT-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.0.11 (Baidu; P1 6.0)",
    "Mozilla/5.0 (iPhone 6s; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.9.0 Mobile/14F89 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 6.0; EVA-AL10 Build/HUAWEIEVA-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.0.11 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; Android 7.0; MHA-AL00 Build/HUAWEIMHA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.0.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92 MicroMessenger/6.5.21 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.1.1; vivo X9 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 V1_AND_SQ_7.2.5_744_YYB_D QQ/7.2.5.3305 NetType/4G WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; MI 6 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.1",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MIX Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.8.958 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; LON-AL00 Build/HUAWEILON-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.0.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; MI 5s Plus Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.8",
    "Mozilla/5.0 (Linux; Android 7.1.1; vivo X9i Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.19.1140 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_3 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G34 rabbit%2F1.0 baiduboxapp/0_7.0.5.7_enohpi_4331_057/3.3.9_2C2%257enohPi/1099a/E3CFBAE6CAD4E6084B479AFB1B5B1A47C15292191FCRHOQTCAP/1",
    "Mozilla/5.0 (Linux; Android 6.0.1; vivo X9 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.19.1140 NetType/WIFI Language/en",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; HUAWEI NXT-TL00 Build/HUAWEINXT-TL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 4.4.4; HM NOTE 1LTE Build/KTU84P; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36",
    "(Linux; Android 4.4.4; HM NOTE 1S-MIUI 7.1 Build/KTU84P; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 4.4.4; HM NOTE 1S-MIUI 7.1 Build/KTU84P; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.20 Mobile Safari/537.36 AliApp(TB/7.0.2) WindVane/8.0.0 1080X1776",
    "Mozilla/5.0 (Linux; Android 6.0; DIG-TL10 Build/HUAWEIDIG-TL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.5.11 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; Android 7.0; HUAWEI MLA-AL10 Build/HUAWEIMLA-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.0.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; Android 7.0; FRD-AL00 Build/HUAWEIFRD-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.19.1140 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.21 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone 91; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0 MQQBrowser/7.9.0 Mobile/15B150 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 6.0.1; SM-C7000 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.19.1140 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92 MicroMessenger/6.5.21 NetType/4G Language/zh_HK",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; SM919 Build/MXB48T) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.7 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone 6sp; CPU iPhone OS 11_0_2 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 MQQBrowser/7.9.0 Mobile/15A421 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 baiduboxapp/0_01.5.2.8_enohpi_8022_2421/3.3.01_2C2%258enohPi/1099a/FFA68BE5116410BF5A90204F49EAC7E31EA2C3C25OCAPQGSEDP/1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_1_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Mobile/14B100 MicroMessenger/6.5.21 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.1.1; OPPO R11 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/10.0 baiduboxapp/10.0.0.11 (Baidu; P1 7.1.1)",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; OPPO R9 Plusm A Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.6) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; HUAWEI MLA-AL10 Build/HUAWEIMLA-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.6) WindVane/8.0.0 1080X1800",
    "Mozilla/5.0 (Linux; Android 7.0; EVA-AL10 Build/HUAWEIEVA-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile MQQBrowser/6.2 TBS/043715 Safari/537.36 V1_AND_SQ_7.1.5_708_YYB_D PA QQ/7.1.5.3215 NetType/WIFI WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; VTR-TL00 Build/HUAWEIVTR-TL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone 6s; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.9.0 Mobile/14E304 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; SM-G9350 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.7.957 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_2_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13D15 MicroMessenger/6.5.15 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.3.31 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; MI 5s Plus Build/MXB48T) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.7.957 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MI 6 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.7.957 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; HUAWEI MLA-AL10 Build/HUAWEIMLA-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; FRD-AL10 Build/HUAWEIFRD-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.7.957 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.3.31 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B93 MicroMessenger/6.5.21 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.1.2; zh-cn; OPPO R11 Plus Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.8",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; VKY-AL00 Build/HUAWEIVKY-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.7.957 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; PE-CL00 Build/HuaweiPE-CL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.7.957 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; M5 Note Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.7.957 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; m2 note Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/6.2 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92 MicroMessenger/6.5.14 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; MI 5 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.1",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; MX4 Pro Build/LMY48W) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MI 6 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.6.956 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; en-us; ONEPLUS A3000 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; Mi-4c Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.8",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_3 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G34 MicroMessenger/6.5.21 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone 5SGLOBAL; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.9.0 Mobile/14G60 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 7.1.1; MX6 Build/NMF26O; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.5.11 (Baidu; P1 7.1.1)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; EVA-AL10 Build/HUAWEIEVA-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.6) WindVane/8.0.0 1080X1794",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; EVA-AL00 Build/HUAWEIEVA-AL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.1.1; vivo X9 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 V1_AND_SQ_7.2.5_744_YYB_D QQ/7.2.5.3305 NetType/WIFI WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; HUAWEI NXT-TL00 Build/HUAWEINXT-TL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.7 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.1.1; OPPO R11 Pluskt Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.19.1140 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; MI 6 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.8 tae_sdk_a_2.1.0 AliApp(BC/2.1.0)",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MIX 2 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.6) WindVane/8.0.0 1080X2030",
    "Mozilla/5.0 (Linux; Android 6.0; NEM-AL10 Build/HONORNEM-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MP1512 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.6) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_1 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A402 MicroMessenger/6.5.21 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0.1; NX549J Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 baiduboxapp/9.0.0.10 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; VIE-AL10 Build/HUAWEIVIE-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.7.957 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.21 NetType/4G Language/zh_TW",
    "Mozilla/5.0 (Linux; Android 7.0; DUK-AL20 Build/HUAWEIDUK-AL20; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.19.1140 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone1 03; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0 MQQBrowser/7.9.0 Mobile/15B150 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; vivo X9s Plus Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 MicroMessenger/6.5.21 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MP1701 Build/NMF26O) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.21 Mobile Safari/537.36 AliApp(TB/7.1.1) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 4.4.4; OPPO R7 Build/KTU84P; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.0.10 (Baidu; P1 4.4.4)",
    "Mozilla/5.0 (Linux; Android 7.1.2; MI 5X Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.19.1140 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 8.0.0; zh-CN; ALP-AL00 Build/HUAWEIALP-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.7.957 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; SM-G9350 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; OPPO A59s Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.6) WindVane/8.0.0 720X1280",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.5.21 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.1.2; OPPO R11 Plus Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.5.11 (Baidu; P1 7.1.2)11.7.5.955",
    "Mozilla/5.0 (Linux; Android 7.1.2; OPPO R11 Plus Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.5.11 (Baidu; P1 7.1.2)",
    "Mozilla/5.0 (Linux; U; Android 7.1.2; zh-CN; OPPO R11 Plus Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.5.955 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; BAC-AL00 Build/HUAWEIBAC-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043610 Safari/537.36 MicroMessenger/6.5.16.1120 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; BAC-AL00 Build/HUAWEIBAC-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043610 Safari/537.36 V1_AND_SQ_7.2.5_744_YYB_D QQ/7.2.5.3305 NetType/WIFI WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; Android 6.0.1; KIW-AL10 Build/HONORKIW-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.0.0 MQQBrowser/6.6 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; HUAWEI VNS-AL00 Build/HUAWEIVNS-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 baiduboxapp/6.3.1 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; OPPO R9m Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.7.957 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.1.1; vivo X9i Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.16.1120 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; MI 5 Build/MXB48T) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; BLN-AL10 Build/HONORBLN-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.5.943 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; EVA-TL00 Build/HUAWEIEVA-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.6) WindVane/8.0.0 1080X1794",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; MP1512 Build/MRA58K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/1.0.0.100 U3/0.8.0 Mobile Safari/534.30 AliApp(TB/6.5.0) WindVane/8.0.0 1080X1920 GCanvas/1.4.2.21",
    "Mozilla/5.0 (Linux; Android 5.0.2; Redmi Note 2 Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 V1_AND_SQ_7.2.5_744_YYB_D QQ/7.2.5.3305 NetType/WIFI WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OPPO R9s Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.6) WindVane/8.0.0 1080X1920",
    "Mozilla/5.0 (Linux; Android 5.0; F303 Build/LRX21M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.4.1000 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone 91; CPU iPhone OS 11_0_3 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 MQQBrowser/7.9.0 Mobile/15A432 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92 MicroMessenger/6.5.21 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0.1; Redmi Note 3 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.16.1120 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; Redmi Pro Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.8",
    "Mozilla/5.0 (Linux; Android 6.0.1; OPPO R9s Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.19.1140 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 4.4.4; MI 4LTE Build/KTU84P; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 V1_AND_SQ_7.2.5_744_YYB_D QQ/7.2.5.3305 NetType/WIFI WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; Android 7.1.1; ONEPLUS A3010 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 V1_AND_SQ_7.1.0_692_YYB_D QQ/7.1.0.3175 NetType/4G WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; Android 6.0; HUAWEI CAZ-AL10 Build/HUAWEICAZ-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043610 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone 6sp; CPU iPhone OS 11_0_3 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 MQQBrowser/7.9.0 Mobile/15A432 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; 1505-A02 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.0.953 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; 1505-A02 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.16.1120 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; SM-G9500 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.5.955 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; vivo X9 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.16.1120 NetType/WIFI Language/en",
    "Mozilla/5.0 (iPhone 6; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 MQQBrowser/7.9.0 Mobile/13B143 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 5.1.1; vivo X7 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.16.1120 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_3 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A432 baiduboxapp/0_01.5.2.8_enohpi_4331_057/3.0.11_1C2%259enohPi/1099a/6F0EEC41311DC618BE4F12BD5CE9C9F62019DFA6FORTICGARGP/1",
    "Mozilla/5.0 (Linux; Android 6.0; M5 Note Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.10.1080 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; MI PAD 3 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Safari/537.36 T7/9.3 baiduboxapp/9.3.5.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; Android 5.1.1; ATH-AL00 Build/HONORATH-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043610 Safari/537.36 MicroMessenger/6.5.16.1120 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_1 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A402 MicroMessenger/6.5.21 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; SM-G9350 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.4.950 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; EVA-AL00 Build/HUAWEIEVA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.16.1120 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; MI 5 Build/MXB48T) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.8",
    "Mozilla/5.0 (Linux; Android 7.0; HUAWEI MLA-AL10 Build/HUAWEIMLA-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.5.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; Android 7.1.1; vivo X9i Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.16.1120 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; MIX Build/MXB48T) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.1.2; zh-cn; MI 5X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.8",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12H321 rabbit%2F1.0 baiduboxapp/0_0.0.9.6_enohpi_4331_057/1.4.8_2C2%257enohPi/1099a/7A45581F380667E30AAA2C5E932D4C50A08E48B99ORRBEKHMDF/1",
    "Mozilla/5.0 (Linux; Android 5.1; M3s Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.127 Mobile Safari/537.36 UCBrowser/11.0.4.842 U3/0.8.0",
    "Mozilla/5.0 (Linux; Android 6.0; Letv X500 Build/DAXCNCU5902605181S; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.5.11 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MIX 2 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.6.956 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; FRD-AL00 Build/HUAWEIFRD-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.2.954 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; SM-C5000 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.5.11 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B93 MicroMessenger/6.5.21 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 4.4.2; HUAWEI MT7-CL00 Build/HuaweiMT7-CL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/7.4 baiduboxapp/8.1 (Baidu; P1 4.4.2)",
    "Mozilla/5.0 (Linux; Android 7.1.1; OS105 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.16.1120 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; H60-L01 Build/HDH60-L01) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.6.956 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; VIE-AL10 Build/HUAWEIVIE-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.6.956 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; FRD-AL10 Build/HUAWEIFRD-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.16.1120 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; EVA-DL00 Build/HUAWEIEVA-DL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043610 Safari/537.36 V1_AND_SQ_7.2.5_744_YYB_D QQ/7.2.5.3305 NetType/WIFI WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 MicroMessenger/6.5.19 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; M5 Note Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.16.1120 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.1.1; ONEPLUS A3010 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.16.1120 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone 6s; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 MQQBrowser/7.9.0 Mobile/15A372 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 6.0.1; vivo X9 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043610 Safari/537.36 MicroMessenger/6.5.19.1120 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.1.1; MI MAX 2 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.16.1120 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone 6s; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.9.0 Mobile/14D27 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 7.0; BND-AL10 Build/HONORBND-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.19.1120 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; vivo V3 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.1.2; zh-cn; MI 5X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.11",
    "Mozilla/5.0 (Linux; Android 7.0; HUAWEI NXT-TL00 Build/HUAWEINXT-TL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.5.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A346 MicroMessenger/6.5.4 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0.1; M836 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043520 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12B411 MicroMessenger/6.3.31 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; SM-G9200 Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.6.956 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone 91; CPU iPhone OS 11_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0 MQQBrowser/7.9.0 Mobile/15B93 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; MIX 2 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.8",
    "Mozilla/5.0 (Linux; Android 6.0.1; OPPO R9st Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.5.11 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (Linux; Android 7.1.1; OD105 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.16.1120 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; FRD-AL00 Build/HUAWEIFRD-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.6.956 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; Le X620 Build/HEXCNFN5902606111S; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.16.1120 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; FRD-AL00 Build/HUAWEIFRD-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.16.1120 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; PLK-TL01H Build/HONORPLK-TL01H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; PLK-AL10 Build/HONORPLK-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.16.1120 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_3 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A432 MicroMessenger/6.5.21 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; MHA-AL00 Build/HUAWEIMHA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.16.1120 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.16.1120 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; EVA-TL00 Build/HUAWEIEVA-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.6.951 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 5.0.2; zh-cn; Redmi Note 2 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.85 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.1.6",
    "Mozilla/5.0 (Linux; Android 6.0; EVA-AL10 Build/HUAWEIEVA-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043611 Safari/537.36 V1_AND_SQ_7.2.5_744_YYB_D QQ/7.2.5.3305 NetType/WIFI WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13C75 search%2F1.0 baiduboxapp/0_0.0.0.7_enohpi_4331_057/2.9_1C2%258enohPi/1099a/D8F39AE87FDA57C4BDFFAD4D00874BDA3860FC5ACFRMOPESIIM/1",
    "Mozilla/5.0 (Linux; Android 6.0.1; Redmi Note 3 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.5.16.1120 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; CHM-CL00 Build/CHM-CL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/8.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.1.1; vivo X9s Plus L Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.5.11 (Baidu; P1 7.1.1)",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; 2014812 Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.9.1",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; DUK-AL20 Build/HUAWEIDUK-AL20) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.6.956 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 MicroMessenger/6.5.15 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; EVA-TL00 Build/HUAWEIEVA-TL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; EVA-TL00 Build/HUAWEIEVA-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.6.956 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone 6s; CPU iPhone OS 11_0_3 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 MQQBrowser/7.9.0 Mobile/15A432 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_1_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Mobile/14B100 baiduboxapp/0_11.0.1.8_enohpi_1002_5211/1.1.01_2C2%259enohPi/1099a/30193750FD8A79577E82B753FBA176D1665D212DAFRTOGGKHMS/1",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MI MAX Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.6.956 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; BAC-AL00 Build/HUAWEIBAC-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.6.956 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; VTR-AL00 Build/HUAWEIVTR-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 lite baiduboxapp/2.4.0.10 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; Redmi Note 3 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.6.956 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_3 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A432 MicroMessenger/6.5.19 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone 6; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.9.0 Mobile/14F89 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; Mi Note 2 Build/MXB48T) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.0.3",
    "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 MicroMessenger/6.5.16.1120 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 wxwork/2.1.3 MicroMessenger/6.3.22",
    "Mozilla/5.0 (Linux; Android 6.0.1; KIW-AL10 Build/HONORKIW-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; vivo X9s Plus Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.5.955 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; SM-C5000 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.4 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; ATH-AL00 Build/HONORATH-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.5.11 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; MIX 2 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.0",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; ATH-AL00 Build/HONORATH-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.6.956 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone 6sp; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.9.0 Mobile/14C92 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; m3 note Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.6.956 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1; OPPO R9tm Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.16.1120 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0.1; SM-C7000 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.16.1120 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_1_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12B436 baiduboxapp/0_6.0.0.8_enohpi_4331_057/1.1.8_2C2%257enohPi/1001867b/00C0941C12BE72FD43E5882E0EE74C10D86D3A89FFRQGJIJFGJ/1",
    "Mozilla/5.0 (Linux; Android 7.1.1; vivo X9s Plus Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.5.11 (Baidu; P1 7.1.1)",
    "Mozilla/5.0 (Linux; Android 7.0; VKY-AL00 Build/HUAWEIVKY-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.16.1120 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; PLK-TL01H Build/HONORPLK-TL01H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043610 Safari/537.36 MicroMessenger/6.5.8.1060 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; ATH-AL00 Build/HONORATH-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.5.955 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; WAS-AL00 Build/HUAWEIWAS-AL00) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.1.0.870 U3/0.8.0 Mobile Safari/534.30",
    "Mozilla/5.0 (Linux; Android 7.0; M1 E Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.5.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; Hisense A2 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.7 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.0.2; vivo X6A Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.16.1120 NetType/4G Language/en",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; M5 Note Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.6.956 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 baiduboxapp/0_01.0.4.8_enohpi_8022_2421/2.3.9_1C2%257enohPi/1099a/1434680245B3075EDE4E7952AEDFA76EEA47C1117FCIOPICTME/1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B93 MicroMessenger/6.5.20 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.1.2; Redmi Note 3 Build/NJH47F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043602 Safari/537.36 V1_AND_SQ_7.2.5_744_YYB_D QQ/7.2.5.3305 NetType/WIFI WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; Android 7.1.2; MI 6 Build/NJH47F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 V1_AND_SQ_7.2.0_730_YYB_D QQ/7.2.0.3270 NetType/WIFI WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; Android 7.1.2; MI 6 Build/NJH47F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 V1_AND_SQ_7.2.0_730_YYB_D QQ/7.2.0.3270 NetType/4G WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; Android 8.0; ONEPLUS A3000 Build/OPR6.170623.013; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 V1_AND_SQ_7.2.5_744_YYB_D QQ/7.2.5.3305 NetType/4G WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; Android 8.0; ONEPLUS A3000 Build/OPR6.170623.013; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 V1_AND_SQ_7.2.5_744_YYB_D QQ/7.2.5.3305 NetType/WIFI WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; Android 6.0; PRO 6s Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043610 Safari/537.36 V1_AND_SQ_7.1.0_0_TIM_D TIM2.0/2.0.1.1720 QQ/6.5.5  NetType/4G WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; Android 7.1.1; ONEPLUS A5000 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile MQQBrowser/6.2 TBS/043715 Safari/537.36 V1_AND_SQ_7.2.5_744_YYB_D QQ/7.2.5.3305 NetType/WIFI WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 V1_AND_SQ_7.2.5_744_YYB_D QQ/7.2.5.3305 NetType/WIFI WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; Android 7.1.1; MIX 2 Build/NMF26X-wesley_iui-17.10.20; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043602 Safari/537.36 V1_AND_SQ_7.1.0_0_TIM_D TIM2.0/2.0.1.1720 QQ/6.5.5  NetType/4G WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; Android 6.0.1; M2 E Build/MMB29U; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 V1_AND_SQ_7.2.5_744_YYB_D QQ/7.2.5.3305 NetType/4G WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; Android 7.0; MI 5 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 V1_AND_SQ_7.2.5_744_YYB_D QQ/7.2.5.3305 NetType/4G WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; Android 7.1.1; MX6 Build/NMF26O; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 V1_AND_SQ_7.2.5_744_YYB_D QQ/7.2.5.3305 NetType/4G WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; Android 7.1.1; ONEPLUS A3010 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 V1_AND_SQ_7.2.5_744_YYB_D QQ/7.2.5.3305 NetType/4G WebP/0.3.0 Pixel/1080",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MHA-AL00 Build/HUAWEIMHA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.6.956 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; EVA-DL00 Build/HUAWEIEVA-DL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.2.942 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.16.1120 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0.1; KIW-AL10 Build/HONORKIW-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043610 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; HUAWEI GRA-UL10 Build/HUAWEIGRA-UL10) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; MI 5 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.8 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; VIE-AL10 Build/HUAWEIVIE-AL10) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; vivo X9 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043610 Safari/537.36 MicroMessenger/6.5.16.1120 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; vivo X9i Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OD103 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.6.956 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.1.1; OD105 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043610 Safari/537.36 MicroMessenger/6.5.16.1120 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.1.1; OPPO R11 Pluskt Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.16.1120 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; PIC-AL00 Build/HUAWEIPIC-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.16.1120 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.1; SM-J5008 Build/LMY47O; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.5.11 (Baidu; P1 5.1)",
    "Mozilla/5.0 (Linux; Android 6.0.1; Redmi Note 4X Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.5.11 (Baidu; P1 6.0.1)",
    "Mozilla/5.0 (iPhone 91; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.9.0 Mobile/14G60 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; Android 6.0; HUAWEI MLA-AL10 Build/HUAWEIMLA-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.5.11 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; Android 4.4.4; OPPO R7s Build/KTU84P; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.16.1120 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_3 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A432 MicroMessenger/6.5.20 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; MI 6 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.0",
    "Mozilla/5.0 (Linux; Android 7.0; HUAWEI NXT-DL00 Build/HUAWEINXT-DL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.16.1120 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B93 MicroMessenger/6.5.9 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.1.1; OPPO R9 Plusm A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.5.11 (Baidu; P1 5.1.1)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_2_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13D15 MicroMessenger/6.3.13 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0.1; Redmi Note 3 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.16.1120 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; MI 5 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.16.1120 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 6.0; HUAWEI MLA-AL10 Build/HUAWEIMLA-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043610 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; FRD-AL10 Build/HUAWEIFRD-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.6.956 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; M5 Note Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.5.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; EVA-AL10 Build/HUAWEIEVA-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.6.956 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; HUAWEI GRA-TL00 Build/HUAWEIGRA-TL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.5.11 (Baidu; P1 6.0)",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; MI 5 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.3.0",
    "Mozilla/5.0 (Android 5.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.9.4.1000 Chrome/39.0.2146.0 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; Redmi Note 4X Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.16.1120 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.1.1; vivo Xplay6 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/7.9 lite baiduboxapp/2.4.0.10 (Baidu; P1 7.1.1)",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; MI NOTE LTE Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.11",
    "Mozilla/5.0 (Linux; Android 7.0; M1 E Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043610 Safari/537.36 MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 5.1; K-Touch X7 Build/LMY47D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.5.11 (Baidu; P1 5.1)",
    "Mozilla/5.0 (Linux; Android 7.1.1; vivo X9L Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.5.11 (Baidu; P1 7.1.1)",
    "Mozilla/5.0 (Linux; Android 4.4.4; vivo X5S L Build/KTU84P; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.5.11 (Baidu; P1 4.4.4)",
    "Mozilla/5.0 (Linux; Android 6.0.1; vivo X9Plus Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043610 Safari/537.36 MicroMessenger/6.5.16.1120 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; EDI-AL10 Build/HUAWEIEDISON-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.5.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (Linux; Android 5.0; R7Plus Build/LRX21M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.5.11 (Baidu; P1 5.0)",
    "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; TA-1000 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; GT-I9508 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; DUK-AL20 Build/HUAWEIDUK-AL20) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.8.952 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 4.3; zh-cn; X9077 Build/JLS36C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 lite baiduboxapp/2.4.0.10 (Baidu; P1 4.3)",
    "Mozilla/5.0 (Linux; U; Android 8.0.0; zh-cn; ONEPLUS A3000 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; SM-G9280 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/7.4 baiduboxapp/8.1 (Baidu; P1 7.0)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.21 NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Mobile/14D27 baiduboxapp/0_01.5.2.8_enohpi_4331_057/1.2.01_1C2%259enohPi/1099a/65D205F6EC3FAC765305F590E912B38EE83B04FACFRTJNDMIOM/1",
    "Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; PRO 5 Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.8.952 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; Redmi Note 3 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.8",
    "Mozilla/5.0 (iPhone 6sp; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.9.0 Mobile/14G60 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; NCE-AL10 Build/HUAWEINCE-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.8.952 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; KNT-AL10 Build/HUAWEIKNT-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.5.11 (Baidu; P1 7.0)",
    "Mozilla/5.0 (iPhone 6s; CPU iPhone OS 11_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0 MQQBrowser/7.9.0 Mobile/15B93 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_3 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A432 baiduboxapp/0_01.5.2.8_enohpi_4331_057/3.0.11_1C2%259enohPi/1099a/42A2BCE504692B8B5FAEA6243671EE417BEFE9FD3FCNNTFTJAK/1",
    "Mozilla/5.0 (Linux; Android 7.0; MI 5 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043610 Safari/537.36 MicroMessenger/6.5.16.1120 NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 7.0; MI 5 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.1 baidubrowser/7.15.15.0 (Baidu; P1 7.0)"
    ]


def 返回(欲返回的内容):
    return 欲返回的内容


def 调试输出(欲输出的内容):
    print(欲输出的内容)


def 到文本(欲转换的数据, 编码方式=None):
    try:
        if 编码方式 == None:
            return str(欲转换的数据)
        else:
            return str(欲转换的数据, 编码方式)
    except Exception as error:
        print('到文本：运行出错|' + str(error))
        return ''


def 到整数(欲转换的数据):
    try:
        return int(欲转换的数据)
    except Exception as error:
        print('到整数：运行出错|' + str(error))
        return -1


def 到数值(欲转换的数据):
    try:
        return float(欲转换的数据)
    except Exception as error:
        print('到数值：运行出错|' + str(error))
        return -1.0


def 对象到文本(欲转换的数据):
    try:
        return repr(欲转换的数据)
    except Exception as error:
        print('对象到文本：运行出错|' + str(error))
        return ''


def 到元组(欲转换的数据):
    try:
        return tuple(欲转换的数据)
    except Exception as error:
        print('到元组：运行出错|' + str(error))
        return ()


def 到列表(欲转换的数据):
    try:
        return list(欲转换的数据)
    except Exception as error:
        print('到列表：运行出错|' + str(error))
        return []


def 到字典(欲转换的数据):
    try:
        return dict(欲转换的数据)
    except Exception as error:
        print('到字典：运行出错|' + str(error))
        return {}


def 到字节(欲转换的数据, 编码方式=None):
    '传入字符串类型需要传编码'
    try:
        if 编码方式 == None:
            return bytes(欲转换的数据)
        else:
            return bytes(欲转换的数据, 编码方式)
    except Exception as error:
        print('到字节：运行出错|' + str(error))
        return b''


def 到字节数组(欲转换的数据, 编码方式=None):
    '可变的字节序列，相当于bytes的可变版本'
    try:
        if 编码方式 == None:
            return bytearray(欲转换的数据)
        else:
            return bytearray(欲转换的数据, 编码方式)
    except Exception as error:
        print('到字节数组：运行出错|' + str(error))
        return bytearray(b'')


def 序列_是否都为真(欲检验的序列):
    '判断传入的列表 字典 元组 range是否都为真,字典检验的是键,空列表为真 空元组为假'
    try:
        return all(欲检验的序列)
    except Exception as error:
        print('序列_是否都为真：运行出错|' + str(error))
        return False


def 序列_是否有真(欲检验的序列):
    '判断传入的列表 字典 元组 range是否有一个值为真,字典检验的是键,空列表 0 空文本都为假'
    try:
        return any(欲检验的序列)
    except Exception as error:
        print('序列_是否都为真：运行出错|' + str(error))
        return False


def 字节数组_清空(字节数组):
    '成功返回True,失败返回False'
    if isinstance(字节数组, bytearray) != True:
        print('字节数组_清空：传入参数有误')
        return False
    字节数组.clear()
    return True


def 字节数组_顺序反转(字节数组):
    '成功返回True,失败返回False'
    if isinstance(字节数组, bytearray) != True:
        print('字节数组_顺序反转：传入参数有误')
        return False
    字节数组.reverse()
    return True


def 取数据类型(欲查询的数据):
    return type(欲查询的数据)


def 取数据长度(欲查询的数据):
    '成功返回长度,失败返回-1'
    try:
        return len(欲查询的数据)
    except Exception as error:
        print('取数据长度：运行出错|' + str(error))
        return -1


def 集合(集合的数据):
    try:
        return set(集合的数据)
    except Exception as error:
        print('集合：运行出错|' + str(error))
        return set()


def 文本_取出现次数(原文本, 欲查询的文本, 开始的位置=0, 结束的位置=0):
    '成功返回次数,失败返回-1,,在字符串里边出现的次数，start 和 end 参数表示范围，可选'
    if isinstance(原文本, str) != True or isinstance(欲查询的文本, str) != True or isinstance(开始的位置, int) != True or isinstance(
            结束的位置, int) != True:
        print('文本_取出现次数：传入参数有误')
        return -1
    elif 结束的位置 < 1:
        结束的位置 = len(原文本)
    return 原文本.count(欲查询的文本, 开始的位置, 结束的位置)


def 文本_是否指定文本结尾(原文本, 结尾的文本, 开始的位置=0, 结束的位置=0):
    '如果字符串为指定的后缀返回True，否则返回False'
    if isinstance(原文本, str) != True or isinstance(结尾的文本, str) != True or isinstance(开始的位置, int) != True or isinstance(
            结束的位置, int) != True:
        print('文本_是否指定文本结尾：传入参数有误')
        return False
    elif 结束的位置 < 1:
        结束的位置 = len(原文本)
    return 原文本.endswith(结尾的文本, 开始的位置, 结束的位置)


def 文本_是否指定文本开头(原文本, 开头的文本, 开始的位置=0, 结束的位置=0):
    '如果字符串为指定的开头返回True，否则返回False'
    if isinstance(原文本, str) != True or isinstance(开头的文本, str) != True or isinstance(开始的位置, int) != True or isinstance(
            结束的位置, int) != True:
        print('文本_是否指定文本开头：传入参数有误')
        return False
    elif 结束的位置 < 1:
        结束的位置 = len(原文本)
    return 原文本.startswith(开头的文本, 开始的位置, 结束的位置)


def 文本_TAB转空格(原文本, 转换的数量=8):
    '失败出错返回空文本,把字符串中的 tab 符号（\t）转换为空格，如不指定参数，默认的空格数是 tabsize=8'
    if isinstance(原文本, str) != True or isinstance(转换的数量, int) != True:
        return '文本_TAB转空格：传入参数有误'
    try:
        return 原文本.expandtabs(tabsize=转换的数量)  # 默认数量比传入的少不知道为啥
    except Exception as error:
        print('文本_TAB转空格：运行出错|' + str(error))
        return ''


def 文本_寻找文本(原文本, 欲寻找的文本, 开始的位置=0, 结束的位置=0):
    '失败出错返回-1,检测是否包含在字符串中，如果有则返回索引值，否则返回 -1，start 和 end 参数表示范围，可选'
    if isinstance(原文本, str) != True or isinstance(欲寻找的文本, str) != True or isinstance(开始的位置, int) != True or isinstance(
            结束的位置, int) != True:
        print('文本_寻找文本：传入参数有误')
        return -1
    elif 结束的位置 < 1:
        结束的位置 = len(原文本)
    try:
        return 原文本.find(欲寻找的文本, 开始的位置, 结束的位置)
    except Exception as error:
        print('文本_寻找文本：运行出错|' + str(error))
        return -1


def 文本_倒找文本(原文本, 欲寻找的文本, 开始的位置=0, 结束的位置=0):
    '失败出错返回-1,类似于 find() 方法，不过是从右边开始查找'
    if isinstance(原文本, str) != True or isinstance(欲寻找的文本, str) != True or isinstance(开始的位置, int) != True or isinstance(
            结束的位置, int) != True:
        print('文本_倒找文本：传入参数有误')
        return -1
    elif 结束的位置 < 1:
        结束的位置 = len(原文本)
    try:
        return 原文本.rfind(欲寻找的文本, 开始的位置, 结束的位置)
    except Exception as error:
        print('文本_倒找文本：运行出错|' + str(error))
        return -1


def 文本_寻找文本index(原文本, 欲寻找的文本, 开始的位置=0, 结束的位置=0):
    '失败出错返回-1,跟 find 方法一样，不过如果 sub 不在 string 中会产生一个异常'
    if isinstance(原文本, str) != True or isinstance(欲寻找的文本, str) != True or isinstance(开始的位置, int) != True or isinstance(
            结束的位置, int) != True:
        print('文本_寻找文本index：传入参数有误')
        return -1
    elif 结束的位置 < 1:
        结束的位置 = len(原文本)
    try:
        return 原文本.index(欲寻找的文本, 开始的位置, 结束的位置)
    except Exception as error:
        print('文本_寻找文本index：运行出错|' + str(error))
        return -1


def 文本_倒找文本index(原文本, 欲寻找的文本, 开始的位置=0, 结束的位置=0):
    '失败出错返回-1,类似于 index() 方法，不过是从右边开始'
    if isinstance(原文本, str) != True or isinstance(欲寻找的文本, str) != True or isinstance(开始的位置, int) != True or isinstance(
            结束的位置, int) != True:
        print('文本_倒找文本index：传入参数有误')
        return -1
    elif 结束的位置 < 1:
        结束的位置 = len(原文本)
    try:
        return 原文本.rindex(欲寻找的文本, 开始的位置, 结束的位置)
    except Exception as error:
        print('文本_寻找文本rindex：运行出错|' + str(error))
        return -1


def 文本_是否全十进制数字U(原文本):
    '返回True,False,如果字符串只包含十进制数字则返回 True，否则返回False。这种方法是只针对unicode对象'
    if isinstance(原文本, str) != True:
        print('文本_是否全十进制数字U：传入参数有误')
        return False
    return 原文本.isdecimal()


def 文本_是否全数字字母(原文本):
    '返回True,False,如果字符串至少有一个字符并且所有字符都是字母或数字则返回 True，否则返回 False'
    if isinstance(原文本, str) != True:
        print('文本_是否全数字字母：传入参数有误')
        return False
    return 原文本.isalnum()


def 文本_是否全数字(原文本):
    '返回True,False,如果字符串只包含数字则返回 True，否则返回 False'
    if isinstance(原文本, str) != True:
        print('文本_是否全数字：传入参数有误')
        return False
    return 原文本.isdigit()


def 文本_是否全数字U(原文本):
    '返回True,False,检测字符串是否只由数字组成，是则返回True，否则返回False。这种方法是只针对unicode对象'
    if isinstance(原文本, str) != True:
        print('文本_是否全数字U：传入参数有误')
        return False
    return 原文本.isnumeric()


def 文本_是否全空格(原文本):
    '返回True,False,如果字符串中只包含空格，则返回 True，否则返回 False'
    if isinstance(原文本, str) != True:
        print('文本_是否全空格：传入参数有误')
        return False
    return 原文本.isspace()


def 文本_是否标题化(原文本):
    '返回True,False,如果字符串是标题化（所有的单词都是以大写开始，其余字母均小写），则返回 True，否则返回 False'
    if isinstance(原文本, str) != True:
        print('文本_是否标题化：传入参数有误')
        return False
    return 原文本.istitle()


def 文本_是否全小写(原文本):
    '返回True,False,如果字符串中至少包含一个区分大小写的字符，并且这些字符都是小写，则返回 True，否则返回 False'
    if isinstance(原文本, str) != True:
        print('文本_是否全小写：传入参数有误')
        return False
    return 原文本.islower()


def 文本_是否全大写(原文本):
    '返回True,False,如果字符串中至少包含一个区分大小写的字符，并且这些字符都是大写，则返回 True，否则返回 False'
    if isinstance(原文本, str) != True:
        print('文本_是否全大写：传入参数有误')
        return False
    return 原文本.isupper()


def 文本_是否全字母(原文本):
    '返回True,False,如果字符串至少有一个字符并且所有字符都是字母则返回 True，否则返回 False'
    if isinstance(原文本, str) != True:
        print('文本_是否全字母：传入参数有误')
        return False
    return 原文本.isalpha()


def 文本_标题化(原文本):
    '失败返回空文本,返回标题化（所有的单词都是以大写开始，其余字母均小写）的字符串'
    if isinstance(原文本, str) != True:
        print('文本_标题化：传入参数有误')
        return ''
    return 原文本.title()


def 文本_首字母转大写(原文本):
    '失败返回空文本,把字符串的第一个字符改为大写'
    if isinstance(原文本, str) != True:
        print('文本_首字母转大写：传入参数有误')
        return ''
    return 原文本.capitalize()


def 文本_到小写(原文本):
    '失败返回空文本,把整个字符串的所有字符改为小写'
    if isinstance(原文本, str) != True:
        print('文本_到小写：传入参数有误')
        return ''
    return 原文本.casefold()


def 文本_到大写(原文本):
    '失败返回空文本,转换字符串中的所有小写字符为大写'
    if isinstance(原文本, str) != True:
        print('文本_到大写：传入参数有误')
        return ''
    return 原文本.upper()


def 文本_大小写字符到小写(原文本):
    '失败返回空文本,转换字符串中所有大写字符为小写'
    if isinstance(原文本, str) != True:
        print('文本_大小写字符到小写：传入参数有误')
        return ''
    return 原文本.lower()


def 文本_大小写翻转(原文本):
    '失败返回空文本,翻转字符串中的大小写'
    if isinstance(原文本) != True:
        print('文本_大小写翻转：传入参数有误')
        return ''
    return 原文本.swapcase()


def 文本_拼接(连接符, 欲拼接的序列):
    '失败返回空文本,以字符串作为分隔符，插入到 sub 中所有的字符之间'
    if isinstance(连接符, str) != True:
        print('文本_拼接：传入参数有误')
        return ''
    try:
        return 连接符.join(欲拼接的序列)
    except Exception as error:
        print('文本_拼接：运行出错|' + str(error))
        return ''


def 文本_居中(原文本, 填充目标长度=0):
    '失败返回空文本,返回一个居中的字符串，并使用空格填充长度'
    if isinstance(原文本, str) != True or isinstance(填充目标长度, int) != True:
        print('文本_居中：传入参数有误')
        return ''
    return 原文本.center(填充目标长度)


def 文本_左对齐(原文本, 填充目标长度=0):
    '失败返回空文本,返回一个左对齐的字符串，并使用空格填充长度'
    if isinstance(原文本, str) != True or isinstance(填充目标长度, int) != True:
        print('文本_左对齐：传入参数有误')
        return ''
    return 原文本.ljust(填充目标长度)


def 文本_右对齐(原文本, 填充目标长度=0):
    '失败返回空文本,返回一个右对齐的字符串，并使用空格填充长度'
    if isinstance(原文本, str) != True or isinstance(填充目标长度, int) != True:
        print('文本_右对齐：传入参数有误')
        return ''
    return 原文本.rjust(填充目标长度)


def 文本_右对齐0(原文本, 填充目标长度):
    '失败返回空文本,返回一个右对齐的字符串，并使用0填充长度'
    if isinstance(原文本, str) != True or isinstance(填充目标长度, int) != True:
        print('文本_右对齐0：传入参数有误')
        return ''
    return 原文本.zfill(填充目标长度)


def 文本_删左边全部空格(原文本):
    '失败返回空文本,去掉字符串左边的所有空格'
    if isinstance(原文本, str) != True:
        print('文本_删左边全部空格：传入参数有误')
        return ''
    return 原文本.lstrip()


def 文本_删右边全部空格(原文本):
    '失败返回空文本,去掉字符串右边的所有空格'
    if isinstance(原文本, str) != True:
        print('文本_删右边全部空格：传入参数有误')
        return ''
    return 原文本.rstrip()


def 文本_删首尾指定字符(原文本, 欲删除的内容=' '):
    '失败返回空文本,删除字符串首尾指定的字符,默认删除首尾空格'
    if isinstance(原文本, str) != True or isinstance(欲删除的内容, str) != True:
        print('文本_删首尾指定字符：传入参数有误')
        return ''
    return 原文本.strip(欲删除的内容)


def 文本_三元分割_左(原文本, 分割标识):
    '失败返回('','',原文本),将字符串分割成三元元组，存放分割的前面，分割标识本身，分割的后面'
    if isinstance(原文本, str) != True or isinstance(分割标识, str) != True:
        print('文本_三元分割_左：传入参数有误')
        return ('', '', 原文本)
    return 原文本.partition(分割标识)


def 文本_三元分割_右(原文本, 分割标识):
    '失败返回('','',原文本),类似于 partition() 方法，不过是从右边开始查找'
    if isinstance(原文本, str) != True or isinstance(分割标识, str) != True:
        print('文本_三元分割_右：传入参数有误')
        return ('', '', 原文本)
    return 原文本.rpartition(分割标识)


def 文本_子文本替换(原文本, 要替换的文本, 用作替换的文本, 替换的次数=-1):
    '失败返回空文本'
    if isinstance(原文本, str) != True or isinstance(要替换的文本, str) != True or isinstance(用作替换的文本,
                                                                                     str) != True or isinstance(替换的次数,
                                                                                                                int) != True:
        print('文本_子文本替换：传入参数有误')
        return ''
    return 原文本.replace(要替换的文本, 用作替换的文本, 替换的次数)


def 文本_分割文本(原文本, 分割标识=' ', 分割次数=-1):
    '失败返回空列表,如果分割次数被指定，则返回分割次数+1的列表，后面的不做分割在最后一个列表里'
    if isinstance(原文本, str) != True or isinstance(分割标识, str) != True or isinstance(分割次数, int) != True:
        print('文本_分割文本：传入参数有误')
        return []
    return 原文本.split(分割标识, 分割次数)


def 文本_换行分割(原文本, 保留换行=False):
    '失败返回空列表,用换行符做分割，可设置分割后是否保留换行符'
    if isinstance(原文本, str) != True or isinstance(保留换行, bool) != True:
        print('文本_换行分割：传入参数有误')
        return []
    return 原文本.splitlines(保留换行)


def 文本_生成翻译表(原文本, 翻译文本, 翻译表类型=0):
    '失败返回空字典,类型0是str 1是bytes  2是bytearray'
    if isinstance(原文本, str) != True or isinstance(翻译文本, str) != True or isinstance(翻译表类型, int) != True:
        print('文本_生成翻译表：传入参数有误')
        return {}
    elif 翻译表类型 < 0:
        翻译表类型 = 0
    elif 翻译表类型 > 2:
        翻译表类型 = 2
    try:
        if 翻译表类型 == 0:
            return str.maketrans(原文本, 翻译文本)
        elif 翻译表类型 == 1:
            return bytes.maketrans(原文本, 翻译文本)
        elif 翻译表类型 == 2:
            return bytearray.maketrans(原文本, 翻译文本)
    except Exception as error:
        print('文本_生成翻译表：运行出错|' + str(error))
        return {}


def 文本_转换字符(原文本, 翻译表, 过滤的内容=None):
    '失败返回空文本,配合生成的翻译表批量转换字符串中的字符，不想显示的可以过滤不做转换,使用过滤功能用bytes类型'
    if isinstance(原文本, (str, bytes, bytearray)) != True or isinstance(翻译表, dict) != True:
        print('文本_转换字符：传入参数有误')
        return ''
    try:
        if 过滤的内容 == None:
            return 原文本.translate(翻译表)
        else:
            return 原文本.translate(翻译表, 过滤的内容)
    except Exception as error:
        print('文本_转换字符：运行出错|' + str(error))
        return ''


def 文本_按键名转键值(按键名):
    "失败返回-1,传入按键名 如 A  或者1  2 3  返回整数的键值"
    if isinstance(按键名, str) != True:
        print('文本_按键名转键值：传入参数有误')
        return -1
    try:
        return ord(按键名)
    except Exception as error:
        print('文本_按键名转键值：运行出错|' + str(error))
        return -1


def 文本_键值转按键名(键值):
    '失败返回空文本,传入整数的键值 返回对应键值的键符'
    if isinstance(键值, int) != True:
        print('文本_键值转按键名：传入参数有误')
        return ''
    try:
        return chr(键值)
    except Exception as error:
        print('文本_键值转按键名：运行出错|' + str(error))
        return ''


def 文本_取出中间文本(原文本, 前面的文本, 后面的文本, 开始的位置=0):
    '失败返回空文本'
    if isinstance(原文本, str) != True or isinstance(前面的文本, str) != True or isinstance(后面的文本, str) != True or isinstance(
            开始的位置, int) != True:
        print('文本_取出中间文本：传入参数有误')
        return ''
    elif 原文本.find(前面的文本, 开始的位置) != -1 and 原文本.find(后面的文本, 开始的位置 + len(前面的文本)) != -1:
        return 原文本[原文本.find(前面的文本, 开始的位置) + len(前面的文本):原文本.find(后面的文本, 原文本.find(前面的文本) + len(前面的文本))]
    else:
        return ""


def 文本_取文本左边(原文本, 指定的文本):
    if isinstance(原文本, str) != True or isinstance(指定的文本, str) != True:
        print('文本_取文本左边：传入参数有误')
        return ''
    elif 原文本.find(指定的文本) != -1:
        return 原文本[0:原文本.find(指定的文本)]
    else:
        return ""


def 文本_取文本右边(原文本, 指定的文本):
    if isinstance(原文本, str) != True or isinstance(指定的文本, str) != True:
        print('文本_取文本右边：传入参数有误')
        return ''
    elif 原文本.rfind(指定的文本) != -1:
        return 原文本[原文本.rfind(指定的文本) + len(指定的文本):len(原文本)]
    else:
        return ""


def 文本_取左边(原文本, 要取出的数量):
    if isinstance(原文本, str) != True or isinstance(要取出的数量, int) != True:
        print('文本_取左边：传入参数有误')
        return ''
    return 原文本[0:要取出的数量]


def 文本_取右边(原文本, 要取出的数量):
    if isinstance(原文本, str) != True or isinstance(要取出的数量, int) != True:
        print('文本_取右边：传入参数有误')
        return ''
    return 原文本[len(原文本) - 要取出的数量:len(原文本)]


def 文本_取字符长度(原文本):
    '失败出错返回-1,这里只做字符串跟整数的长度返回'
    if isinstance(原文本, (str, int)) != True:
        print('文本_取字符长度：传入参数有误')
        return -1
    return len(str(原文本))


def 文本_取随机IP():
    return socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))


def 文本_取随机邮箱():
    邮箱后缀 = ['@qq.com', '@sina.com', '@126.com', '@163.com', '@hotmail.com', '@139.com', '@189.com', '@sohu.com',
            '@21cn.com', '@189.com', '@tom.com', '@aol.com', '@263.com', '@aliyun.com', '@foxmail.com', '@yeah.net']
    return 变量_取出随机元素([文本_取随机字母(int(文本_取随机范围数字(5, 9))), 文本_取随机数字(int(文本_取随机范围数字(5, 9))),
                      文本_取随机字符(int(文本_取随机范围数字(5, 9)))]) + 变量_取出随机元素(邮箱后缀)


def 文本_取随机手机号():
    号码前缀 = ['130', '131', '132', '134', '135', '136', '137', '138', '139', '147', '150', '151', '152', '153', '155',
            '156', '157', '158', '159', '170', '171', '180', '182', '183', '185', '186', '187', '188', '189']
    return 变量_取出随机元素(号码前缀) + 文本_取随机数字(8)


def 文本_取随机字母(取出的数量=1, 类型=0):
    '失败返回空文本,类型 0是小写 1是大写 2是混合'
    if isinstance(取出的数量, int) != True or isinstance(类型, int) != True:
        print('文本_取随机字母：传入参数有误')
        return ''
    if 取出的数量 < 1 or 取出的数量 > 9999999:
        取出的数量 = 1
    if 类型 < 0 or 类型 > 9999999:
        类型 = 0
    字母 = 'abcdefghijklnmopqrstuvwxyz'
    文本 = ''
    if 类型 == 0:
        for x in range(取出的数量):
            文本 = 文本 + 变量_取出随机元素(字母)
    elif 类型 == 1:
        for x in range(取出的数量):
            文本 = 文本 + 变量_取出随机元素(字母).upper()
    else:
        for x in range(取出的数量):
            随机数 = 文本_取随机范围数字(1, 2)
            if 随机数 == "1":
                文本 = 文本 + 变量_取出随机元素(字母)
            else:
                文本 = 文本 + 变量_取出随机元素(字母).upper()
    return 文本


def 文本_取随机数字(取出的数量=1, 是否排除0开头=False):
    '失败返回空文本'
    if isinstance(取出的数量, int) != True or isinstance(是否排除0开头, bool) != True:
        print('文本_取随机数字：传入参数有误')
        return ''
    if 取出的数量 < 1 or 取出的数量 > 9999999:
        取出的数量 = 1
    文本 = ''
    if 是否排除0开头 == False:
        for x in range(取出的数量):
            文本 = 文本 + 文本_取随机范围数字(0, 9)
    else:
        文本 = 文本 + 文本_取随机范围数字(1, 9)
        for x in range(取出的数量 - 1):
            文本 = 文本 + 文本_取随机范围数字(0, 9)
    return 文本


def 文本_取随机字符(取出的数量=1):
    '失败返回空文本,包括0-9 a-z A-Z'
    if isinstance(取出的数量, int) != True:
        print('文本_取随机字符：传入参数有误')
        return ''
    if 取出的数量 < 1 or 取出的数量 > 9999999:
        取出的数量 = 1
    字符 = '0123456789abcdefghijklnmopqrstuvwxyzABCDEFGHIJKLNMOPQRSTUVWXYZ'
    文本 = ''
    for x in range(取出的数量):
        文本 = 文本 + 变量_取出随机元素(字符)
    return 文本


def 文本_取随机姓氏(取常见姓氏=False):
    '失败返回空文本,常见姓氏为自己设置挑选的,仅做参考'
    if isinstance(取常见姓氏, bool) != True:
        print('文本_取随机姓氏：传入参数有误')
        return ''
    百家姓 = """赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺
    倪汤滕殷罗毕郝邬安常乐于时傅皮卞齐康伍余元卜顾孟平黄和穆萧尹姚邵湛汪祁毛禹狄米贝明臧计伏成戴谈宋茅庞熊纪舒屈项祝董梁杜阮蓝闵席季麻强贾路娄危江童颜郭梅盛林刁钟徐邱骆高夏蔡田樊胡凌霍虞万支柯昝管卢莫柯房裘缪干解应宗丁宣贲邓郁单杭洪包诸左石崔吉钮龚程嵇邢滑裴陆荣翁荀羊于惠甄曲家封芮羿储靳汲邴糜松井段富巫乌焦巴弓牧隗山谷车侯宓蓬全郗班仰秋仲伊宫宁仇栾暴甘钭历戎祖武符刘景詹束龙叶幸司韶郜黎蓟溥印宿白怀蒲邰从鄂索咸籍赖卓蔺屠蒙池乔阳郁胥能苍双闻莘党翟谭贡劳逄姬申扶堵冉宰郦雍却璩桑桂濮牛寿通边扈燕冀浦尚农温别庄晏柴瞿阎充慕连茹习宦艾鱼容向古易慎戈廖庾终暨居衡步都耿满弘匡国文寇广禄
    阙东欧殳沃利蔚越夔隆师巩厍聂晁勾敖融冷訾辛阚那简饶空曾毋沙乜养鞠须丰巢关蒯相查后荆红游竺权逮盍益桓公"""
    常见百家姓 = '赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛范彭郎鲁韦昌马苗凤花方俞任袁柳史唐费薛雷贺罗毕于齐萧尹姚顾孟平黄宋庞项祝董梁杜阮刘万丁石洪白田夏'
    if 取常见姓氏 == False:
        取出的姓氏 = ''
        while 取出的姓氏 == '' or 取出的姓氏 == '\n':
            取出的姓氏 = 变量_取出随机元素(百家姓)
        return 取出的姓氏
    else:
        return 变量_取出随机元素(常见百家姓)


def 文本_取随机汉字(取出的数量=1):
    '失败返回空文本,只有部分常见字'
    if isinstance(取出的数量, int) != True:
        print('文本_取随机汉字：传入参数有误')
        return ''
    if 取出的数量 < 1 or 取出的数量 > 9999999:
        取出的数量 = 1
    ming = [
        '的', '一', '是', '了', '我', '不', '人', '在', '他', '有', '这', '个', '上', '们', '来', '到', '时', '大', '地', '为',
        '子', '中', '你', '说', '生', '国', '年', '着', '就', '那', '和', '要', '她', '出', '也', '得', '里', '后', '自', '以',
        '会', '家', '可', '下', '而', '过', '天', '去', '能', '对', '小', '多', '然', '于', '心', '学', '么', '之', '都', '好',
        '看', '起', '发', '当', '没', '成', '只', '如', '事', '把', '还', '用', '第', '样', '道', '想', '作', '种', '开', '美',
        '总', '从', '无', '情', '己', '面', '最', '女', '但', '现', '前', '些', '所', '同', '日', '手', '又', '行', '意', '动',
        '方', '期', '它', '头', '经', '长', '儿', '回', '位', '分', '爱', '老', '因', '很', '给', '名', '法', '间', '斯', '知',
        '世', '什', '两', '次', '使', '身', '者', '被', '高', '已', '亲', '其', '进', '此', '话', '常', '与', '活', '正', '感',
        '见', '明', '问', '力', '理', '尔', '点', '文', '几', '定', '本', '公', '特', '做', '外', '孩', '相', '西', '果', '走',
        '将', '月', '十', '实', '向', '声', '车', '全', '信', '重', '三', '机', '工', '物', '气', '每', '并', '别', '真', '打',
        '太', '新', '比', '才', '便', '夫', '再', '书', '部', '水', '像', '眼', '等', '体', '却', '加', '电', '主', '界', '门',
        '利', '海', '受', '听', '表', '德', '少', '克', '代', '员', '许', '稜', '先', '口', '由', '死', '安', '写', '性', '马',
        '光', '白', '或', '住', '难', '望', '教', '命', '花', '结', '乐', '色', '更', '拉', '东', '神', '记', '处', '让', '母',
        '父', '应', '直', '字', '场', '平', '报', '友', '关', '放', '至', '张', '认', '接', '告', '入', '笑', '内', '英', '军',
        '候', '民', '岁', '往', '何', '度', '山', '觉', '路', '带', '万', '男', '边', '风', '解', '叫', '任', '金', '快', '原',
        '吃', '妈', '变', '通', '师', '立', '象', '数', '四', '失', '满', '战', '远', '格', '士', '音', '轻', '目', '条', '呢',
        '病', '始', '达', '深', '完', '今', '提', '求', '清', '王', '化', '空', '业', '思', '切', '怎', '非', '找', '片', '罗',
        '钱', '紶', '吗', '语', '元', '喜', '曾', '离', '飞', '科', '言', '干', '流', '欢', '约', '各', '即', '指', '合', '反',
        '题', '必', '该', '论', '交', '终', '林', '请', '医', '晚', '制', '球', '决', '窢', '传', '画', '保', '读', '运', '及',
        '则', '房', '早', '院', '量', '苦', '火', '布', '品', '近', '坐', '产', '答', '星', '精', '视', '五', '连', '司', '巴',
        '奇', '管', '类', '未', '朋', '且', '婚', '台', '夜', '青', '北', '队', '久', '乎', '越', '观', '落', '尽', '形', '影',
        '红', '爸', '百', '令', '周', '吧', '识', '步', '希', '亚', '术', '留', '市', '半', '热', '送', '兴', '造', '谈', '容',
        '极', '随', '演', '收', '首', '根', '讲', '整', '式', '取', '照', '办', '强', '石', '古', '华', '諣', '拿', '计', '您',
        '装', '似', '足', '双', '妻', '尼', '转', '诉', '米', '称', '丽', '客', '南', '领', '节', '衣', '站', '黑', '刻', '统',
        '断', '福', '城', '故', '历', '惊', '脸', '选', '包', '紧', '争', '另', '建', '维', '绝', '树', '系', '伤', '示', '愿',
        '持', '千', '史', '谁', '准', '联', '妇', '纪', '基', '买', '志', '静', '阿', '诗', '独', '复', '痛', '消', '社', '算',
        '义', '竟', '确', '酒', '需', '单', '治', '卡', '幸', '兰', '念', '举', '仅', '钟', '怕', '共', '毛', '句', '息', '功',
        '官', '待', '究', '跟', '穿', '室', '易', '游', '程', '号', '居', '考', '突', '皮', '哪', '费', '倒', '价', '图', '具',
        '刚', '脑', '永', '歌', '响', '商', '礼', '细', '专', '黄', '块', '脚', '味', '灵', '改', '据', '般', '破', '引', '食',
        '仍', '存', '众', '注', '笔', '甚', '某', '沉', '血', '备', '习', '校', '默', '务', '土', '微', '娘', '须', '试', '怀',
        '料', '调', '广', '蜖', '苏', '显', '赛', '查', '密', '议', '底', '列', '富', '梦', '错', '座', '参', '八', '除', '跑',
        '亮', '假', '印', '设', '线', '温', '虽', '掉', '京', '初', '养', '香', '停', '际', '致', '阳', '纸', '李', '纳', '验',
        '助', '激', '够', '严', '证', '帝', '饭', '忘', '趣', '支', '春', '集', '丈', '木', '研', '班', '普', '导', '顿', '睡',
        '展', '跳', '获', '艺', '六', '波', '察', '群', '皇', '段', '急', '庭', '创', '区', '奥', '器', '谢', '弟', '店', '否',
        '害', '草', '排', '背', '止', '组', '州', '朝', '封', '睛', '板', '角', '况', '曲', '馆', '育', '忙', '质', '河', '续',
        '哥', '呼', '若', '推', '境', '遇', '雨', '标', '姐', '充', '围', '案', '伦', '护', '冷', '警', '贝', '著', '雪', '索',
        '剧', '啊', '船', '险', '烟', '依', '斗', '值', '帮', '汉', '慢', '佛', '肯', '闻', '唱', '沙', '局', '伯', '族', '低',
        '玩', '资', '屋', '击', '速', '顾', '泪', '洲', '团', '圣', '旁', '堂', '兵', '七', '露', '园', '牛', '哭', '旅', '街',
        '劳', '型', '烈', '姑', '陈', '莫', '鱼', '异', '抱', '宝', '权', '鲁', '简', '态', '级', '票', '怪', '寻', '杀', '律',
        '胜', '份', '汽', '右', '洋', '范', '床', '舞', '秘', '午', '登', '楼', '贵', '吸', '责', '例', '追', '较', '职', '属',
        '渐', '左', '录', '丝', '牙', '党', '继', '托', '赶', '章', '智', '冲', '叶', '胡', '吉', '卖', '坚', '喝', '肉', '遗',
        '救', '修', '松', '临', '藏', '担', '戏', '善', '卫', '药', '悲', '敢', '靠', '伊', '村', '戴', '词', '森', '耳', '差',
        '短', '祖', '云', '规', '窗', '散', '迷', '油', '旧', '适', '乡', '架', '恩', '投', '弹', '铁', '博', '雷', '府', '压',
        '超', '负', '勒', '杂', '醒', '洗', '采', '毫', '嘴', '毕', '九', '冰', '既', '状', '乱', '景', '席', '珍', '童', '顶',
        '派', '素', '脱', '农', '疑', '练', '野', '按', '犯', '拍', '征', '坏', '骨', '余', '承', '置', '臓', '彩', '灯', '巨',
        '琴', '免', '环', '姆', '暗', '换', '技', '翻', '束', '增', '忍', '餐', '洛', '塞', '缺', '忆', '判', '欧', '层', '付',
        '阵', '玛', '批', '岛', '项', '狗', '休', '懂', '武', '革', '良', '恶', '恋', '委', '拥', '娜', '妙', '探', '呀', '营',
        '退', '摇', '弄', '桌', '熟', '诺', '宣', '银', '势', '奖', '宫', '忽', '套', '康', '供', '优', '课', '鸟', '喊', '降',
        '夏', '困', '刘', '罪', '亡', '鞋', '健', '模', '败', '伴', '守', '挥', '鲜', '财', '孤', '枪', '禁', '恐', '伙', '杰',
        '迹', '妹', '藸', '遍', '盖', '副', '坦', '牌', '江', '顺', '秋', '萨', '菜', '划', '授', '归', '浪', '听', '凡', '预',
        '奶', '雄', '升', '碃', '编', '典', '袋', '莱', '含', '盛', '济', '蒙', '棋', '端', '腿', '招', '释', '介', '烧', '误',
        '乾', '坤']
    文本 = ''
    for x in range(取出的数量):
        文本 = 文本 + 变量_取出随机元素(ming)
    return 文本


def 文本_取随机范围数字(最小值, 最大值, 是否返回整数=False):
    '出错返回0,如果设置返回整数则返回int类型'
    if isinstance(最小值, (int, str)) != True or isinstance(最大值, (int, str)) != True:
        print('文本_取随机范围数字：传入参数有误')
        return 0
    elif int(最小值) > int(最大值):
        return 0
    try:
        if 是否返回整数 == False:
            return str(random.randint(int(最小值), int(最大值)))
        else:
            return random.randint(int(最小值), int(最大值))
    except Exception as error:
        print('文本_取随机范围数字：运行出错|' + str(error))
        return 0


def 文本_到时间_datetime(时间文本, 时间格式='%Y-%m-%d %H:%M:%S'):
    '失败返回空文本,把文本格式的时间转成datetime的时间格式，文本跟时间格式要匹配'
    if isinstance(时间文本, str) != True or isinstance(时间格式, str) != True:
        print('文本_到时间_datetime：传入参数有误')
        return ''
    try:
        return datetime.datetime.strptime(时间文本, 时间格式)
    except Exception as error:
        print('文本_到时间_datetime：运行出错|' + str(error))
        return ''


def 文本_取中间_批量(原文本, 前面的文本, 后面的文本):
    搜索位置 = 0
    列表 = []
    if isinstance(原文本, str) != True or isinstance(前面的文本, str) != True or isinstance(后面的文本, str) != True:
        print('文本_取中间_批量：传入的参数有误')
        return []
    while 1 == 1:
        搜索位置 = 原文本.find(前面的文本, 搜索位置)
        if 搜索位置 != -1:
            后面的位置 = 原文本.find(后面的文本, 搜索位置 + len(前面的文本))
            if 后面的位置 != -1:
                搜索位置 = 搜索位置 + len(前面的文本)
                取出的文本 = 原文本[搜索位置:后面的位置]
                if len(取出的文本) > 0:
                    列表.append(取出的文本)
            else:
                break
        else:
            break
    return 列表


def 文本_拼音转换(原文本, 连接符='', 拼音风格=0, 遍历多音=False, 无拼音处理=0, 严格规范=False):
    '默认返回全拼,失败返回空,拼音风格:0是不带声调的全拼,1是带声调的全拼,2是取声母部分,3是取首字母,无拼音处理：0是保留原始字符,1是忽略该字符,2是 替换为去掉 \\u 的 unicode 编码字符串'
    if isinstance(原文本, str) != True or isinstance(连接符, str) != True or isinstance(拼音风格, int) != True or isinstance(遍历多音,
                                                                                                                   bool) != True or isinstance(
            无拼音处理, int) != True or isinstance(严格规范, bool) != True:
        print('文本_拼音转换：传入的参数有误')
        return ''
    if 拼音风格 > 3 or 拼音风格 < 0:
        拼音风格 = 0

    if 无拼音处理 > 2 or 无拼音处理 < 0:
        无拼音处理 = 0

    if 拼音风格 == 0:
        rStyle = Style.NORMAL
    elif 拼音风格 == 1:
        rStyle = Style.TONE
    elif 拼音风格 == 2:
        rStyle = Style.INITIALS
    elif 拼音风格 == 3:
        rStyle = Style.FIRST_LETTER

    if 无拼音处理 == 0:
        Errors = 'default'
    elif 无拼音处理 == 1:
        Errors = 'ignore'
    elif 无拼音处理 == 2:
        Errors = 'replace'
    try:
        拼音 = ''
        拼音列表 = pinyin(hans=原文本, style=rStyle, heteronym=遍历多音, errors=Errors, strict=严格规范)
        for x in 拼音列表:
            for i in x:
                拼音 = 拼音 + 连接符 + i
        return 拼音[1:]
    except Exception as error:
        print('文本_拼音转换：运行出错|' + str(error))
        return ''


def 数值_求次方(数值, 次方数):
    '出错返回-1'
    if isinstance(数值, (int, float)) != True or isinstance(次方数, (int, float)) != True:
        print('数值_求次方：传入参数有误')
        return -1
    try:
        return pow(数值, 次方数)
    except Exception as error:
        print('数值_求次方：运行出错|' + str(error))
        return -1


def 数值_四舍五入(数值, 保留位数=0):
    '出错返回-1'
    if isinstance(数值, (int, float)) != True or isinstance(保留位数, (int)) != True:
        print('数值_四舍五入：传入参数有误')
        return -1
    try:
        return round(数值, 保留位数)
    except Exception as error:
        print('数值_四舍五入：运行出错|' + str(error))
        return -1


def 数值_取绝对值(待处理的数值):
    "'出错返回-1',传入一个数值,正负数还是小数都返回正的数值"
    if isinstance(待处理的数值, (int, float)) != True:
        print('数值_取绝对值：传入参数有误')
        return -1
    return abs(待处理的数值)


def 数值_取上入整数(待处理的数值):
    "'出错返回-1',示例:1.1返回2"
    if isinstance(待处理的数值, (int, float)) != True:
        print('数值_取绝对值：传入参数有误')
        return -1
    return math.ceil(待处理的数值)


def 数值_取下入整数(待处理的数值):
    "'出错返回-1',示例:1.9返回1"
    if isinstance(待处理的数值, (int, float)) != True:
        print('数值_取绝对值：传入参数有误')
        return -1
    return math.floor(待处理的数值)


def 数值_取最大数(待处理的数值):
    "'出错返回-1',传入要对比的列表,如(1,2,3),返回里面最大的数字"
    try:
        return max(待处理的数值)
    except Exception as error:
        print('数值_取最大数：运行出错|' + str(error))
        return -1


def 数值_取最小数(待处理的数值):
    "'出错返回-1',传入要对比的列表,如(1,2,3),返回里面最小的数字"
    try:
        return min(待处理的数值)
    except Exception as error:
        print('数值_取最小数：运行出错|' + str(error))
        return -1


def 字典_取值并删除(字典, 键, 失败返回值=None):
    '失败返回空文本 如果查找键不存在则返回设置的失败返回值,该值可空'
    if isinstance(字典, dict) != True:
        print('字典_取值并删除：传入字典有误')
    try:
        if 失败返回值 == None:
            return 字典.pop(键)
        else:
            return 字典.pop(键, 失败返回值)
    except Exception as error:
        print('字典_取值并删除：运行出错|' + str(error))
        return ''


def 字典_取指定键值(字典, 键, 失败返回值=None):
    '失败返回空文本 如果查找键不存在则返回设置的失败返回值'
    if isinstance(字典, dict) != True:
        print('字典_取指定键值：传入字典有误')
    try:
        if 失败返回值 == None:
            return 字典.get(键)
        else:
            return 字典.get(键, 失败返回值)
    except Exception as error:
        print('字典_取指定键值：运行出错|' + str(error))
        return ''


def 字典_清空(字典):
    '清空字典内的全部元素,成功返回True 失败返回False'
    if isinstance(字典, dict) != True:
        print('字典_清空：传入字典有误')
    try:
        字典.clear()
        return True
    except Exception as error:
        print('字典_清空：运行出错|' + str(error))
        return False


def 字典_拷贝(新字典, 原字典):
    '成功返回True 失败返回False,直接赋值拷贝值会跟着原字典改变,用copy不会'
    if isinstance(新字典, dict) != True or isinstance(原字典, dict) != True:
        print('字典_拷贝：传入字典有误')
    try:
        新字典 = 原字典.copy()
        return True
    except Exception as error:
        print('字典_拷贝：运行出错|' + str(error))
        return False


def 字典_生成(键值列表, 键值):
    '失败返回空字典,传入键值列表创建字典,字典内的值都为设置的键值'
    if isinstance(键值列表, list) != True:
        print('字典_生成：传入字典有误')
    try:
        return dict.fromkeys(键值列表, 键值)
    except Exception as error:
        print('字典_生成：运行出错|' + str(error))
        return {}


def 字典_转列表(字典):
    '失败返回空列表,返回列表格式[(1,2),(2,3),(3,4)]'
    if isinstance(字典, dict) != True:
        print('字典_转列表：传入字典有误')
    try:
        return list(字典.items())
    except Exception as error:
        print('字典_转列表：运行出错|' + str(error))
        return []


def 字典_取全部键(字典):
    '失败返回空列表'
    if isinstance(字典, dict) != True:
        print('字典_取全部键：传入字典有误')
    try:
        return list(字典.keys())
    except Exception as error:
        print('字典_取全部键：运行出错|' + str(error))
        return []


def 字典_取全部值(字典):
    '失败返回空列表'
    if isinstance(字典, dict) != True:
        print('字典_取全部值：传入字典有误')
    try:
        return list(字典.values())
    except Exception as error:
        print('字典_取全部值：运行出错|' + str(error))
        return []


def 字典_取出并删除最后键值(字典):
    '失败返回空元组,删除字典中最后一个键跟值并以元组格式返回删除的键跟值'
    if isinstance(字典, dict) != True:
        print('字典_取出并删除最后键值：传入字典有误')
    try:
        return 字典.popitem()
    except Exception as error:
        print('字典_取出并删除最后键值：运行出错|' + str(error))
        return ()


def 字典_取值添加(字典, 键, 失败返回值=None):
    '失败返回空文本 如果查找键不存在则返回设置的失败返回值且为字典新建该键值'
    if isinstance(字典, dict) != True:
        print('字典_取值添加：传入字典有误')
    try:
        if 失败返回值 == None:
            return 字典.setdefault(键)
        else:
            return 字典.setdefault(键, 失败返回值)
    except Exception as error:
        print('字典_取值添加：运行出错|' + str(error))
        return ''


def 列表_转字典(列表1, 列表2):
    '传入两个列表转换成字典'
    if isinstance(列表1, list) != True or isinstance(列表2, list) != True:
        print('列表_转字典：传入列表有误')
    try:
        return dict(zip(列表1, 列表2))
    except Exception as error:
        print('列表_转字典：运行出错|' + str(error))
        return {}


def 列表_加入成员(列表, 要加入的值):
    '成功返回True 失败返回False'
    if isinstance(列表, list) != True:
        print('列表_加入成员：传入列表有误')
        return False
    try:
        列表.append(要加入的值)
        return True
    except Exception as error:
        print('列表_加入成员：运行出错|' + str(error))
        return False


def 列表_插入成员(列表, 位置, 要加入的值):
    '成功返回True 失败返回False,在指定位置插入指定值'
    if isinstance(列表, list) != True or isinstance(位置, int) != True:
        print('列表_插入成员：传入列表有误')
        return False
    try:
        列表.insert(位置, 要加入的值)
        return True
    except Exception as error:
        print('列表_插入成员：运行出错|' + str(error))
        return False


def 列表_取出现次数(列表, 要查询的数值):
    '失败未找到返回0,搜索时 True 会当成1   False 是0'
    if isinstance(列表, list) != True:
        print('列表_取出现次数：传入列表有误')
        return 0
    try:
        return 列表.count(要查询的数值)
    except Exception as error:
        print('列表_取出现次数：运行出错|' + str(error))
        return 0


def 列表_加入新列表(列表, 新的列表):
    '成功返回True 失败返回False,在列表后面追加新的列表或元组成员进去'
    if isinstance(列表, list) != True or isinstance(新的列表, (list, tuple)) != True:
        print('列表_加入新列表：传入列表有误')
        return False
    列表.extend(新的列表)
    return True


def 列表_查找成员位置(列表, 要查找的值):
    '失败返回-1'
    if isinstance(列表, list) != True:
        return -1
    try:
        if 要查找的值 in 列表 == True:
            return 列表.index(要查找的值)
        else:
            return -1
    except Exception as error:
        print('列表_查找成员位置：运行出错|' + str(error))
        return -1


def 列表_取值并删除(列表, 位置=None):
    '失败返回空文本,取出列表的一个成员值 并删除该成员,默认最后一个,位置为0则为第一个'
    if isinstance(列表, list) != True:
        print('列表_取值并删除：传入参数有误')
        return ''
    try:
        if 位置 == None:
            return 列表.pop()
        elif isinstance(位置, int) == True:
            return 列表.pop(位置)
        else:
            print('列表_取值并删除：传入参数有误')
            return ''
    except Exception as error:
        print('列表_取值并删除：运行出错|' + str(error))
        return ''


def 列表_删除指定值(列表, 要删除的值):
    '成功返回True 失败返回False,删除列表中找到的第一个值'
    if isinstance(列表, list) != True:
        print('列表_删除指定值：传入列表有误')
        return ''
    try:
        列表.remove(要删除的值)
        return True
    except Exception as error:
        print('列表_删除指定值：运行出错|' + str(error))
        return ''


def 列表_倒序排列(列表):
    '成功返回True 失败返回False,把列表的成员顺序到过来排序'
    if isinstance(列表, list) != True:
        print('列表_倒序排列：传入列表有误')
        return False
    列表.reverse()
    return True


def 列表_大小排序(列表, 排序方式=False):
    '成功返回True 失败返回False,排序的列表只能全为整数型的,排序方式True为从大到小,默认False从小到大'
    if isinstance(列表, list) != True or isinstance(排序方式, bool) != True:
        print('列表_大小排序：传入列表有误')
        return False
    列表.sort(reverse=排序方式)
    return True


def 时间_取指定格式时间(原时间='', 格式=time_时间格式_取时分秒):
    '失败返回空文本'
    if isinstance(原时间, str) != True or isinstance(格式, str) != True:
        print('时间_取指定格式时间：传入参数有误')
        return ''
    elif 原时间 == '':
        原时间 = time.time()
    try:
        lt = time.localtime(原时间)
        return time.strftime(格式, lt)
    except Exception as error:
        print('时间_取指定格式时间：运行出错|' + str(error))
        return ''


def 时间_亚马逊操作时间():
    '返回文本型亚马逊API需要的操作时间,2019-10-15T02:07:57Z'
    return datetime.datetime.utcnow().strftime("%Y" + "-" + "%m" + "-" + "%dT%H" + ":" + "%M" + ":" + "%S") + "Z"


def 时间_取启动时间():
    '返回浮点数时间，可以拿去计算启动时间'
    return time.clock()


def 时间_取现行时间time(时间格式="%Y-%m-%d %H:%M:%S"):
    '失败返回空文本,返回字符串格式的时间'
    if isinstance(时间格式, str) != True:
        print('时间_取现行时间time：传入列表有误')
        return ''
    try:
        return time.strftime(时间格式)
    except Exception as error:
        print('时间_取现行时间time：运行出错|' + str(error))
        return ''


def 时间_取日期(增减天数=0):
    '失败返回空文本,默认返回当天日期,-1表示取昨天'
    if isinstance(增减天数, int) != True:
        print('时间_取日期：传入列表有误')
        return ''
    if (增减天数 < 0):
        增减天数 = abs(增减天数)
        return str(datetime.date.today() - datetime.timedelta(days=增减天数))
    else:
        return str(datetime.date.today() + datetime.timedelta(days=增减天数))


def 时间_取某年某月日历(年份, 月份):
    '失败返回空文本,返回字符串格式的日历'
    if isinstance(年份, int) != True or isinstance(月份, int) != True:
        print('时间_取某年某月日历：传入列表有误')
        return ''
    try:
        return calendar.month(年份, 月份)
    except Exception as error:
        print('时间_取某年某月日历：运行出错|' + str(error))
        return ''


def 时间_取某年日历(年份):
    '失败返回空文本,返回字符串格式的日历'
    if isinstance(年份, int) != True:
        print('时间_取某年日历：传入列表有误')
        return ''
    try:
        return calendar.calendar(年份)
    except Exception as error:
        print('时间_取某年日历：运行出错|' + str(error))
        return ''


def 时间_是否为闰年(年份):
    '返回True跟False返回指定的年份是否为闰年，若是返回True，否则返回False'
    if isinstance(年份, int) != True:
        print('时间_是否为闰年：传入列表有误')
        return False
    try:
        return calendar.isleap(年份)
    except Exception as error:
        print('时间_是否为闰年：运行出错|' + str(error))
        return False


def 时间_指定范围闰年总数(开始年份, 结束年份):
    '失败返回0,返回[开始年份,结束年份)之间闰年的总和'
    if isinstance(开始年份, int) != True or isinstance(结束年份, int) != True:
        print('时间_指定范围闰年总数：传入列表有误')
        return 0
    try:
        return calendar.leapdays(开始年份, 结束年份)
    except Exception as error:
        print('时间_指定范围闰年总数：运行出错|' + str(error))
        return 0


def 时间_取某月天数(年份, 月份):
    '失败返回0'
    if isinstance(年份, int) != True or isinstance(月份, int) != True:
        print('时间_取某月天数：传入列表有误')
        return 0
    try:
        return calendar.monthrange(年份, 月份)[1]
    except Exception as error:
        print('时间_取某月天数：运行出错|' + str(error))
        return 0


def 时间_取某月一号星期几(年份, 月份):
    '失败返回-1,返回0-6 0是周1'
    if isinstance(年份, int) != True or isinstance(月份, int) != True:
        print('时间_取某月一号星期几：传入列表有误')
        return -1
    try:
        return calendar.monthrange(年份, 月份)[0]
    except Exception as error:
        print('时间_取某月一号星期几：运行出错|' + str(error))
        return -1


def 时间_取某天星期几(年份, 月份, 日期):
    '失败返回-1,返回0-6 0是周1'
    if isinstance(年份, int) != True or isinstance(月份, int) != True or isinstance(日期, int) != True:
        print('时间_取某天星期几：传入列表有误')
        return -1
    try:
        return calendar.weekday(年份, 月份, 日期)
    except Exception as error:
        print('时间_取某天星期几：运行出错|' + str(error))
        return -1


def 时间_取现行时间datetime():
    '返回datetime格式的时间'
    return datetime.datetime.now()


def 时间_取随机时间戳():
    "返回字符串类型的随机时间戳,0-1中间的数"
    return str(random.random())


def 时间_格式化(原时间, 时间格式="%Y-%m-%d %H:%M:%S"):
    '失败返回False,传入datetime时间，返回字符串类型时间'
    if isinstance(原时间, (str, datetime.datetime)) != True or isinstance(时间格式, str) != True:
        print('时间_格式化：传入参数有误')
        return False
    try:
        if isinstance(原时间, str) == True:
            return datetime.datetime.strftime(datetime.datetime.strptime(原时间, "%Y-%m-%d %H:%M:%S"), 时间格式)
        else:
            return datetime.datetime.strftime(原时间, 时间格式)
    except Exception as error:
        print('时间_格式化：运行出错|' + str(error))
        return False


def 时间_文本转datetime时间(原时间, 时间格式="%Y-%m-%d %H:%M:%S"):
    '失败返回False,返回字符串时间,时间格式要跟原时间格式匹配'
    if isinstance(原时间, str) != True or isinstance(时间格式, str) != True:
        print('时间_文本转datetime时间：传入参数有误')
        return False
    try:
        return datetime.datetime.strptime(原时间, 时间格式)
    except Exception as error:
        print('时间_文本转datetime时间：运行出错|' + str(error))
        return False


def 时间_datetime时间转文本(原时间, 时间格式="%Y-%m-%d %H:%M:%S"):
    '失败返回False'
    if isinstance(原时间, datetime.datetime) != True or isinstance(时间格式, str) != True:
        print('时间_datetime时间转文本：传入参数有误')
        return False
    try:
        return 原时间.strftime("%Y-%m-%d %H:%M:%S")
    except Exception as error:
        print('时间_datetime时间转文本：运行出错|' + str(error))
        return False


def 时间_增减datetime(原时间, 增减部分, 增减数值, 操作类型=True):
    "失败返回False,返回datetime类型的时间,增减部分：1是星期,2是天,3是时,4是分,5是秒,6是毫秒,加时间就传正数,减时间传负数,操作类型：增加时间为True减少为False"
    if isinstance(原时间, datetime.datetime) != True or isinstance(增减部分, int) != True or isinstance(增减数值,
                                                                                                 int) != True or isinstance(
        操作类型, bool) != True:
        print('时间_增减datetime：传入参数有误')
        return False
    try:
        if 增减部分 == 1:
            时间差 = datetime.timedelta(weeks=增减数值)
        elif 增减部分 == 2:
            时间差 = datetime.timedelta(days=增减数值)
        elif 增减部分 == 3:
            时间差 = datetime.timedelta(hours=增减数值)
        elif 增减部分 == 4:
            时间差 = datetime.timedelta(minutes=增减数值)
        elif 增减部分 == 5:
            时间差 = datetime.timedelta(seconds=增减数值)
        elif 增减部分 == 6:
            时间差 = datetime.timedelta(milliseconds=增减数值)

        if 操作类型 == True:
            return 原时间 + 时间差
        else:
            return 原时间 - 时间差
    except Exception as error:
        print('时间_增减datetime：运行出错|' + str(error))
        return False


def 时间_取上月最后一天(年份=None, 月份=None):
    "失败返回False,返回datetime格式时间,年月格式为整数型如：年 2019 月 4,默认返回上个月的"
    if 年份 != None and 月份 != None:
        if isinstance(年份, (str, int)) != True or isinstance(月份, (str, int)) != True:
            print('时间_取上月最后一天：传入参数有误')
            return False
        try:
            return datetime.date(int(年份), int(月份), 1) - datetime.timedelta(1)
        except Exception as error:
            print('时间_取上月最后一天：运行出错|' + str(error))
            return False
    else:
        return datetime.date(datetime.date.today().year, datetime.date.today().month, 1) - datetime.timedelta(1)


def 时间_取时间间隔(原时间, 对比时间):
    "失败返回0,传入字符串类型的时间,可以用时间_取现行时间time获取,返回秒数,整数型"
    if isinstance(原时间, str) != True or isinstance(对比时间, str) != True:
        print('时间_取时间间隔：传入参数有误')
        return 0
    try:
        return int(time.mktime(time.strptime(对比时间, "%Y-%m-%d %H:%M:%S"))) - int(
            time.mktime(time.strptime(原时间, "%Y-%m-%d %H:%M:%S")))
    except Exception as error:
        print('时间_取时间间隔：运行出错|' + str(error))
        return 0


def 时间_时间转时间戳(原时间, 时间格式="%Y-%m-%d %H:%M:%S"):
    "失败返回空文本,传入字符串类型时间 时间_取现行时间time 命令获取 返回十位字符串类型时间戳"
    if isinstance(原时间, str) != True or isinstance(时间格式, str) != True:
        print('时间_时间到时间戳：传入参数有误')
        return ''
    try:
        return str(int(time.mktime(time.strptime(原时间, 时间格式))))
    except Exception as error:
        print('时间_时间到时间戳：运行出错|' + str(error))
        return ''


def 时间_时间戳转时间(时间戳, 格式='%Y:%m:%d %H:%M:%S'):
    '失败返回空文本,时间戳转换成时间文本，支持10位13位时间戳'
    if isinstance(时间戳, (str, int)) != True or isinstance(格式, str) != True:
        print('时间_时间戳转时间：传入的参数有误')
        return ''
    try:
        if len(str(时间戳)) == 13 and str(时间戳).isdigit() == True:
            return time.strftime(格式, time.localtime(int(int(时间戳) / 1000)))
        elif len(str(时间戳)) == 10 and str(时间戳).isdigit() == True:
            return time.strftime(格式, time.localtime(int(时间戳)))
        else:
            print("时间_时间戳转时间：传入的时间戳有误")
            return ''
    except Exception as error:
        print('时间_时间戳转时间：运行出错|' + str(error))
        return ''


def 时间_取现行时间戳(是否取十位=False):
    "返回字符串类型时间戳,默认取十三位时间戳"
    if 是否取十位 == True:
        return str(round(time.time()))
    else:
        return str(round(time.time() * 1000))


def 队列_创建队列(队列大小=0, Lifo=False):
    '如果maxsize小于1就表示队列长度无限,Lifo为真则队列是后进先出'
    if isinstance(队列大小, int) != True or isinstance(Lifo, bool) != True:
        return '队列_创建队列：传入参数有误'
    elif Lifo == False:
        return queue.Queue(maxsize=队列大小)
    else:
        return queue.LifoQueue(maxsize=队列大小)


def 队列_加入成员(队列, 要加入的值):
    '成功返回True,失败返回False'
    if isinstance(队列, (queue.Queue, queue.LifoQueue)) != True:
        print('队列_加入成员：传入参数有误')
        return False
    try:
        队列.put(要加入的值)
        return True
    except Exception as error:
        print('队列_加入成员：运行出错|' + str(error))
        return False


def 队列_取出成员(队列):
    "失败返回空文本,取出队列最前面或最后的一个值"
    if isinstance(队列, (queue.Queue, queue.LifoQueue)) != True:
        print('队列_加入成员：传入参数有误')
        return ''
    if 队列.qsize() <= 0:
        return ""
    else:
        return 队列.get()


def 队列_取队列成员数(队列):
    '失败返回0'
    if isinstance(队列, (queue.Queue, queue.LifoQueue)) != True:
        print('队列_取队列成员数：传入参数有误')
        return 0
    return 队列.qsize()


def 队列_清空队列(队列):
    '返回True,False'
    if isinstance(队列, (queue.Queue, queue.LifoQueue)) != True:
        print('队列_清空队列：传入参数有误')
        return False
    队列.queue.clear()
    return True


def 队列_是否为空(队列):
    '返回True,False'
    if isinstance(队列, (queue.Queue, queue.LifoQueue)) != True:
        print('队列_是否为空：传入参数有误')
        return False
    return 队列.empty()


def 队列_是否已满(队列):
    '返回True,False'
    if isinstance(队列, (queue.Queue, queue.LifoQueue)) != True:
        print('队列_是否已满：传入参数有误')
        return False
    return 队列.full()


def 正则_匹配(原文本, 匹配规则):
    '失败返回空列表,匹配成功返回匹配到的列表'
    if isinstance(原文本, str) != True or isinstance(匹配规则, str) != True:
        print('正则_匹配：传入的参数有误')
        return []
    try:
        return re.findall(匹配规则, 原文本)
    except Exception as error:
        print('正则_匹配：运行出错|' + str(error))
        return []


def 编码_编码(欲编码的内容, 编码格式='UTF-8', 错误处理='strict'):
    '失败返回空文本'
    if isinstance(欲编码的内容, str) != True or isinstance(错误处理, str) != True:
        print('编码_编码：传入的参数有误')
        return ''
    try:
        return 欲编码的内容.encode(encoding=编码格式, errors=错误处理)
    except Exception as error:
        print('编码_编码：运行出错|' + str(error))
        return ''


def 编码_解码(欲解码的内容, 解码格式='UTF-8', 错误处理='strict'):
    '失败返回空文本'
    if isinstance(欲解码的内容, str) != True or isinstance(错误处理, str) != True:
        print('编码_解码：传入的参数有误')
        return ''
    try:
        return 欲解码的内容.decode(encoding=解码格式, errors=错误处理)
    except Exception as error:
        print('编码_解码：运行出错|' + str(error))
        return ''


def 编码_UTF8编码(欲编码的内容):
    '失败返回空文本'
    if isinstance(欲遍码的内容, str) != True:
        print('编码_UTF8编码：传入的参数有误')
        return ''
    return 欲编码的内容.encode(encoding='UTF-8', errors='strict')


def 编码_UTF8解码(欲解码的内容):
    '失败返回空文本'
    if isinstance(欲解码的内容, str) != True:
        print('编码_UTF8解码：传入的参数有误')
        return ''
    return 欲解码的内容.decode(encoding='UTF-8', errors='strict')


def 编码_GBK编码(欲编码的内容):
    '失败返回空文本'
    if isinstance(欲编码的内容, str) != True:
        print('编码_GBK编码：传入的参数有误')
        return ''
    return 欲编码的内容.encode(encoding='GBK', errors='strict')


def 编码_GBK解码(欲解码的内容):
    '失败返回空文本'
    if isinstance(欲解码的内容, str) != True:
        print('编码_GBK解码：传入的参数有误')
        return ''
    return 欲解码的内容.decode(encoding='GBK', errors='strict')


def 编码_URL编码(欲编码的内容):
    '失败返回空文本'
    if isinstance(欲编码的内容, str) != True:
        print('编码_URL编码：传入的参数有误')
        return ''
    return parse.quote(欲编码的内容)


def 编码_URL解码(欲解码的内容):
    '失败返回空文本'
    if isinstance(欲解码的内容, str) != True:
        print('编码_URL解码：传入的参数有误')
        return ''
    return parse.unquote(欲解码的内容)


def 编码_ANSI到USC2(欲编码的内容):
    '失败返回空文本'
    if isinstance(欲编码的内容, (str, int)) != True:
        print('编码_ANSI到USC2：传入的参数有误')
        return ''
    return ascii(欲编码的内容)


def 编码_USC2到ANSI(欲编码的内容):
    '失败返回空文本'
    if isinstance(欲编码的内容, str) != True:
        print('编码_USC2到ANSI：传入的参数有误')
        return ''
    return 欲编码的内容.encode('utf-8').decode('unicode_escape')


def 编码_BASE64编码(欲编码的内容):
    '失败返回空文本'
    if isinstance(欲编码的内容, str) != True:
        print('编码_BASE64编码：传入的参数有误')
        return ''
    return base64.b64encode(欲编码的内容.encode('UTF-8')).decode("UTF-8")


def 编码_BASE64解码(欲解码的内容):
    '失败返回空文本'
    if isinstance(欲解码的内容, str) != True:
        print('编码_BASE64解码：传入的参数有误')
        return ''
    return base64.b64decode(欲解码的内容).decode("UTF-8")


def 加密_MD5(要加密的内容, 编码="utf-8"):
    '失败返回空文本'
    if isinstance(要加密的内容, str) != True or isinstance(编码, str) != True:
        print('加密_MD5：传入的参数有误')
        return ''
    try:
        MD5 = hashlib.md5()
        MD5.update(要加密的内容.encode(encoding=编码))
        return MD5.hexdigest()
    except Exception as error:
        print('加密_MD5：运行出错|' + str(error))
        return ''


def 加密_SHA(要加密的内容, 方式="SHA1"):
    '失败返回空文本,支持SHA1 224 256 384 512'
    if isinstance(要加密的内容, str) != True or isinstance(方式, str) != True:
        print('加密_SHA：传入的参数有误')
        return ''
    elif 方式 == "SHA1":
        sha = hashlib.sha1()
    elif 方式 == "SHA224":
        sha = hashlib.sha224()
    elif 方式 == "SHA256":
        sha = hashlib.sha256()
    elif 方式 == "SHA384":
        sha = hashlib.sha384()
    elif 方式 == "SHA512":
        sha = hashlib.sha512()
    else:
        print('加密_SHA：加密方式有误')
        return ''
    sha.update(str(要加密的内容).encode('utf-8'))
    return sha.hexdigest()


def 加密_SHA3(要加密的内容, 方式="SHA224"):
    '失败返回空文本,支持224 256 384 512'
    if isinstance(要加密的内容, str) != True or isinstance(方式, str) != True:
        print('加密_SHA3：传入的参数有误')
        return ''
    elif 方式 == "SHA224":
        sha = hashlib.sha3_224()
    elif 方式 == "SHA256":
        sha = hashlib.sha3_256()
    elif 方式 == "SHA384":
        sha = hashlib.sha3_384()
    elif 方式 == "SHA512":
        sha = hashlib.sha3_512()
    else:
        print('加密_SHA3：加密方式有误')
        return ''
    sha.update(要加密的内容.encode('utf-8'))
    return sha.hexdigest()


def 加密_HmacSHA256(key, 加密内容):
    '失败出错返回空文本'
    if isinstance(key, str) != True:
        print('加密_HmacSHA256：传入参数有误')
        return ''
    try:
        return base64.b64encode(hmac.new(bytes(key, encoding='utf-8'), bytes(加密内容, encoding='utf-8'),
                                         digestmod=hashlib.sha256).digest()).decode("utf-8")
    except Exception as error:
        print('加密_HmacSHA256：运行出错|' + str(error))
        return ''


def 加密_CRC32(要加密的内容):
    '失败返回空文本'
    if isinstance(要加密的内容, str) != True:
        print('加密_CRC32：传入的参数有误')
        return ''
    return binascii.crc32(要加密的内容.encode("utf-8"))


def JS_调试(JS代码, 方法名, 参数1=None, 参数2=None, 参数3=None, 参数4=None, 参数5=None, 参数6=None, 参数7=None, 参数8=None, 参数9=None,
          参数10=None):
    '失败返回空文本,用*args不知道怎么分配给下面参数'
    if isinstance(JS代码, str) != True or isinstance(方法名, str) != True:
        print('JS_调试：传入参数有误')
        return ''
    try:
        return execjs.compile(JS代码).call(方法名, 参数1, 参数2, 参数3, 参数4, 参数5, 参数6, 参数7, 参数8, 参数9, 参数10)
    except Exception as error:
        print('JS_调试：运行出错|' + str(error))
        return ''


def JS_加载(JS代码):
    '失败返回False,成功返回个对象给JS_运行调用'
    if isinstance(JS代码, str) != True:
        print('JS_加载：传入参数有误')
        return False
    try:
        return execjs.compile(JS代码)
    except Exception as error:
        print('JS_加载：运行出错|' + str(error))
        return False


def JS_运行(JS对象, 方法名, 参数1=None, 参数2=None, 参数3=None, 参数4=None, 参数5=None, 参数6=None, 参数7=None, 参数8=None, 参数9=None,
          参数10=None):
    ',失败返回空文本,通过JS_加载返回的对象'
    if isinstance(JS对象, execjs._external_runtime.ExternalRuntime.Context) != True or isinstance(方法名, str) != True:
        print('JS_加载：传入参数有误')
        return ''
    try:
        return JS对象.call(方法名, 参数1, 参数2, 参数3, 参数4, 参数5, 参数6, 参数7, 参数8, 参数9, 参数10)
    except Exception as error:
        print('JS_运行：运行出错|' + str(error))
        return ''


def GZIP_压缩(欲压缩的字节):
    '失败返回空字节'
    if isinstance(欲压缩的字节, bytes) != True:
        print('GZIP_压缩：传入的参数有误')
        return bytes()
    try:
        return gzip.compress(欲压缩的字节)
    except Exception as error:
        print('GZIP_压缩：运行出错|' + str(error))
        return bytes()


def GZIP_解压(欲解压的字节):
    '失败返回空字节'
    if isinstance(欲解压的字节, bytes) != True:
        print('GZIP_解压：传入的参数有误')
        return bytes()
    try:
        return gzip.decompress(欲解压的字节)
    except Exception as error:
        print('GZIP_解压：运行出错|' + str(error))
        return bytes()


def 文件_取运行目录():
    '返回当前运行目录'
    return os.getcwd()


def 文件_更改当前工作目录(路径):
    '成功返回True,失败返回False'
    if isinstance(路径, str) != True:
        print('文件_更改当前工作目录：传入参数有误')
        return False
    try:
        os.chdir(路径)
        return True
    except Exception as error:
        print('文件_更改当前工作目录：运行出错|' + str(error))
        return False


def 文件_更改当前进程目录(路径):
    '成功返回True,失败返回False'
    if isinstance(路径, str) != True:
        print('文件_更改当前进程目录：传入参数有误')
        return False
    try:
        os.chroot(路径)
        return True
    except Exception as error:
        print('文件_更改当前进程目录：运行出错|' + str(error))
        return False


def 文件_遍历指定路径文件(路径='.'):
    '失败返回空列表,.为单前目录，..为上级目录，返回列表格式不带路径的文件名'
    if isinstance(路径, str) != True:
        print('文件_遍历指定路径文件：传入参数有误')
        return []
    try:
        return os.listdir(路径)
    except Exception as error:
        print('文件_遍历指定路径文件：运行出错|' + str(error))
        return []


def 文件_遍历指定路径所有子目录(路径='.'):
    '失败返回空元组,成功返回一个三元组：(路径, [包含目录], [包含文件]),用法 for root, dirs, files in os.walk("..", topdown=False):'
    if isinstance(路径, str) != True:
        print('文件_遍历指定路径所有子目录：传入参数有误')
        return ()
    try:
        return os.walk(路径)
    except Exception as error:
        print('文件_遍历指定路径所有子目录：运行出错|' + str(error))
        return ()


def 文件_创建单层目录(路径):
    '成功返回True,失败返回False,创建单层目录，如该目录已存在抛出异常'
    if isinstance(路径, str) != True:
        print('文件_创建单层目录：传入参数有误')
        return False
    try:
        os.mkdir(路径)
        return True
    except Exception as error:
        print('文件_创建单层目录：运行出错|' + str(error))
        return False


def 文件_创建多层目录(路径):
    '成功返回True,失败返回False,创建单层目录，如该目录已存在抛出异常'
    if isinstance(路径, str) != True:
        print('文件_创建多层目录：传入参数有误')
        return False
    try:
        os.makedirs(路径)
        return True
    except Exception as error:
        print('文件_创建多层目录：运行出错|' + str(error))
        return False


def 文件_删除文件(路径):
    '成功返回True,失败返回False'
    if isinstance(路径, str) != True:
        print('文件_删除文件：传入参数有误')
        return False
    try:
        os.remove(路径)
        return True
    except Exception as error:
        print('文件_删除文件：运行出错|' + str(error))
        return False


def 文件_删除文件2(路径):
    '成功返回True,失败返回False,用于删除文件,如果文件是一个目录则返回一个错误'
    if isinstance(路径, str) != True:
        print('文件_删除文件：传入参数有误')
        return False
    try:
        os.unlink(路径)
        return True
    except Exception as error:
        print('文件_删除文件：运行出错|' + str(error))
        return False


def 文件_删除单层空目录(路径):
    '成功返回True,失败返回False,删除单层目录，如该目录非空则抛出异常'
    if isinstance(路径, str) != True:
        print('文件_删除单层空目录：传入参数有误')
        return False
    try:
        os.rmdir(路径)
        return True
    except Exception as error:
        print('文件_删除单层空目录：运行出错|' + str(error))
        return False


def 文件_删除多层空目录(路径):
    '成功返回True,失败返回False,递归删除目录，从子目录到父目录逐层尝试删除，遇到目录非空则抛出异常'
    if isinstance(路径, str) != True:
        print('文件_删除多层空目录：传入参数有误')
        return False
    try:
        os.removedirs(路径)
        return True
    except Exception as error:
        print('文件_删除多层空目录：运行出错|' + str(error))
        return False


def 文件_获取访问修改时间(路径):
    '失败返回False,成功返回对象.st_atime 是访问时间 返回对象.st_mtime 是修改时间，返回的是10位时间戳'
    if isinstance(路径, str) != True:
        print('文件_获取访问修改时间：传入参数有误')
        return False
    try:
        return os.stat(路径)
    except Exception as error:
        print('文件_获取访问修改时间：运行出错|' + str(error))
        return False


def 文件_设置访问修改时间(路径, 访问修改时间):
    '成功返回True,失败返回False,传入的修改时间为10位时间戳元组类型(访问时间戳,修改时间戳)'
    if isinstance(路径, str) != True or isinstance(访问修改时间, tuple) != True:
        print('文件_设置访问修改时间：传入参数有误')
        return False
    try:
        os.utime(路径, 访问修改时间)
        return True
    except Exception as error:
        print('文件_设置访问修改时间：运行出错|' + str(error))
        return False


def 文件_重命名(原文件名, 新文件名):
    '成功返回True,失败返回False'
    if isinstance(原文件名, str) != True or isinstance(新文件名, str) != True:
        print('文件_重命名：传入参数有误')
        return False
    try:
        os.rename(原文件名, 新文件名)
        return True
    except Exception as error:
        print('文件_重命名：运行出错|' + str(error))
        return False


def 文件_修改权限(路径, 权限类型=0):
    '成功返回True,失败返回False,权限类型： 0 设为只读 1 取消只读,更多权限参考 http://www.runoob.com/python/os-chmod.html'
    if isinstance(路径, str) != True or isinstance(权限类型, int) != True:
        print('文件_修改权限：传入参数有误')
        return False
    try:
        if 权限类型 == 0:
            os.chmod(路径, stat.S_IREAD)
            return True
        elif 权限类型 == 1:
            os.chmod(路径, stat.S_IWRITE)
            return True
        else:
            print('文件_修改权限：传入参数有误')
            return False
    except Exception as error:
        print('文件_修改权限：运行出错|' + str(error))
        return False


def 文件_是否为绝对路径(路径):
    '传入路径返回True或False'
    if isinstance(路径, str) != True:
        print('文件_是否为绝对路径：传入参数有误')
        return False
    try:
        return os.path.isabs(路径)
    except Exception as error:
        print('文件_是否为绝对路径：运行出错|' + str(error))
        return False


def 文件_是否为目录(路径):
    '传入路径返回True或False'
    if isinstance(路径, str) != True:
        print('文件_是否为目录：传入参数有误')
        return False
    try:
        return os.path.isdir(路径)
    except Exception as error:
        print('文件_是否为目录：运行出错|' + str(error))
        return False


def 文件_是否为文件(路径):
    '传入路径返回True或False'
    if isinstance(路径, str) != True:
        print('文件_是否为文件：传入参数有误')
        return False
    try:
        return os.path.isfile(路径)
    except Exception as error:
        print('文件_是否为文件：运行出错|' + str(error))
        return False


def 文件_是否存在(路径):
    '传入路径返回True或False'
    if isinstance(路径, str) != True:
        print('文件_是否存在：传入参数有误')
        return False
    try:
        return os.path.exists(路径)
    except Exception as error:
        print('文件_是否存在：运行出错|' + str(error))
        return False


def 文件_取文件大小(路径):
    '返回文件长度,失败返回-1'
    if isinstance(路径, str) != True:
        print('文件_取文件大小：传入参数有误')
        return -1
    try:
        return os.path.getsize(路径)
    except Exception as error:
        print('文件_取文件大小：运行出错|' + str(error))
        return -1


def 文件_取最近访问时间(路径):
    '返回时间戳,失败返回0'
    if isinstance(路径, str) != True:
        print('文件_取最近访问时间：传入参数有误')
        return 0
    try:
        return os.path.getatime(路径)
    except Exception as error:
        print('文件_取最近访问时间：运行出错|' + str(error))
        return 0


def 文件_取创建时间(路径):
    '返回时间戳,失败返回0'
    if isinstance(路径, str) != True:
        print('文件_取创建时间：传入参数有误')
        return 0
    try:
        return os.path.ctime(路径)
    except Exception as error:
        print('文件_取创建时间：运行出错|' + str(error))
        return 0


def 文件_取修改时间(路径):
    '返回时间戳,失败返回0'
    if isinstance(路径, str) != True:
        print('文件_取修改时间：传入参数有误')
        return 0
    try:
        return os.path.mtime(路径)
    except Exception as error:
        print('文件_取修改时间：运行出错|' + str(error))
        return 0


def 文件_取文件目录(路径):
    '失败返回空文本,去掉文件名，返回目录路径'
    if isinstance(路径, str) != True:
        print('文件_取文件目录：传入参数有误')
        return ''
    try:
        return os.path.dirname(路径)
    except Exception as error:
        print('文件_取文件目录：运行出错|' + str(error))
        return ''


def 文件_取路径文件名(路径):
    '失败返回空文本,去掉目录路径，返回文件名'
    if isinstance(路径, str) != True:
        print('文件_取路径文件名：传入参数有误')
        return ''
    try:
        return os.path.basename(路径)
    except Exception as error:
        print('文件_取路径文件名：运行出错|' + str(error))
        return ''


def 文件_文件扩展名分割(路径):
    '失败返回空元组,传入文件路径,返回元组类型 (文件名,扩展名)'
    if isinstance(路径, str) != True:
        print('文件_文件扩展名分割：传入参数有误')
        return ()
    try:
        return os.path.splitext(路径)
    except Exception as error:
        print('文件_文件扩展名分割：运行出错|' + str(error))
        return ()


def 文件_目录文件名分割(路径):
    '失败返回空元组,传入路径,返回元组类型 (目录,文件名)'
    if isinstance(路径, str) != True:
        print('文件_目录文件名分割：传入参数有误')
        return ()
    try:
        return os.path.split(路径)
    except Exception as error:
        print('文件_目录文件名分割：运行出错|' + str(error))
        return ()


def 文件_创建文件(路径):
    '成功返回True,失败返回False,创建空文件'
    if isinstance(路径, str) != True:
        print('文件_创建文件：传入参数有误')
        return False
    try:
        文件_写入文件(路径, '', 'w')
        return True
    except Exception as error:
        print('文件_创建文件：运行出错|' + str(error))
        return False


def 文件_检测权限(路径, 权限类型=0):
    '权限类型：0 是否存在 1 是否可读 2 是否可写 3 是否可执行，返回True或False'
    if isinstance(路径, str) != True or isinstance(权限类型, int) != True:
        print('文件_是否有权限：传入参数有误')
        return False
    try:
        if 权限类型 == 0:
            return os.access(路径, os.F_OK)
        elif 权限类型 == 1:
            return os.access(路径, os.R_OK)
        elif 权限类型 == 2:
            return os.access(路径, os.W_OK)
        elif 权限类型 == 3:
            return os.access(路径, os.X_OK)
        else:
            print('文件_是否有权限：传入参数有误')
            return False
    except Exception as error:
        print('文件_是否有权限：运行出错|' + str(error))
        return False


def 文件_写入文件(文件名, 写入的数据, 方式='a'):
    '成功返回True,失败返回False,如果文件不存在会创建新文件,方式默认为a 追加写入 覆盖写入用w'
    if isinstance(文件名, str) != True or isinstance(方式, str) != True:
        print('文件_写入文件：传入参数有误')
        return False
    try:
        with open(文件名, 方式, encoding="utf-8") as a:
            a.write(写入的数据)
        return True
    except Exception as error:
        print('文件_写入文件：运行出错|' + str(error))
        return False


def 文件_读取文件(文件名, 读取长度=-1, 方式='r'):
    '失败返回False,方式默认用r 二进制用rb 长度默认读取全部'
    if isinstance(文件名, str) != True or isinstance(方式, str) != True or isinstance(读取长度, int) != True:
        print('文件_读取文件：传入参数有误')
        return False
    try:
        with open(文件名, 方式, encoding="utf-8") as a:
            return a.read(读取长度)
    except Exception as error:
        print('文件_读取文件：运行出错|' + str(error))
        return False


def 文件_读取某行(文件名, 行位置=0, 方式='r'):
    '失败返回False,方式默认用r 二进制用rb,这里的行位置是字符串的位置 可以用寻找文本定位位置取出那一行,返回的是列表'
    if isinstance(文件名, str) != True or isinstance(方式, str) != True or isinstance(行位置, int) != True:
        print('文件_读取某行：传入参数有误')
        return False
    try:
        if 行位置 < 1:
            with open(文件名, 方式, encoding="utf-8") as a:
                return a.readline()
        else:
            with open(文件名, 方式, encoding="utf-8") as a:
                return a.readlines(行位置)
    except Exception as error:
        print('文件_读取某行：运行出错|' + str(error))
        return False


def 数据_排列(列表, 长度):
    '失败返回空列表,生产多种不相同组合，返回列表，列表里每个成员是元组'
    if isinstance(列表, list) != True or isinstance(长度, int) != True:
        print('数据_排列：传入参数有误')
        return []
    try:
        return list(itertools.permutations(列表, 长度))
    except Exception as error:
        print('数据_排列：运行出错|' + str(error))
        return []


def 数据_组合(列表, 长度):
    '失败返回空列表,生产多种不相同组合，但不会使用相同数值做顺序不一样的组合，返回列表，列表里每个成员是元组'
    if isinstance(列表, list) != True or isinstance(长度, int) != True:
        print('数据_组合：传入参数有误')
        return []
    try:
        return list(itertools.combinations(列表, 长度))
    except Exception as error:
        print('数据_组合：运行出错|' + str(error))
        return []


def 数据_排列组合(列表, 长度):
    '失败返回空列表,没看懂先放着吧'
    if isinstance(列表, list) != True or isinstance(长度, int) != True:
        print('数据_排列组合：传入参数有误')
        return []
    try:
        return list(itertools.product(列表, 长度))
    except Exception as error:
        print('数据_排列组合：运行出错|' + str(error))
        return []


def 进制_十到二(原内容):
    '失败返回空文本'
    if isinstance(原内容, int) != True:
        print('进制_十到二：传入参数有误')
        return ''
    try:
        return bin(原内容)
    except Exception as error:
        print('进制_十到二：运行出错|' + str(error))
        return ''


def 进制_十到八(原内容):
    '失败返回空文本'
    if isinstance(原内容, int) != True:
        print('进制_十到八：传入参数有误')
        return ''
    try:
        return oct(原内容)
    except Exception as error:
        print('进制_十到八：运行出错|' + str(error))
        return ''


def 进制_十到十六(原内容):
    '失败返回空文本'
    if isinstance(原内容, int) != True:
        print('进制_十到十六：传入参数有误')
        return ''
    try:
        return hex(原内容)
    except Exception as error:
        print('进制_十到十六：运行出错|' + str(error))
        return ''


def 进制_二到十(原内容):
    '失败返回00'
    if isinstance(原内容, str) != True:
        print('进制_二到十：传入参数有误')
        return '00'
    try:
        return int(原内容, base=2)
    except Exception as error:
        print('进制_二到十：运行出错|' + str(error))
        return '00'


def 进制_八到十(原内容):
    '失败返回00'
    if isinstance(原内容, str) != True:
        print('进制_八到十：传入参数有误')
        return '00'
    try:
        return int(原内容, base=8)
    except Exception as error:
        print('进制_八到十：运行出错|' + str(error))
        return '00'


def 进制_十六到十(原内容):
    '失败返回00'
    if isinstance(原内容, str) != True:
        print('进制_十六到十：传入参数有误')
        return '00'
    try:
        return int(原内容, base=16)
    except Exception as error:
        print('进制_十六到十：运行出错|' + str(error))
        return '00'


def 网页_取外网IP(返回地区=False):
    '失败返回空文本,使用ip138接口,如果设置返回地区则返回两个参数,ip,地区'
    if isinstance(返回地区, bool) != True:
        print('网页_取外网IP：传入参数有误')
        return ''
    try:
        网页源码 = requests.get("http://www.ip138.com", verify=False, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36"})
        网页源码.encoding = 'gbk'
        网页源码 = requests.get(文本_取出中间文本(网页源码.text, '<iframe src="', '" rel="nofollow'), verify=False)
        if 返回地区 == False:
            return 文本_取出中间文本(网页源码.text, '是：[', ']')
        else:
            return 文本_取出中间文本(网页源码.text, '是：[', ']'), 文本_取出中间文本(网页源码.text, "来自：", "\r")
    except Exception as error:
        print("网页_取外网IP：运行出错|" + str(error))
        return ''


def 网页_取外网IP_S(返回地区=False):
    '失败返回空文本,使用sohu接口,如果设置返回地区则返回两个参数,ip,地区'
    if isinstance(返回地区, bool) != True:
        print('网页_取外网IP_S：传入参数有误')
        return ''
    try:
        网页源码 = requests.get("http://pv.sohu.com/cityjson", verify=False, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36"})
        if 返回地区 == False:
            return 文本_取出中间文本(网页源码.text, 'cip": "', '"')
        else:
            return 文本_取出中间文本(网页源码.text, 'cip": "', '"'), 文本_取出中间文本(网页源码.text, 'cname": "', '"')
    except Exception as error:
        print("网页_取外网IP_S：运行出错|" + str(error))
        return ''


def 网页_访问_对象(请求地址, 请求方式=0, 提交的内容='', 提交的COOKIE='', 提交的协议头={}, 允许重定向=True, 上传文件=None, 代理地址=None, 最长等待=30, 编码方式=None,
             证书验证=False):
    '请求方式：0是GET 1是POST.提交的内容跟提交的Cookie可以是字符串也可以是字典。返回的Cookie是文本型,返回的协议头是字典,证书验证：默认为False,需要引用证书时传入证书路径,上传文件传入文件路径'
    网页 = 网页类型()
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    http = requests.session()
    if type(上传文件) == str:
        try:
            files = {'file': open(上传文件, 'rb')}
        except:
            上传文件 = None
    else:
        上传文件 = None

    if 提交的协议头 == {} or 提交的协议头 == '':
        提交的协议头 = {"Accept": "*/*",
                  "Referer": 请求地址,
                  "Accept-Language": "zh-cn",
                  "Content-Type": "application/x-www-form-urlencoded",
                  "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36"}

    if type(提交的协议头) == str:
        if len(提交的协议头) > 3:
            协议头数组 = 文本_分割文本(提交的协议头, '\n')
            提交的协议头 = {}
            for x in 协议头数组:
                键 = 文本_删首尾指定字符(文本_取文本左边(x, ':'))
                值 = 文本_删首尾指定字符(文本_取文本右边(x, ':'))
                if 键 != '' and 值 != '':
                    提交的协议头[键] = 值
        else:
            提交的协议头 = {}

    if 请求方式 < 0 or 请求方式 > 1:
        请求方式 = 0
    if 最长等待 < 1 or 最长等待 > 60:
        最长等待 = 30
    if 代理地址 != None:
        代理地址 = {"http": "http://" + 代理地址, "https": "https://" + 代理地址}
    if 提交的COOKIE != '' and type(提交的COOKIE) == str:
        if 文本_寻找文本(提交的COOKIE, "=") == -1:
            提交的COOKIE = {}
        elif 文本_寻找文本(提交的COOKIE, ";") == -1:
            键 = 文本_删首尾指定字符(文本_取文本左边(提交的COOKIE, '='))
            值 = 文本_删首尾指定字符(文本_取文本右边(提交的COOKIE, '='))
            if 键 != '' and 值 != '':
                提交的COOKIE = {键: 值}
        else:
            COOKIE数组 = 文本_分割文本(提交的COOKIE, ';')
            提交的COOKIE = {}
            for x in COOKIE数组:
                键 = 文本_删首尾指定字符(文本_取文本左边(x, '='))
                值 = 文本_删首尾指定字符(文本_取文本右边(x, '='))
                if 键 != '' and 值 != '':
                    提交的COOKIE[键] = 值
    try:
        if 请求方式 == 0:
            网页对象 = http.get(文本_删首尾指定字符(请求地址), params=提交的内容, cookies=提交的COOKIE, headers=提交的协议头, allow_redirects=允许重定向,
                            files=上传文件,
                            proxies=代理地址, timeout=最长等待, verify=证书验证)
        else:
            网页对象 = http.post(文本_删首尾指定字符(请求地址), data=提交的内容, cookies=提交的COOKIE, headers=提交的协议头, allow_redirects=允许重定向,
                             files=上传文件,
                             proxies=代理地址, timeout=最长等待, verify=证书验证)

        if 编码方式 != None:
            网页对象.encoding = 编码方式
        网页.源码 = 网页对象.text
        返回的COOKIE = ''
        返回的COOKIE字典 = dict(网页对象.cookies)
        for x in 返回的COOKIE字典:
            返回的COOKIE = 返回的COOKIE + x + '=' + 返回的COOKIE字典[x] + '; '
        网页.Cookie = 返回的COOKIE
        网页.状态码 = 网页对象.status_code
        网页.协议头 = 网页对象.headers
    except Exception as error:
        print('网页_访问_对象：运行出错|' + str(error))

    return 网页


def 网页_COOKIE合并更新(原COOKIE, 新COOKIE):
    '返回更新后的COOKIE,所有COOKIE格式均为文本型'
    if isinstance(原COOKIE, str) != True or isinstance(新COOKIE, str) != True:
        print('网页_COOKIE合并更新：传入参数有误')
        return ''
    try:
        更新后的COOKIE = {}
        if 文本_寻找文本(原COOKIE, "=") != -1 and 文本_寻找文本(原COOKIE, ";") == -1:
            键 = 文本_删首尾指定字符(文本_取文本左边(原COOKIE, '='))
            值 = 文本_删首尾指定字符(文本_取文本右边(原COOKIE, '='))
            if 键 != '' and 值 != '':
                更新后的COOKIE[键] = 值
        else:
            COOKIE数组 = 文本_分割文本(原COOKIE, ';')
            for x in COOKIE数组:
                键 = 文本_删首尾指定字符(文本_取文本左边(x, '='))
                值 = 文本_删首尾指定字符(文本_取文本右边(x, '='))
                if 键 != '' and 值 != '':
                    更新后的COOKIE[键] = 值

        if 文本_寻找文本(新COOKIE, "=") != -1 and 文本_寻找文本(新COOKIE, ";") == -1:
            键 = 文本_删首尾指定字符(文本_取文本左边(新COOKIE, '='))
            值 = 文本_删首尾指定字符(文本_取文本右边(新COOKIE, '='))
            if 键 != '' and 值 != '':
                更新后的COOKIE[键] = 值
        else:
            COOKIE数组 = 文本_分割文本(新COOKIE, ';')
            for x in COOKIE数组:
                键 = 文本_删首尾指定字符(文本_取文本左边(x, '='))
                值 = 文本_删首尾指定字符(文本_取文本右边(x, '='))
                if 键 != '' and 值 != '':
                    更新后的COOKIE[键] = 值

        返回的COOKIE = ''
        for x in 更新后的COOKIE:
            返回的COOKIE = 返回的COOKIE + x + '=' + 更新后的COOKIE[x] + '; '
        return 返回的COOKIE
    except Exception as error:
        print('网页_COOKIE合并更新：运行出错|' + str(error))
        return ''


def 启动线程(函数名, 元组参数=(), 跟随主线程结束=False):
    "成功返回线程对象,失败返回False,参数用元组形式传入,返回线程对象,daemon属性为False，主线程结束时会检测该子线程是否结束"
    if isinstance(元组参数, tuple) != True:
        print('启动线程：传入参数有误')
        return False
    try:
        线程 = threading.Thread(target=函数名, args=元组参数, daemon=跟随主线程结束)
        线程.start()
        return 线程
    except Exception as error:
        print('启动线程：运行出错|' + str(error))
        return False


def 创建线程许可证():
    return threading.Lock()


def 进入许可区(许可证):
    '许可证如果错误则无效'
    try:
        许可证.acquire()
    except Exception as error:
        print('进入许可区：运行出错|' + str(error))
        return False


def 退出许可区(许可证):
    '许可证如果错误则无效'
    try:
        许可证.release()
    except Exception as error:
        print('退出许可区：运行出错|' + str(error))
        return False


def 程序_延时(延迟秒数):
    '延迟时间，可以用小数'
    if isinstance(延迟秒数, (int, float)) != True:
        print('程序_延时：传入参数有误')
        return False
    elif 延迟秒数 < 0:
        延迟秒数 = 1
    time.sleep(延迟秒数)


def 程序_退出():
    '终止当前进程,不知道有没有效'
    os.exit()


def 讯代理_计算协议头(单号, 秘钥):
    '失败返回空,返回讯代理Proxy-Authorization的完整值'
    if isinstance(单号, str) != True or isinstance(秘钥, str) != True:
        print('讯代理_计算协议头：传入参数有误')
        return ''
    时间戳 = 时间_取现行时间戳(True)
    sign = 加密_MD5("orderno=" + 单号 + "," + "secret=" + 秘钥 + "," + "timestamp=" + 时间戳).upper()
    return "sign=" + sign + "&" + "orderno=" + 单号 + "&" + "timestamp=" + 时间戳


def 系统_运行CMD命令(命令):
    '失败返回False,成功返回执行结果'
    if isinstance(命令, str) != True:
        print('系统_运行CMD命令：传入参数有误')
        return False
    try:
        f = os.popen('ipconfig')
        结果 = str(f.read())
        f.close()
        return 结果
    except Exception as error:
        print('系统_运行CMD命令：运行出错|' + str(error))
        return False


def 变量_取出随机元素(原参数):
    '失败返回False,注意,取出的类型看传入的参数,不一定是文本,可以传入字符 元组 列表'
    if isinstance(原参数, (str, list, tuple)) != True:
        print('变量_取出随机元素：传入参数有误')
        return False
    try:
        return random.choice(原参数)
    except Exception as error:
        print('变量_取出随机元素：运行出错|' + str(error))
        return False


def 信息框(标题='提示', 提示内容='你好易语言', 类型=0):
    '失败返回-1,,请在窗口代码下调用,0普通信息框,1带确认取消信息框,2黄色警告,3红色错误,4黄色警告重试'
    if isinstance(标题, str) != True or isinstance(提示内容, str) != True or isinstance(类型, int) != True or 类型 < 0 or 类型 > 4:
        print('信息框：传入参数有误')
        return -1
    try:
        if 类型 == 0:
            return messagebox.showinfo(标题, 提示内容)
        elif 类型 == 1:
            return messagebox.askokcancel(标题, 提示内容)  # 确定返回True 取消返回False
        elif 类型 == 2:
            return messagebox.showwarning(标题, 提示内容)
        elif 类型 == 3:
            return messagebox.showerror(标题, 提示内容)
        elif 类型 == 4:
            return messagebox.askretrycancel(标题, 提示内容)  # 重试返回True 取消返回False
    except Exception as error:
        print('信息框：运行出错|' + str(error))
        return -1


class 线程:
    def __init__(self):
        self.__线程列表 = []

    def 多线程(self, 函数名, 任务数, 线程数, 元组参数=(), 最长等待时间=0, 跟随主线程结束=False):
        '顺利执行返回True,否则返回False'
        if isinstance(任务数, int) != True or isinstance(线程数, int) != True or isinstance(元组参数,
                                                                                      tuple) != True or isinstance(
            最长等待时间, int) != True or isinstance(跟随主线程结束, bool) != True:
            print('多线程：传入参数有误')
            return False
        __多线程列表 = []
        剩余数 = 任务数
        try:
            while 剩余数 > 0:
                for x in __多线程列表:
                    if x.is_alive() == False:
                        __多线程列表.remove(x)
                if len(__多线程列表) >= 线程数:
                    time.sleep(0.1)
                else:
                    线程 = threading.Thread(target=函数名, args=元组参数, daemon=跟随主线程结束)
                    线程.start()
                    __多线程列表.append(线程)
                    剩余数 = 剩余数 - 1

            for i in __多线程列表:
                if 最长等待时间 <= 0:
                    i.join()
                else:
                    i.join(最长等待时间)
            print("多线程：任务全部执行完毕")
            return True
        except Exception as error:
            print('多线程：运行出错|' + str(error))
            return False

    def 启动线程(self, 函数名, 元组参数=(), 跟随主线程结束=False):
        "失败返回False,成功返回线程对象,参数用元组形式传入,daemon属性为False，主线程结束时会检测该子线程是否结束"
        if isinstance(元组参数, tuple) != True or isinstance(跟随主线程结束, bool) != True:
            print('启动线程：传入参数有误')
            return False
        try:
            线程 = threading.Thread(target=函数名, args=元组参数, daemon=跟随主线程结束)
            线程.start()
            self.__线程列表.append(线程)
            return 线程
        except Exception as error:
            print('启动线程：运行出错|' + str(error))
            return False

    def 等待线程结束(self, 最长等待时间=0):
        '顺利结束返回True,出错返回False如果启动线程参数daemon设置为True,则可以设置最长等待时间,超过时间强制结束线程'
        if isinstance(最长等待时间, (int, float)) != True:
            print('等待线程结束：传入参数有误')
            return False
        try:
            for i in self.__线程列表:
                if 最长等待时间 <= 0:
                    i.join()
                else:
                    i.join(最长等待时间)
            return True
        except Exception as error:
            print('等待线程结束：运行出错|' + str(error))
            return False

    def 取运行的线程数(self):
        '只返回该类创建后使用该类启动线程创建的线程数量'
        try:
            for x in self.__线程列表:
                if x.is_alive() == False:
                    self.__线程列表.remove(x)
            return len(self.__线程列表)
        except Exception as error:
            print('取运行的线程数：运行出错|' + str(error))
            return 0

    def 取运行中的线程对象(self):
        return threading.enumerate()

    def 线程是否在运行(self, 线程对象):
        '返回True或False'
        try:
            return 线程对象.is_alive()
        except Exception as error:
            print('线程是否在运行：运行出错|' + str(error))
            return False


class Mysql:

    def __init__(self):
        self.__数据库 = None
        self.__游标 = None
        self.__连接地址 = None
        self.__用户名 = None
        self.__密码 = None
        self.__数据库名 = None
        self.__端口号 = None
        self.__编码 = None
        self.__许可 = threading.Lock()

    def 连接(self, 连接地址, 用户名, 密码, 数据库名, 端口号, 编码='utf8'):
        '连接成功返回True,失败返回False'
        # self.__许可.acquire()
        if isinstance(连接地址, str) != True or isinstance(用户名, str) != True or isinstance(密码, str) != True or isinstance(
                数据库名, str) != True or isinstance(端口号, int) != True or isinstance(编码, str) != True:
            print('数据库_连接：传入参数有误')
            # self.__许可.release()
            return False
        try:
            self.__数据库 = pymysql.connect(host=连接地址, port=端口号, user=用户名, passwd=密码, db=数据库名, charset=编码)
            self.__游标 = self.__数据库.cursor()
            self.__连接地址 = 连接地址
            self.__用户名 = 端口号
            self.__密码 = 用户名
            self.__数据库名 = 密码
            self.__端口号 = 数据库名
            self.__编码 = 编码
            print('数据库连接成功')
            # self.__许可.release()
            return True
        except Exception as error:
            print('数据库_连接：运行出错|' + str(error))
            # self.__许可.release()
            return False

    def 关闭游标(self):
        '成功返回True,失败返回False'
        self.__许可.acquire()
        try:
            self.__游标.close()
            self.__许可.release()
            return True
        except Exception as error:
            print('数据库_关闭游标：运行出错|' + str(error))
            self.__许可.release()
            return False

    def 关闭连接(self):
        '成功返回True,失败返回False'
        self.__许可.acquire()
        try:
            self.__数据库.close()
            self.__许可.release()
            return True
        except Exception as error:
            print('数据库_关闭连接：运行出错|' + str(error))
            self.__许可.release()
            return False

    def 事务提交(self):
        '成功返回True,失败返回False'
        self.__许可.acquire()
        try:
            self.__数据库.commit()
            self.__许可.release()
            return True
        except Exception as error:
            print('数据库_事务提交：运行出错|' + str(error))
            self.__许可.release()
            return False

    def 事务回滚(self):
        '成功返回True,失败返回False'
        self.__许可.acquire()
        try:
            self.__数据库.rollback()
            self.__许可.release()
            return True
        except Exception as error:
            print('数据库_事务回滚：运行出错|' + str(error))
            self.__许可.release()
            return False

    def 执行SQL语句(self, Sql语句):
        '成功返回执行结果,失败返回False'
        self.__许可.acquire()
        if isinstance(Sql语句, str) != True:
            print('数据库_执行SQL语句：传入Sql语句有误')
            self.__许可.release()
            return False
        try:
            结果 = self.__游标.execute(Sql语句)
            self.__数据库.commit()
            self.__许可.release()
            return 结果
        except Exception as error:
            print('数据库_执行SQL语句：运行出错|' + str(error))
            self.__许可.release()
            return False

    def 获取所有记录列表(self):
        '成功返回一个列表,列表成员是元组,失败返回空列表'
        self.__许可.acquire()
        try:
            self.__许可.release()
            return self.__游标.fetchall()
        except Exception as error:
            print('数据库_获取所有记录列表：运行出错|' + str(error))
            self.__许可.release()
            return []

    def 保持在线(self):
        '返回True,False'
        self.__许可.acquire()
        try:
            self.__数据库.ping(reconnect=True)
            self.__许可.release()
            return True
        except Exception as error:
            self.__许可.release()
            return self.连接(连接地址=self.__连接地址, 用户名=self.__用户名, 密码=self.__密码, 数据库名=self.__数据库名, 端口号=self.__端口号,
                           编码=self.__编码)

    def 更新记录(self, 表名, 更新条件, 更新内容):
        "成功返回更新的数量,失败返回0,更新条件如果为空则全表更新"
        self.__许可.acquire()
        if isinstance(表名, str) != True or isinstance(更新条件, str) != True or isinstance(更新内容, str) != True:
            print('数据库_更新记录：传入参数有误')
            self.__许可.release()
            return 0
        Sql语句 = ""
        if 更新条件 == "":
            Sql语句 = "update " + 表名 + " set " + 更新内容
        else:
            Sql语句 = "update " + 表名 + " set " + 更新内容 + " where " + 更新条件 + ";"

        try:
            结果 = self.__游标.execute(Sql语句)
            self.__数据库.commit()
            self.__许可.release()
            return 结果
        except Exception as error:
            # self.__数据库.rollback()
            print('数据库_更新记录：运行出错|' + str(error))
            self.__许可.release()
            return 0

    def 查找记录(self, 表名, 字段名, 查找条件="", 搜索方式=0, 取出的数量=0, 排序=""):
        "失败返回空元组,字段名可以是* 表示全部字段,搜索方式 0为指定,1是模糊,取出的数量默认是0取出全部,排序order by 字段名 desc/asc"
        self.__许可.acquire()
        if isinstance(表名, str) != True or isinstance(字段名, str) != True or isinstance(查找条件, str) != True or isinstance(
                搜索方式, (str, int)) != True or isinstance(取出的数量, (str, int)) != True or isinstance(排序, str) != True:
            print('数据库_查找记录：传入参数有误')
            self.__许可.release()
            return ()
        文本 = ""
        Sql语句 = ""

        if str(搜索方式) == "0":
            if 查找条件 == "":
                Sql语句 = "select " + 字段名 + " from " + 表名
            else:
                Sql语句 = "select " + 字段名 + " from " + 表名 + " where " + 查找条件
        elif str(搜索方式) == "1":
            数组 = 查找条件.split(" and ")
            for x in 数组:
                文本 = 文本 + 文本_取文本左边(x, "=") + " like '%" + 文本_取出中间文本(x, "'", "'") + "%' and "
            Sql语句 = "select " + 字段名 + " from " + 表名 + " where " + 文本[0:len(文本) - 5]
        if 取出的数量 != 0:
            Sql语句 = Sql语句 + "limit " + str(取出的数量)
        Sql语句 = Sql语句 + 排序
        try:
            self.__游标.execute(Sql语句)
            结果 = self.__游标.fetchall()
            self.__数据库.commit()
            self.__许可.release()
            return 结果
        except Exception as error:
            # self.数据库.rollback()
            print('数据库_查找记录：运行出错|' + str(error))
            self.__许可.release()
            return ()

    def 增加记录(self, 表名, 字段名, 插入的内容):
        "失败返回-1,成功返回更新数量,字段名格式是 字段名,字段名  插入的内容格式是 ('123456','456789')多换后面带逗号跟换行"  # 传入字段跟内容示例 '字段1,字段2'    "(字段1值,字段2值)"
        self.__许可.acquire()
        if isinstance(表名, str) != True or isinstance(字段名, str) != True or isinstance(插入的内容, str) != True:
            print('数据库_增加记录：传入的参数有误')
            self.__许可.release()
            return -1
        Sql语句 = ""
        try:
            Sql语句 = "insert into " + 表名 + " " + "\n\n" + "( " + 字段名 + " )" + "\n\n" + "values" + "\n\n" + 插入的内容 + ";"
            结果 = self.__游标.execute(Sql语句)
            self.__数据库.commit()
            self.__许可.release()
            return 结果
        except Exception as error:
            # self.__数据库.rollback()
            print('数据库_增加记录：运行出错|' + str(error))
            self.__许可.release()
            return -1

    def 删除记录(self, 表名, 删除条件):
        '失败返回-1,成功返回删除数量'
        self.__许可.acquire()
        if isinstance(表名, str) != True or isinstance(删除条件, str) != True:
            print('数据库_删除记录：传入的参数有误')
            self.__许可.release()
            return -1
        try:
            sql语句 = "DELETE FROM " + 表名 + " WHERE " + 删除条件 + ";"
            结果 = self.__游标.execute(sql语句)
            self.__数据库.commit()
            self.__许可.release()
            return 结果
        except Exception as error:
            # self.__数据库.rollback()
            print('数据库_删除记录：运行出错|' + str(error))
            self.__许可.release()
            return -1


class 网页类型:
    def __init__(self):
        self.源码 = ''
        self.Cookie = ''
        self.协议头 = {}
        self.状态码 = 0


if __name__ == '__main__':
    print('欢迎查看Python中文示例模块,模块可能存在使用,示范错误,仅做参考使用！有新建议或错误代码指正欢迎跟我反馈,一同进步。QQ:99396686')
