# -*- coding:utf-8 -*-
from selenium import webdriver
import time

# 1、Firefox浏览器加载配置文件流程：
# 找到配置文件路径：帮助>故障排除信息>配置文件夹>显示文件夹
path=r'C:\Users\lenovo\AppData\Roaming\Mozilla\Firefox\Profiles\wxglh3q7.default'

proffile=webdriver.FirefoxProfile(path)

driver=webdriver.Firefox(firefox_profile=proffile)
driver.get('https://www.cnblogs.com/lmp199198/')

driver.implicitly_wait(30)
# 点击新随笔：
driver.find_element_by_link_text('新随笔').click()
driver.find_element_by_link_text('文件').click()
driver.find_element_by_id('AddFiles_myFile').send_keys(r'C:\Users\lenovo\Desktop\123.xml')
driver.find_element_by_id('AddFiles_lbkAddFile').click()



# time.sleep(5)
# driver.quit()