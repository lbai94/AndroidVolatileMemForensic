#-*- coding: UTF-8 -*-
from sys import argv
import re
import time
#############################################
class card:
    bank_name=""
    bank_type=""
    bind_tail=""
    mobile=""
    name=""
    def print_profile(self):
        print u"银行：",self.bank_name
        print u"银行卡类型：", self.bank_type
        print u"卡尾号：", self.bind_tail
        print u"手机号：", self.mobile
        print u"真实姓名：", self.name
    def write_profile(self,file):
        file.write(u"卡尾号：".encode("gbk"))
        file.write(self.bind_tail+'\r\n')
        if self.bank_type!="":
            file.write(u"银行卡类型：".encode("gbk"))
            file.write(self.bank_type.encode("gbk")+'\r\n')
        if self.bank_name!="":
            file.write(u"银行：".encode("gbk"))
            file.write(self.bank_name.encode("gbk")+'\r\n')  
        if self.mobile!="":
            file.write(u"手机号：".encode("gbk"))
            file.write(self.mobile.encode("gbk")+'\r\n')
        if self.name!="":
            file.write(u"姓名：".encode("gbk"))
            file.write(self.name.encode("gbk")+'\r\n')
################################################################
class trans:
    id=""
    fee=""
    goods=""
    creat_time=""
    modified_time=""
    state=""
    type=""
    actual_pay=""
    def print_profile(self):
        print u"订单编号：", self.id
        print u"购买商品：", self.goods
        print u"应付金额：", self.fee, self.type
        print u"实付金额：", self.actual_pay, self.type
        print u"创建时间：", self.creat_time
        print u"支付时间：", self.modified_time
        print u"订单状态：", self.state
    def write_profile(self,file):
        if  self.id!="":
            file.write(u"订单编号：".encode("gbk"))
            file.write(self.id.encode("gbk")+'\r\n')
        if self.goods!="":
            file.write(u"购买商品：".encode("gbk"))
            file.write(self.goods.encode("gbk")+'\r\n')
        if self.fee!="":
            file.write(u"应付金额: ".encode("gbk"))
            file.write(str(self.fee)+self.type+'\r\n')
        if self.actual_pay!="":
            file.write(u"实付金额: ".encode("gbk"))
            file.write(str(self.actual_pay)+self.type+'\r\n')
        if self.creat_time!="":
            file.write(u"创建时间: ".encode("gbk"))
            file.write(self.creat_time.encode("gbk")+'\r\n')
        if self.modified_time!="":
            file.write(u"支付时间: ".encode("gbk"))
            file.write(self.modified_time.encode("gbk")+'\r\n')
        if self.state!="":
            file.write(u"订单状态: ".encode("gbk"))
            file.write(self.state.encode("gbk")+'\r\n')
########################################################################
class month:
    year=""
    month=""
    money=""
    def print_profile(self):
        print u"时间：", self.year,'-', self.month
        print u"消费总额：￥", self.money
    def write_profile(self,file):
        if  self.year!="":
            file.write(u"时间：".encode("gbk"))
            file.write((self.year+u"年"+self.month+u"月").encode("gbk")+'\r\n')
        if self.money!="":
            file.write(u"消费总额：￥".encode("gbk"))
            file.write(self.money.encode("gbk")+'\r\n')
