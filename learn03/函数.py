#!/usr/bin/python
#coding:utf-8
def getIPhone(user):
    print('上帝给了%s一部IPhone' % user)
def addnum(num):
    return num[0] - num[1]
# numnote.py
def numnote(lst):
    msg = []

    for num in lst:

        if num <0:

            s = str(num) + 'fushu'

        elif 0 <= num <= 9:

            s = str(num) + 'zhengshu'

        msg.append(s)

    return msg
print numnote([1,-1])
    