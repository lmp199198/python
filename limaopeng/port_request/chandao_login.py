# -*- coding:utf-8 -*-
import requests

s=requests.session()

url='http://127.0.0.1/zentao/user-login.html'
header={
'User-Agent': "User-Agent: Mozilla/5.0 (Windows NT 10.0;"
              " WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"}

body={'account':'admin',
    'password':'e10adc3949ba59abbe56e057f20f883e',
     "keepLogin[]":"on"
    ,'referer':'http://127.0.0.1/zentao/my/'}

r1=s.post(url,headers=header,data=body)
print(s.cookies)
res=r1.content.decode('utf-8')
print(res)

# r2=s.get('http://127.0.0.1/zentao/qa/')


# 定义函数中有打印结果，需要在最后顶行def输入print：
def is_login_success():
    if "登录失败，请检查您的用户名或密码是否填写正确。" in res:
        print("登陆失败！！！！！！！！！")
        return False
    elif "parent.location='http://127.0.0.1/zentao/my/'" in res:
        print("登录成功")
        return True
# print(is_login_success())
assert is_login_success()==True


