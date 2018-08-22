# -*- coding:utf-8 -*-
from limaopeng.sale_project.login.login_01 import login
from selenium import webdriver
import unittest
import time

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        # login(cls.driver)    #只登录一次
        cls.result=login(cls.driver)


    def test_01(self):
        # login(self.driver)   #公共的函数可以放在一起，移到setUpClass下面：
        print('测试用例01')
        self.assertTrue(self.result=='admin')


    def test_02(self):
        # login(self.driver)
        print('测试用例02')
        canshu=self.result
        print(canshu,'lmp')


    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()
    @classmethod
    def tearDownClass(cls):
        # time.sleep(3)
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
