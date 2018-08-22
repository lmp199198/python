# -*- coding:utf-8 -*-
#  1.通过id定位：
# driver.find_element_by_css_selector("#kw").send_keys("hao")   id以#开头；


#  2.通过class定位：
# driver.find_element_by_css_selector(".s_ipt").send_keys("hao")  class以.开头

#  3.通过标签：
# driver.find_element_by_css_selector("input").send_keys("hao")   tag直接写

#  4.其它属性——name，value：
# driver.find_element_by_css_selector("[name='kw']")      #  [name='kw'],[autocomplete='off']  #
# driver.find_element_by_css_selector("[autocomplete='off']")

#  注意：
# 除了id、class、tag，其他都是[xxx='xxx'],例如：[name='wd']


# 1、父子关系（用>表示）
# driver.find_element_by_css_selector("span>input")

# 2、组合定位
# driver.find_element_by_css_selector("form.fm>span>input.s_ipt")
# driver.find_element_by_css_selector("form#form>span>input#kw")

# 定位到第几组，就取第几个：
# :nth-child()——.mnav:nth-child(2)


# 注意：
# 1.官方说法，css定位比xpath更快
# 2.Xpath更容易理解
# 3.css语法更简洁

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
driver.find_element_by_css_selector("select>option[value='50']").click()
time.sleep(2)
driver.find_element_by_css_selector('#nr').click()
time.sleep(3)
driver.quit()
