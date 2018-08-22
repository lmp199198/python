# -*- coding:utf-8 -*-
def login(username,psw):
    if username !='admin':
        return '账号错误'
    elif psw != '11111':
        return '密码错误'
    elif username == 'admin' and psw == '11111':
        # print('登陆成功')
        return 'token=xxxxx'

    else:
        return '账户名不存在'

if __name__ == '__main__':
    # print(login('admin1','11111'))
    res=login('admin','11111')   # 返回的是字符串
    print(res)