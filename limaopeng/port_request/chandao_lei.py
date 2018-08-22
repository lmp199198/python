# -*- coding:utf-8 -*-
import requests,unittest,re

url='http://127.0.0.1:81/zentao/user-login.html'
header={
'User-Agent': "User-Agent: Mozilla/5.0 (Windows NT 10.0;"
              " WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"}

body={'account':'admin',
    'password':'e10adc3949ba59abbe56e057f20f883e',
     "keepLogin[]":"on"
    ,'referer':'http://127.0.0.1/zentao/my/'}

body1={'account':'admi',
    'password':'e10adc3949ba59abbe56e057f20f883e',
     "keepLogin[]":"on"
    ,'referer':'http://127.0.0.1/zentao/my/'}

class TestLoginZenTao(unittest.TestCase):

    def setUp(self):
        self.s=requests.session()

    def test_login_successs(self):
        r1=self.s.post(url,headers=header,data=body)
        print(self.s.cookies)
        res1=r1.content.decode('utf-8')
        print(res1)
        result1=re.findall("location='(.+?)'",res1)
        print(result1[0])
        location_url='http://127.0.0.1/zentao/my/'
        self.assertEqual(result1[0],location_url)

    def test_login_fail(self):
        r1=self.s.post(url,headers=header,data=body1)
        res=r1.content.decode('utf-8')
        print(res)
        result=re.findall("alert\('(.+?)'\)",res)
        print(result[0])
        ex='登录失败，请检查您的用户名或密码是否填写正确。'
        self.assertTrue(result[0]==ex)


if __name__ == '__main__':
    unittest.main()


