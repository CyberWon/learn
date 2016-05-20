#!/usr/bin/python
#coding:utf-8
a=1
while a<10:
    li=''
    for b in range(1,10):
        if a>=b:
            li+='%sx%s=%s '%(a,b,a*b)
    print li
    a+=1