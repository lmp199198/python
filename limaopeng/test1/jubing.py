# -*- coding:utf-8 -*-
from selenium import webdriver
import time
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys


# 显示当前句柄 current_window_handle
# driver.current_window_handle

# 列出所有句柄 window_handle:
# driver.window_handle

# 切换句柄
# switch_to_window()   括号里面接具体handle




driver=webdriver.Firefox()
url='https://sz.ganji.com/'
driver.get(url)

handle=driver.current_window_handle  # 获取当前的handle
print(handle)
print(type(handle))
print(driver.title)

driver.find_elements_by_class_name('dt-t')[3].click()

handle1=driver.current_window_handle  # 获取点击后的handle
print(handle1)
print(type(handle1))

handles=driver.window_handles  # 获取所有的handle
print(handles)
print(type(handles))


driver.switch_to.window(handles[-1])     #切换过去了
time.sleep(3)
print(driver.title)


#新页面元素操作完了，关掉了，回到主页面
time.sleep(3)
#driver.close()   #关闭当前页面
driver.switch_to_window(handles[0])
print(driver.title)


#复数定位的时候，如果页面没有刷新，可以直接用一次定位复数的list

#如果页面没有刷新，需要再一次定位(刷新后的元素变了)


time.sleep(3)
driver.quit()




































