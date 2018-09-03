# -*- coding:utf-8 -*-
import requests


class Zendao():

    def __init__(self,s):  # 初始化
        self.s=s
        self.base = 'http://127.0.0.1:80'  # 禅道的服务器地址

    def login_zendao(self,username,psw):
        #  s=requests.session()  # 不需要在函数里定义，用形参代替
        url='http://127.0.0.1:80/zentao/user-login.html'
        header={
        'User-Agent': "User-Agent: Mozilla/5.0 (Windows NT 10.0;"
                      " WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"}

        body={'account':username,
            'password':psw,
             "keepLogin[]":"on"
            ,'referer':'http://127.0.0.1/zentao/my/'}


        r1=self.s.post(url,headers=header,data=body)
        print(r1.content.decode('utf-8'))
        return r1.content.decode('utf-8')

    def send_img(self):
        url1 = "http://127.0.0.1:80/zentao/file-ajaxUpload-5a26aca290b59.html?dir=image"
        f ={
            "localUrl": (None,"1.png"),
            "imgFile": ("1.png", open("d:\\1.png", "rb"), "image/jpeg")
          }
        r = self.s.post(url1, files=f)
        print(r.text)
        try:
            jpgurl = self.base+r.json()["url"]
            print(u"上传图片后的url地址：%s" % jpgurl)
        except Exception as msg:
            print(u"返回值不是json格式：%s"%str(msg))
            print(r.content)

if __name__ == '__main__':
    s=requests.session()  # 实例化传参数
    log=Zendao(s)    # 类调用方法,
    log.login_zendao('admin','e10adc3949ba59abbe56e057f20f883e')
    log.send_img()
