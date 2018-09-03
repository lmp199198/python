# -*- coding:utf-8 -*-
from selenium import webdriver
import time

driver=webdriver.Firefox()
driver.get("https://passport.cnblogs.com/user/signin")

username="$('#input1').val('lmp199198')"
driver.execute_script(username)

psw="$('#input2').val('ppp199198@')"
driver.execute_script(psw)

time.sleep(3)
# 清空文本
clear="$('#input1').val('')"
driver.execute_script(clear)
time.sleep(2)
clear1="$('#input2').val('')"
driver.execute_script(clear1)

# button = "$('#signin').click()"
# driver.execute_script(button)



