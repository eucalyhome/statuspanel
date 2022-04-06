#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageOps, ImageFont, ImageFilter, ImageChops, ImageColor
import time, re, copy, os, codecs, random, datetime, json

class worker(object):
    fontreg = 0
    fontbold = 0
    fontelec = 0
    statusdata = ["LOADING: loading"]
    statusdict = dict()
    imagecanvas = 0
    imagespeed = []
    imagelength = []
    imagebgbright = []
    imagebgcolor = 0

    def __init__(self,basedir):
        fontdata = basedir + "PixelMplus10-Regular.ttf"
        self.fontreg = ImageFont.truetype(fontdata, 10)
        fontdata = basedir + "PixelMplus10-Bold.ttf"
        self.fontbold = ImageFont.truetype(fontdata, 10)
        fontdata = basedir + "electroharmonix.ttf"
        self.fontelec = ImageFont.truetype(fontdata, 10)
        self.imagecanvas = Image.new("RGBA", (1024, 128), (0,0,0))
        for i in range(0,16):
            self.imagespeed.append(1)
            self.imagelength.append(0)
            self.imagebgbright.append(0)

    def imagenew(self):
        imagecolorspace = 'RGBA'
        imagecolorfill = (0, 0, 80)
        imagesizex = 128
        imagesizey = 64
        image = Image.new(imagecolorspace, (imagesizex, imagesizey), imagecolorfill)
        return (image)

    def draw(self,aspect):
        draw = ImageDraw.Draw(self.imagecanvas)
        imagetemp = Image.new("RGBA", (1024, 9), (0,0,0))
        size = (128,64)
        if aspect == 'h':
            size = (64,128)
        if aspect == 'eh':
            size = (64,128)
        imagebg = Image.new("RGBA", size, (0,0,0))
        drawbg = ImageDraw.Draw(imagebg)
        rnd = random.uniform(0,10)
        if rnd > 9.9:
            self.imagebgcolor = int(random.uniform(0,8))
        for row in range(0,14):
            if self.imagelength[row] < 128:
                rnd = int (random.uniform(0,len(self.statusdata)))
                drawtextarray = self.statusdata[rnd].split(':')
#                drawtextarray[1] = ":" + drawtextarray[1]
                if aspect == 'eh' or aspect == 'ew':
                    drawlengthb = draw.textsize(drawtextarray[0], font=self.fontelec)
                    drawlengthr = draw.textsize(drawtextarray[1], font=self.fontelec)
                else:
                    drawlengthb = draw.textsize(drawtextarray[0], font=self.fontbold)
                    drawlengthr = draw.textsize(drawtextarray[1], font=self.fontreg)
                drawxpos = self.imagelength[row] + 9
                drawypos = row * 9 - 1
                if aspect == 'eh' or aspect == 'ew':
                    draw.text((drawxpos,drawypos), drawtextarray[0], (255, 255, 255),font=self.fontelec)
                else:
                    draw.text((drawxpos,drawypos), drawtextarray[0], (255, 255, 255),font=self.fontbold)
                drawxpos = drawxpos + drawlengthb[0]
                if aspect == 'eh' or aspect == 'ew':
                    draw.text((drawxpos,drawypos), drawtextarray[1], (255, 255, 255),font=self.fontelec)
                else:
                    draw.text((drawxpos,drawypos), drawtextarray[1], (255, 255, 255),font=self.fontreg)
                self.imagelength[row] = self.imagelength[row] + drawlengthb[0] + drawlengthr[0] + 9
                self.imagebgbright[row] = 16
                rnd = int(random.uniform(0,8))
                self.imagespeed[row] = self.imagespeed[row] - 4 + rnd
                if self.imagespeed[row] < 1:
                    self.imagespeed[row] = 1
                if self.imagespeed[row] > 6:
                    self.imagespeed[row] = 6
            drawypos = row * 9 * (-1)
            imagetemp.paste(self.imagecanvas,(0,drawypos))
            drawxpos = self.imagespeed[row] * (-1)
            drawypos = row * 9
            self.imagecanvas.paste(imagetemp,(drawxpos,drawypos))
            self.imagelength[row] = self.imagelength[row] - self.imagespeed[row]
            drawbgystart = row * 9
            drawbgyend = drawbgystart + 9
            drawbright = self.imagebgbright[row] * 4
            drawbright = drawbright + 192
            if drawbright > 255:
                drawbright = 255
            drawcolor = (80,80,80)
            if self.imagebgcolor > 6:
                drawcolor = (drawbright,drawbright,drawbright)
            elif self.imagebgcolor > 5:
                drawcolor = (0,drawbright,drawbright)
            elif self.imagebgcolor > 4:
                drawcolor = (drawbright,0,drawbright)
            elif self.imagebgcolor > 3:
                drawcolor = (drawbright,drawbright,0)
            elif self.imagebgcolor > 2:
                drawcolor = (0,0,drawbright)
            elif self.imagebgcolor > 1:
                drawcolor = (0,drawbright,0)
            else:
                drawcolor = (drawbright,0,0)
            self.imagebgbright[row] = self.imagebgbright[row] - 1
            if self.imagebgbright[row] < 0:
                self.imagebgbright[row] = 0
            drawbg.rectangle((0, drawbgystart, 128, drawbgyend), fill=drawcolor)
        drawbg.rectangle((0, 63, 128, 64), fill=(0,0,0))
        image = ImageChops.darker(imagebg, self.imagecanvas)
        return (image)

    def drawelec(self,aspect):
        if aspect == 'h':
            image = self.draw('ew').transpose(Image.ROTATE_90)
        else:
            image = self.draw('eh').transpose(Image.ROTATE_90)
        return (image)


    def load(self,jsondata):
        for rootstatus in jsondata['Children'][0]['Children']:
            for rawstatus1 in rootstatus['Children']:
                if len(rawstatus1['Children']) > 0:
                    for rawstatus2 in rawstatus1['Children']:
                        if len(rawstatus2['Children']) > 0:
                            for rawstatus3 in rawstatus2['Children']:
                                self.store(rawstatus3['Text'],rawstatus3['Value'])
                        else:
                            self.store(rawstatus2['Text'],rawstatus2['Value'])
                else:
                    self.store(rawstatus1['Text'],rawstatus1['Value'])
        self.statusdata = []
        for title, value in self.statusdict.items():
            self.statusdata.append(title + ": " + value)

    def store(self,title,value):
        if value.startswith('0.0 '):
            return
        self.statusdict[title] = value
