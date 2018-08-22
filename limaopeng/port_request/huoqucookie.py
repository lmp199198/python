# -*- coding:utf-8 -*-
from selenium import webdriver
import requests
import urllib3
urllib3.disable_warnings()

def sele_login():
    path=r'C:\Users\lenovo\AppData\Roaming\Mozilla\Firefox\Profiles\wxglh3q7.default'
    profile=webdriver.FirefoxProfile(path)
    driver=webdriver.Firefox(firefox_profile=profile)

    driver.get('https://www.cnblogs.com/yoyoketang/')
    cookie=driver.get_cookies()
    print(cookie)   # list对象
    driver.quit()
    return cookie
    # print(sele_login())

url='https://passport.cnblogs.com/user/signin'
header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0;"
        " WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"}
s=requests.session()
s1=s.cookies
# print(s1)
cookie=sele_login()
c=requests.cookies.RequestsCookieJar()
for i in cookie:
    c.set(i["name"],i["value"])
s.cookies.update(c)
print(c)

new_url1='https://i.cnblogs.com/EditPosts.aspx?opt=1'
r1=requests.get(new_url1,verify=False,cookies=c)
# print(r1.content.decode("utf-8"))
