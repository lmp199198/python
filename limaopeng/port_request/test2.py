# -*- coding:utf-8 -*-
import requests
import json

# data
# payload={'yoyo':'hello world',
#          'python':'1235465'}
# r=requests.post('http://httpbin.org/post',params=payload)
# # 两者相等
# print(r.content.decode())
# print(r.text)
url='http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html'
body={'account':'admin','password':'e10adc3949ba59abbe56e057f20f883e'
    ,'referer':'%2Fzentao%2F'}

r1=requests.post(url,json=body)

print(r1.content)

# data转换成json
# data_json=json.dumps(body)
r2=requests.post(url,data=json.dumps(body))
print(r2.content)