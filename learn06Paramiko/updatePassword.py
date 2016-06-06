# coding:utf-8 
import random,paramiko,csv,sys
#定义随机生成密码函数
def randomPass():
    #passStr:随机从这些字符串生成组成密码
    passStr="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    #passLength:密码长度
    passLength=16
    #使用循环,每次从passStr选择一个字符赋值给newPass,直到达到passLength定义的长度
    newPass=""
    for x in xrange(passLength):
        newPass+=random.choice(passStr)
    #返回随机生成的密码
    return  newPass
#定义ssh连接函数并执行修改密码
def sshConn(hostname,username,password,edituser,newPass):
    #创建SSH连接
    ssh=paramiko.SSHClient()
    #自动添加hostkey ,使用这个是为了在Windows下面可以使用
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #修改密码的命令
    execEditPass="echo %s:"% (edituser)+"%s|chpasswd"  % (newPass)
    try:
        #开始SSH连接
        ssh.connect(hostname=hostname,username=username,password=password)
        #执行的命令
        stdin,stdout,stderr=ssh.exec_command(execEditPass)
        #输出账号修改后的信息
        print hostname+":"+edituser+":"+newPass
    #发生错误时候显示错误信息
    except Exception,e:
        print "Error:"+str(e)
    #不管运行是否正常,强制关闭ssh连接        
    finally:
        ssh.close()
        return newPass
def readUser(csvUser):
    try:
        #打开账号配置文件
        userCsv=file(csvUser,'rb')
        #以csv格式 读取
        userLine=csv.reader(userCsv)
        #利用循环实现批量更改 1:hostname 2.username 3.password 4.要修改的用户名
        for user in userLine:
            #使用sshConn来进行密码更改
            sshConn(user[1],user[2],user[3],user[4],randomPass())
        userCsv.close()
    #发生错误时候显示错误信息
    except Exception,e:
        print "Error:"+str(e)
def main():
    readUser('user.csv')
if __name__=="__main__":
    main()