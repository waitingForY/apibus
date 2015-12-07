# -*- coding: cp936 -*-
import re
import os
import codecs
import redis
import json
r=redis.StrictRedis(host='127.0.0.1',port=6379,db=1)

receiveAUser=r' recv kahaoo '
serviceType=""
#userNumber=0
file=open(r'/home/wjb/banklog/ylk_err20150825.err20150825')
lines=file.readline()
class User:

    def __init__(self,serviceType,kahao,area,jiaoYiJinE,status,reasion):
        self.serviceType=serviceType
        self.kahao=kahao
        self.area=area
        self.jiaoYiJinE=jiaoYiJinE
        self.status=status
        self.reasion=reasion
    def displayUser(self):
        print "\n"
        print " tradeType：",self.serviceType, " cadeNumber：",self.kahao," area：",self.area," tradeAmount：",self.jiaoYiJinE,"status:",self.status,"reasion:",self.reasion
users=[] #用户数组，用以存放用户信息，记录何时输出用户信息
def object2dict(obj):#将python对象转换为json数据dict类型
    d={}
    d.update(obj.__dict__)
    return d

while lines:
    linePart=lines.split()
    if re.search(receiveAUser,lines):   #如果检查到有用户交易就创建用户对象
        lineSplit=lines.split()
        user=User("","","",0,"","")
        kahao=lineSplit[6][1:20]
        area=lineSplit[8]
        user.kahao=kahao
        user.area=area
        user.jiaoYiJinE=0
        if len(users)==0:
            users.append(user)
        isHere=False
        for us in users:
            if us.kahao==kahao:
                isHere=True
                break
        if not isHere:
            users.append(user)


    if re.search(r':Begin',lines):
        for user0 in users:
            if re.search(user0.kahao,lineSplit[3]):
                user=user0
                users.append(user)
                break

    if re.search(r':End',lines):
        lineSplit=lines.split()
        serviceType=lineSplit[2][:lineSplit[2].index(':')]
        if re.search(r'Success!',lines):
            for user1 in users:
                
                if re.search(user1.kahao,lineSplit[3]):
                    user1.serviceType=serviceType
                    user1.status="succeed"
                    user1.reasion="succeed"
                if re.search(r',',lineSplit[3]):
                    user1.jiaoYiJinE=float(lineSplit[3][lineSplit[3].index(',')+1:len(lineSplit[3])-2])
                else:
                    user1.jiaoYiJinE=0
                #user1.displayUser()
                d=object2dict(user1)
                print d
                r.publish("channel",d)
                #userNumber+=1
                #userName="user%d"%userNumber
                #r.hset(userName,'tradeType',user1.serviceType)
                #r.hset(userName,'cadeNumber',user1.kahao)
                #r.hset(userName,'area',user1.area)
                #r.hset(userName,'tradeAmount',user1.jiaoYiJinE)
                #r.hset(userName,'status',user1.status)
                #r.hset(userName,'reasion',user1.reasion)
                users.remove(user1)
                break
        if re.search(r'Failed,',lines):
            for user in users:
                if re.search(user.kahao,lineSplit[3]):
                    user.serviceType=serviceType
                    user.status="failded"
                    user.reasion=serviceType+"失败"
                    user.jiaoYiJinE=0
                    #user.displayUser()
                    #userNumber+=1
                    #userName="user%d"%userNumber
                    #r.hset(userName,'tradeType',user.serviceType)
                    #r.hset(userName,'cadeNumber',user.kahao)
                    #r.hset(userName,'area',user.area)
                    #r.hset(userName,'tradeAmount',user.jiaoYiJinE)
                    #r.hset(userName,'status',user.status)
                    #r.hset(userName,'reasion',user.reasion)
                    
                    d=object2dict(user)
                    print d
                    r.publish("channel",d)
                    users.remove(user)
                    break
    if re.search(r'卡号',lines):
        lineSplit2=lines.split()
        for user2 in users:
            if re.search(user2.kahao,lines):
                user2.status="failed"
                user2.serviceType="交易失败"
                user2.reasion=lineSplit2[4]
                #user2.displayUser()
                #userNumber+=1
                #userName="user%d"%userNumber
                #r.hset(userName,'tradeType',user2.serviceType)
                #r.hset(userName,'cadeNumber',user2.kahao)
                #r.hset(userName,'area',user2.area)
                #r.hset(userName,'tradeAmount',user2.jiaoYiJinE)
                #r.hset(userName,'status',user2.status)
                #r.hset(userName,'reasion',user2.reasion)
                d=object2dict(user2)
                print d
                r.publish("channel",d)
                users.remove(user2)
                break
    lines=file.readline()
file.close()




