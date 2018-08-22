# -*- coding:utf-8 -*-
import requests
import json
import re
import urllib3
urllib3.disable_warnings()

# 没有界面的微型浏览器：
s=requests.session()
# print('# 没有发请求之前的cookis：')
# print(s.cookies)
url='https://i.cnblogs.com/EditPosts.aspx?opt=1'
r=s.get(url,verify=False)
# print('# 发了请求之后的cookies：')
# # print(s.cookies)

# 登陆的cookies：
c=requests.cookies.RequestsCookieJar()
c.set(".CNBlogsCookie","729F3D4F7E08AAAB48F32733331711636610FF4F5D487C855D6F5CF05292532BA82DA3092E7939A507D85C899724806FF9464B9335F45D8B1DC39C016DE0C4F784647CDE262351E2260B21A9BD70AC76C37C6065")
c.set(".Cnblogs.AspNetCore.Cookies",
      "CfDJ8FHXRRtkJWRFtU30nh_M9mBAR7Kq8ik1sXm_iwtAHIcFsa5Foo13OtJnrKki84R3u2gL5bFwa8wjqgqfqfn6uxTQMNvi3FisSvck-k8Z5XwHaUuDXXwvZgKYUl-R1pK-RvhT06vdZUjui6WT7K-mmmg_FFB0OyhXBDa6BGC3My0NUfFi900cK6EytcVLqGdvOgPuKJPlSY_xxsJ5UtaWDs3p7AHPg_YbZTcp_bHwct7Dwws6H_2l8fpaBgB3ygXK_89E_DAvIvSRQb4GcnLxI47fYCCojhCxuppwrTEQ0YqxlA3BxZ7-D5DF2XsCm0UYEQ")
s.cookies.update(c)
print('# 登陆之后的cookies:')
print(s.cookies)
# r1=s.get(url,verify=False)
# print(r1.content.decode("utf=8"))
# print(r2.content.decode("utf-8"))

# 发帖接口：
body={'__VIEWSTATE':'',
      '__VIEWSTATEGENERATOR':'FE27D343',
      'Editor$Edit$txbTitle':'逝水伊人1',
      'Editor$Edit$EditorBody':'<p>格的恢复大会受广大是固定格式的</p>',
      'Editor$Edit$Advanced$ckbPublished':'on',
      'Editor$Edit$Advanced$chkDisplayHomePage':'on',
      'Editor$Edit$Advanced$chkComments':'on',
      'Editor$Edit$Advanced$chkMainSyndication':'on',
      'Editor$Edit$Advanced$txbEntryName':'',
      'Editor$Edit$Advanced$txbExcerpt':'',
      'Editor$Edit$Advanced$txbTag':'',
      'Editor$Edit$Advanced$tbEnryPassword':'',
      'Editor$Edit$lkbDraft':'存为草稿'}

r1=s.post(url,data=body,verify=False)
print(r1.url)

# 正则提取
# 知道前后字符，如：postid=9255297
postid=re.findall('postid=(.+?)&',r1.url)
print(postid[0])

# 删除草稿接口
url2='https://i.cnblogs.com/post/delete'
body1={'postId':postid[0]}

r2=s.post(url2,json=body1,verify=False)
res=r2.json()['isSuccess']
print(res)

assert res==True