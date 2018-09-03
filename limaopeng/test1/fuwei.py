# -*- coding:utf-8 -*-
from selenium import webdriver
import time
driver=webdriver.Firefox()
driver.get('http://www.baidu.com')

time.sleep(1)

# a=driver.find_element_by_id('kw')   #单数定位
# b=driver.find_elements_by_id('kw')  #复数定位
# print(a)
# print(b)
# print(type(a))
# b[0].send_keys('尼玛')

#driver.find_element_by_class_name('s_ipt').send_keys('中文')     #class属性元素定位
#driver.find_element_by_id('su').click()
elements=driver.find_elements_by_class_name('mnav')

print(len(elements))    #定位到了几个

a = 3
if len(elements) > 2:
    elements[a].click()

time.sleep(3)

driver.quit()