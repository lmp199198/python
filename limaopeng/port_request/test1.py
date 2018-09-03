# -*- coding:utf-8 -*-
import requests

# r=requests.get('http://www.cnblogs.com/yoyoketang')
#
# print(r.status_code)
# print(r.text)

# params(参数)
# 参数搜索
url='http://zzk.cnblogs.com/s/blogpost'
par={'Keywords':'yoyoketang'}
header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
'Accept-Encoding': 'gzip, deflate, br',
'Cookie': '_ga=GA1.2.1054404613.1524193805; __utma=59123430.1054404613.1524193805.1524296850.1528185203.2;'
          ' __utmz=59123430.1524296850.1.1.utmcsr=cnblogs.com|utmccn=(referral)|utmcmd=referral|utmcct=/; '
          '__gads=ID=a22eeb9c2c4ece62:T=1524296858:S=ALNI_MZUowc5F2SwW0M_cUUBjcHbCNbKgQ; UM_distinctid=16320308a4f184-019176b32ccdc-13656f4a-1fa400-16320308a50473;'
          ' _gid=GA1.2.2128766084.1528103753; '
          '.CNBlogsCookie=521E0EDAA111083321FA0DB36D0BBB79D44849CDA1D16E479D444A62300572C122678E763B29C1A753A0799787737ADE876DC511303C0FD4D5A4CEF435BDE7F4378339CB1E04D111B02300E1C1CB4D1743CCBF25; .Cnblogs.AspNetCore.Cookies=CfDJ8FHXRRtkJWRFtU30nh_M9mARktWSC7ksgPbrk3hz3-4BUIFFuKqqTBnqfK7tkZirmnOC2EiQwCr2TgvJTED1JL2_l20HZTB6Ll0_-KDYgNUypGC3nnmeuPWnnDBqk-F_aeukkMBH7rA3G_PAt_Tfc00Urf22HH3uPkLNC9A7hBi9DDyNN9TOhT4o8tNi8nCJWXaLSMDpLlUNzelrAow5mnKylu6l0HEE9CyMnXShaj_MsMsv0hyL002E2t8dnXK50aJtYnTMXYWmqjU71j3nXamdZrTS905-f8B7lbTNWL_I;'
          ' __utmc=59123430',
'Connection': 'keep-alive'
}

r=requests.get(url,params=par,headers=header)
print(r.status_code)
print(r.text)

# r=requests.get('https://www.baidu.com')
# print(r.status_code)
# print(r.url)
# print(r.encoding)
# print(r.content)
# print(r.headers)
# print(r.cookies)
'''
-- r.status_code   # 响应状态码
-- r.content   # 字节方式的响应体，会自动为你解码 gzip 和deflate 压缩
-- r.headers   # 以字典对象存储服务器响应头，但是这个字典比较特殊，
字典键不区分大小写，若键不存在则返回 None
-- r.json()   #Requests 中内置的 JSON 解码器
-- r.url  # 获取 url
-- r.encoding  # 编码格式
-- r.cookies  # 获取 cookie
-- r.raw   # 返回原始响应体
-- r.text  # 字符串方式的响应体，会自动根据响应头部的字符编码进行解码
-- r.raise_for_status()   #失败请求(非 200 响应)抛出异常
'''