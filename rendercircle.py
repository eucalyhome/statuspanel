#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageOps, ImageFont, ImageFilter, ImageChops, ImageColor
import time, re, copy, os, codecs, random, datetime, json

class worker(object):

    def __init__(self):
        pass

    def draw(self,parm,parm2):
        image = Image.new("RGBA",(64,128),(0,0,0))
        draw = ImageDraw.Draw(image)
        barprimary = (int(float(parm) / 100 * 260) + 130) % 360
        barsecondary = (int(float(parm2) / 100 * 260) + 130) % 360
        if barprimary == 0:
            barprimary = 1
        if barsecondary == 0:
            barsecondary = 1
        draw.arc((( 0, 0),( 63, 63)), 130, 50, fill=(0, 64, 64), width=16)
        draw.arc((( 0, 64),( 63, 127)), 130, 50, fill=(0, 64, 0), width=16)

        draw.arc((( 0, 0),( 63, 63)), 130, barprimary, fill=(0, 255, 255), width=16)
        draw.arc((( 0, 64),( 63, 127)), 130, barsecondary, fill=(0, 255, 0), width=16)
        return (image)
