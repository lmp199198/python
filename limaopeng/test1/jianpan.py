# -*- coding:utf-8 -*-
from selenium import webdriver
import time
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox()
url='http://www.baidu.com'
driver.get(url)

driver.find_element_by_id('kw').send_keys('我心永恒')
#driver.find_element_by_id('kw').send_keys(Keys.ENTER)  #回车键
# driver.find_element(By.ID,'wd1').submit()   #submit 模拟回车键进行提交
# driver.find_element_by_id('kw').submit()    #submit 模拟回车键进行提交
driver.find_element_by_id('kw').click()       #点击按钮，进行提交
# driver.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)  #删除键。一行代表删除一个字
# driver.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)

time.sleep(1)
# driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')   #全选
# time.sleep(2)
# driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')   #剪切
# time.sleep(2)
# driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'v')   #粘贴


time.sleep(3)
driver.quit()