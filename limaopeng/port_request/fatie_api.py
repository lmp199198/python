# -*- coding:utf-8 -*-
from selenium import webdriver
import requests
import urllib3
import re
urllib3.disable_warnings()

class Blog():
    def __init__(self):
        self.s=requests.session()

    def zidong_login(self):
        path=r'C:\Users\lenovo\AppData\Roaming\Mozilla\Firefox\Profiles\wxglh3q7.default'
        profile=webdriver.FirefoxProfile(path)
        driver=webdriver.Firefox(firefox_profile=profile)

        driver.get('https://www.cnblogs.com/yoyoketang/')
        cookie=driver.get_cookies()
        # print(cookie)   # list对象
        driver.quit()

        c=requests.cookies.RequestsCookieJar()
        for i in cookie:
            c.set(i["name"],i["value"])
        self.s.cookies.update(c)
        url='https://i.cnblogs.com/EditPosts.aspx?opt=1'
        r1=self.s.get(url,verify=False)
        # print(r1.content.decode('utf-8'))
        # print(c)
        return r1.content.decode('utf-8'),c
    # 发帖接口
    def fatie(self):
        url='https://i.cnblogs.com/EditPosts.aspx?opt=1'
        header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0;"
                    " WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"}
        body={'__VIEWSTATE':'',
              '__VIEWSTATEGENERATOR':'FE27D343',
              'Editor$Edit$txbTitle':'逝水伊人238',
              'Editor$Edit$EditorBody':'<p>格的恢复大会受广大是固定格式的</p>',
              'Editor$Edit$Advanced$ckbPublished':'on',
              'Editor$Edit$Advanced$chkDisplayHomePage':'on',
              'Editor$Edit$Advanced$chkComments':'on',
              'Editor$Edit$Advanced$chkMainSyndication':'on',
              'Editor$Edit$Advanced$txbEntryName':'',
              'Editor$Edit$Advanced$txbExcerpt':'',
              'Editor$Edit$Advanced$txbTag':'',
              'Editor$Edit$Advanced$tbEnryPassword':'',
              'Editor$Edit$lkbDraft':'存为草稿'}

        r2=self.s.post(url,data=body,headers=header,verify=False)
        print(r2.url)
        return r2.url

    # 正则提取
    # 知道前后字符，如：postid=9255297
    def get_postid(self,fatie_url):
        postid=re.findall('postid=(.+?)&',fatie_url)[0]
        # print(postid[0])
        print(postid)
        return postid

    # 删除草稿接口
    def deletejiekou(self,postid):
        url2='https://i.cnblogs.com/post/delete'
        body1={'postId':postid}
        r2=self.s.post(url2,json=body1,verify=False)
        res=r2.json()['isSuccess']   # 返回响应中的字典信息
        print(res)
        print(type(res))
        return res
        # assert res==True



if __name__ == '__main__':
    # s=requests.session()
    blog=Blog()
    blog.zidong_login()
    fatie_url=blog.fatie()
    postid=blog.get_postid(fatie_url)
    deletetiezi=blog.deletejiekou(postid)



