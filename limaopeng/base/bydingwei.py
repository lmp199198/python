# -*- coding:utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Firefox()
driver.get('https://www.baidu.com')

def findElement(driver,by,value):
    element = WebDriverWait(driver,10,0.4).until(lambda x: x.find_element(by,value))
    element.click()
    return element

# 输入搜索内容：
# *arg可变参数
locator1=('id','kw')
element1=findElement(driver,*locator1).send_keys('我爱你')
# element1=findElement(driver,'id','kw').send_keys('我爱你')
# element1.send_keys('我爱你')

# 点击查询按钮：
locator2=('id','su')
element2=findElement(driver,*locator2).click()
# element2=findElement(driver,'id','su').click()
driver.quit()