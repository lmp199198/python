# -*- coding:utf-8 -*-
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# driver=webdriver.Firefox()
# driver.get("https://www.baidu.com")
#
# driver.find_element_by_id('kw').send_keys('我爱你')
# driver.find_element_by_id("kw").click()    # 调用方法
# a=driver.find_element_by_id('kw').text     # 属性
# b=driver.find_element_by_id('kw').tag_name # 属性
# print(a,b)

class Qest():
    def __init__(self):
        self.a=5
        self.b=4
        self.acc=self.add()

    def add(self):
        j=self.a*self.b
        return j



if __name__ == '__main__':
    aa=Qest()
    # print(aa.acc)
    print(aa.add())   # 属性
    print(aa.a)       # 方法
    print(aa.b)

