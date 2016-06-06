#!/usr/bin/python
#coding:utf-8
from flask import Flask
from flask import request
import pycurl
import StringIO
app = Flask(__name__)
@app.route('/ip', methods=['GET', 'POST'])
def FlaskIP():
    ip=request.args.get('ip')   #/ip?ip=192.168.1.1,8.8.8.8
    ip_list=ip.split(',')       #以,分割将字符串转换成list['192.168.1.1','8.8.8.8']
    res=''
    for i in ip_list:
       res+='<br>%s'% IP138(i)
    return res
def IP138(ip,TIME_OUT=3):
    url = 'http://test.ip138.com/query/?ip=%s&datatype=text' % ip 
    c = pycurl.Curl()           # 创建一个curl
    c.setopt(pycurl.URL,url)    # 设置请求url的地址
    c.setopt(pycurl.CONNECTTIMEOUT,TIME_OUT)
    c.setopt(pycurl.TIMEOUT,TIME_OUT)
    HTML_BODY=StringIO.StringIO()
    c.setopt(pycurl.WRITEFUNCTION,HTML_BODY.write)
    c.perform() 
    return HTML_BODY.getvalue()
if __name__=='__main__':
    app.run(debug=True)