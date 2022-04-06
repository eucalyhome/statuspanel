#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageOps, ImageFont, ImageFilter, ImageChops, ImageColor
import time, re, copy, os, codecs, random, datetime, json

class worker(object):
    font = 0
    fontsmall = 0
    statusbg = 0

    def __init__(self,basedir):
        fontdata = basedir + "GDhwGoJA-OTF112b2.otf"
        self.font = ImageFont.truetype(fontdata, 16)
        self.fontsmall = ImageFont.truetype(fontdata, 7)
        self.statusbg = Image.new("RGBA",(64,128),(0,0,0,0))

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

        draw.text((1,1), "CPU", (0, 0, 0),font=self.font)
        self.writetext(draw,17,1,cpuload,(0, 0, 0),self.font)
        draw.text((49,25), "%", (0, 0, 0),font=self.fontsmall)
        self.writetext(draw,33,1,cputemp,(0, 0, 0),self.font)
        draw.text((49,41), "'C", (0, 0, 0),font=self.fontsmall)
        self.writetext(draw,49,1,cpufreq,(0, 0, 0),self.font)
        draw.text((49,57), "MHz", (0, 0, 0),font=self.fontsmall)
        draw.text((1,75), "GPU", (0, 0, 0),font=self.font)
        self.writetext(draw,91,1,gpuload,(0, 0, 0),self.font)
        draw.text((49,99), "%", (0, 0, 0),font=self.fontsmall)
        self.writetext(draw,107,1,gputemp,(0, 0, 0),self.font)
        draw.text((49,115), "'C", (0, 0, 0),font=self.fontsmall)


        draw.text((0,0), "CPU", (0, 255, 255),font=self.font)
        self.writetext(draw,16,0,cpuload,(255, 255, 255),self.font)
        draw.text((48,24), "%", (0, 255, 255),font=self.fontsmall)
        self.writetext(draw,32,0,cputemp,(255, 255, 255),self.font)
        draw.text((48,40), "'C", (0, 255, 255),font=self.fontsmall)
        self.writetext(draw,48,0,cpufreq,(255, 255, 255),self.font)
        draw.text((48,56), "MHz", (0, 255, 255),font=self.fontsmall)
        draw.text((0,74), "GPU", (0, 255, 0),font=self.font)
        self.writetext(draw,90,0,gpuload,(255, 255, 255),self.font)
        draw.text((48,98), "%", (0, 255, 0),font=self.fontsmall)
        self.writetext(draw,106,0,gputemp,(255, 255, 255),self.font)
        draw.text((48,114), "'C", (0, 255, 0),font=self.fontsmall)

        image = Image.alpha_composite(image,statusimage)
        return (image)

    def writetext(self,draw,hpos,wpos,message,color,font):
        w, h = draw.textsize(str(message), font)
        w = 48 - w + wpos
        draw.text((w,hpos), str(message), color,font=font)
