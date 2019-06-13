#!/usr/bin/python
# -*- coding: gbk -*-

from tkinter import *
from PIL import Image,ImageTk

path = 'E:\KIKO.gif'

def leftRight():
    root = Toplevel()
    img = Image.open(path).transpose(Image.FLIP_LEFT_RIGHT)
    image1 = ImageTk.PhotoImage(img)
    Label1 = Label(root,image = image1)
    Label1.pack()
    root.mainloop()

root = Tk()
img = Image.open(path)
image1 = ImageTk.PhotoImage(img)

Button1 = Button(root,command = leftRight,text="leftRight")
Button1.pack()

Label1 = Label(root,image = image1)
Label1.pack()

root.mainloop()