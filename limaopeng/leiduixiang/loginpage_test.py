# -*- coding:utf-8 -*-
from selenium import webdriver
import unittest
from limaopeng.leiduixiang.loginpage import LoginPage

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.loginpage=LoginPage(cls.driver)

    # def setUp(self):
    #     self.driver=webdriver.Firefox()
    #     self.loginpage=LoginPage(self.driver)

    def test_01(self):
        # 第一步：登陆
        self.loginpage.login()

        #第二步：获取结果
        result=self.loginpage.get_login_result()

        #第三步：断言
        self.assertTrue('admin'==result)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def tearDown(self):
        self.loginpage.logout()

if __name__ == '__main__':
    unittest.main()
