# -*- coding:utf-8 -*-
from selenium import webdriver
import time
driver=webdriver.Firefox()
driver.get('https://tieba.baidu.com/index.html')

time.sleep(1)

# driver.find_element_by_id('kw').send_keys('python')
#
# driver.find_element_by_id('su').click()
# time.sleep(3)
# driver.find_element_by_id('kw').clear()  #清空输入的内容
# time.sleep(3)
# driver.find_element_by_id('kw').send_keys('王尼玛')
# driver.find_element_by_id('su').click()


#class属性有空格，取其中一个

driver.find_element_by_class_name('j_search_input').send_keys('爱吧')
driver.find_element_by_class_name('search_btn_enter_ba').click()

#search_ipt search_inp_border j_search_input tb_header_search_input
time.sleep(3)
driver.quit()