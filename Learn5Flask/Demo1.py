#!/usr/bin/python
#coding:utf-8
from flask import Flask
from flask import request
app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name
@app.route('/get/browser')
def GetBrowser():
    '''HTTP_USER_AGENT是用来检查浏览页面的访问者在用什么操作系统（包括版本号）浏览器（包括版本号）和用户个人偏好的代码。'''
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent
if __name__ == '__main__':
    app.run(debug=True)