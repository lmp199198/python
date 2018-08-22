# -*- coding:utf-8 -*-
# from selenium import webdriver
# driver=webdriver.Firefox()
# driver.get('')
  #层级关系：
#  相对路径：  driver.find_element_by_xpath("//form[@id='form']/span/input")

#  索引：driver.find_element_by_xpath("//*[@id='nr']/option[3]")
  # 单属性
#driver.find_element_by_xpath("//input[@autocomplete='off']").send_keys("hao")

  #组合属性
#driver.find_elements_by_xpath("//input[@type='text' and @name='wd']")

  # text属性：
#  语法：.//*[text()='文本内容']
#  注意：除了这个文本属性匹配是.//*[text()=‘文本’]这种格式(无@)
#  其它的属性，如id,name,class等都是.//*[@id=‘xxx’]  .//*[@name=‘xxx’]这种格式，必须加@，文本属性除外。
#  '/..'——斜杠两个点代表父级目录，一级一级向上查询。

#  模糊匹配：
# contains 匹配text：
# driver.find_element_by_xpath("//a[contains(text(),'糯')]").click()  指定标签
# 或者
# driver.find_element_by_xpath("//*[contains(text(),'糯')]").click()  匹配所有标签

# contains 匹配某个具体属性：
# xpath("//input[contains(@id,'xx')]") or ("//*[contains(@id,'xx')]")
# driver.find_element_by_xpath("//input[contains(@class,'s_ip')]").send_keys("hao")

# contains 匹配以xxx开头的：
# xpath("//input[starts-with(@id,'xx') ]")
# driver.find_element_by_xpath("//input[starts-with(@class,'s_ip')]").send_keys("hao")



# 注意：
# 1.官方说法，css定位比xpath更快
# 2.Xpath更容易理解
# 3.css语法更简洁









