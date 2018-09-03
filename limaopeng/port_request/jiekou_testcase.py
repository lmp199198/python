# -*- coding:utf-8 -*-
import requests,unittest
from limaopeng.jiekou_wenjianshangchuan.chandao_login import Zendao_login


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.s=requests.session()
        self.log=Zendao_login(self.s)

    def test01(self):
        '''正确的账号和密码'''
        result=self.log.login('admin','e10adc3949ba59abbe56e057f20f883e')
        login_result=self.log.is_login_success(result)
        print(login_result)
        self.assertTrue(login_result)

    def test02(self):
        '''错误的账号正确的密码'''
        result=self.log.login('admi','e10adc3949ba59abbe56e057f20f883e')
        login_result=self.log.is_login_success(result)
        print(login_result)
        self.assertFalse(login_result)
    def test03(self):
        '''错误的账号正确的密码'''
        result=self.log.login('admin','10adc3949ba59abbe56e057f20f883e')
        login_result=self.log.is_login_success(result)
        print(login_result)
        self.assertFalse(login_result)

if __name__ == '__main__':
    unittest.main()