#############################################            
script, heap_name, save_file=argv
write_file=open(save_file,'wb') 
###################trans###############################
file=open(heap_name,"rb")
#file=open("wcpay_dev_ashmem_dalvik-heap","rb")
tag="\"\x00U\x00s\x00e\x00r\x00R\x00o\x00l\x00l\x00L\x00i\x00s\x00t\x00\"\x00:\x00[\x00"
transs=dict()
months=dict()
for line in file:
    pos=line.find(tag)
    if pos!=-1:
        u_search_line=unicode(line[pos:],'utf-16','ignore')       
        trans_iter=re.finditer(u"\{[\u0020-\u007e\u4e00-\u9fa0\uff1a\uffe5]+?\}",u_search_line)
        if trans_iter!= None:
            for trans_raw in trans_iter:
                trans_raw=trans_raw.group()
                #print trans_raw,'\n'
                trans_list=trans_raw.split(u',')
                if "Transid" in trans_list[0]:
                    trans_obj=trans()
                    for j in trans_list:
                        if u"Transid" in j:
                            trans_obj.id=re.search(u":\"[0-9]+\"",j).group().strip(":\" ")
                        elif u"\"TotalFee\"" in j:
                            trans_obj.fee=re.search(u":[0-9]+",j).group().strip(":\" ")
                            trans_obj.fee=float(trans_obj.fee)/100
                        elif u"GoodsName" in j:
                            trans_obj.goods=re.search(u":\"[\u0020-\u007e\u4e00-\u9fa0]+\"",j).group().strip(":\" ")
                        elif u"CreateTime" in j:
                            trans_obj.creat_time=re.search(u":[0-9]+",j).group().strip(":\" ")
                            trans_obj.creat_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(int(trans_obj.creat_time)))
                        elif u"TradeStateName" in j:
                            trans_obj.state=re.search(u":\"[\u0020-\u007e\u4e00-\u9fa0]+\"",j).group().strip(":\" ")
                        elif u"ModifyTime" in j:
                            trans_obj.modified_time=re.search(u":[0-9]+",j).group().strip(":\" ")
                            trans_obj.modified_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(int(trans_obj.modified_time)))
                        elif u"FeeType" in j:
                            trans_obj.type=re.search(u":\"[a-zA-Z]+\"",j)
                            if trans_obj.type!=None:
                                trans_obj.type=trans_obj.type.group().strip(":\" ")
                            else:
                                trans_obj.type=""
                        elif u"ActualPayFee" in j:
                            trans_obj.actual_pay=re.search(u":[0-9]+",j).group().strip(":\" ")
                            trans_obj.actual_pay=float(trans_obj.actual_pay)/100
                    if trans_obj.id!="":
                            transs[trans_obj.id]=trans_obj
                elif "year" in trans_list[0]:
                    trans_obj=month()
                    for j in trans_list:
                        if u"year" in j:
                            trans_obj.year=re.search(u":[0-9]{4}",j).group().strip(":\" ")
                        elif u"month" in j:
                            trans_obj.month=re.search(u":[0-9]{1,2}",j).group().strip(":\" ")
                        elif u"feetext" in j:
                            trans_obj.money=re.search(u"[0-9.]+",j).group().strip(":\" ")
                    months[trans_obj.year+'-'+trans_obj.month]=trans_obj
write_file.write(u"月度消费:\r\n".encode('gbk'))
for key,value in months.items():
   # value.print_profile()
    value.write_profile(write_file)
write_file.write(u"\r\n消费记录:\r\n".encode('gbk'))
for key,value in transs.items():
    #value.print_profile()
    value.write_profile(write_file)    

file.close() 
#####################card############################         

       
file=open(heap_name,"rb")
#file=open("wcpay_dev_ashmem_dalvik-heap","rb")
tag="\"\x00b\x00a\x00n\x00k\x00_\x00n\x00a\x00m\x00e\x00\"\x00"
cards=dict()
for line in file:
    pos=line.find(tag)
    if pos!=-1:
        u_search_line=unicode(line[pos:],'utf-16','ignore')       
        card_raw=re.search(u"[\u0020-\u007e\u4e00-\u9fa0]+",u_search_line)
        if card_raw!=None:
            card_raw=card_raw.group()
            card_list=card_raw.split(u',')
            card_obj=card()
            for j in card_list:
                if u"bank_name" in j:
                    card_obj.bank_name=re.search(u":[\u0020-\u007e\u4e00-\u9fa0]+",j).group().strip(":\" ")
                elif u"bank_type" in j:
                    card_obj.bank_type=re.search(u":\"[\u0020-\u007e]+\"",j).group().strip(":\" ")
                elif u"bind_tail" in j:
                    card_obj.bind_tail=re.search(u":\"[\u00200-9]+\"",j).group().strip(":\" ")
                elif u"mobile" in j:
                    card_obj.mobile=re.search(u":\"[\u0020\u002A0-9]+\"",j).group().strip(":\" ")
                elif u"true_name" in j:
                    card_obj.name=re.search(u":\"[\u0020-\u007e\u4e00-\u9fa0]+\"",j).group().strip(":\" ")
            if card_obj.bind_tail!="":
                    cards[card_obj.bind_tail]=card_obj

write_file.write(u"\r\n银行卡资料：\r\n".encode("gbk"))
for key,value in cards.items():
    #value.print_profile()
    value.write_profile(write_file)
file.close()
write_file.close()    

