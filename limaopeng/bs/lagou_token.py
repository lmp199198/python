# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import urllib3
import re
urllib3.disable_warnings()

class Login_lg():
    def __init__(self):
        self.s=requests.session()
        self.url='https://passport.lagou.com/login/login.html'
        self.h={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0'}

    def get_token(self):
        r1=self.s.get(self.url,headers=self.h,verify=False)
        # print(r1.content.decode('utf-8'))
        soup=BeautifulSoup(r1.content.decode('utf-8'),'html.parser')
        TokenCode={}
        try:
            t=soup('script')[1].get_text()
            Forge_Token=re.findall("Forge_Token = '(.+?)'",t)[0]
            Forge_Code=re.findall("Forge_Code = '(.+?)'",t)[0]

            # 建立字典，将token和code添加到TokenCode：
            TokenCode['X-Anit-Forge-Token']=Forge_Token
            TokenCode['X-Anit-Forge-Code']=Forge_Code
            print(TokenCode)
            return TokenCode
        except:
            print(False)

    def login_lagou(self,anti_token,username,psw):
        url2='https://passport.lagou.com/login/login.json'
        h1={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding':'gzip, deflate, br',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Anit-Forge-Token':anti_token['X-Anit-Forge-Token'],
    'X-Anit-Forge-Code':anti_token['X-Anit-Forge-Code'],
    'Referer':'https://passport.lagou.com/login/login.html',
    'Content-Length':'111'}

        body2={'isValidate':'true',
               'username':username,
               'password':psw,
               'request_form_verifyCode':'',
               'submit':''
        }
        self.s.headers.update(h1)
        r2=self.s.post(url2,headers=h1,data=body2,verify=False)
        json=r2.json()
        print('登录结果：%s' % json)
        return json

    def get_submitToken(self,re):
        result=re['submitToken']
        print('submitToken:',result)
        return result

if __name__ == '__main__':
    login=Login_lg()
    token=login.get_token()
    res=login.login_lagou(token,17665480259,'f66315560097b81047a962bc318afc12')
    login.get_submitToken(res)



