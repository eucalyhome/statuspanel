#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageOps, ImageFont, ImageFilter, ImageChops, ImageColor, ImageTk, ImageDraw
import time, re, copy, os, codecs, random, datetime, json
import tkinter
import threading

class tktoolkit:
    def guiinit(self):
        global guiimg,guitkimage,guiitem,guicanvas
        root = tkinter.Tk()
        root.title('tktoolkit')
        root.geometry("384x256")
        guiimg = Image.new("RGB", (384, 256), (0,0,0))
        guitkimage = ImageTk.PhotoImage(guiimg)
        guicanvas = tkinter.Canvas(bg = "black", width=384, height=256)
        guicanvas.place(x=0, y=0)
        guiitem = guicanvas.create_image(0, 0, image=guitkimage, anchor=tkinter.NW)
        root.mainloop()

    def __init__(self):
       thread1 = threading.Thread(target=self.guiinit)
       thread1.setDaemon(True)
       thread1.start()

    def output(self,imagep,images):
        global guiimg,guitkimage,guiitem,guicanvas
# x2 image
        outputimagep = imagep.resize(size=(256,128))
        outputimages = images.resize(size=(128,256))
# x1 image
#        outputimagep = imagep.resize(size=(128,64))
#        outputimages = images.resize(size=(64,128))

#        outputimages = outputimages.rotate(90, expand=True)
        guiimg = Image.new("RGB", (384, 256), (0,0,0))
        guiimg.paste(outputimagep, (0, 64))
        guiimg.paste(outputimages, (256, 0))
        guitkimage = ImageTk.PhotoImage(guiimg)
        guicanvas.itemconfig(guiitem,image=guitkimage,anchor=tkinter.NW)
