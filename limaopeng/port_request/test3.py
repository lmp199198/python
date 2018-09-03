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
result=r.json()
print(result)
# print(result['company'])
# data=result['data']
# # print(data)
# for i in data:
#     print(i)
# # print(data[0])
# get_result=data[0]['context']
# print(get_result)
# if "已签收" in get_result:
#     print('快递单已被签收')
# else:
#     print('未签收')
