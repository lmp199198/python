# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

url='http://www.cnblogs.com/yoyoketang/p/'
r=requests.get(url)

html=r.content.decode('utf-8')
# print(r.content.decode('utf-8'))

soup=BeautifulSoup(html,'html.parser')

# 第一种方法：
# 查找的是img标签下的class属性：
all=soup(class_="PostList")
# print(all)
for i in all:
    print(i.div.a['href'])
    print(i.div.a['id'])
    print(i.div['class'])
    print(i.div.a.string)