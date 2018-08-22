# -*- coding:utf-8 -*-
import unittest
from selenium import webdriver
import time

class TestLogin(unittest.TestCase):
    '''测试登陆功能点：'''

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()

    def setUp(self):  #前置：
        self.driver.get("http://127.0.0.1/zentao/user-login.html")
        time.sleep(3)


    def test_01(self):   #正确的psw：
        '''测试登陆:账号-admin,密码-123456'''
        self.driver.find_element_by_xpath(".//*[@id='account']").send_keys('admin')
        self.driver.find_element_by_xpath(".//*[@id='login-form']/form/table/tbody/tr[2]/td/input").send_keys('123456')
        self.driver.find_element_by_xpath(".//*[@id='submit']").click()

        time.sleep(2)   #页面跳转必须加time.sleep(2)，否则会报错；

        t=self.driver.find_element_by_xpath(".//*[@id='userMenu']/a").text
        print(t)   #实际结果
        self.assertTrue(t=="admin")  #  与前面的相等self.assertEqual('admin',t)
    #   self.assertTrue('admin' in t)  ==  self.assertIn('admin',t)

    def test_02(self):   #错误的psw：
        '''测试登陆:账号-admin,密码-111111'''
        self.driver.find_element_by_xpath(".//*[@id='account']").send_keys('admin')
        self.driver.find_element_by_xpath(".//*[@id='login-form']/form/table/tbody/tr[2]/td/input").send_keys('000000')
        # self.driver.find_element_by_xpath(".//*[@id='submit']").click()

        time.sleep(2)   #页面跳转必须加time.sleep(2)，否则会报错；

        # t=self.driver.find_element_by_xpath(".//*[@id='userMenu']/a").text
        # print(t)   #实际结果
        # self.assertTrue(t=="admin")

    def test_03(self):
        '''测试登陆:账号-admin,密码-123456'''
        self.driver.find_element_by_id("account").send_keys("admin")
        self.driver.find_element_by_name("password").send_keys("123456")
        self.driver.find_element_by_id("submit").click()

        time.sleep(3)  # 页面跳转地方sleep下
        t = self.driver.find_element_by_css_selector("#userMenu>a").text
        print(t)  # 实际结果
        self.assertTrue("admin" == t)
        # self.assertEqual("admin", t)

    def tearDown(self):   #后置处理：
        self.driver.delete_all_cookies()    #清除cookies，退出登陆
        self.driver.refresh()               #刷新页面

    @classmethod
    def tearDownClass(cls):
         cls.driver.quit()

if __name__ == '__main__':
    unittest.main()