# -*- coding:utf-8 -*-
import requests
class Zendao_login():
    def __init__(self,s):
        self.s= s
        self.base = 'http://127.0.0.1:81/'  # 禅道的服务器地址
    def login(self,username='admin',psw="e10adc3949ba59abbe56e057f20f883e"):
        loginUrl = self.base+"/zentao/user-login.html"
        h = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate",
            "Referer": "http://127.0.0.1/zentao/user-login.html",
            # "Cookie":  # 头部没登录前不用传cookie，因为这里cookie就是保持登录的
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            }
        body = {"account":username,
                "password":psw,
                "keepLogin[]":"on",
                "referer":"http://127.0.0.1/zentao/my/"
                }
          # 保持会话
        r = self.s.post(loginUrl, data=body, headers=h)
        print(r.text)  # 打印结果看到location='http://127.0.0.1/zentao/my/'说明登录成功了
        return r.text


    # # 上传图片
    # url1 = "http://127.0.0.1/zentao/file-ajaxUpload-5a26aca290b59.html?dir=image"
    #
    # f ={
    #     "localUrl": (None,"1.png"),
    #     "imgFile": ("1.png", open("d:\\1.png", "rb"), "image/png")
    #   }
    # r = self.s.post(url1, files=f)
    # print(r.text)
    # try:
    #     jpgurl = base+r.json()["url"]
    #     print(u"上传图片后的url地址：%s" % jpgurl)
    # except Exception as msg:
    #     print(u"返回值不是json格式：%s"%str(msg))
    #     print(r.content)


if __name__ == '__main__':
    s=requests.session()
    denglu=Zendao_login(s)
    denglu.login()
