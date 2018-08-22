# -*- coding:utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
class Base():
    def __init__(self,driver):
        self.driver=driver
        self.driver.get('https://www.baidu.com')
        self.timeout=30
        self.poll=0.5

    '''第一种查询方法'''
    def findElement1(self,locator):
        # *arg可变参数
        element1 = WebDriverWait(self.driver,self.timeout,self.poll).until(lambda x: x.find_element(*locator))
        return element1

    '''第二种查询方法(单数)'''
    # def findElement2(self,locator):
    #     # *arg可变参数
    #     element2 = WebDriverWait(self.driver,self.timeout,self.poll).until(EC.presence_of_element_located(locator))
    #     return element2
    # 找到元素返回element2，没找到抛异常
    '''第二种查询方法(复数)'''
    # def findElement(self,locator):
    #     # *arg可变参数
    #     elements = WebDriverWait(self.driver,self.timeout,self.poll).until(EC.presence_of_all_elements_located(locator))
    #     return elements

    # sendkeys发送方法：
    def sendKeys(self,locator,text='我爱你'):
        ele1=self.findElement1(locator)
        ele1.send_keys(text)


    def clear(self,locator):
        ele3=self.findElement1(locator)
        ele3.clear()
    # click点击方法：
    def click(self,locator):
        ele2=self.findElement1(locator)
        ele2.click()


if __name__ == '__main__':
    driver=webdriver.Firefox()
    base=Base(driver)
# 输入搜索内容：
    locator1=('id','kw')
    base.sendKeys(locator1)# .send_keys('我爱你')
    base.clear(locator1)
    # element1=findElement(driver,'id','kw').send_keys('我爱你')
    # element1.send_keys('我爱你')
    # 点击查询按钮：
    locator2=('id','su')
    base.click(locator2)

    # element2=findElement(driver,'id','su').click()
    # driver.quit()