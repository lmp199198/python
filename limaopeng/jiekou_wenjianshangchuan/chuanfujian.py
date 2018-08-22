# -*- coding:utf-8 -*-
import requests
import time
from limaopeng.jiekou_wenjianshangchuan.chandao_login import Zendao_login

class SendFiles():
    def __init__(self,s):
        self.s=s

    def sendfile(self):
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
        # 使用list分开传附件参数：因为字典的键是唯一的，为了可以重复使用list传参数：
        file=[('files[]',('1.png',open('d:\\1.png','rb'),"image/jpeg")),
              ('lables[]','image1'),
               ('files[]',('2.png',open('d:\\2.png','rb'),"image/jpeg")),
               ('lables[]','image2'),
        ]

        r = self.s.post(url,data=body,files=file)
        res=r.text
        print(res)
        return res

if __name__ == '__main__':
    s=requests.session()
    denglu=Zendao_login(s)
    log=denglu.login()
    send=SendFiles(s)
    send.sendfile()
