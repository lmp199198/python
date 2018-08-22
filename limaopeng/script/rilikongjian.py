# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Firefox()
driver.get("https://kyfw.12306.cn/otn/index/init")

driver.find_element_by_css_selector("#fromStationText").clear()
driver.find_element_by_css_selector("#fromStationText").send_keys('深圳')
driver.find_element_by_css_selector("#fromStationText").send_keys(Keys.ENTER)
time.sleep(1)
driver.find_element_by_css_selector("#toStationText").send_keys('长沙')
driver.find_element_by_css_selector("#toStationText").send_keys(Keys.ENTER)
time.sleep(1)
# 去掉元素属性并对value进行赋值：
js='document.getElementById("train_date").removeAttribute("readonly");' \
    'document.getElementById("train_date").value="2018-05-20"'
driver.execute_script(js)
time.sleep(1)

# 清空后文本输入值
# driver.find_element_by_id('train_date').clear()
# driver.find_element_by_id('train_date').send_keys('2018-05-17')

# 返程日：
time.sleep(1)
js1='document.getElementById("back_train_date").removeAttribute("readonly");' \
    'document.getElementById("back_train_date").value="2018-05-25"'
driver.execute_script(js1)
time.sleep(1)
driver.find_element_by_css_selector("#a_search_ticket").click()
time.sleep(2)
driver.quit()