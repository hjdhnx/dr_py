#!/bin/bash
# 建立文件夹
mkdir -p /home/pywork/dr_py && cd /home/pywork/dr_py
# 下载仓库包
wget https://ghproxy.net/https://github.com/hjdhnx/dr_py/archive/refs/heads/main.zip -O dr_py.zip
# 解压
unzip dr_py.zip
# 移动文件到当前目录
mv dr*/* ./
# 清理临时文件
rm *.zip
# 启动容器
# docker run -it -p 5705:5705 -p 9001:9001 -v /home/pywork/dr_py:/root/sd/pywork/dr_py --restart=always --name drpy -d hjdhnx/drpy