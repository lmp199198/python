# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
from selenium import webdriver
import time
import os
# 1、Firefox浏览器加载配置文件流程：
# 找到配置文件路径：帮助>故障排除信息>配置文件夹>显示文件夹
path=r'C:\Users\lenovo\AppData\Roaming\Mozilla\Firefox\Profiles\wxglh3q7.default'
proffile=webdriver.FirefoxProfile(path)
driver=webdriver.Firefox(firefox_profile=proffile)
# driver=webdriver.Firefox()
driver.get('https://mail.qq.com/')

# driver.implicitly_wait(30)
# 发送邮件：
# 登陆：
driver.switch_to_frame('login_frame')
driver.find_element_by_xpath(".//*[@id='img_out_1123957070']").click()
time.sleep(5)
# #切回主机面：
driver.switch_to.default_content()
driver.find_element_by_xpath(".//*[@id='composebtn']").click()   #写信
time.sleep(3)

#iframeid定位：
driver.switch_to_frame('mainFrame')
#收件人：
driver.find_element_by_xpath(".//*[@id='toAreaCtrl']/div[2]/input").send_keys('1123957070@qq.com')
driver.find_element_by_id("subject").send_keys("主题")
time.sleep(1)
driver.switch_to.default_content()
# 1、单一文件上传
# 执行autoit上传文件
# os.system(r'C:\Users\lenovo\Desktop\123.exe')   # exe文件所在位置
# 2、批量发送文件：
list=[r'C:\Users\lenovo\Desktop\1.jpg',r'C:\Users\lenovo\Desktop\12.jpg',
       r'C:\Users\lenovo\Desktop\3.jpg',r'C:\Users\lenovo\Desktop\4.jpg']
for i in list:
    js = "document.getElementById('mainFrame').contentWindow.document.getElementsByName('UploadFile')[0].click()"
    driver.execute_script(js)
    time.sleep(2)
    # i=r'C:\Users\lenovo\Desktop\12.jpg'  # 单一发送文件：
    os.system(r"C:\Users\lenovo\Desktop\2.exe %s" % i )   # exe文件所在位置
# C:\Users\lenovo\Desktop\2.exe C:\Users\lenovo\Desktop\12.jpg
# 发送按钮
driver.switch_to_frame('mainFrame')
driver.find_element_by_xpath(".//*[@id='toolbar']/div/a[1]").click()
driver.switch_to.default_content()

# # 关闭按钮
# driver.find_element_by_xpath(".//*[@id='toolbar']/div/a[4]").click()
#
# time.sleep(2)
#
# #弹框提示：
# driver.switch_to.default_content()
# driver.find_element_by_xpath(".//*[@id='composeExitAlert_QMDialog_btn_delete_save']").click()


# 标签定位：
# iframe=driver.find_elements_by_tag_name('iframe')[1]
# driver.switch_to_frame(iframe)

# 点开上传文件按钮：
# driver.find_element_by_xpath(".//*[@id='jquery-wrapped-fine-uploader']/div/div/input").click()

#send_keys(r'C:\Users\lenovo\Desktop\12.png')

# 执行autoit上传文件
# os.system(r'C:\Users\lenovo\Desktop\123.exe')   # exe文件所在位置
#
# time.sleep(5)
# driver.quit()