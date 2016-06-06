#!/usr/bin/python
#coding:utf-8
import pycurl
import StringIO
import threading                #导入多线程模块

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
        print (url,HTTP_CODE,SERVER_TYPE)
    except Exception as e:
        print (url,000,e[1])
    finally:
        c.close()
def main():
    T_thread=[]                     #先定义一个多线程list，也就是线程队列
    for i in open('ip.txt','r'):
        url=i.replace('\n','')
        t=threading.Thread(target=curl,args=(url,3))  #创建线程对象
        T_thread.append(t)                          #将线程对象放入队列
    for i in range(len(T_thread)):                  #循环从线程队列取出线程
        t.setDaemon(True)
        T_thread[i].start()                         #启动线程
    for i in range(len(T_thread)):
        fina_flag=True
        if T_thread[i].is_alive():
            while fina_flag:
                if T_thread[i].is_alive():
                    continue
                else:
                    fina_flag=False
if __name__=='__main__':
    main()
