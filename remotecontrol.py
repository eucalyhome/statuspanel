#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageOps, ImageFont, ImageFilter, ImageChops, ImageColor
import time, re, copy, os, codecs, random, datetime, json

class worker(object):
    imagebase = 0
    basedir = './'

    def __init__(self,basedirvalue):
        self.basedir = basedirvalue

    def getdata(self):
        datafile_remotecontroldata = self.basedir + 'remote.json'
        outdata = {}
        outdata['viewmain'] = 0
        outdata['viewsub'] = 0
        outdata['viewstatus'] = 0
        if not os.path.exists(datafile_remotecontroldata):
            return (outdata)
        try:
            with open(datafile_remotecontroldata) as f:
                remdata = json.load(f)
        except:
            return (outdata)
        try:
            outdata['viewmain'] = int(remdata['valuemain'])
            outdata['viewsub'] = int(remdata['valuesub'])
            outdata['viewstatus'] = int(remdata['valuestatus'])
        except:
            outdata['viewmain'] = 0
            outdata['viewsub'] = 0
            outdata['viewstatus'] = 0
        return (outdata)

    def putdata(self,parm):
        datafile_remotecontroldata = self.basedir + 'remoteoutput'
        f = open(datafile_remotecontroldata, 'w')
        f.write(parm)
        f.close()
