# -*- coding:utf-8 -*-
from selenium import webdriver
import time

driver=webdriver.Firefox()
driver.get('http://www.cnblogs.com/yoyoketang/')
time.sleep(0.5)
 # 定位到目标元素：
ele=driver.find_element_by_xpath("//h3[text()='最新评论']")
# 执行js并滚动到元素出现的位置:
driver.execute_script("arguments[0].scrollIntoView();", ele)

# 封装js

# 无所谓封装：
def js_execute(self,js):
   '''执行js'''
   self.driver.execute_script(js)

def js_scroll_bottom(self):
    '''滚动到底部'''
    js_heig = "window.scrollTo(0, document.body.scrollHeight)"
    self.driver.execute_script(js_heig)

# 重点封装聚焦元素(focus):
def js_focus(self, loctor):
    '''聚焦元素'''
    targe = self.findElement(loctor)
    self.driver.execute_script("arguments[0].scrollIntoView();", targe)

def js_scroll_top(self):
    '''回到顶部'''
    js = "window.scrollTo(0, 0)"
    self.driver.execute_script(js)
