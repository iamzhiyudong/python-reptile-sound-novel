#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tkinter
from tkinter import *

import next

root = tkinter.Tk()  # 创建窗口对象的背景色
root.title("听书爬虫程序")
root.geometry("450x350")

L1 = Label(root, text="小说名字：(如：黄河鬼棺)")
L1.pack( side = TOP)
E1 = Entry(root, bd =1, width='50')
E1.pack(side = TOP)

L2 = Label(root, text="保存路径：(如：D:/黄河鬼棺)")
L2.pack( side = TOP)
E2 = Entry(root, bd =1, width='50')
E2.insert(0, "D:/")
E2.pack(side = TOP)

L3 = Label(root, text="小说网址：(如：https://www.qktsw.net/ting-book-play-3483-1-1.shtml)")
L3.pack( side = TOP)
E3 = Entry(root, bd =1, width='50')
E3.pack(side = TOP)

L4 = Label(root, text="起始集数：(如：1)")
L4.pack( side = TOP)
E4 = Entry(root, bd =1, width='50')
E4.pack(side = TOP)

L5 = Label(root, text="终止集数：(如:67)")
L5.pack( side = TOP)
E5 = Entry(root, bd =1, width='50')
E5.pack(side = TOP)

L6 = Label(root,text="作者：***",fg="red")
L6.pack( side = BOTTOM)


E7 = Entry(root, bd =1, width='50')
E7.insert(0, 'https://www.qktsw.net/')  #在文本框开始位置插入“内容一”
E7.pack(side = BOTTOM)
L7 = Label(root, text="网址备忘：(复制后用浏览器打开)")
L7.pack( side = BOTTOM)


def on():
    name = E1.get()
    path = E2.get()
    wangzhi = E3.get()
    begin = E4.get()
    end = E5.get()

    next.onclick(name,path,wangzhi,begin,end)



B = tkinter.Button(root, text="确认", height="1", command=on, width='50')
B.pack(side=TOP)

root.mainloop()  # 进入消息循环
