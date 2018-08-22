# -*- coding:utf-8 -*-
import time
import unittest
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

    time.sleep(3)  # 页面跳转地方sleep下

    # 获取用户名：
    # 通过 try 和 except 去判断结果是否正确：
    try:
        t = driver.find_element_by_css_selector("#userMenu>a").text
        print(t)
        return t

    except:
        print(False)
        return None
if __name__ == '__main__':
    from selenium import webdriver
    driver=webdriver.Firefox()
    login(driver)
    time.sleep(3)
    driver.quit()


