#!/bin/bash
#kill -9 $(cat supervisord.pid) # 杀掉进程
docker manifest rm hjdhnx/drpy
docker manifest create hjdhnx/drpy hjdhnx/drpy:amd64-v3.9.0 hjdhnx/drpy:arm64-v3.9.0 hjdhnx/drpy:armv7-v3.9.0
docker manifest annotate hjdhnx/drpy hjdhnx/drpy:amd64-v3.9.0 --os linux --arch amd64
docker manifest annotate hjdhnx/drpy hjdhnx/drpy:arm64-v3.9.0 --os linux --arch arm64/v8
docker manifest annotate hjdhnx/drpy hjdhnx/drpy:armv7-v3.9.0 --os linux --arch arm/v7
docker manifest push hjdhnx/drpy
# 保留一个 bash
#/bin/bash