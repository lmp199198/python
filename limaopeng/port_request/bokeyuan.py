# -*- coding:utf-8 -*-
import requests
import urllib3
urllib3.disable_warnings()
url='https://passport.cnblogs.com/user/signin'
header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
'Accept-Encoding': 'gzip, deflate, br',
'Content-Type': 'application/json; charset=utf-8',
'VerificationToken': '@TokenHeaderValue()',
'X-Requested-With': 'XMLHttpRequest',
'Referer': 'https://passport.cnblogs.com/user/signin',
'Content-Length': '557',
'Connection': 'keep-alive'}

payload={'input1':'SWz5mheppg4eWVf1qhu1vc6ZhZucJ/4DbQJv2xgGSnotp/3I2gW/0nBnns6HBPxrbNroH+uD8UotZczKgUud1xvZHeaC2AHhJ36cCUi'
               'qlJFJ8TTb4qGNfL7rIrgmB2N8oNjo5RpkPVktbZMe3GZiCB5hOitB9XY8cH3yxdt4lMs=',
      'input2':'rKNIM6cLsvIBDOnYHTFGzJi8w85JqrTCOU4mBEGWXCljEP9TWEqxYlff5rHjPwYjjB+MbHfHm3HO6j/hQnY97KrudRHCzBvEVmrzVz'
               'IQYvy89O/AqebNidKUHzZJnYC5xRSpmBBxgwRD+zCWlk68TjV1wGRP6+yA4HULFuqJWUE="',
      'remember':False}

s=requests.session()
r=s.post(url,json=payload,verify=False)
print(r.text)