# -*- coding:utf-8 -*-
def login():    #调用login方法，每一条用例都会调用该方法
    print('登陆')
    return "登陆"

def logout():   #调用logout方法，每一条用例都会调用该方法
    print('退出')
    return "退出"
print(login(),logout())