# -*- coding:utf-8 -*-
import requests,unittest
from limaopeng.port_request.jiekou_fengzhuang import Login


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.s=requests.session()
        self.log=Login()

    def test01(self):
        '''正确的账号和密码'''
        result=self.log.login('admin','e10adc3949ba59abbe56e057f20f883e')
        print(result)
        self.assertIn('parent.location',result)

    def test02(self):
        '''错误的账号正确的密码'''
        result=self.log.login('admi','e10adc3949ba59abbe56e057f20f883e')
        print(result)
        self.assertNotIn('parent.location',result)

if __name__ == '__main__':
    unittest.main()

