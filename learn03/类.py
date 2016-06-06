#!/usr/bin/python
#coding:utf-8
class myHouse():
    def __init__(self,houseType='',houseOwner=''):
        self.houseType=houseType
        self.houseOwner=houseOwner
        self.things=''
    def showHouse(self):
        print '''这里是%s家,
        %s:%s''' % ( self.houseOwner , self.houseType,self.things)
    def buyThings(self,thingsName=''):
        self.things+='%s ' % thingsName
        
xiaohong=myHouse(houseType='两室一厅',houseOwner='小红')
xiaoming=myHouse(houseType='三室一厅',houseOwner='小明')
xiaohong.buyThings('马桶')
xiaohong.showHouse()
xiaoming.showHouse()
        
    
        