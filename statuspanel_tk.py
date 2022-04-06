#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

import tktoolkit
#import ledtoolkit

import hwmonitor
import remotecontrol

import renderstatusstream
import renderstatusstreammain
import renderlifegame

import rendermainstatus
import renderbigstatus

import renderlogo
import rendermonsterpalade
import renderfieldview
import rendertile
import renderbar
import rendercircle

def main():
    basedir = './'
    ramdiskdir = './'
    hwmonitorurl = 'http://127.0.0.1:8085/data.json'

    tktoolkitobject = tktoolkit.tktoolkit()
#    ledtoolkitobject = ledtoolkit.worker()
    monitor = hwmonitor.worker()
    remote = remotecontrol.worker(ramdiskdir)
    statusstream = renderstatusstream.worker(basedir)
    statusstreammain = renderstatusstreammain.worker(basedir)
    lifegame = renderlifegame.worker()

    monsterpalade = rendermonsterpalade.worker(basedir)
    monsterpaladeimage = monsterpalade.imagenew()
    fieldview = renderfieldview.worker(basedir)
    tile = rendertile.worker()
    bar = renderbar.worker()
    circle = rendercircle.worker()
    logo = renderlogo.worker(basedir)

    mainstatus = rendermainstatus.worker(basedir)
    bigstatus = renderbigstatus.worker(basedir)

    statustime = 0

    ledmainimage = logo.draw()
    ledsubimage = logo.draw()
    viewmain = 0
    viewsub = 0
    viewstatus = 0

#    ledimage = ledtoolkitobject.imagenew()

    while True:
        statustimenow = int(time.time())
        if statustimenow != statustime:
            (status,outdata,jsondata) = monitor.getdata(hwmonitorurl)
            if status == 'success':
                statusstream.load(jsondata)
                statusstreammain.load(jsondata)
                lifegame.add(outdata['cputempper'],outdata['gputempper'])
                tile.add(outdata['cpuload'],outdata['gpuload'])
                remote.putdata('CPU: ' + str(outdata['cpuload']) + '% GPU: ' + str(outdata['gpuload']) + '%                          \n')
            remdata = remote.getdata()
            viewmain = remdata['viewmain']
            viewsub = remdata['viewsub']
            viewstatus = remdata['viewstatus']
            statustime = statustimenow

        if viewsub == 0:
            ledsubimage = statusstream.draw('w')
        elif viewsub == 1:
            ledsubimage = statusstream.drawelec('w')
        elif viewsub == 2:
            ledsubimage = tile.draww()
        elif viewsub == 3:
            ledsubimage = lifegame.draw()
        lifegame.next()
        tile.next()

        if viewmain == 0:
            monsterpaladebgimage = monsterpalade.bgdraw(outdata['gputempper'])
            ledmainimage = monsterpalade.draw(monsterpaladebgimage,outdata['cpuloadper'],outdata['cputempper'])
        elif viewmain == 1:
            ledmainimage = fieldview.draw(outdata['cpuloadper'],outdata['cputempper'])
        elif viewmain == 2:
            ledmainimage = tile.draw()
        elif viewmain == 3:
            ledmainimage = bar.draw(outdata['cpuclockper'],outdata['cpuclocksecper'])
        elif viewmain == 4:
            ledmainimage = circle.draw(outdata['cpuloadper'],outdata['gpuloadper'])
        elif viewmain == 5:
            ledmainimage = statusstreammain.draw('h')
        elif viewmain == 6:
            ledmainimage = statusstreammain.drawelec('h')
        elif viewmain == 7:
            ledmainimage = logo.draw()
        elif viewmain == 8:
            ledmainimage = logo.drawnull()

        if viewstatus == 0:
            ledmainimage = mainstatus.draw(ledmainimage,outdata['cpuclock'],outdata['cpuload'],outdata['cputemp'],outdata['gpuload'],outdata['gputemp'])
        elif viewstatus == 1:
            ledmainimage = bigstatus.draw(ledmainimage,outdata['cpuclock'],outdata['cpuload'],outdata['cputemp'],outdata['gpuload'],outdata['gputemp'])
        tktoolkitobject.output(ledsubimage,ledmainimage)
#        ledtoolkitobject.output(ledimage,ledsubimage,ledmainimage)
        time.sleep(0.03)
if __name__ == '__main__':
    main()
