# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# profileDir 路径对应直接电脑的配置路径
profileDir =r'C:\Users\lenovo\AppData\Roaming\Mozilla\Firefox\Profiles\wxglh3q7.default'
profile = webdriver.FirefoxProfile(profileDir)
driver = webdriver.Firefox(profile)
bolgurl = "http://www.cnblogs.com/"
yoyobolg = bolgurl + "yoyoketang"
driver.get(yoyobolg)

# 点击新随笔：
driver.find_element_by_id("blog_nav_newpost").click()
time.sleep(2)
edittile = "富文本111"
# editbody = "这里是发帖的正文"

driver.find_element_by_id("Editor_Edit_txbTitle").send_keys(edittile)
body = "这里是通过 js 发的正文内容"
# js 处理 iframe 问题(js 代码太长了，我分成两行了)
js = 'document.getElementById("Editor_Edit_EditorBody_ifr")' \
     '.contentWindow.document.body.innerHTML="%s"' % body
# 方法二：
# js1='document.getElementById("Editor_Edit_EditorBody_ifr")' \
#      '.contentWindow.document.getElementById("tinymce").body.innerHTML'
driver.execute_script(js)
time.sleep(3)
# 保存草稿
driver.find_element_by_id("Editor_Edit_lkbDraft").click()