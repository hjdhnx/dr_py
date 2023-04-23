import tkinter as tk
import time
import threading
from tkinter import ttk
from tkinter import messagebox#信息框模块, messagebox.showinfo('标题','普通信息框'),messagebox.askquestion('标题','信息框带确认取消按钮')


class 启动窗口:
    def __init__(self, 主窗口):
        self.点击记录 = False
        self.主窗口 = 主窗口
        self.主窗口.title('这是个窗口')#设置窗口标题
        self.主窗口.resizable(width=False, height=False)#设置窗口宽高是否可调
        screenwidth = self.主窗口.winfo_screenwidth()#获取屏幕宽度
        screenheight = self.主窗口.winfo_screenheight()#获取屏幕高度
        size = '%dx%d+%d+%d' % (561, 380, (screenwidth - 561) / 2, (screenheight - 380) / 2)
        self.主窗口.geometry(size)#设置窗口左边,顶边,宽度,高度
        #self.主窗口.iconbitmap(设置软件图标，ICO图标完整路径)
        
        self.标签2_标题 = tk.StringVar()#创建存放标签标题的变量
        self.标签2_标题.set('密码')
        self.标签2 = ttk.Label(self.主窗口,textvariable=self.标签2_标题,anchor=tk.W)#创建标签,设置标签标题,对齐方式
        self.标签2.place(x=72,y=47,width=48,height=24)#设置标签左边 顶边 宽度 高度
        
        self.标签1_标题 = tk.StringVar()#创建存放标签标题的变量
        self.标签1_标题.set('账号')
        self.标签1 = ttk.Label(self.主窗口,textvariable=self.标签1_标题,anchor=tk.W)#创建标签,设置标签标题,对齐方式
        self.标签1.place(x=72,y=16,width=48,height=24)#设置标签左边 顶边 宽度 高度
        
        self.编辑框4_滚动条_横 = tk.Scrollbar(self.主窗口,orient=tk.HORIZONTAL)#创建滚动条在窗口上 设置成横向
        self.编辑框4_滚动条_横.place(x=160,y=358,width=176,height=18)#设置滚动条左边 顶边 宽度 高度
        self.编辑框4_滚动条_纵 = tk.Scrollbar(self.主窗口)#创建滚动条在窗口上 默认纵向
        self.编辑框4_滚动条_纵.place(x=318,y=256,width=18,height=120)#设置滚动条左边 顶边 宽度 高度
        self.编辑框4 = tk.Text(self.主窗口,yscrollcommand=self.编辑框4_滚动条_纵.set,xscrollcommand=self.编辑框4_滚动条_横.set,wrap=tk.NONE)#创建编辑框 设置输入方式 绑定横向滚动条 绑定横向滚动条 设置不自动换行
        self.编辑框4_滚动条_纵.config(command=self.编辑框4.yview)#编辑框关联纵向滚动条
        self.编辑框4_滚动条_横.config(command=self.编辑框4.xview)#编辑框关联横向滚动条
        self.编辑框4.insert(tk.END,'123\n456000000000000000000000000000000012312345678\n789\n000\n123\n456000000000000000000000000000000012312345678\n789\n000\n123\n456000000000000000000000000000000012312345678\n789\n000\n123\n456000000000000000000000000000000012312345678\n789\n000\n123\n456000000000000000000000000000000012312345678\n789\n000\n123\n456000000000000000000000000000000012312345678\n789\n000\n123\n456000000000000000000000000000000012312345678\n789\n000\n123\n456000000000000000000000000000000012312345678\n789\n000\n123\n456000000000000000000000000000000012312345678\n789\n000\n123\n456000000000000000000000000000000012312345678\n789\n000\n123\n456000000000000000000000000000000012312345678\n789\n000')#在编辑框最后加入内容
        self.编辑框4.place(x=160,y=256,width=158,height=102)#设置编辑框左边 顶边 宽度 高度
        
        self.编辑框3_滚动条_纵 = tk.Scrollbar(self.主窗口)#创建滚动条在窗口上 默认纵向
        self.编辑框3_滚动条_纵.place(x=126,y=248,width=18,height=128)#设置滚动条左边 顶边 宽度 高度
        self.编辑框3 = tk.Text(self.主窗口,yscrollcommand=self.编辑框3_滚动条_纵.set,wrap=tk.NONE)#创建编辑框 设置输入方式 绑定纵向滚动条 设置不自动换行
        self.编辑框3_滚动条_纵.config(command=self.编辑框3.yview)#编辑框关联纵向滚动条
        self.编辑框3.insert(tk.END,'123\n456000000000000000000000000000000012312345678\n789\n000\n123\n456000000000000000000000000000000012312345678\n789\n000\n123\n456000000000000000000000000000000012312345678\n789\n000\n123\n456000000000000000000000000000000012312345678\n789\n000\n123\n456000000000000000000000000000000012312345678\n789\n000\n123\n456000000000000000000000000000000012312345678\n789\n000\n123\n456000000000000000000000000000000012312345678\n789\n000\n123\n456000000000000000000000000000000012312345678\n789\n000\n123\n456000000000000000000000000000000012312345678\n789\n000\n123\n456000000000000000000000000000000012312345678\n789\n000\n123\n456000000000000000000000000000000012312345678\n789\n000')#在编辑框最后加入内容
        self.编辑框3.place(x=40,y=248,width=86,height=128)#设置编辑框左边 顶边 宽度 高度
        
        self.编辑框2_滚动条_横 = tk.Scrollbar(self.主窗口,orient=tk.HORIZONTAL)#创建滚动条在窗口上 设置成横向
        self.编辑框2_滚动条_横.place(x=160,y=230,width=176,height=18)#设置滚动条左边 顶边 宽度 高度
        self.编辑框2 = tk.Text(self.主窗口,xscrollcommand=self.编辑框2_滚动条_横.set,wrap=tk.NONE)#创建编辑框 设置输入方式 绑定横向滚动条 设置不自动换行
        self.编辑框2_滚动条_横.config(command=self.编辑框2.xview)#编辑框关联横向滚动条
        self.编辑框2.insert(tk.END,'123\n456000000000000000000000000000000012312345678\n789\n000\n123\n456000000000000000000000000000000012312345678\n789\n000\n123\n456000000000000000000000000000000012312345678\n789\n000\n123\n456000000000000000000000000000000012312345678\n789\n000\n123\n456000000000000000000000000000000012312345678\n789\n000\n123\n456000000000000000000000000000000012312345678\n789\n000\n123\n456000000000000000000000000000000012312345678\n789\n000\n123\n456000000000000000000000000000000012312345678\n789\n000\n123\n456000000000000000000000000000000012312345678\n789\n000\n123\n456000000000000000000000000000000012312345678\n789\n000\n123\n456000000000000000000000000000000012312345678\n789\n000')#在编辑框最后加入内容
        self.编辑框2.place(x=160,y=176,width=176,height=54)#设置编辑框左边 顶边 宽度 高度
        
        self.编辑框1 = tk.Text(self.主窗口,wrap=tk.NONE)#创建编辑框 设置输入方式 设置不自动换行
        self.编辑框1.insert(tk.END,'123\n456\n789')#在编辑框最后加入内容
        self.编辑框1.place(x=40,y=176,width=104,height=64)#设置编辑框左边 顶边 宽度 高度
        
        self.编辑框_密码_内容 = tk.StringVar()#创建存放编辑框内容的变量
        self.编辑框_密码_内容.set('我是编辑框')
        self.编辑框_密码 = ttk.Entry(self.主窗口,textvariable=self.编辑框_密码_内容,justify=tk.LEFT)#创建编辑框 设置标题 输入方式 是否密码输入
        self.编辑框_密码.place(x=104,y=50,width=80,height=21)#设置编辑框左边 顶边 宽度 高度
        
        self.编辑框_账号_内容 = tk.StringVar()#创建存放编辑框内容的变量
        self.编辑框_账号_内容.set('456')
        self.编辑框_账号 = ttk.Entry(self.主窗口,textvariable=self.编辑框_账号_内容,show='*',justify=tk.CENTER)#创建编辑框 设置标题 输入方式 是否密码输入
        self.编辑框_账号.place(x=104,y=18,width=80,height=20)#设置编辑框左边 顶边 宽度 高度
        
        self.按钮_退出_标题 = tk.StringVar()
        self.按钮_退出_标题.set('按钮')
        self.按钮_退出 = ttk.Button(self.主窗口,textvariable=self.按钮_退出_标题)#command=按钮点击触发的函数,创建按钮 绑定主窗口 设置标题 是否禁止
        self.按钮_退出.place(x=208,y=47,width=88,height=24)#设置按钮左边 顶边 宽度 高度
        
        self.按钮_退出['command'] = self.按钮_退出_被鼠标左键单击
        self.按钮1_标题 = tk.StringVar()
        self.按钮1_标题.set('我是按钮')
        self.按钮1 = ttk.Button(self.主窗口,textvariable=self.按钮1_标题)#command=按钮点击触发的函数,创建按钮 绑定主窗口 设置标题 是否禁止
        self.按钮1.place(x=208,y=16,width=88,height=24)#设置按钮左边 顶边 宽度 高度
        
        self.按钮1['command'] = self.按钮1_被鼠标左键单击
        self.组合框2 = ttk.Combobox(self.主窗口,values=('123','456','789'), state='readonly')#创建组合框,设置组合框项目,类型
        self.组合框2.current(0)#设置组合框现行选中项
        self.组合框2.place(x=159,y=144,width=168,height=23)#设置组合框左边 顶边 宽度 高度
        
        self.组合框1 = ttk.Combobox(self.主窗口,values=())#创建组合框,设置组合框项目,类型
        self.组合框1.place(x=39,y=144,width=100,height=23)#设置组合框左边 顶边 宽度 高度
        
        self.单选框选中变量 = tk.IntVar()#创建一个变量存放单选框状态，同一组单选框要用一个变量
        self.单选框3_标题 = tk.StringVar()#创建个变量存放单选框标题
        self.单选框3_标题.set('单选框3')
        self.单选框3 = ttk.Radiobutton(self.主窗口,textvariable=self.单选框3_标题,variable=self.单选框选中变量,value='单选框3')#command=单选框选中时执行的函数,创建单选框 设置标题 是否禁止 关联选中变量 设置标识名称
        self.单选框3.place(x=219,y=88,width=80,height=24)#设置单选框左边 顶边 宽度 高度
        
        self.单选框选中变量.set('单选框2')#设置要选中的单选框
        self.单选框2_标题 = tk.StringVar()#创建个变量存放单选框标题
        self.单选框2_标题.set('单选框2')
        self.单选框2 = ttk.Radiobutton(self.主窗口,textvariable=self.单选框2_标题,variable=self.单选框选中变量,value='单选框2')#command=单选框选中时执行的函数,创建单选框 设置标题 是否禁止 关联选中变量 设置标识名称
        self.单选框2.place(x=131,y=88,width=80,height=24)#设置单选框左边 顶边 宽度 高度
        
        self.单选框1_标题 = tk.StringVar()#创建个变量存放单选框标题
        self.单选框1_标题.set('单选框1')
        self.单选框1 = ttk.Radiobutton(self.主窗口,textvariable=self.单选框1_标题,variable=self.单选框选中变量,value='单选框1')#command=单选框选中时执行的函数,创建单选框 设置标题 是否禁止 关联选中变量 设置标识名称
        self.单选框1.place(x=35,y=88,width=80,height=24)#设置单选框左边 顶边 宽度 高度
        
        self.选择框3_是否选中 = tk.IntVar()#创建变量存放选择框是否选中
        self.选择框3_是否选中.set(1)#设置选择框为选中状态
        self.选择框3_标题 = tk.StringVar()#创建变量存放选择框标题
        self.选择框3_标题.set('选择框3')
        self.选择框3 = ttk.Checkbutton(self.主窗口,textvariable=self.选择框3_标题,variable=self.选择框3_是否选中,onvalue=1,offvalue=0)#command=选择框选中时执行的函数,创建选择框 设置标题 设置是否禁止 是否选中 选中时为1 反则0 可修改
        self.选择框3.place(x=219,y=120,width=80,height=24)#设置选择框左边 顶边 宽度 高度
        
        self.选择框2_是否选中 = tk.IntVar()#创建变量存放选择框是否选中
        self.选择框2_是否选中.set(0)#设置选择框为未选中状态
        self.选择框2_标题 = tk.StringVar()#创建变量存放选择框标题
        self.选择框2_标题.set('选择框2')
        self.选择框2 = ttk.Checkbutton(self.主窗口,textvariable=self.选择框2_标题,variable=self.选择框2_是否选中,onvalue=1,offvalue=0)#command=选择框选中时执行的函数,创建选择框 设置标题 设置是否禁止 是否选中 选中时为1 反则0 可修改
        self.选择框2.place(x=131,y=120,width=80,height=24)#设置选择框左边 顶边 宽度 高度
        
        self.选择框1_是否选中 = tk.IntVar()#创建变量存放选择框是否选中
        self.选择框1_是否选中.set(1)#设置选择框为选中状态
        self.选择框1_标题 = tk.StringVar()#创建变量存放选择框标题
        self.选择框1_标题.set('选择框1')
        self.选择框1 = ttk.Checkbutton(self.主窗口,textvariable=self.选择框1_标题,variable=self.选择框1_是否选中,onvalue=1,offvalue=0)#command=选择框选中时执行的函数,创建选择框 设置标题 设置是否禁止 是否选中 选中时为1 反则0 可修改
        self.选择框1.place(x=35,y=120,width=80,height=24)#设置选择框左边 顶边 宽度 高度
        
        self.超级列表框1 = ttk.Treeview(self.主窗口,show='headings',columns=('id','账号','密码'))#创建超级列表框,去掉首列,设置表头
        self.超级列表框1.column('id', width=50,anchor='w') 
        self.超级列表框1.column('账号', width=80,anchor='center') 
        self.超级列表框1.column('密码', width=70,anchor='e') #设置列属性
        self.超级列表框1.heading('id', text='id',anchor='w') 
        self.超级列表框1.heading('账号', text='账号',anchor='center') 
        self.超级列表框1.heading('密码', text='密码',anchor='e') #设置表头属性
        self.超级列表框1.place(x=343,y=8,width=204,height=360)#设置超级列表框左边 顶边 宽度 高度
        
        
    
    def 按钮_退出_被鼠标左键单击(self):
        threading.Thread(target=self.按钮_退出_被鼠标左键单击_线程).start()
        
    def 按钮_退出_被鼠标左键单击_线程(self):
        time.sleep(0.25)
        if self.点击记录 == False:
            self.点击记录 = True
            time.sleep(0.2)
            self.点击记录 = False
            print('被鼠标左键单击')
        else:
            self.点击记录 = False
        
    def 按钮1_被鼠标左键单击(self):
        threading.Thread(target=self.按钮1_被鼠标左键单击_线程).start()
        
    def 按钮1_被鼠标左键单击_线程(self):
        time.sleep(0.25)
        if self.点击记录 == False:
            self.点击记录 = True
            time.sleep(0.2)
            self.点击记录 = False
            print('被鼠标左键单击')
        else:
            self.点击记录 = False
        
if __name__ == '__main__':
    root = tk.Tk()
    app = 启动窗口(root)
    root.mainloop()
    