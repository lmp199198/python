# -*- coding:utf-8 -*-
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get('file:///D:/APP/QQ/1123957070/FileRecv/alert.html')
time.sleep(1)

driver.find_element_by_id('prompt').click()
# time.sleep(2)
driver.switch_to_alert().send_keys('草泥马')

time.sleep(2)
driver.switch_to_alert().accept()     #确定按钮
# a=driver.switch_to.alert
# a.accept()
# driver.switch_to_alert().dismiss()  #取消按钮
time.sleep(2)
driver.quit()


# driver.switch_to_alert() 与 a=driver.switch_to.alert.相等
# a=driver.switch_to.alert.  #需接一个参数，因为灰显
# driver.switch_to_alert().accept()  ==  a=driver.switch_to.alert》》》a.accept()
#
#