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
c.set(".CNBlogsCookie","8CC2EF3F7C8295D7665BF47FD21EAF632A4B9A4695727E41"
                       "69372CF88296F12AAC8C9C23FB1CDADCAF0446DF43A9CB173"
                       "36AD36CE5A868FD71131F48186C6718CC80E6E1AD1D92E14DB75AF87A900C7352B51C16")
c.set(".Cnblogs.AspNetCore.Cookies",
      "CfDJ8FHXRRtkJWRFtU30nh_M9mBI5I3ul1aWrEuPutwH4W30zJoaa__0ZpLFE7LOnPvvrrMr06-SlAlC2jXS1GupEAqVc"
    "jGq1PMdvbRK_X8hPJbhqdP73I2zHcAKbME_ists1PPllwe0HId49haCDyTFzurxd4-0ASFDXxgKg9OzVtDSb6BQUURo8Ud-VtSvkJNRY1SQopp5JhQ4su7xnFjcTKw6"
    "TvwmD28dibnk26Hhc4UcZqxpeWmBdsZkyO0M30_dxRCrOUGsgpwMrSeIE4pZVnj7kJb2LOYqfRrn8RAYdV1l")
s.cookies.update(c)
# print('# 登陆之后的cookies:')
# print(s.cookies)
# r1=s.get(url,verify=False)
# print(r1.content.decode("utf=8"))
# print(r2.content.decode("utf-8"))

# 发帖接口：
body={'__VIEWSTATE':'',
      '__VIEWSTATEGENERATOR':'FE27D343',
      'Editor$Edit$txbTitle':'98456',
      'Editor$Edit$EditorBody':'<p>3213</p>',
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
#  断言
assert res==True