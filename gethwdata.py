import urllib.request
import json
import time

url = 'http://172.16.19.1:8085/data.json'
datafile = '/ramdisk/hwdata.json'

req = urllib.request.Request(url)

while True:
    try:
        with urllib.request.urlopen(req) as res:
            body = json.load(res)
        fw = open(datafile,'w')
        json.dump(body,fw,indent=4)
        fw.close()
    except:
        time.sleep(30)
    time.sleep(2)