#!/usr/bin/python
#coding:utf-8
# -*- coding:utf-8 -*-
import pycurl
import StringIO
import threading

def curl(url,TIME_OUT=5):       # 设置超时时间，默认为5s
    c = pycurl.Curl()           # 创建一个curl
    c.setopt(pycurl.URL,url)    # 设置请求url的地址
    c.setopt(pycurl.CONNECTTIMEOUT,TIME_OUT)
    c.setopt(pycurl.TIMEOUT,TIME_OUT)
    HTML_HEAD=StringIO.StringIO() # HEADER信息存放
    HTML_BODY=StringIO.StringIO() # HTML 代码存放 
    c.setopt(pycurl.HEADERFUNCTION,HTML_HEAD.write)
    c.setopt(pycurl.WRITEFUNCTION,HTML_BODY.write)
    try:
        c.perform()     #开始连接。有问题抛出异常
        HTTP_CODE=c.getinfo(c.HTTP_CODE)
        HEAD=HTML_HEAD.getvalue()
        SERVER_TYPE=''
        for i in HEAD.split('\n'):
            if "Server" in i:
                SERVER_TYPE=i.split()[1]
        return (url,HTTP_CODE,SERVER_TYPE)
    except Exception as e:
        return (url,000,e[1])
    finally:
        c.close()
def main():
    for i in open('ip.txt','r'):
        url=i.replace('\n','')
        print curl(url,TIME_OUT=3)
if __name__=='__main__':
    main()
