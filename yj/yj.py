#!/usr/bin/python
#
#通过linux管道读取数据，然后解析出数据的源地址，url，转换成json传给一介网络
#
#
#
import sys
import base64
import urllib2
import urllib


def main():
    bi=sys.stdin.read()
    srcIP=bi.split(" ")[2]

    if(bi.find("GET")):
        str1=bi[bi.find("GET")+4:]
    if(bi.find("POST")):
        str1=bi[bi.find("POST")+5:]
    str1=bi[bi.find("GET")+4:]
    url_str=str1[:str1.find(" ")]
    str2=bi[bi.find("Host")+6:]
    host_str=str2[:str2.find("\\n")]
    Url=host_str+url_str
    values = {'srcIP':srcIP,'Url':Url}
    params = urllib.urlencode(values)
    print params
    value=base64.b64encode(params)
    url = 'http://rv.dugesheying.com/dd/re/yh?url='
    #req = urllib2.Request(url + value)
    #response = urllib2.urlopen(req)
    #print response.read()
    print url+value

if __name__ == '__main__':
    main()
