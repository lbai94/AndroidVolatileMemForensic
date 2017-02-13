from sys import argv
import re
import codecs

script, heap_name, save_file=argv
write_file=open(save_file,'wb')

#########username################
read_file=open(heap_name,"rb")
#head="50C9B841".decode('hex')
mailaddress=dict()
for search_line in read_file:
    #pos=line.find(head)
    #if pos!=-1: 
    #search_line=line[pos:]
    i=0
    #u_search_line=unicode(search_line,'utf-16','ignore')
    #a=re.finditer(u"\"[0-9a-zA-Z\.\-\_]+@[0-9a-zA-Z\-\_]+\.[0-9a-zA-Z\.\-\_]+\"",u_search_line)
    a=re.finditer("\"[0-9a-zA-Z\.\-\_]+@[0-9a-zA-Z\-\_]+\.[0-9a-zA-Z\.\-\_]+\"",search_line)
    if a!=None:
        for i in a:
            #if not (u"mail.gmail" in i.group() ) and len(i.group())>7:
            mailaddress[i.group().lower().strip("\"")]= mailaddress.get(i.group().lower(),0)+1
                
comment=u'\u4ee5\u4e0b\u53ef\u80fd\u662f\u60a8\u66fe\u7ecf\u767b\u9646\u7684\u7535\u5b50\u90ae\u7bb1\u8d26\u53f7:'
#print comment
write_file.write(comment.encode("gbk")+'\r\n')
for key in mailaddress:    
    #print key
    write_file.write(key.encode("gbk")+'\r\n')
read_file.close()


###########password#####################
read_file=open(heap_name,"rb")
head="android-mail-aes"
password=dict()
for line in read_file:
    pos=line.find(head)
    if pos!=-1: 
        #print line[pos:],'\n\n'
        search_line=line[pos:]
        #print search_line
        #password=password+(re.findall("([!-~]\0){2,}",search_line)
        a=re.finditer("[!-~]{6,20}",search_line)
        if a!=None:
            #password.append(a.group(0))
            for i in a:
                if not ("android-mail-aes" in i.group()):
                    password[i.group()]=password.get(i.group(),0)+1
comment=u'\r\n\u4ee5\u4e0b\u662f\u60a8\u53ef\u80fd\u66fe\u7ecf\u4f7f\u7528\u7684\u5bc6\u7801:'
#print comment
write_file.write(comment.encode("gbk")+'\r\n')
for key in password:
    #print key
    write_file.write(key.encode("gbk")+'\r\n')
read_file.close()
 
######wifi##############
"""read_file=open(heap_name,"rb")
head="C\x00O\x00N\x00N\x00E\x00C\x00T\x00E\x00D"
wifi=dict()
for line in read_file:
    pos=line.find(head)
    if pos!=-1: 
        #print line[pos:],'\n\n'
        search_line=line[pos:]
        #print search_line
        #password=password+(re.findall("([!-~]\0){2,}",search_line)
        u_search_line=unicode(search_line,'utf-16','ignore')
        a=re.finditer(u"\"[\u0020-\u007e\u4e00-\u9fa0\u3001-\u3005\uFF01-\uFF1F\u2013\u2014\u2026]+\"",u_search_line)
        if a!=None:
            #password.append(a.group(0))
            for i in a:
                #if not ("android-mail-aes" in i.group()):
                ssid=i.group()
                wifi[ssid]=wifi.get(ssid,0)+1
comment=u'\r\n\u4ee5\u4e0b\u662f\u60a8\u53ef\u80fd\u66fe\u7ecf\u8fde\u63a5\u7684wifi:'
#print comment
write_file.write(comment.encode("gbk")+'\r\n')
for key in wifi:
    #print key
    write_file.write(key.encode("gbk")+'\r\n')
read_file.close() """
   
#######mailaddress######

read_file=open(heap_name,"rb")
#head="50C9B841".decode('hex')
mailaddress=dict()
for search_line in read_file:
    #pos=line.find(head)
    #if pos!=-1: 
    #search_line=line[pos:]
    a=re.finditer("([a-zA-Z\.\-\_]\x00)+@\x00([a-zA-Z\-\_]\x00)+\.\x00([a-zA-Z\.\-\_]\x00)+",search_line)
    if a!=None:
        for i in a:
            m_address=unicode(i.group(),'utf-16','ignore').strip("\"")
            if not ("mail.gmail" in m_address) and len(i.group())>9:
                mailaddress[m_address]=mailaddress.get(m_address,0)+1
comment=u'\r\n\u4ee5\u4e0b\u90ae\u4ef6\u5730\u5740\u53ef\u80fd\u66fe\u4e0e\u60a8\u901a\u4fe1:'
#print comment
write_file.write(comment.encode("gbk")+'\r\n')
for key in mailaddress:
    #print key
    write_file.write(key.encode("gbk")+'\r\n')
read_file.close() 


######content#######

read_file=open(heap_name,"rb")
#head="50C9B84100000000".decode('hex')
mailcontent=dict()
for search_line in read_file:
    #pos=line.find(head)
    #if pos!=-1:   
    #search_line=line[pos:]
    #a=re.finditer("([a-zA-Z\.\-\_]\x00)+@\x00([a-zA-Z\.\-\_]\x00)+",search_line)
    i=0
    u_search_line=unicode(search_line,'utf-16','ignore')
   
    a=re.finditer(u"[\u0020-\u007e\u4e00-\u9fa0\u3001-\u3005\uFF01-\uFF1F\u2013\u2014\u2026]+\s[\u0020-\u007e\s\u4e00-\u9fa0\u3001-\u3005\uFF01-\uFF1F\u2013\u2014\u2026]{10,}",u_search_line)
    #a=re.finditer(u"[\u0020-\u007e\s\u4e00-\u9fa0\u3001-\u3005\uFF01-\uFF1F\u2013\u2014\u2026]{20,3000}",u_search_line)
    if a!=None:
        for i in a:
            content=i.group().lstrip()
            if (u'A'<=content[0] and u'Z'>=content[0]) or (u'\u4e00'<=content[0] and u'\u9fa0'>=content[0]):
                first=content.split(u' ')[0]
                if not (re.match(u'[A-Z]+$',first) or re.match(u'[A-Za-z\-]+\-[A-Za-z\-]+:',first)):
                    mailcontent[content]= mailcontent.get(content,0)+1
"""for key in mailcontent:    
    print key, len(key),mailcontent[key],'\n'"""

content_sort=sorted(mailcontent.items())

comment=u'\r\n\u4ee5\u4e0b\u662f\u60a8\u53ef\u80fd\u7684\u901a\u4fe1\u5185\u5bb9:'
#print comment
write_file.write(comment.encode("gbk")+'\r\n')
key_previous=""
for key,value in content_sort:    
    if not (key_previous[:len(key_previous)-4] in key):
        #print key_previous,'\n'
        write_file.write((key_previous).encode('gbk')) 
        write_file.write('\r\n')
    key_previous=key
#print key_previous,'\r\n'
write_file.write(key_previous.encode('gbk'))
write_file.close()
read_file.close()

