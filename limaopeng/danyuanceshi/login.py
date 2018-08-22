# -*- coding:utf-8 -*-
import unittest
from selenium import webdriver
import time

class TestLogin(unittest.TestCase):

    def setUp(self):  #前置：
        self.driver=webdriver.Firefox()
        self.driver.get("http://127.0.0.1/zentao/user-login.html")
        time.sleep(1)

    def test_01(self):   #正确的psw：
        self.driver.find_element_by_xpath(".//*[@id='account']").send_keys('admin')
        self.driver.find_element_by_xpath(".//*[@id='login-form']/form/table/tbody/tr[2]/td/input").send_keys('123456')
        self.driver.find_element_by_xpath(".//*[@id='submit']").click()

        time.sleep(2)   #页面跳转必须加time.sleep(2)，否则会报错；

        t=self.driver.find_element_by_xpath(".//*[@id='userMenu']/a").text
        print(t)   #实际结果
        self.assertTrue(t=="admin")  #  与前面的相等self.assertEqual('admin',t)
    #   self.assertTrue('admin' in t)  ==  self.assertIn('admin',t)

    def test_02(self):   #错误的psw：
        self.driver.find_element_by_xpath(".//*[@id='account']").send_keys('admin')
        self.driver.find_element_by_xpath(".//*[@id='login-form']/form/table/tbody/tr[2]/td/input").send_keys('000000')
        self.driver.find_element_by_xpath(".//*[@id='submit']").click()

        time.sleep(2)   #页面跳转必须加time.sleep(2)，否则会报错；

        t=self.driver.find_element_by_xpath(".//*[@id='userMenu']/a").text
        print(t)   #实际结果
        self.assertTrue(t=="admin")

    def tearDown(self):   #后置
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()