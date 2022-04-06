#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial
import json,os,re,time

outputfile = '/ramdisk/remoteoutput'
inputfile = '/ramdisk/remote.json'

valuemain = 0
valuesub = 0
valuestatus = 0
valuedata = 0
oldvaluedata = 0

while (True):
    try:
        ser.close()
    except:
        pass

    try:
        ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1.0)
        while (True):
            if os.path.isfile(outputfile):
                f = open(outputfile, 'r')
                data = f.read()
                f.close()
                ser.write(str.encode(data))

            line = ser.read_all().decode()
            for sline in line.splitlines():
                if 'valuemain' in sline:
                    valuemain = re.sub(r"\D", "", str(sline))
                if 'valuesub' in sline:
                    valuesub = re.sub(r"\D", "", str(sline))
                if 'valuestatus' in sline:
                    valuestatus = re.sub(r"\D", "", str(sline))
                valuedata = str(valuemain) + str(valuesub) + str(valuestatus)
                if valuedata != oldvaluedata:
                    outputdata = {}
                    outputdata['valuemain'] = str(valuemain)
                    outputdata['valuesub'] = str(valuesub)
                    outputdata['valuestatus'] = str(valuestatus)
                    filepointer = open(inputfile,'w')
                    json.dump(outputdata,filepointer,indent=4,sort_keys=True)
                    filepointer.close()
                    oldvaluedata = valuedata
            time.sleep(0.5)
    except:
        time.sleep(5)
