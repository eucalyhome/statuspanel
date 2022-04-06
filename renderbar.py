#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageOps, ImageFont, ImageFilter, ImageChops, ImageColor
import time, re, copy, os, codecs, random, datetime, json

class worker(object):
    jflag = 0
    jdata = 0

    def __init__(self):
        pass

    def draw(self,parm,parm2):
        image = Image.new("RGBA",(64,128),(0,0,0))
        draw = ImageDraw.Draw(image)
        barprimary = int(float(parm) / 100 * 128)
        barsecondary = int(float(parm2) / 100 * 128)
        if barprimary == 0:
            barprimary = 1
        if barsecondary == 0:
            barsecondary = 1
        barprimary = 127 - barprimary
        barsecondary = 127 - barsecondary
        jdatatest = (barprimary * 10) + barsecondary
        if self.jdata != jdatatest:
            randdata = random.random()
            if randdata > 0.5:
                self.jflag = 1
            else:
                self.jflag = 0
        self.jdata = jdatatest
        if self.jflag == 1:
            bartemp = barprimary
            barprimary = barsecondary
            barsecondary = bartemp
        draw.rectangle((0, barprimary, 15, 127), (0,192,64), outline=(0, 0, 0))
        draw.rectangle((48, barsecondary, 63, 127), (0,192,64), outline=(0, 0, 0))
        return (image)
