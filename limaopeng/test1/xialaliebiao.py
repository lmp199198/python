# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
url='https://www.baidu.com/'
driver.get(url)

# 选项框，鼠标放在上面就可以看到选项 就可以点击：
ele=driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(ele).perform()

time.sleep(1)
driver.find_element_by_link_text('搜索设置').click()

time.sleep(1)

#1、下拉列表第一种方法：(直接使用xpath语法子元素)
# driver.find_element_by_xpath(".//*[@id='nr']/option[2]").click()
#
# # time.sleep(1)
# # a=driver.find_element_by_xpath(".//*[@id='nr']/option[3]")   or .//*[@id='nr']/option[@value='10']
# # ActionChains(driver).move_to_element(a).perform()
#
# time.sleep(1)
# driver.find_element_by_xpath(".//*[@id='nr']").click()

#2、下拉列表第二种方法：(索引index定位)
# select=driver.find_element_by_id('nr')
# Select(select).select_by_index(1)
#
# time.sleep(1)
# driver.find_element_by_xpath(".//*[@id='nr']").click()

#3、下拉列表第三种方法：(value定位)
# select=driver.find_element_by_id('nr')
# Select(select).select_by_value('50')
# driver.find_element_by_xpath(".//option[@value='50']")   .//*[@id='nr']/option[@value='10']
#
# time.sleep(1)
# driver.find_element_by_xpath(".//*[@id='nr']").click()

#4、下拉列表第四种方法：(选项定位)
select=driver.find_element_by_id('nr')
Select(select).select_by_visible_text('每页显示50条')

select.click()
# driver.find_element_by_xpath(".//*[@id='nr']").click()

#弹框

#1、确定按钮(accept)
driver.find_element_by_class_name('prefpanelgo').click()  #获取确定按钮元素
time.sleep(3)
driver.switch_to_alert().accept()   #获取弹框元素并用accept确定

# 取消按钮（dismiss）
time.sleep(3)
driver.quit()