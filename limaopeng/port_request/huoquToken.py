# -*- coding:utf-8 -*-
import requests
url='http://www.kuaidi.com/index-ajaxselectcourierinfo-1202247993797-yunda.html'
header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
'Accept-Encoding': 'gzip, deflate',
'Connection': 'keep-alive'}

s=requests.session()
r=s.get(url,headers=header)
# 返回的是json格式信息：
# result=r.json()['token']      # json转字典,并取出token
# print(result)
print(s.headers)

# 统一在session里面管理头部信息：

token='xxxx'
s.headers['token']=token   # 更新toke
# n

# 如果这个post请求的头部其它参数变了，也可以直接更新:
s.headers["Content-Length"]="9"
print(s.headers)



# 第二次发送登陆请求需要把上一次请求中的token获取出来：
# token在url里面：进行参数化
# url2='http://www.xxxx.com？token=%s' % result  #方法1

# par={'token':result}   # par参数化    #方法2


# token请求在body信息中：
body={'key1':'value1',
       'key2':'value2',
      'token':token
         }

# 利用session管理的header，发送请求就不需要携带头部了
r1=s.post(url,json=body)



