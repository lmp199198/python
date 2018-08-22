# -*- coding:utf-8 -*-
from selenium import webdriver
import time

driver=webdriver.Firefox()
driver.get('http://www.cnblogs.com/yoyoketang/p/')

time.sleep(0.5)
 # 拉到底部：
# js1='document.documentElement.scrollTop=10000'  # 火狐浏览器用法
# js1="window.scrollTo(0,10000)"
# 通用方法;
js1="window.scrollTo(0,document.body.scrollHeight)"
driver.execute_script(js1)

# 这个写法也是可以的 ("var q=document.documentElement.scrollTop=0")

time.sleep(2)
# 回到顶端：
# js2='document.documentElement.scrollTop=0'   # 火狐浏览器用法
js2="window.scrollTo(0,0)"
driver.execute_script(js2)

time.sleep(2)
# 横向移动：
js3="window.scrollTo(1000,0)"
driver.execute_script(js3)

time.sleep(3)
driver.quit()


# 最底部 ：scrollTop=10000
#
# 最顶部 ：scrollTop=0

# 备注：以上方法，在chrome浏览器上并不管用，
# chrome上js代码为： document.body.scrollTop=0

# 两个浏览器都生效的函数：
# js_all="window.scrollTo(0,10000)"  # 0代表最左端，10000代表最底部
# driver.execute_script(js_all)

# 自动获取高度：
# js_heit="window.scrollTo(0,document.body.scrollHeight)"
# driver.execute_script(js_heit)