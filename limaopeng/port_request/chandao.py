# -*- coding:utf-8 -*-
import requests

url='http://127.0.0.1:81/zentao/my/'

header={
'User-Agent': "User-Agent: Mozilla/5.0 (Windows NT 10.0;"
              " WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"}
r=requests.get(url,headers=header)
print('# 之前的cookies：')
print(r.cookies)

c=requests.cookies.RequestsCookieJar()
print(c)
c.set('za','admin')
c.set('zp','341a7937d7850d169f2980d95d6a9b4a44088920')
c.set('zentaosid','vobckiorr50s1r9vovhpd2s4t4')
c.set(name='.cnblogs.com',value='.CNBlogsCookie',
      expiry=1554959887,path='/',httOnly=True,secure=False)
r.cookies.update(c)
print("# 更新的cookies：")
print(r.cookies)
url1='http://127.0.0.1/zentao/my/'
r=requests.get(url1,headers=header,cookies=c)
print(r.content.decode('utf-8'))

# cookies完整实例：
cookie ={'domain':'.cnblogs.com',
         'name':'.CNBlogsCookie',
         'value':'xxxx',
         'expiry': 1554959887,
         'path': '/',
         'httpOnly': True,
         'secure': False}
