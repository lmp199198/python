# -*- coding:utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import urllib3
import re
urllib3.disable_warnings()

class Followers():
    def __init__(self):
        self.s=requests.session()
        self.path=r'C:\Users\lenovo\AppData\Roaming\Mozilla\Firefox\Profiles\wxglh3q7.default'
        self.url='https://home.cnblogs.com/u/yoyoketang/relation/followers'
# 获取cookies
    def get_cookie(self):
        try:
            profile=webdriver.FirefoxProfile(self.path)
            self.driver=webdriver.Firefox(firefox_profile=profile)
            self.driver.get('https://www.cnblogs.com/yoyoketang/')
            cookies=self.driver.get_cookies()
            # print(cookie)   # list对象
            self.driver.quit()
            return cookies
        except Exception as msg:
            print('浏览器启动失败:%s' % msg)

    # 添加cookies
    def add_cookie(self,cookies):
        c=requests.cookies.RequestsCookieJar()
        for i in cookies:
            c.set(i["name"],i["value"])
        self.s.cookies.update(c)

    # 爬取粉丝数量：
    def get_page_num(self):
        try:
            r1=self.s.get(self.url,verify=False)
            # print(r1.content.decode('utf-8'))
            self.soup=BeautifulSoup(r1.content.decode('utf-8'),'html.parser')
            fensinub = self.soup.find_all(class_="current_nav")
            num = re.findall("Ta的粉丝\((.+?)\)", fensinub[0].string)
            print("Ta的粉丝数量:%s" % int(num[0]))
            # print(type(num))   <class 'list'>
            # 计算页数：
            self.yeshu=int(int(num[0])/45)+1
            print('总的页数:%d' % self.yeshu)
            return self.yeshu
        except Exception as msg1:
            print('获取粉丝数量错误：%s' % msg1)

    # 抓取页面数粉丝：：
    def save_fensi_name(self,n):
        try:
            for page in range(1,n+1):
                if page <= 1:
                    url_page=self.url
                else:
                    url_page=self.url+'/?page=%s' % str(page)
                print('正在爬取的页面：%s' % url_page)
                r2=self.s.get(url_page,verify=False)
                soup2=BeautifulSoup(r2.content.decode('utf-8'),'html.parser')
                fensi_name = soup2.find_all(class_='avatar_name')
                for i in fensi_name:
                    # replace(),将前一个字符替换成后一个字符（'\n',''），去掉换行
                    name1 = i.string.replace('\n','').replace(' ','')
                    # print(name1)
                    f=open('name.txt','a',encoding='utf-8')
                    f.write(name1+'\n')
        except Exception as msg2:
            print('抓取页面粉丝名称失败：%s' % msg2)

if __name__ == '__main__':
    follower=Followers()
    cookies=follower.get_cookie()
    follower.add_cookie(cookies)
    m=follower.get_page_num()
    follower.save_fensi_name(m)






