# -*- coding:utf-8 -*-
from selenium import webdriver
import time
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox()
# url='https://www.baidu.com/'
driver.get('https://www.baidu.com/')

#隐式等待
driver.implicitly_wait(30)   #全局生效，只需设置一次
#缺点：需要等待整个页面元素加载完毕才会执行下一个命令，有时候页面想要的元素加载完毕了，
# 但是还有部分js元素为加载完毕就会一直转圈圈，而显示等待只需要所需元素加载完毕，满足条件就ok。


#如果页面一直转圈圈，js出错了。

print(driver.title)

driver.find_element_by_id('kw').send_keys('草泥马')
driver.find_element_by_id('kw').send_keys(Keys.ENTER)
time.sleep(1)
print(driver.title)
time.sleep(5)
driver.quit()