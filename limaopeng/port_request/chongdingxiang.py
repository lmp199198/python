# -*- coding:utf-8 -*-
import requests
import urllib3
urllib3.disable_warnings()
host='https://i.cnblogs.com/'
url=host+'EditPosts.aspx?opt=1'

header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
'Accept-Encoding': 'gzip, deflate, br',
}


# 重定向   allow_redirects=True
s=requests.session()
r=s.get(url,headers=header,verify=False)   #200
# r=s.get(url,headers=header,allow_redirects=False,verify=False)  # 302
# print(r.status_code)
# print(r.url)
# print(r.headers)
# new_url=r.headers['location']  #urlencode编码
# print(host+new_url)
print(r.history)
for i in r.history:
    print(i.url)
    print(i.status_code)
    print(i.headers)