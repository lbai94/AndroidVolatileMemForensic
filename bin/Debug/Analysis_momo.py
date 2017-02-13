#-*- coding: UTF-8 -*-
from sys import argv
import re
import time
#############################################
class msg:
    msg_id=""
    content=""
    sender=""
    send_time=""
    receive_time=""
    distance=""
    msg_form=0
    def print_profile(self):
        print u"消息id：",self.msg_id
        print u"内容：", self.content
        print u"发送or接收：", self.sender
        print u"发送时间：", self.send_time
        print u"接收/查看时间：", self.receive_time
        print u"聊天双方距离：", self.distance
       
    def write_profile(self,file):
        file.write(u"\r\n聊天记录：\r\n".encode("gbk"))
        if  self.msg_id!="":
            file.write(u"消息id：".encode("gbk"))
            file.write(self.msg_id+'\r\n')
        if self.content!="":
            file.write(u"内容：".encode("gbk"))
            file.write(self.content.encode("gbk")+'\r\n')
        if self.sender!="":
            file.write(u"发送or接收：".encode("gbk"))
            file.write(self.sender.encode("gbk")+'\r\n')
        if self.send_time!="" and self.send_time!='0':
            file.write(u"发送时间：".encode("gbk"))
            file.write(self.send_time.encode("gbk")+'\r\n')
        if self.receive_time!="":
            file.write(u"接收/查看时间：".encode("gbk"))
            file.write(self.receive_time.encode("gbk")+'\r\n')
        if self.distance!="":
            file.write(u"聊天双方的距离：".encode("gbk"))
            file.write(self.distance+'m\r\n') 
################################################################
class user:
    momoid=""
    name=""
    sex=""
    relation=""
    regtime=""
    birthday=""
    countrycode=""
    phone=""
    distance=""
    def print_profile(self):
        print u"陌陌id：",self.momoid
        print u"昵称：", self.name
        print u"性别：", self.sex
        print u"关系：", self.relation
        print u"注册时间：", self.regtime
        print u"生日：", self.birthday
        print u"国家代码：", self.countrycode
        print u"手机号：",self.phone
        print u"与你的距离：", self.distance
    def write_profile(self,file):
        file.write(u"\r\n用户资料：\r\n".encode("gbk"))
        file.write(u"陌陌id：".encode("gbk"))
        file.write(self.momoid+'\r\n')
        if self.name!="":
            file.write(u"昵称：".encode("gbk"))
            file.write(self.name+'\r\n')
        if self.sex!="":
            file.write(u"性别：".encode("gbk"))
            file.write(self.sex+'\r\n')
        if self.relation!="":
            file.write(u"关系：".encode("gbk"))
            file.write(self.relation+'\r\n')
        if self.regtime!="":
            file.write(u"注册时间：".encode("gbk"))
            file.write(self.regtime+'\r\n')
        if self.birthday!="":
            file.write(u"生日：".encode("gbk"))
            file.write(self.birthday+'\r\n')
        if self.countrycode!="":
            file.write(u"国家代码：".encode("gbk"))
            file.write(self.phone+'\r\n')
        if self.phone!="":
            file.write(u"手机号：".encode("gbk"))
            file.write(self.phone+'\r\n')
        if self.distance!="":
            file.write(u"与你的距离：".encode("gbk"))
            file.write(self.phone+'km\r\n') 
        if self.relation=="":
            file.write(u"这可能是本手机登陆的账号。\r\n".encode("gbk"))
#########################################################
class wifi:
    ssid=""
    bssid=""
    mac=""
    def print_profile(self):
        print u"ssid：",self.ssid
        print u"bssid：", self.bssid
        print u"MAC：", self.mac
    def write_profile(self,file):
        file.write(u"\r\n曾经连接的wifi：\r\n".encode("gbk"))
        if  self.ssid!="":
            file.write(u"SSID: ")
            file.write(self.ssid.encode("gbk")+'\r\n')
        if self.bssid!="":
            file.write(u"BSSID: ")
            file.write(self.bssid+'\r\n')
        if self.mac!="":
            file.write(u"MAC: ")
            file.write(self.mac+'\r\n')
#############################################            
script, heap_name, save_file=argv
write_file=open(save_file,'wb') 
###################id###############################
file=open(heap_name,"rb")
tag="\"momoid\""
users=dict()
for line in file:
    pos=line.find(tag)
    if pos!=-1:
        profile=re.search('{[\x20-\x7e]+}',line)
        if profile!=None:
            #print profile.group(),'\n'
            profiles=re.finditer('\"[a-z]+\":',line)
            if profiles!=None:
                user_info=list()
                for i in profiles:
                    search_text=line[i.end():]
                    find=re.search("[\x20-\x2b\x2d-\x7a\x7c\x7e\x7f]+",search_text)
                    if len(find.group())>2 and re.search("[a-zA-Z0-9]",find.group())!=None:
                            user_info.append((i.group().strip(" :\""),find.group().strip(" []\"")))
                find_new_user=False            
                for info in user_info:
                    if "momoid" in info:
                        if not(info[1] in users.keys()):
                            user_object=user()
                            user_object.momoid=info[1]
                            find_new_user=True
                            break
                if find_new_user:            
                    for infos in user_info:
                        if infos[0]=="name" :
                            user_object.name=infos[1]
                        elif infos[0]=="sex" :
                            user_object.sex=infos[1]
                        elif infos[0]=="relation" :
                            user_object.relation=infos[1]
                        elif infos[0]=="regtime":
                            user_object.regtime=infos[1]
                        elif infos[0]=="birthday":
                            user_object.birthday=infos[1]
                        elif infos[0]=="countrycode":
                            user_object.countrycode=infos[1]
                        elif infos[0]=="phonenumber":
                            user_object.phone=infos[1]
                        elif infos[0]=="distance":
                            user_object.distance=infos[1]
                        
                users[user_object.momoid]=user_object
