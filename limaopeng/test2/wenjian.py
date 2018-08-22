# -*- coding:utf-8 -*-
from selenium import webdriver
import time
import os

# 1、Firefox浏览器加载配置文件流程：
# 找到配置文件路径：帮助>故障排除信息>配置文件夹>显示文件夹
path=r'C:\Users\lenovo\AppData\Roaming\Mozilla\Firefox\Profiles\wxglh3q7.default'

proffile=webdriver.FirefoxProfile(path)

driver=webdriver.Firefox(firefox_profile=proffile)
driver.get('https://www.cnblogs.com/lmp199198/')

# driver.implicitly_wait(30)
#文件上传：
driver.find_element_by_link_text('新随笔').click()
time.sleep(2)
driver.find_element_by_id('Editor_Edit_txbTitle').send_keys('qwe')
time.sleep(2)
driver.find_element_by_xpath(".//*[@id='Editor_Edit_EditorBody_uploadImage']/span[1]/img").click()
time.sleep(2)

# iframe索引定位：
# driver.switch_to_frame(1)
# driver.find_element_by_xpath(".//*[@id='jquery-wrapped-fine-uploader']/div/div/input").send_keys(r'C:\Users\lenovo\Desktop\123.png')

# 标签定位：
iframe=driver.find_elements_by_tag_name('iframe')[1]
driver.switch_to_frame(iframe)

# 点开上传文件按钮：
driver.find_element_by_xpath(".//*[@id='jquery-wrapped-fine-uploader']/div/div/input").click()
#send_keys(r'C:\Users\lenovo\Desktop\12.png')

# 执行autoit上传文件
os.system(r'C:\Users\lenovo\Desktop\123.exe')   # exe文件所在位置

# # 切回主界面：
# driver.switch_to.default_content()

# time.sleep(3)
# # 取消上传：
# driver.find_element_by_css_selector('#Editor_Edit_lkbCancel').click()
# #
# #
# time.sleep(2)
# driver.switch_to_alert().accept()