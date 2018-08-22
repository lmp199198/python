# -*- coding:utf-8 -*-
from selenium import webdriver
import time


def login(self,driver, user, password):
    '''登录github'''
    # 打开github首页
    driver.get("https://github.com/login")
    driver.implicitly_wait(10)
    # 输入账号
    driver.find_element_by_id("login_field").send_keys(user)
    # 输入密码
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_name("commit").click()

def get_text(driver):
    # 点右上角设置
    driver.find_element_by_css_selector(".HeaderNavlink.name.mt-1").click()
    # try:
    #     t=driver.find_element_by_xpath(".//*[@id='user-links']/li[3]/details/ul/li[1]/strong").text
    #     print(t)
    #     return t
    # except:
    #     return False
    t=driver.find_element_by_xpath(".//*[@id='user-links']"
                                   "/li[3]/details/ul/li[1]/strong").text
    print(t)


def logout(self,driver):
    '''退出github'''
    time.sleep(3)
    # 点右上角设置
    # driver.find_element_by_css_selector(".HeaderNavlink.name.mt-1").click()
    time.sleep(1)
    # 点sign out
    driver.find_element_by_css_selector(".dropdown-item.dropdown-signout").click()
    driver.quit()

if __name__ == "__main__":
    driver = webdriver.Firefox()
    # 调用登录
    lmp=Git()
    lmp.login(driver, "lmp199198", "ppp199198")
    print("hello  lmp")
    lmp.get_text(driver)
    # 调用退出
    lmp.logout(driver)