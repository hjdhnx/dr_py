# Windows搭建说明
######  Termux qq官群1:714730084
######  Termux qq官群3:878847174
##### [加群链接生成器](https://qun.qq.com/join.html)
##### [git图标生成器](https://github.com/badges/shields)


## 方法一:docker安装(推荐)
### 先确认本地有docker

```shell
docker version
```

如输出类似
```
Client:
 Version:           20.10.23
 API version:       1.41
 Go version:        go1.18.10
 Git commit:        7155243
 Built:             Thu Jan 19 17:43:10 2023
 OS/Arch:           windows/amd64
 Context:           default
 Experimental:      true
 ```
则说明本地有docker

如果没有这样的提示则说明本地没有docker,可以参考[这篇文章](https://www.runoob.com/docker/windows-docker-install.html)

接下来安装容器,输入以下指令即可安装
```shell
docker run -it -p 5705:5705 -p 9001:9001 --restart=always --name drpy -d hjdhnx/drpy
```

没有错误提示的话就可以在**这台电脑打开**[链接](http://localhost:5705/index)

若能打开即搭建成功

## 方法二:使用python运行
```shell
#先将项目克隆到本地
git clone https://github.com/hjdhnx/dr_py.git

#进入目录
cd dr_py

#换源
pip config set global.index-url https://mirrors.cloud.tencent.com/pypi/simple

#安装所需依赖
pip install -r requirements.txt

#运行主程序
python app.py
```

若报错,请检查是否有python环境`python --version`,入如果没有,请到[淘宝python镜像站下载 python-3.8.8-amd64.exe](https://registry.npmmirror.com/binary.html?path=python/3.8.8/)

同样,没有错误提示的话就可以在**这台电脑打开**[链接](http://localhost:5705/index)

---
如果有问题,请提出[issue](https://github.com/hjdhnx/dr_py/issues)