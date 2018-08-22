# -*- coding:utf-8 -*-
import requests
import urllib3
urllib3.disable_warnings()
url='https://i.cnblogs.com/EditPosts.aspx?opt=1'
header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
'Accept-Encoding': 'gzip, deflate, br',
}
r=requests.get(url,verify=False,headers=header)
print(r.cookies)
# 显灰色是因为编辑器的原因：
c=requests.cookies.RequestsCookieJar()
# print(c)
# 添加登陆需要的cookies,不需要的cookies可以不用添加，
c.set(".CNBlogsCookie","8CC2EF3F7C8295D7665BF47FD21EAF632A4B9A4695727E41"
                       "69372CF88296F12AAC8C9C23FB1CDADCAF0446DF43A9CB173"
                       "36AD36CE5A868FD71131F48186C6718CC80E6E1AD1D92E14DB75AF87A900C7352B51C16")
c.set(".Cnblogs.AspNetCore.Cookies","CfDJ8FHXRRtkJWRFtU30nh_M9mBI5I3ul1aWrEuPutwH4W30zJoaa__0ZpLFE7LOnPvvrrMr06-SlAlC2jXS1GupEAqVcjGq1PMdvbRK_X8hPJbhqdP73I2zHcAKbME_ists1PPllwe0HId49haCDyTFzurxd4-0ASFDXxgKg9OzVtDSb6BQUURo8Ud-VtSvkJNRY1SQopp5JhQ4su7xnFjcTKw6TvwmD28dibnk26Hhc4UcZqxpeWmBdsZkyO0M30_dxRCrOUGsgpwMrSeIE4pZVnj7kJb2LOYqfRrn8RAYdV1l")
r.cookies.update(c)
print("# 添加后的cookies：")
print(r.cookies)

# 登陆之前把cookies提取出来，
login_cookies=r.cookies

url1='https://i.cnblogs.com/EditPosts.aspx?opt=1'
# r1=requests.get(url1,verify=False,cookies=c)
# print(r1.content.decode("utf-8"))

body={'__VIEWSTATE':'',
      '__VIEWSTATEGENERATOR':'FE27D343',
      'Editor$Edit$txbTitle':'李茂鹏13',
      'Editor$Edit$EditorBody':'<p>风格的恢复大会受到广大是固定格式的</p>',
      'Editor$Edit$Advanced$ckbPublished':'on',
      'Editor$Edit$Advanced$chkDisplayHomePage':'on',
      'Editor$Edit$Advanced$chkComments':'on',
      'Editor$Edit$Advanced$chkMainSyndication':'on',
      'Editor$Edit$Advanced$txbEntryName':'',
      'Editor$Edit$Advanced$txbExcerpt':'',
      'Editor$Edit$Advanced$txbTag':'',
      'Editor$Edit$Advanced$tbEnryPassword':'',
      'Editor$Edit$lkbDraft':'存为草稿'}
