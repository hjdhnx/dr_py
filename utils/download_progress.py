#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : download_progress.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2023/10/30
# 下载进度条工具

import os
import time
# import logging
import requests
from urllib.parse import unquote
from contextlib import closing
from utils.log import logger

chunkSize = 1024 * 1024
loop = 5

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}


def speed_handle(process, file_length):
    if process != file_length:
        num = process / file_length
        progress = ': \033[1;33m{:.2f}\033[0m%|{}{}| '.format(float(num * 100), '■' * round(num * 20),
                                                              '□' * round((1 - num) * 20))
    else:
        progress = ' \033[1;33m{}\033[0m% |{}|'.format(100, '■' * 50)
    # print(progress, flush=True, end='')
    logger.info(progress)


def get_file_name(url, headers):
    filename = ''
    if 'Content-Disposition' in headers and headers['Content-Disposition']:
        disposition_split = headers['Content-Disposition'].split(';')
        if len(disposition_split) > 1:
            if disposition_split[1].strip().lower().startswith('filename='):
                file_name = disposition_split[1].split('=')
                if len(file_name) > 1:
                    filename = unquote(file_name[1])
    if not filename and os.path.basename(url):
        filename = os.path.basename(url).split("?")[0]
    if not filename:
        return time.time()
    return filename


def file_download(fileUrl, filePath):
    if os.path.exists(filePath):
        os.remove(filePath)
    # response = requests.get(fileUrl, headers=headers, stream=True, verify=False)
    response = requests.get(fileUrl, headers=headers, stream=True)
    fileSize = int(response.headers['content-length'])  # 文件大小
    logger.info(f'fileSize:{fileSize}')

    tmpSize = 0
    n = 0
    isDownloaded = False
    while n < loop:

        if os.path.exists(filePath):  # 判断文件是否存在
            tmpSize = os.path.getsize(filePath)

        _headers = {"Range": "bytes={}-{}".format(tmpSize, fileSize),
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

        # headers.update({"Range": "bytes={}-{}".format(tmpSize, fileSize)})

        contentSize = 0
        remainSize = (fileSize - tmpSize) / chunkSize
        filename = os.path.basename(filePath)

        st = time.perf_counter()

        if remainSize > 0:

            with closing(requests.get(fileUrl, headers=_headers, stream=True)) as _response, open(
                    filePath,
                    "ab") as file:
                for content in _response.iter_content(chunk_size=chunkSize):
                    file.write(content)
                    timeTook = time.perf_counter() - st
                    contentSize += len(content) / chunkSize
                    # print('\r{}/{}: {}'.format(cnt + 1, len(fileUrls), filename), flush=True, end='')
                    # logger.info('\r{}/{}: {}'.format(cnt + 1, len(fileUrls), filename))
                    logger.info(f'文件{filename}下载中...')

                    speed_handle(contentSize + tmpSize / chunkSize, fileSize / chunkSize)
                    downloadSpeed = contentSize / timeTook  # 平均下载速度
                    remainingTime = int(timeTook / (contentSize / remainSize) - timeTook)  # 估计剩余下载时间

                    # print(
                    #     '[' + 'average speed: \033[1;31m{:.2f}MiB/s\033[0m, remaining time: \033[1;32m{}s\033[0m, file size: \033[1;34m{:.2f}MiB\033[0m'.format(
                    #         downloadSpeed,
                    #         remainingTime,
                    #         fileSize / chunkSize) + ']', flush=True, end=' '
                    #     )

                    logger.info(
                        '[' + 'average speed: \033[1;31m{:.2f}MiB/s\033[0m, remaining time: \033[1;32m{}s\033[0m, file size: \033[1;34m{:.2f}MiB\033[0m'.format(
                            downloadSpeed,
                            remainingTime,
                            fileSize / chunkSize) + ']'
                    )
        else:
            isDownloaded = True
            break

        n += 1

    return isDownloaded


def file_downloads(files, save_path='download'):
    """
    files = [{'url':'https://ghproxy.liuzhicong.com/https://github.com/hjdhnx/dr_py/archive/refs/heads/main.zip','name':'dr_py.zip'}]
    :param save_path:
    :param files:
    :return: 
    """
    # save_path = 'tmp'
    os.makedirs(save_path, exist_ok=True)

    # logging.basicConfig(level=logging.INFO, filename='download/downloading.log', filemode='a', format="%(message)s")
    localtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    logger.info(localtime + ': Start downloading task: {}'.format(files))
    failedUrl = []

    for cnt, file in enumerate(files):
        fileUrl = file.get('url')
        if not fileUrl:
            print('file error:no url')
            continue
        fileName = file.get('name')
        filename = fileName or get_file_name(fileUrl, headers)  # 获取文件名称
        logger.info(f'开始下载{filename}: {fileUrl}')
        try:
            t0 = time.perf_counter()
            isDload = file_download(fileUrl, os.path.join(save_path, filename))
            t1 = time.perf_counter()
            localtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

            if isDload:
                logger.info(
                    localtime + ': {} download successfully! Time consuming: {:.3f}s'.format(filename, t1 - t0))
            else:
                logger.info(localtime + ': {} download failed! Url: {}'.format(filename, fileUrl))
                failedUrl.append(fileUrl)

        except:
            failedUrl.append(fileUrl)

    if len(failedUrl):
        with open(os.path.join(save_path, 'failedUrl.txt'), 'w') as p:
            for url in failedUrl:
                p.write(url + '\n')

    fn = len(failedUrl)
    sn = len(files) - fn
    # print("\n{} file{} download successfully, {} file{} download failed!".format(sn, 's' * (sn > 1), fn, 's' * (fn > 1)))
    logger.info(
        "\n{} file{} download successfully, {} file{} download failed!".format(sn, 's' * (sn > 1), fn, 's' * (fn > 1)))

    if fn > 0:
        return False
    else:
        return True


if __name__ == '__main__':
    # urlTxt = 'download/urls.txt'
    # with open(urlTxt, "r") as f:
    #     fileUrls = [line.strip() for line in f.readlines()]

    files = [{'url': 'https://ghproxy.liuzhicong.com/https://github.com/hjdhnx/dr_py/archive/refs/heads/main.zip',
              'name': 'dr_py.zip'}]
    file_downloads(files, 'tmp')
