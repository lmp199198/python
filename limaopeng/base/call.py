# -*- coding:utf-8 -*-

# 1、title_is 判断当前页面的标题是否等于预期
# 2、title_contains 判断当前页面标题是否包含预期字符串
# 3、presence_of_element_located 判断元素是否被加在DOM树里，并不代表该元素一定可见
# 4、visbility_of_element_located 判断元素是否可见（可见代表元素非隐藏，并且元素的宽和高都不等于0）
# 5、visbility_of  与上一个方法作用相同，只是接收参数不同。上一个接收参数是定位，这一个参数是定位后的元素
# 6、presence_of_all_elements_located 判断是否至少有一个元素存在于DOM树中。只要有1个就返回True
# 7、text_to_be_present_in_element 判断某个元素中的text是否包含了预期的字符串
# 8、text_to_be_present_in_element_value 判断某个元素的value属性是否包含了预期的字符串
# 9、frame_to_be_available_and_switch_to_it 判断该表单是否可以切换进去，如果可以，返回True并且switch进去，否则返回False
# 10、invisbility_of_element_located 判断某个元素是否不存在于DOM树或不可见
# 11、element_to_be_clickable() 判断某个元素是否可见并且是可以点击的
# 12、staleness_of 等到一个元素从DOM树中移除,判断一个元素是否仍在DOM，可判断页面是否已经刷新
# 13、element_to_be_selected 判断某个元素是否被选中，一般用在下拉列表
# 14、element_selection_state_to_be 判断某个元素的选中状态是否符合预期,传入元素对象以及状态，相等返回True，否则返回False
# 15、element_located_selection_state_to_be 与上一个方法作用相同，只是上一个方法参数是定位后的元素，该方法接收的参数是定位
# 16、alert_is_present 判断页面上是否存在alert

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Firefox()
driver.get('https://www.baidu.com')

def findElement(driver,by,value):
    element = WebDriverWait(driver,10,0.4).until(lambda x: x.find_element(by,value)).click
    # element.click()
    return element

class find_element():
    def __init__(self,by,value):
        self.by=by
        self.value=value

    def __call__(self, driver):  # call就是变成函数
        element=WebDriverWait(driver,10,0.4).until(lambda x: x.find_element(self.by,self.value))
        return element

ele=find_element('id','kw')     # 实例
ele(driver).send_keys('我爱你') # 实例化后变成了函数


# import time
# time.sleep(1)
# t=expected_conditions.title_is('我爱你_百度搜索')(driver)   # 返回布尔值
# print(t)

# 显示等待与判断相结合：
# 1、title_is 判断当前页面的标题是否等于预期
ad=WebDriverWait(driver,30,0.5).until(expected_conditions.title_is('我爱你_百度搜索'))
print(ad)
# 2、title_contains 判断当前页面标题是否包含预期字符串
ad1=WebDriverWait(driver,30,0.5).until(expected_conditions.title_contains('我爱'))
print(ad1)
# 判断元素存在与否，只要在DOM里面就是存在的，即使是不可见：
# 3、presence_of_element_located 判断元素是否被加在DOM树里，并不代表该元素一定可见
loc=('id','su')
ad2=WebDriverWait(driver,30,0.5).until(expected_conditions.presence_of_element_located(loc))
print(ad2)
# 定位元素不存在时，会抛异常：TimeoutException
loc=('id','s')
ad3=WebDriverWait(driver,5,0.5).until(expected_conditions.presence_of_element_located(loc))
print(ad3)
