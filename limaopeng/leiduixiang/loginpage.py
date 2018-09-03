# -*- coding:utf-8 -*-
import time
from selenium import webdriver
class LoginPage():
    '''登陆页面'''
    def __init__(self,driver):
        self.driver=driver
        self.driver.get("http://127.0.0.1/zentao/user-login.html")
    def logout(self):
        '''登出'''
        self.driver.delete_all_cookies()
        self.driver.refresh()
    def input_username(self,username):
        '''输入账号'''
        self.driver.find_element_by_xpath(".//*[@id='account']").send_keys(username)
    def input_psw(self,psw):
        '''输入密码'''
        self.driver.find_element_by_xpath(".//*[@id='login-form']/form/table/tbody/tr[2]/td/input").send_keys(psw)
    def click_login_button(self):
        '''点击登陆按钮'''
        self.driver.find_element_by_xpath(".//*[@id='submit']").click()
    def login(self,username='admin',psw=123456):
        '''登录三步走'''
        self.input_username(username)
        self.input_psw(psw)
        self.click_login_button()
        time.sleep(2)
    def get_login_result(self):
        # 写判断
        try:
            t = self.driver.find_element_by_css_selector("#userMenu>a").text
            return t
        except:
            print(False)
            return ''
if __name__ == '__main__':
    driver=webdriver.Firefox()
    loginpage=LoginPage(driver)
    loginpage.login()
    # result=loginpage.login()
    result=loginpage.get_login_result()
    print(result)
    loginpage.logout()

