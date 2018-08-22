# -*- coding:utf-8 -*-
from selenium import webdriver
import time
driver=webdriver.Firefox()
driver.get("file:///C:/Users/lenovo/Desktop/div.html")
time.sleep(2)
# 纵向底部
# 获取id是单个元素，id是页面唯一的元素
js1="document.getElementById('yoyoketang').scrollTop=10000"
# 获取的class属性有多个，取list的第一个对象
# js2="document.getElementsByClassName('scroll')[0].scrollTop=10000"
driver.execute_script(js1)
time.sleep(2)

# 纵向顶部
js3="document.getElementById('yoyoketang').scrollTop=0"
# js2="document.getElementsByClassName('scroll')[0].scrollTop=0"
driver.execute_script(js3)
time.sleep(2)

# 横向左移
js4="document.getElementById('yoyoketang').scrollLeft=10000"
# js2="document.getElementsByClassName('scroll')[0].scrollLeft=0"
driver.execute_script(js4)
time.sleep(2)

# 横向右移
js5="document.getElementById('yoyoketang').scrollLeft=0"
# js2="document.getElementsByClassName('scroll')[0].scrollLeft=10000"
driver.execute_script(js5)

time.sleep(3)
driver.quit()

# scrollTop   上下移动
# scrollLeft  左右移动