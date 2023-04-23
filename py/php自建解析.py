#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : php自建解析.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/10/16


import zlib
import base64
# gzip解压
def gzinflate(compressed: bytes) -> bytes:
    return zlib.decompress(compressed, -zlib.MAX_WBITS)

def base64Encode(text):
    return base64.b64encode(text.encode("utf8")).decode("utf-8") #base64编码

def base64Decode(text:str):
    return base64.b64decode(text).decode("utf-8") #base64解码

def un_encode(a:str):
    a =  gzinflate(base64.b64decode(a))
    print(a)
    b = []
    for i in range(len(a)):
        print(i)
        print(a[i])
        print(ord(str(a[i])))
        b[i] = chr(ord(str(a[i]))-1)
    print(b)

if __name__ == '__main__':
    # a = "pVRtT9tWFP6+/IqrKpLtyrMDSYAQoSoFM1AJSR2n04aQZeybxMOxI7+UvqhS6UahGxtdWUe1lU7b2lFtKm23jrVsKX8mNs6v6PVLQgihijTLsqXz8jznPOfcCwB6ItGJDJcBY0C0dAXHKqZZM0Zp+rJcoxRZUEvCokCJWtUz0OdQyBhGRXmWuVhkCtwchgzYPJGORGo6LPNVwRQrOEYbmqWLEBi6OHYGp86eI87QGOnzkFGU4cXLJYDDas28inuWuYF5ggDXIx9EBUmaw0RNgtg8qikRS6RbxqpR9m2Yu/Or8+iu/fil++oJ1naXdK0a+C+ODiaHU6lEKj48cuRXhSoM8ze33W82kecGgIoBe9AOxmKn0Tprd+0vf/pftKHHlw45wv5ROREoVjTwmaGpPFS9YnAvkkwkhzzFSpYqmrKmBoPyskgQFTVtUYYePEZEvHFe97/eQ9PAXtu2d76y178Xi+xM2xH1AMKB87IqmziC78hyd98e1ncP69/a2zfbdj/YgKZWM3EfgATjCDSX53j0I0E41xMwxUzbBqIVKEhQn/PlYGEJ6lAfBa2NW1paoqSrQ2Vv27AjpGNJRQPqH2bKUDVHQVa7JiuKQCepGMBnZNW6kgYZVdI1WQJDVIwaSINcPp8DbMoAecUywHlLViQ6mz0/mMqmwdJlAmRqNQV+DBcuyCadjA9T8SGAX5jisqgfRV6E4CMoLmoEuAR1AwlPJxDTeAUNHNJJxEoNjozEqdQAqmRBViAoCCVBl0MgLO1Xf9T8MVXc5/84L2/Zj1/1o+8Ux+WnmMwEw5ItNXopnc8VOOf+C+fr3Q6fvbLs7r527uy4P68f/vCF8/Bm8/7B4c49FAjcvRVnaw+9za2+6uCms0yuyJEgHuviP1gtFGaav6+7z5fR23jzWz9wKIW/xLDTk5/kGa+1koAOYwdwX6lTqOmTqd7qv7iN5G1+/rRRf9h4vR8I4/y97L7dtFf3+5I9lLwHeCB4498n9saD5uqGXf/F/m/DfvbAvvXUPfjO/vFR1xzew8IyXJGd5djMbGHSYzN1q5ss2JU3ewFBF3RUh6alq63jDK9AMaDokmPttn3nz0AR+966u/9Ho77ZDvAuYz+9DE1ZLWmdRU7PTub8FeTHcxMMAcbQMUT3I0Z0XDUdhfDBgvKGfA22ijoV1VeYL0x/ynRUexIM4RjWgmHqeGgnQYzsRXgKiiSYQg+M9wPcOCbfyl/NrWfHblG/M1HRDNhL755rEI4q5A3iA5qjzzs="
    # print(a)
    # b = un_encode(a)
    # print(b)
    # c = """
    # \n$DATA = curl('https://jx.80k.tv/jxplayer.php?v='.$_REQUEST['url']);\n\npreg_match('/src="(h.*?)"/',$DATA,$url);\n\nif (empty($url[1])) {\n\t$add['code'] = 404;\n\t$add['msg'] = '解析失败';\n\t$add['from'] = 'Q:2579949378';\n\t$add['name'] = '蓝莓';\n} else {\n\t$add['code'] = 200;\n\t$add['msg'] = '解析成功';\n\t$add['from'] = 'Q:2579949378';\n\t$add['name'] = '蓝莓';\n\t$add['url'] = $url[1];\n}\necho json_encode($add,456);\n\nfunction curl($url, $cookie = '')\n    {\n        // 初始化cURL\n        $curl = curl_init();\n        // 设置网址\n        curl_setopt($curl, CURLOPT_URL, $url);\n        // 设置UA\n         $header[] = 'Referer: https://1080p.tv';\n        $header[] = 'User-Agent: Mozilla/5.0 (Linux; Android 6.0.1; OPPO R9s Plus Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36';     \n             // 设置请求头\n        curl_setopt($curl, CURLOPT_HTTPHEADER, $header);\n        // 设置POST数据\n        //允许执行的最长秒数 超时时间\n        curl_setopt($curl, CURLOPT_TIMEOUT, 30);\n        // 过SSL验证证书\n        curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, false);\n        curl_setopt($curl, CURLOPT_SSL_VERIFYHOST, false);\n        // 将头部作为数据流输出\n        curl_setopt($curl, CURLOPT_HEADER, false);\n        // 设置以变量形式存储返回数据\n        curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);\n        // 请求并存储数据\n        $return = curl_exec($curl);\n        // 分割头部和身体\n        if (curl_getinfo($curl, CURLINFO_HTTP_CODE) == '200') {\n            $return_header_size = curl_getinfo($curl, CURLINFO_HEADER_SIZE);\n            $return_header = substr($return, 0, $return_header_size);\n            $return_data = substr($return, $return_header_size);\n        }\n        // 关闭cURL\n        curl_close($curl);\n        // 返回数据\n        return $return;\n    }\n    \n    \n
    # """
    # print(c)
    false = False
    data = {"isBase64Encoded":false,"statusCode":200,"headers":{"Content-Type":"text\/html; charset=utf-8"},"body":"     \n$DATA = curl('https:\/\/80k.tv\/jxplayer.php?v='.$_REQUEST['url']);\n\npreg_match('\/src=\"(h.*?)\"\/',$DATA,$url);\n\nif (empty($url[1])) {\n\t$add['code'] = 404;\n\t$add['msg'] = '解析失败';\n\t$add['from'] = 'Q:2579949378';\n\t$add['name'] = '蓝莓';\n} else {\n\t$add['code'] = 200;\n\t$add['msg'] = '解析成功';\n\t$add['from'] = 'Q:2579949378';\n\t$add['name'] = '蓝莓';\n\t$add['url'] = $url[1];\n}\necho json_encode($add,456);\n\nfunction curl($url, $cookie = '')\n    {\n        \/\/ 初始化cURL\n        $curl = curl_init();\n        \/\/ 设置网址\n        curl_setopt($curl, CURLOPT_URL, $url);\n        \/\/ 设置UA\n         $header[] = 'Referer: https:\/\/1080p.tv';\n        $header[] = 'User-Agent: Mozilla\/5.0 (Linux; Android 6.0.1; OPPO R9s Plus Build\/MMB29M; wv) AppleWebKit\/537.36 (KHTML, like Gecko) Version\/4.0 Chrome\/55.0.2883.91 Mobile Safari\/537.36';     \n             \/\/ 设置请求头\n        curl_setopt($curl, CURLOPT_HTTPHEADER, $header);\n        \/\/ 设置POST数据\n        \/\/允许执行的最长秒数 超时时间\n        curl_setopt($curl, CURLOPT_TIMEOUT, 30);\n        \/\/ 过SSL验证证书\n        curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, false);\n        curl_setopt($curl, CURLOPT_SSL_VERIFYHOST, false);\n        \/\/ 将头部作为数据流输出\n        curl_setopt($curl, CURLOPT_HEADER, false);\n        \/\/ 设置以变量形式存储返回数据\n        curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);\n        \/\/ 请求并存储数据\n        $return = curl_exec($curl);\n        \/\/ 分割头部和身体\n        if (curl_getinfo($curl, CURLINFO_HTTP_CODE) == '200') {\n            $return_header_size = curl_getinfo($curl, CURLINFO_HEADER_SIZE);\n            $return_header = substr($return, 0, $return_header_size);\n            $return_data = substr($return, $return_header_size);\n        }\n        \/\/ 关闭cURL\n        curl_close($curl);\n        \/\/ 返回数据\n        return $return;\n    }\n    \n    \n    "}
    print(data['body'].replace('\/\/','//').replace('\/','/'))