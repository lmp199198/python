# -*- coding:utf-8 -*-
from selenium import webdriver
import time
driver=webdriver.Firefox()
url='http://www.baidu.com'
driver.get(url)

time.sleep(1)

#name定位
#a=driver.find_element_by_tag_name('body').text   #tag标签-获取元素文本，并打印text文件

#link(超链接定位)
#driver.find_element_by_link_text('贴吧').click()  #link(href页面链接)
#driver.find_element_by_partial_link_text('新闻').click()         #截取一部分link链接

#class定位
#driver.find_element_by_class_name('s_ipt').send_keys('中文')     #class属性元素定位

#class属性有空格，取其中一个
#driver.find_element_by_class_name('j_search_input').send_keys('爱吧')
#driver.find_element_by_class_name('search_btn_enter_ba').click()

#Xpath定位
# 通过*匹配任何标签：.//*[@id='kw']
#driver.find_element_by_xpath(".//*[@id='kw']").send_keys('Weinstein')
# 通过指定的tag标签：
#driver.find_element_by_xpath(".//input[class='s_ipt']")

# 通过text文本定位，切记没有@符号
#.//*[text()='文本内容']

#.//*[id/name/class=''或者href="http://map.baidu.com/"]

# 层级关系
#driver.find_element_by_xpath("//form[@id='form']/span/input")


#driver.find_element_by_xpath(".//*[@id='su']").click()

#css定位
driver.find_element_by_css_selector('#kw').send_keys('你好')
driver.find_element_by_css_selector('#su').click()
time.sleep(5)
driver.quit()
