# -*- coding:utf-8 -*-
import requests
s=requests.session()

print(s.headers)   # 微型浏览器

s.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'

print(s.headers)  # 更新后的头部


# 头部中中加入token，对token进行参数化处理： 避免多次传token参数
token='xxxx'

s.headers['token']=token
# s.headers.update(h)
print(s.headers)

url='http://www.cnblogs.com/yoyoketang/p/'

s.get(url)
