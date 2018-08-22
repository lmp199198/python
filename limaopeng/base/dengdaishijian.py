# -*- coding:utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Firefox()
driver.get('https://www.baidu.com')
'''
class By(object):
    """
    Set of supported locator strategies.
    """
    ID = "id"
    XPATH = "xpath"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"
    NAME = "name"
    TAG_NAME = "tag name"
    CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector"
'''

# 参数化元素定位：
# driver.find_element(By.ID,'KW')
# 另一种定位方式：
'''
driver.find_element('id','kw')       # id属性
driver.find_element('name','wd')     #  name属性
driver.find_element('class name','s_ipt') # class属性
driver.find_element('tag name','新闻')    # text文本
driver.find_element('link text','新闻')   # 超链接
driver.find_element('partial link text','新')   # 截取一部分link链接
driver.find_element('xpath',".//*[@id='kw'")   # xpath属性
driver.find_element('css selector',"#kw")      # css属性
'''
# 等待时长10秒，默认0.5秒询问一次
# element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("someId"))
# 判断页面上不存在某个元素
# is_disappeared = WebDriverWait(driver, 30, 1, (ElementNotVisibleException))
# until_not(lambda x: x.find_element_by_id("someId").is_displayed())

element = WebDriverWait(driver,10,0.4).until(lambda x: x.find_element_by_id("kw"))
element.send_keys('我爱你')

def findElemnet(by,value):
    element = WebDriverWait(driver,10,0.4).until(lambda x: x.find_element(by,value))
    element.click()