for key,value in users.items():
    #value.print_profile()
    value.write_profile(write_file)
file.close() 
######################msg############################         
file=open(heap_name,"rb")
#head="5019C541".decode('hex')
tag1=u"content="
tag2=u"\"content\""
msg_raw=""
msgs=dict()
unknown=1
for line in file:
    u_search_line=unicode(line,'utf-16','ignore')
    if (tag1 in u_search_line) or (tag2 in u_search_line):
        msg_structures=re.finditer(u"[\u0020-\u007e\u4e00-\u9fa0\u3001-\u3005\uFF01-\uFF1F\u2013\u2014\u2026]+",u_search_line)
        if msg_structures!=None:
            for i in msg_structures:
                if len(i.group())>=100:
                    #print i.group(),'\n'
                    msg_raw=i.group()
                    format=re.search(u"\[[0-9][\u0020-\u007e\u4e00-\u9fa0\u3001-\u3005\uFF01-\uFF1F\u2013\u2014\u2026]+\]",msg_raw)
                    if format!=None:
                        message=msg()
                        msg_raw=format.group()
                        msg_list=msg_raw.split(u',')
                        #print msg_list
                        message.msg_id=msg_list[7].strip(' ')
                        message.send_time=msg_list[0].strip(u"[")
                        if message.send_time=='0':
                            message.sender=u"接收"
                        else:
                            message.send_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(int(message.send_time)/1000000))
                            message.sender=u"发送"
                        message.receive_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(int(msg_list[1].strip(' '))/1000))
                        for j in msg_list:
                            if u"content"in j:
                                message.content=re.search(u":\"[\u0020-\u007e\u4e00-\u9fa0\u3001-\u3005\uFF01-\uFF1F\u2013\u2014\u2026]+\"",j).group().strip(u' :\"')
                            if u"diatance" in j:
                               
                                message.distance=re.search(u"[\u0030-\u0039]+",j).group()
                                break
                        msgs[message.msg_id]=message        
                    elif msg_raw.startswith(u"send"):
                        message=msg()    
                        msg_list=msg_raw.split(u',')
                        pos=msg_list[0].find(u"=")
                        message.msg_id=msg_list[0][pos+1:].strip(' ')
                        if message.msg_id in msgs.keys():
                            continue;
                        message.sender=u"发送"    
                        for j in msg_list:
                            if u"content"in j:
                                message.content=re.search(u"=[\u0020-\u007e\u4e00-\u9fa0\u3001-\u3005\uFF01-\uFF1F\u2013\u2014\u2026]+",j).group().strip(u'=')
                            if u"diatance" in j:
                                message.distance=re.search(u"=[0-9]+",j).group().strip(u"=")
                                break
                        msgs[message.msg_id]=message 
                    else:
                        message=msg()
                        message.form=2
                        msg_list=msg_raw.split(u',')
                      #  print msg_list
                        for j in msg_list:
                            if u"content"in j:
                                message.content=re.search(u":\"[\u0020-\u007e\u4e00-\u9fa0\u3001-\u3005\uFF01-\uFF1F\u2013\u2014\u2026]+\"",j)
                                if message.content!=None:
                                    message.content=message.content.group().strip(u' :\"')
                                else:
                                    break
                            if u"diatance" in j:
                                message.diatance=re.search(u":[0-9]+",j)
                                if message.diatance!=None:
                                    message.distance=re.search(u":[0-9]+",j).group().strip(":")
                                break
                        if message.content!=None and len(message.content)>1:
                            msgs[u"unknown"+str(unknown)]=message 
                            unknown=unknown+1
                            
for key,value in msgs.items():
    #print key
    #value.print_profile()
    value.write_profile(write_file)
file.close()
####################wifi#######################
file=open(heap_name,"rb")

tag="S\x00S\x00I\x00D\x00:\x00"
wifis=dict()
for line in file:
    pos=line.find(tag)
    if pos!=-1:
        u_search_line=unicode(line[pos:],'utf-16','ignore')       
        wifi_raw=re.search(u"[\u0020-\u007e\u4e00-\u9fa0]+",u_search_line)
        if wifi_raw!=None:
            wifi_raw=wifi_raw.group()
            wifi_list=wifi_raw.split(u',')
            wifi_obj=wifi()
            for j in wifi_list:
                if u"BSSID" in j:
                    wifi_obj.bssid=re.search(u":[\u00200-9a-f:]+",j).group().strip(": ")
                elif u"SSID" in j:
                    wifi_obj.ssid=re.search(u":[\u0020-\u007e\u4e00-\u9fa0]+",j).group().strip(": ")
                elif u"MAC" in j:
                    wifi_obj.mac=re.search(u":[\u00200-9a-f:]+",j).group().strip(": ")
            if wifi_obj.ssid!="":
                if wifi_obj.ssid in wifis.keys():
                    if wifis[wifi_obj.ssid].bssid=="":
                        wifis[wifi_obj.ssid].bssid=wifi_obj.bssid
                    if wifis[wifi_obj.ssid].mac=="":
                        wifis[wifi_obj.ssid].mac=wifi_obj.mac
                else:
                    wifis[wifi_obj.ssid]=wifi_obj

for key,value in wifis.items():
    #value.print_profile()
    value.write_profile(write_file)  
file.close()
write_file.close()    

