#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageOps, ImageFont, ImageFilter, ImageChops, ImageColor
from rgbmatrix import RGBMatrix, RGBMatrixOptions
import time, re, copy, os, codecs, random, datetime, json

class worker(object):
    def __init__(self):
        self.options = RGBMatrixOptions()
        self.options.hardware_mapping = "regular"
        self.options.led_rgb_sequence = "RBG"
        self.options.rows = 64
        self.options.chain_length = 8
        self.options.parallel = 1
        self.options.pwm_bits = 11
        self.options.brightness = 70
        self.options.pwm_lsb_nanoseconds = 130
        self.options.gpio_slowdown = 3
        self.options.panel_type = "FM6126A"
        self.matrix = RGBMatrix(options = self.options)

    def output(self,handle,subimage,mainimage):
        mainimage = mainimage.transpose(Image.ROTATE_90)
        handle.paste(mainimage,(0, 0))
        subimage = subimage.transpose(Image.ROTATE_180)
        handle.paste(subimage,(128, 0))
        self.matrix.SetImage(handle)

    def imagenew(self):
        imagecolorspace = 'RGB'
        imagecolorfill = (0, 0, 80)
        imagesizex = 256
        imagesizey = 64
        image = Image.new(imagecolorspace, (imagesizex, imagesizey), imagecolorfill)
        return (image)
