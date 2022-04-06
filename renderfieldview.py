#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageOps, ImageFont, ImageFilter, ImageChops, ImageColor
import time, re, copy, os, codecs, random, datetime, json

class worker(object):
    fieldimagearray = []
    fileditemarray = []
    fieldcount = 0
    fielddir = 0
    fieldbg = 32
    fieldbgprev = 32

    def __init__(self,basedir):
        image = Image.open(basedir + 'images/mapchip2/MapChip/base.png').convert("RGBA")
        for x in range(image.size[0]):
            for y in range(image.size[1]):
                pixel = image.getpixel( (x, y) )
                if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                    image.putpixel( (x, y), (0,0,0,0) )
        imagetilemaxx = int (image.size[0] / 16)
        imagetilemaxy = int (image.size[1] / 16)
        for y in range(imagetilemaxy):
            for x in range(imagetilemaxx):
                cropylow = y * 16
                cropyhigh = cropylow + 16
                cropxlow = x * 16
                cropxhigh = cropxlow + 16
                self.fieldimagearray.append(image.crop((cropxlow,cropylow,cropxhigh,cropyhigh)))
        for y in range(10):
            for x in range(6):
                itemposid = y * 6 + x
                self.fileditemarray.append(0)

    def imagenew(self):
        imagecolorspace = 'RGB'
        imagecolorfill = (0, 0, 80)
        imagesizex = 64
        imagesizey = 128
        image = Image.new(imagecolorspace, (imagesizex, imagesizey), imagecolorfill)
        return (image)

    def draw(self,parm,parm2):
        imagecanvasbg = Image.new("RGBA",(96,160),(255,255,255,0))
        bgalpha = 0
        bgalpha = 1 /  float(16 - self.fieldcount)
        bgimagetile = Image.blend(self.fieldimagearray[self.fieldbgprev],self.fieldimagearray[self.fieldbg],bgalpha)
        for tiley in range(10):
            for tilex in range(6):
                posx = tilex * 16
                posy = tiley * 16
                imagecanvasbg.paste(bgimagetile,(posx,posy))

        self.fieldcount = self.fieldcount + 1
        if self.fieldcount == 16:
            self.fieldcount = 0
            self.fieldbgprev = self.fieldbg
            self.fieldbg = int ( 8 * parm2 / 100)
#            self.fieldbg = int ( 8 * random.random() )
            if self.fieldbg == 8:
                self.fieldbg = 7
            self.fieldbg = self.fieldbg + 32
            
            fielditemarraytemp = copy.deepcopy(self.fileditemarray)
            for tiley in range(10):
                for tilex in range(6):
                    copyy = tiley
                    copyx = tilex
                    if self.fielddir == 0:
                        copyx = copyx - 1
                    if self.fielddir == 1:
                        copyy = copyy - 1
                    if self.fielddir == 2:
                        copyx = copyx + 1
                    if self.fielddir == 3:
                        copyy = copyy + 1
                    tileid = tiley * 6 + tilex
                    copyid = copyy * 6 + copyx
                    if copyid < 0:
                        copyid = 0
                    if copyid >= len(self.fileditemarray):
                        copyid = 0
                    self.fileditemarray[tileid] = copy.deepcopy(fielditemarraytemp[copyid])
            randseed = random.random() * 10
            if randseed < 1:
                self.fielddir = int(random.random() * 4)
                if self.fielddir > 3:
                    self.fielddir = 3
            newfields = [0] * 8
            for randid in range(8):
                randseed = random.random() * parm / 20
                if randseed > 1:
                    randseed2 = int (random.random() * 29)
                    newfields[randid] = randseed2
                else:
                    newfields[randid] = 0
            if self.fielddir == 0:
                for tiley in range(8):
                    tileid = (tiley + 1) * 6
                    self.fileditemarray[tileid] = newfields[tiley]
            if self.fielddir == 1:
                for tilex in range(4):
                    tileid = tilex + 1
                    self.fileditemarray[tileid] = newfields[tilex]
            if self.fielddir == 2:
                for tiley in range(8):
                    tileid = (tiley + 1) * 6 + 5
                    self.fileditemarray[tileid] = newfields[tiley]
            if self.fielddir == 3:
                for tilex in range(4):
                    tileid = 54 + tilex + 1
                    self.fileditemarray[tileid] = newfields[tilex]

        imagecanvaschar = Image.new("RGBA",(96,160),(255,255,255,0))
        for tiley in range(10):
            for tilex in range(6):
                tileid = tiley * 6 + tilex
                targetid = self.fileditemarray[tileid]
                if targetid != 0:
                    targetid = targetid + 81
                    if targetid > 85:
                        targetid = targetid + 2
                    posx = tilex * 16
                    posy = tiley * 16
                    imagecanvaschar.paste(self.fieldimagearray[targetid],(posx,posy))
        imagecanvas = Image.alpha_composite(imagecanvasbg,imagecanvaschar)
        cropylow = 16
        cropxlow = 16
        if self.fielddir == 0:
            cropxlow = cropxlow - self.fieldcount
        if self.fielddir == 1:
            cropylow = cropylow - self.fieldcount
        if self.fielddir == 2:
            cropxlow = cropxlow + self.fieldcount
        if self.fielddir == 3:
            cropylow = cropylow + self.fieldcount
        cropyhigh = cropylow + 128
        cropxhigh = cropxlow + 64
        image = imagecanvas.crop((cropxlow,cropylow,cropxhigh,cropyhigh))
        return (image)
