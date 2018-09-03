# -*- coding:utf-8 -*-
import unittest
from selenium import webdriver
import time

# driver=webdriver.Firefox()
# 参数化：
def login(driver,username='admin',psw='123456'):    #driver是形参
    '''登录函数'''
    # 保证函数里面的每个参数都要定义
    driver.get("http://127.0.0.1/zentao/user-login.html")
    time.sleep(3)
    #登陆:
    # username='admin'
    # psw='123456'
    driver.find_element_by_xpath(".//*[@id='account']").send_keys(username)
    driver.find_element_by_xpath(".//*[@id='login-form']/form/table/tbody/tr[2]/td/input").send_keys(psw)
    driver.find_element_by_xpath(".//*[@id='submit']").click()

    # 控制台输入参数：
    # a=input('请输入你的账号:')
    # b=input("请输入你的密码:")

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()

    def test_01(self):
        login(self.driver)

if __name__ == '__main__':
    unittest.main()