#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageOps, ImageFont, ImageFilter, ImageChops, ImageColor
import time, re, copy, os, codecs, random, datetime, json

class worker(object):
    imagebase = 0
    imagebasenull = 0

    def __init__(self,basedir):
        self.imagebase = Image.open(basedir + 'images/logo.png').convert("RGBA")
        self.imagebase = self.imagebase.transpose(Image.ROTATE_90)
        self.imagebasenull = Image.new("RGBA",(64,128),(0,0,0,0))

    def draw(self):
        return (self.imagebase)

    def drawnull(self):
        return (self.imagebasenull)
