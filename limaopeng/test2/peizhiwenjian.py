# -*- coding:utf-8 -*-
from selenium import webdriver
import time

# driver=webdriver.Firefox()
# driver.implicitly_wait(30)

# 加载配置文件，可以免登陆：（重点）#


# 1、Firefox浏览器加载配置文件流程：
# 找到配置文件路径：帮助>故障排除信息>配置文件夹>显示文件夹
path=r'C:\Users\lenovo\AppData\Roaming\Mozilla\Firefox\Profiles\wxglh3q7.default'

proffile=webdriver.FirefoxProfile(path)

driver=webdriver.Firefox(proffile)
driver.get('https://www.cnblogs.com/lmp199198/')




# 2、chrome浏览器加载配置文件流程：

 #设置成用户自己的数据目录【这里只要到User Data，不是User Data\Default】
# path=r'--user-data-dir=C:\Users\lenovo\AppData\Local\Google\Chrome\User Data'
# option=webdriver.ChromeOptions()
# option.add_argument(path)

# driver=webdriver.Chrome(chrome_options=option)
# driver.get('https://www.baidu.com/')


time.sleep(5)
driver.quit()