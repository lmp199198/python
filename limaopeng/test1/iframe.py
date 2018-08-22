# -*- coding:utf-8 -*-
from selenium import webdriver
import time
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox()
url='https://mail.126.com/'
driver.get(url)

#time.sleep(1)
# driver.find_element_by_partial_link_text('国外').click()

# 切换iframe：
# driver.switch_to_frame('x-URS-iframe')

# 如何判断是否在iframe上——点击firepath：

#关于iframe的四种定位方法
# 1、有id，并且唯一，直接写id；
#driver.switch_to_frame('x-URS-iframe')

# 2、有name，并且唯一，直接写name；
# driver.switch_to_frame('xxxx')

# 3、既无id，也无name，先定位iframe元素,再切换到swich：
# iframe=driver.find_elements_by_tag_name('iframe')[0]   #通过复数标签属性定位，通过list获取索引位置
# driver.switch_to_frame(iframe)              #再切换到swich
# driver.find_element_by_name('email').send_keys('123456')

#xpath属性:
# iframe=driver.find_element_by_xpath(".//*[@id='x-URS-iframe']")   #通过xpath属性定位
# driver.switch_to_frame(iframe)              #再切换到switch

#css属性：
# iframe=driver.find_element_by_css_selector('#x-URS-iframe')   #通过css属性定位
# driver.switch_to_frame(iframe)

# 4、通过索引index定位：（索引最简单）
# driver.switch_to_frame(2)
# driver.find_element_by_class_name('j-inputtext').send_keys('123456')


#退出iframe,回到主界面:
# driver.switch_to_default_content()

#退回到父级页面：
# driver.switch_to.parent_frame()


#先进入F1，再回到主界面，再进入到F2：
# driver.switch_to_frame('F1')
# driver.switch_to_default_content()
# driver.switch_to_frame('F2')

#嵌套,F2在F1中，从父级F1进入到子级F2：
# driver.switch_to_frame('F1')
# driver.switch_to_frame('F2')

#


time.sleep(3)
driver.quit()