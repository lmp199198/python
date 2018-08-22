# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
url ='https://tieba.baidu.com/index.html'
driver=webdriver.Firefox()
driver.get(url)

#By元素 定位
# driver.find_element(By.CLASS_NAME,'j_search_input').send_keys('爱吧')
# driver.find_element(By.CLASS_NAME,'search_btn_enter_ba').click()

# driver.find_element(By.ID,'wd1').send_keys('爱吧')
# driver.find_element(By.CLASS_NAME,'search_btn').click()

# driver.find_element(By.ID,'wd1').send_keys('爱吧')
# driver.find_element(By.ID,'wd1').submit()   #submit 模拟回车键

time.sleep(3)
driver.quit()










































































































