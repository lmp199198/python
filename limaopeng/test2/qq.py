# -*- coding:utf-8 -*-
from selenium import webdriver
import time
import os

driver=webdriver.Firefox()
driver.get('https://mail.qq.com/')

# 登陆：
driver.switch_to_frame('login_frame')
driver.find_element_by_css_selector('#switcher_plogin').click()
driver.find_element_by_css_selector('#u').send_keys('1123957070')
driver.find_element_by_css_selector('#p').send_keys('lmp199198')
# driver.switch_to_frame(0)
driver.find_element_by_css_selector('#login_button').click()

#切回主机面：
driver.switch_to.default_content()
driver.find_element_by_xpath(".//*[@id='composebtn']").click()   #写信
time.sleep(2)

#iframeid定位：
driver.switch_to_frame('mainFrame')

#收件人：
driver.find_element_by_xpath(".//*[@id='toAreaCtrl']/div[2]/input").send_keys('1123957070@qq.com')
time.sleep(2)

# 图片上传
driver.find_element_by_xpath(".//*[@id='AttachFrame']/span/input").click()
time.sleep(2)

# i='C:\\Users\lenovo\Desktop\12.jpg'
# os.system("C:\\Users\lenovo\Desktop\2.exe %s" % i )   # exe文件所在位置
# driver.switch_to.default_content()
#




