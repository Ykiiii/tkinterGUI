#!/usr/bin/python
# coding=utf-8 import tkinter as tk import os class RuKou(tk.Frame): """
    ��������
    ��Ҫ��������ʱ��ʾ�ӿ������ص�ͼƬ��չʾ
    """ def __init__(self, master=None): """
        ������չʾһ��ͼƬ������������
        ����ʱ������ӿ�
        ���䷵�ص�ͼƬ��ʾ�ڴ˴�
        """ super().__init__(master) self.pack() self.createWidgets() #�������������һ�����������������������ʾ��½png�� self.lab1 = tk.Label(self) self.lab1.pack() def createWidgets(self): """
        �������diaoYong������showPng����
        ���е�½�����ȳ���һ�����밴ť�������ť��Ȼ�����diaoYong()
        �Ż᷵��һ��ͼƬ��·��
        """ self.login = tk.Button(self, text="����", command=self.diaoYong) self.login.pack(side="top") def diaoYong(self): """
        ���ص����õ�ͼƬ·��
        """ self.showPng(os.getcwd()+"\\a.png") def showPng(self, pngPath): """
        չʾͼƬ
        """ self.png = tk.PhotoImage(file=pngPath) #��Ҫ����Ϊʵ�����ԣ�����ᱻ�������� self.lab1.configure(image=self.png)## root = tk.Tk() # ������Ϣѭ�� app = RuKou(master=root) root.mainloop()
--------------------- 
���ߣ���nw 
��Դ��CSDN 
ԭ�ģ�https://blog.csdn.net/sinat_39013092/article/details/80159232 
��Ȩ����������Ϊ����ԭ�����£�ת���븽�ϲ������ӣ