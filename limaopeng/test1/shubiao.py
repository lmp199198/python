# -*- coding:utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Firefox()
url='http://www.baidu.com'
driver.get(url)


# 鼠标事件：
# click ——单击鼠标左键
# context_click ——点击鼠标右键
# double_click ——双击鼠标左键
# click_and_hold ——点击鼠标左键，不松开
# drag_and_drop(source, target) ——拖拽到某个元素然后松开
# drag_and_drop_by_offset(source, xoffset, yoffset) ——拖拽到某个坐标然后松开

# move_to_element(to_element) ——鼠标移动到某个元素
# perform() ——执行链中的所有动作
# move_to_element_with_offset(to_element, xoffset, yoffset) ——移动到距某个元素（左上角坐标）多少距离的位置
# release(on_element=None) ——在某个元素位置松开鼠标左键
# move_by_offset(xoffset, yoffset) ——鼠标从当前位置移动到某个坐标


#键盘事件：
# key_down(value, element=None) ——按下某个键盘上的键
# key_up(value, element=None) ——松开某个键


# 发送事件 ：
# send_keys(*keys_to_send) ——发送某个键到当前焦点的元素
# send_keys_to_element(element, *keys_to_send) ——发送某个键到指定元素


ele=driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(ele).perform()  #调用driver函数，然后用move_to_element 鼠标移动到设置元素
#  最后用perform() ——执行链中的所有鼠标的操作

time.sleep(2)

driver.find_element_by_link_text('高级搜索').click()

time.sleep(3)
driver.quit()


