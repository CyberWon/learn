#!/usr/bin/python
#coding:utf-8
import paramiko
class MySSH():
    def __init__(self,hostname=None,password=None,username=None,port=22):
        self.hostname=hostname
        self.password=password
        self.username=username
        self.port=port
        #创建一个ssh客户端
        self.s=paramiko.SSHClient()
        #连接时候自动加载策略。默认对方主机的指纹没在自己电脑上是连接不上的。
        self.s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            #在类初始化的时候就进行连接。
            self.s.connect(hostname = self.hostname,username=self.username, password=self.password,port=self.port)
        except Exception as e:
            #链接时候发生错误将错误的信息显示出来
            print(e)    
    def run(self,command):
        #执行命令的输出结果是tuple（stdin,stdout,stderr）,所以这样写。获取各个对应的值
        #执行命令是通过exec_command('要执行的命令')
        stdin,stdout,stderr=self.s.exec_command(command)
        print(stdout.read()) 
    def close(self):
        self.s.close()
if __name__=='__main__':
    ssh1=MySSH(hostname='127.0.0.1',username='root',password='123456',port=19957)
    ssh2=MySSH(hostname='127.0.0.2',username='root',password='123456')
    ssh1.run('hostname')
    ssh2.run('hostname')
    ssh1.close()
    ssh2.close()