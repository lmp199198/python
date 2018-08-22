# -*- coding:utf-8 -*-
import requests
from urllib import parse

url='http://zzk-s.cnblogs.com/s/blogpost?Keywords=博客'

r=requests.get(url)
print(r.url)
res=r.url

# 对整个url解码：
s1=res.split('?')[1]
print(s1)
s2=s1.split('&')
print(s2)

for i in s2:
    if 'Keywords' in i:
        print(i.split('=')[1])
        a=i.split('=')[1]

# 对整个url解码：
b='%E5%8D%9A%E5%AE%A2'
# d='李茂鹏'
c=parse.unquote(b)   # 解码
print('李茂鹏',parse.quote('李茂鹏'),sep='=')  #编码
print(c)