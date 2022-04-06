#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageOps, ImageFont, ImageFilter, ImageChops, ImageColor
import time, re, copy, os, codecs, random, datetime, json

class worker(object):
    dataarray = []
    datacolorarray = []


    def __init__(self):
        for i in range(128):
            self.dataarray.append(0)
            self.datacolorarray.append(0)

    def draw(self):
        imagecanvasbg = Image.new("RGBA",(64,128),(0,0,0))
        draw = ImageDraw.Draw(imagecanvasbg)
        for posx in range(8):
            for posy in range(16):
                startx = (posx * 8 ) + 1
                starty = (posy * 8 ) + 1
                endx = startx + 6
                endy = starty + 6
                datai = ( posx * 8) + posy
                fill = (0,0,0)
                if self.dataarray[datai] > 0:
                    bright = self.dataarray[datai] * 2
                    if self.datacolorarray[datai] == 0:
                        fill = (bright,0,0)
                    if self.datacolorarray[datai] == 1:
                        fill = (0,bright,0)
                    if self.datacolorarray[datai] == 2:
                        fill = (0,0,bright)
                    if self.datacolorarray[datai] == 3:
                        fill = (bright,bright,0)
                    if self.datacolorarray[datai] == 4:
                        fill = (bright,0,bright)
                    if self.datacolorarray[datai] == 5:
                        fill = (0,bright,bright)
                draw.rectangle((startx, starty, endx, endy), fill, outline=(0, 0, 0))
        return (imagecanvasbg)

    def draww(self):
        image = self.draw()
        image = image.transpose(Image.ROTATE_90)
        return (image)


    def next(self):
        for i in range(128):
            if self.dataarray[i] > 0:
                self.dataarray[i] = self.dataarray[i] - 1


    def add(self,parm,parm2):
        parmseed = float(parm) / 100
        parmseed2 = float(parm2) / 100
        for i in range(128):
            randdata = random.random()
            if randdata > 0.5:
                randdata = random.random()
                if randdata < parmseed:
                    if self.dataarray[i] == 0:
                        self.dataarray[i] = 100
                        randdata = int (random.random() * 2.99)
                        self.datacolorarray[i] = randdata
                randdata = random.random()
                if randdata < parmseed2:
                    if self.dataarray[i] == 0:
                        self.dataarray[i] = 100
                        randdata = int (random.random() * 2.99)
                        self.datacolorarray[i] = randdata + 3
