# -*- coding:utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import urllib3
import re
urllib3.disable_warnings()

path=r'C:\Users\lenovo\AppData\Roaming\Mozilla\Firefox\Profiles\wxglh3q7.default'
profile=webdriver.FirefoxProfile(path)
driver=webdriver.Firefox(firefox_profile=profile)

driver.get('https://www.cnblogs.com/yoyoketang/')
cookie=driver.get_cookies()
# print(cookie)   # list对象
driver.quit()

s=requests.session()
c=requests.cookies.RequestsCookieJar()
for i in cookie:
    c.set(i["name"],i["value"])
s.cookies.update(c)
# print(c)

url='https://home.cnblogs.com/u/yoyoketang/relation/followers'
r1=s.get(url,verify=False)
# print(r1.content.decode('utf-8'))


soup=BeautifulSoup(r1.content.decode('utf-8'),'html.parser')
# print(soup)
#
# text=fensi[0].string
# print(text)
#
# num=re.findall("Ta的粉丝\((.+?)\)",r1.content.decode('utf-8'))
# print("他的粉丝数量:%s" % num)

# 爬取粉丝数量：
fensinub = soup.find_all(class_="current_nav")
# print(fensinub[0].string)
num = re.findall("Ta的粉丝\((.+?)\)", fensinub[0].string)
print("Ta的粉丝数量:%s" % int(num[0]))
# print(type(num))   <class 'list'>

# 计算页数：
yeshu=int(int(num[0])/45)+1
print('总的页数:%d' % yeshu)

# 抓取第一页面数据：
fensi=soup.find_all(class_='avatar_name')
for i in fensi:
    # replace(),将前一个字符替换成后一个字符（'\n',''），去掉换行
    name = i.string.replace('\n','').replace(' ','')
    # print(name)
    f=open('name.txt','a',encoding='utf-8')
    f.write(name+'\n')


# 抓取第二页后的数据：
for j in range(2,yeshu+1):
    url2='https://home.cnblogs.com/u/yoyoketang/followers/?page=%s' % str(j)
    r2=s.get(url2,verify=False)
    soup1=BeautifulSoup(r2.content.decode('utf-8'),'html.parser')
    fensiname = soup1.find_all(class_='avatar_name')
    for e in fensiname:
        # replace(),将前一个字符替换成后一个字符（'\n',''），去掉换行
        name1 = e.string.replace('\n','').replace(' ','')
        # print(name1)
        f=open('name.txt','a',encoding='utf-8')
        f.write(name1+'\n')





