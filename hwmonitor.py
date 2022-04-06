#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, re, requests

class worker(object):
    def getdata(self,url):
        status = 'null'
        outdata = {}
        jsondata = {}
        outdata['cpuload'] = 0
        outdata['cputemp'] = 0
        outdata['gpuload'] = 0
        outdata['gputemp'] = 0
        outdata['cpuclock'] = 0
        outdata['cpuclocksec'] = 0
        outdata['cpuclockmax'] = 0
        outdata['cpuclockmin'] = 10000
        outdata['cpuloadper'] = 0
        outdata['cputempper'] = 0
        outdata['gpuloadper'] = 0
        outdata['gputempper'] = 0

        try:
            response = requests.get(url, timeout=3)
            bodydata = response.text
            jsondata = json.loads(bodydata)
        except:
            return (status,outdata,jsondata)

        status = 'success'
        for primarykey in jsondata['Children'][0]['Children']:
            if 'cpu' in primarykey['ImageURL']:
                for secondarykey in primarykey['Children']:
                    if 'Clocks' in secondarykey['Text']:
                        for thirdkey in secondarykey['Children']:
                            if 'Core' in thirdkey['Text']:
                                tempcpuclockmax = float(re.sub("[^0-9\.]","",thirdkey['Max']))
                                if (tempcpuclockmax > outdata['cpuclockmax']):
                                    outdata['cpuclockmax'] = tempcpuclockmax
                                tempcpuclockmin = float(re.sub("[^0-9\.]","",thirdkey['Min']))
                                if (tempcpuclockmin < outdata['cpuclockmin']):
                                    outdata['cpuclockmin'] = tempcpuclockmin
                                tempcpuclock = float(re.sub("[^0-9\.]","",thirdkey['Value']))
                                if (tempcpuclock > outdata['cpuclock']):
                                    outdata['cpuclock'] = tempcpuclock
                                elif (tempcpuclock > outdata['cpuclocksec']):
                                    outdata['cpuclocksec'] = tempcpuclock
                    if 'Load' in secondarykey['Text']:
                        for thirdkey in secondarykey['Children']:
                            if 'CPU Total' in thirdkey['Text']:
                                outdata['cpuload'] = re.sub("[^0-9\.]","",thirdkey['Value'])
            if 'nvidia' in primarykey['ImageURL']:
                for secondarykey in primarykey['Children']:
                    if 'Temperatures' in secondarykey['Text']:
                        outdata['gputemp'] = re.sub("[^0-9\.]","",secondarykey['Children'][0]['Value'])
                    if 'Load' in secondarykey['Text']:
                        outdata['gpuload'] = re.sub("[^0-9\.]","",secondarykey['Children'][0]['Value'])
            if 'mainboard' in primarykey['ImageURL']:
                for secondarykey in primarykey['Children'][0]['Children']:
                    if 'Temperatures' in secondarykey['Text']:
                        outdata['cputemp'] = re.sub("[^0-9\.]","",secondarykey['Children'][0]['Value'])
        outdata['cputempper'] = (float(outdata['cputemp']) - 20) / 0.7
        if outdata['cputempper'] > 100:
            outdata['cputempper'] = 100
        if outdata['cputempper'] < 1:
            outdata['cputempper'] = 1
        outdata['cpuloadper'] = int(float(outdata['cpuload']))
        if outdata['cpuloadper'] > 100:
            outdata['cpuloadper'] = 100
        if outdata['cpuloadper'] < 0:
            outdata['cpuloadper'] = 0
        outdata['gputempper'] = (float(outdata['gputemp']) - 20) / 0.7
        if outdata['gputempper'] > 100:
            outdata['gputempper'] = 100
        if outdata['gputempper'] < 1:
            outdata['gputempper'] = 1
        outdata['gpuloadper'] = int(float(outdata['gpuload']))
        if outdata['gpuloadper'] > 100:
            outdata['gpuloadper'] = 100
        if outdata['gpuloadper'] < 0:
            outdata['gpuloadper'] = 0
        tempcpuclockper = float(outdata['cpuclock']) - float(outdata['cpuclockmin'])
        tempcpuclocksecper = float(outdata['cpuclocksec']) - float(outdata['cpuclockmin'])
        tempcpuclockmax = float(outdata['cpuclockmax']) - float(outdata['cpuclockmin'])
        outdata['cpuclockper'] = int(tempcpuclockper / tempcpuclockmax * 100)
        outdata['cpuclocksecper'] = int(tempcpuclocksecper / tempcpuclockmax * 100)
#        outdata['cpuload'] = "{0:5.2f}".format(float(outdata['cpuload']))
#        outdata['gpuload'] = "{0:5.2f}".format(float(outdata['gpuload']))
#        outdata['cpuclock'] = "{0:4d}".format(int(outdata['cpuclock']))
#        outdata['cpuclocksec'] = "{0:4d}".format(int(outdata['cpuclocksec']))
#        outdata['cpuclockmax'] = "{0:4d}".format(int(outdata['cpuclockmax']))
#        outdata['cpuclockmin'] = "{0:4d}".format(int(outdata['cpuclockmin']))
        outdata['cputemp'] = float(outdata['cputemp'])
        outdata['gputemp'] = float(outdata['gputemp'])
        outdata['cpuload'] = float(outdata['cpuload'])
        outdata['gpuload'] = float(outdata['gpuload'])
        outdata['cpuclock'] = float(outdata['cpuclock'])
        outdata['cpuclocksec'] = float(outdata['cpuclocksec'])
        outdata['cpuclockmax'] = float(outdata['cpuclockmax'])
        outdata['cpuclockmin'] = float(outdata['cpuclockmin'])

        return (status,outdata,jsondata)
