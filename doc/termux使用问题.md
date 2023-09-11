步骤1: 安装Termux并赋予访问本地文件的权限  

安装完Termux之后，我们要让Termux有访问本地SD存储卡的访问权限，可以在Termux的终端中输入：  

termux-setup-storage  

当弹出询问是否允许访问本地存储的窗口时，我们需要点击同意即可。  

步骤2：更新升级软件包  

这个就无须多解释了，直接Termux终端：  

apt update && apt upgrade  

步骤3: 安装Git软件  

pkg install git -y  

步骤4: 安装Python2  

FakeRoot 的源代码python2 ，因而我们需要安装Python2。  

pkg install python2 -y  

步骤5: 下载安装FakeRoot Repo  

git clone https://github.com/MaulanaRyM/FakeRoot  

cd FakeRoot  

python2 root.py  

运行这几个命令后，FakeRoot 要求在FakeRoot和Proot两个选项中进行选择。我们仅需要选择FakeRoot这个模式并按回车确认，让它自动进行root处理。这个root过程稍微要费一些时间，请耐心等候。  
