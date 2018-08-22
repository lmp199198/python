# -*- coding:utf-8 -*-
import requests
from limaopeng.jiekou_wenjianshangchuan.chandao_login import Zendao_login

class Sendfile():
    def __init__(self,s):
        self.s = s
        self.base = 'http://127.0.0.1:81'
    def send_img(self):
        filename="1.png"
        filepath="d:\\1.png"
        url1 = "http://127.0.0.1:81/zentao/file-ajaxUpload-5a26aca290b59.html?dir=image"
        f ={
            "localUrl": (None,"1.png"),
            "imgFile": (filename, open(filepath, "rb"), "image/jpeg")}
        r = self.s.post(url1, files=f)
        print(r.text)
        try:
            jpgurl = self.base+r.json()["url"]
            print(u"上传图片后的url地址：%s" % jpgurl)
            return jpgurl
        except Exception as msg:
            print(u"返回值不是json格式：%s"%str(msg))
            print(r.content)

if __name__ == '__main__':
    s=requests.session()
    log = Zendao_login(s)
    log.login()
    send_file = Sendfile(log.s)
    send_file.send_img()


