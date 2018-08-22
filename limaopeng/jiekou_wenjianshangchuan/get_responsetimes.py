# -*- coding:utf-8 -*-
import requests
r=requests.get('http://www.cnblogs.com/yoyoketang/')

# 获取页面响应时间:
print(r.elapsed.total_seconds())