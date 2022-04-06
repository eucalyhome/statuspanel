#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageOps, ImageFont, ImageFilter, ImageChops, ImageColor
import time, re, copy, os, codecs, random, datetime, json

class worker(object):
    fontreg = 0
    fontbold = 0
    statusbg = 0

    def __init__(self,basedir):
        fontdata = basedir + "PixelMplus10-Regular.ttf"
        self.fontreg = ImageFont.truetype(fontdata, 10)
        fontdata = basedir + "PixelMplus10-Bold.ttf"
        self.fontbold = ImageFont.truetype(fontdata, 10)
        self.statusbg = Image.new("RGBA",(64,128),(0,0,0,0))
        statusspace = Image.new("RGBA",(64,48),(0,0,0,0))
        draw = ImageDraw.Draw(statusspace)
        draw.rectangle((2,2,62,46),fill=(0,0,0,32))
        draw.text((3,3), "CPU", (255, 255, 255,128),font=self.fontbold)
        draw.text((3,25), "GPU", (255, 255, 255,128),font=self.fontbold)
        self.statusbg.paste(statusspace,(0,0))

    def draw(self,image,cpufreq,cpuload,cputemp,gpuload,gputemp):
        cpufreq = int(cpufreq)
        cpufreq = str(cpufreq).rjust(4)
        cpuload = int(cpuload)
        cpuload = str(cpuload).rjust(3)
        cputemp = int(cputemp)
        cputemp = str(cputemp).rjust(2)
        gpuload = int(gpuload)
        gpuload = str(gpuload).rjust(3)
        gputemp = int(gputemp)
        gputemp = str(gputemp).rjust(2)
        statusimage = copy.copy(self.statusbg)
        draw = ImageDraw.Draw(statusimage)

        draw.text((25,4), cpufreq + " MHz", (0, 0, 0, 128),font=self.fontreg)
        draw.text((4,14), cpuload + " % " + cputemp +" C", (0, 0, 0, 128),font=self.fontreg)
        draw.text((4,36), gpuload + " % " + gputemp +" C", (0, 0, 0, 128),font=self.fontreg)

        draw.text((24,3), cpufreq + " MHz", (255, 255, 255,128),font=self.fontreg)
        draw.text((3,13), cpuload + " % " + cputemp +" C", (255, 255, 255,128),font=self.fontreg)
        draw.text((3,35), gpuload + " % " + gputemp +" C", (255, 255, 255,128),font=self.fontreg)

        image = Image.alpha_composite(image,statusimage)
        return (image)
