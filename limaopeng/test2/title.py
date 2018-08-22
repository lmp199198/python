# -*- coding:utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Firefox()
driver.get('http://www.baidu.com/')
time.sleep(1)

# # t=driver.execute_script("$('.display_name')")
# driver.find_element_by_css_selector('.lb').click()
# driver.find_element_by_css_selector('#TANGRAM__PSP_10__userName')
# driver.find_element_by_css_selector('#TANGRAM__PSP_10__password')
# driver.find_element_by_css_selector('#TANGRAM__PSP_10__submit')

t= driver.find_element_by_link_text('地图')
handle=driver.current_window_handle
print(handle)         #获取当前的handle
print(t.text)         #获取当前的元素文本

print('1:',driver.title)   #获取当前页面标题
print('2:',driver.name)    #获取当前浏览器名称
print('3:',driver.current_url)    #获取当前浏览器的url
print('4:',driver.page_source)    #获取当前HTML的源码——（python爬虫应用）



url=t.get_attribute('href')   #获取当前的href地址
print(url)
if url=='http://map.baidu.com/':   #通过if语句判断预期结果
    print('测试通过')
else:
    print('失败')

id=t.get_attribute('class')   #获取当前的class返回值
print(id)

name=t.get_attribute('name')  #获取当前的name返回值
print(name)

tag=t.tag_name          #获取当前的tag返回值
print(tag)

# 注意：
#  chass='',name='',id='',都是通过.get_attribute() 去获取元素返回值
#  标签的返回值则是.tag_name


# 判断元素是显示还是隐藏（返回布尔值）
# ele=driver.find_element_by_link_text('设置')
# ActionChains(driver).move_to_element(ele).perform()
# d=driver.find_element_by_css_selector('.setpref').is_displayed()  #.is_displayed()判断显示或者隐藏
# a=driver.find_element_by_css_selector('.setpref').is_enabled()
# print(d)
# print(a)


# 获取当前元素的size(尺寸大小)：
s=driver.find_element_by_id('kw').size
print(s)
print(s['height'],s['width'])   # 元素size的高度和宽度








time.sleep(3)
driver.quit()