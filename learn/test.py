#--*--encoding:utf-8--*--
import urllib
import re
# def IsIP(s):
#     return len([i for i in s.split('.') if (0<=int(i)<=255)])==4
#
# def URL(ip):
# 	uip=urllib.urlopen('http://wap.ip138.com/ip.asp?ip=%s'%ip)
# 	fip=uip.read()
# 	rip=re.compile(r"<br/><b>查询结果：(.*)</b><br/>")
# 	result=rip.findall(fip)
# 	print "%s\t %s" %(ip,result[0])
#
#
# if __name__=='__main__':
#
#     print URL('44.16.0.255')

import re

line = "dasdsthedsdasd"

matchObj = re.search(r'the', line)

if matchObj:
   print "matchObj.group() : ", matchObj.group()
   # print "matchObj.group(1) : ", matchObj.group(1)
   # print "matchObj.group(2) : ", matchObj.group(2)
   # # print "matchObj.group(3) : ", matchObj.group(3)
else:
   print "No match!!"
