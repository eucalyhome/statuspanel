#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageOps, ImageFont, ImageFilter, ImageChops, ImageColor
import time, re, copy, os, codecs, random, datetime, json
import numpy as np
from scipy import signal

class worker(object):
    lifedataprimary = 0
    lifedatasecondary = 0
    statusbg = 0

    def __init__(self):
        self.lifedataprimary = self.initstate(128, 64, init_alive_prob=0.08)
        self.lifedatasecondary = self.initstate(128, 64, init_alive_prob=0.08)

    def next(self):
        self.lifedataprimary = self.nextgeneration(self.lifedataprimary)
        self.lifedatasecondary = self.nextgeneration(self.lifedatasecondary)

    def draw(self):
        imageblue = self.toimage(self.lifedataprimary)
        imagegreen = self.toimage(self.lifedatasecondary)
        image = Image.new('RGB', (128, 64), (0, 0, 0))
        image.paste(Image.new("RGB", image.size, (0,255,255)), mask=imageblue)
        image.paste(Image.new("RGB", image.size, (0,255,0)), mask=imagegreen)
        return (image)

    def add(self,parm1,parm2):
        seedprimary = float(parm1) / 500
        seedsecondary = float(parm2) / 500
        self.lifedataprimary = self.addstate(self.lifedataprimary,128, 64, init_alive_prob=seedprimary)
        self.lifedatasecondary = self.addstate(self.lifedatasecondary,128, 64, init_alive_prob=seedsecondary)

    def initstate(self, width, height, init_alive_prob=0.5):
        N = width*height
        v = np.array(np.random.rand(N) + init_alive_prob, dtype=int)
        return v.reshape(height, width)

    def addstate(self, F, width, height, init_alive_prob=0.5):
        N = width*height
        v = np.array(np.random.rand(N) + init_alive_prob, dtype=int).reshape(height, width)
        v = F + v
        return v

    def countneighbor(self, F):
        mask = np.ones((3, 3), dtype=int)
        return signal.correlate2d(F, mask, mode="same", boundary="wrap")

    def nextgeneration(self, F):
        N = self.countneighbor(F)
        G = (N == 3) + F * (N == 4)
        return G

    def toimage(self, F):
        nparray = np.array(F, dtype=np.uint8)*255
        image = Image.fromarray(np.uint8(nparray)).convert("1")
        return image
