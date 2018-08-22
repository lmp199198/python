# -*- coding:utf-8 -*-
import requests
import time
from limaopeng.jiekou_wenjianshangchuan.chandao_login import Zendao_login
import re

class Submitbug():
    def __init__(self,s):
        self.s=s

    def submit(self):
        # host="http://127.0.0.1:81"
        url='http://127.0.0.1:81/zentao/bug-create-1-0-moduleID=1.html'
        jpg_url='data/upload/1/201808/1710575803718tnc.png'
        now_time=time.strftime('%Y-%m-%d-%H:%M:%S')
        body = { "product": "1",
                    "module": "1",
                    "project": "",
                    "openedBuild[]": "trunk",
                    "assignedTo": "admin",
                    "type": "codeerror",
                    "os": "",
                    "browser": "",
                    "color": "",
                    "title": "提交bug-%s" % now_time,
                    "severity": "3",
                    "pri": "0",
                    "steps": '<p>[步骤]</p>\
                        <p>1、第一步：点</p>\
                        <p>2、第二步：点</p>\
                        <p>3、上传图片</p>\
                        <p>[结果]</p>\
                        <p><img alt="" src="%s" /></p>\
                        <p>[期望]</p>' % jpg_url,
                    "story": "0",
                    "task": "0",
                    "mailto[]": "",
                    "keywords": "",
                    "uid": "5b7625e7acdc4",
                    "case": "0",
                    "caseVersion": "0",
                    "result": "0",
                    "testtask": "0"
                    }
        r = self.s.post(url,data=body)
        res=r.text
        print(res)
        return res

    def get_location(self,res):
        loc=re.findall("location='(.+?)'",res)[0]
        print('self.location:',loc)
        return loc
        # html='/zentao/bug-browse-1-0-byModule-1.html'


if __name__ == '__main__':
    s=requests.session()
    sub=Zendao_login(s)
    sub.login()
    subfile=Submitbug(sub.s)
    l=subfile.submit()
    subfile.get_location(l)


