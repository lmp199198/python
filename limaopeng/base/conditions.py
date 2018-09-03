# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver=webdriver.Firefox()
driver.get('https://www.cnblogs.com/yoyoketang/p/')

loc1=('css selector','.PostListTitle')
text='我的随笔'
l1=WebDriverWait(driver,4,0.5).until(EC.text_to_be_present_in_element(loc1,text))

