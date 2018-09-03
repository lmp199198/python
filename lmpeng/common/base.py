# -*- coding:utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchFrameException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoAlertPresentException

class Base():

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30
        self.poll = 0.5

    def findElement(self, loctor):
        '''
        args:
        loctor 传元祖，如（"id","xx"）
        '''
        element = WebDriverWait(self.driver, self.timeout, self.poll).until(lambda x: x.find_element(*loctor))
        return element

    def findElementNew(self, loctor):
        # 找到了返回element，没找到抛异常
        element = WebDriverWait(self.driver, self.timeout, self.poll).until(EC.presence_of_element_located(loctor))
        return element

    def findElementsNew(self, loctor):
        # 找到了返回list, 没找到抛异常
        elements = WebDriverWait(self.driver, self.timeout, self.poll).until(EC.presence_of_all_elements_located(loctor))
        return elements

    def findElements(self, loctor):
        '''
        args:
        loctor 传元祖，如（"id","xx"）
        '''
        elements = WebDriverWait(self.driver, self.timeout, self.poll).until(lambda x: x.find_elements(*loctor))
        return elements

    def clickElements(self, loctor, n=0):
        elems = self.findElements(loctor)  # list
        if len(elems) < 1:
            print("没找到元素！！！")
        elif n > len(elems):
            print("越界了！！！！！，最大值是：%s" % len(elems))
        else:
            elems[n].click()

    def sendKeys(self, loctor, text):
        ele = self.findElement(loctor)
        ele.send_keys(text)

    def click(self, loctor):
        ele = self.findElement(loctor)
        ele.click()

    def clear(self, loctor):
        ele = self.findElement(loctor)
        ele.clear()

    def moveToElement(self, loctor):
        '''鼠标悬停事件'''
        mos = self.findElement(loctor)
        ActionChains(self.driver).move_to_element(mos).perform()

    def is_text_in_element(self, locator, text):
        '''判断给定的text在这个元素的文本上
        要么返回true,要么返回false,不要让它抛异常了
        '''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.poll).until(EC.text_to_be_present_in_element(locator, text))
            return result
        except:
            return False


    def is_value_in_element(self, locator, value):
        '''判断给定的value在这个元素的文本上
        要么返回true,要么返回false,不要让它抛异常了

        三种情况为假：0，"", None  python是没有null的
        1.找不到元素返回False
        2.value为空返回False
        3.value不在元素的value值里返回False
        '''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.poll).until(EC.text_to_be_present_in_element_value(locator,value))
            return result
        except:
            return False


    def is_element_exsits(self, locator):
        '''查找元素的时候，存在返回element，不存在的时候Timeout异常了'''
        try:
            self.findElement(locator)
            return True
        except:
            return False

    def is_alert_exsit(self, timeout=5):
         '''语文老师教的：直到，，，，才，，，
        如有alert,返回的是alert对象，
        没有就返回False'''
         alert = WebDriverWait(self.driver, timeout, self.poll).until(EC.alert_is_present())
         return alert

    def js_scroll_bottom(self):
        '''滚动到底部'''
        js_heig = "window.scrollTo(0, document.body.scrollHeight)"
        self.driver.execute_script(js_heig)

    def js_focus(self, loctor):
        '''聚焦元素'''
        targe = self.findElement(loctor)
        self.driver.execute_script("arguments[0].scrollIntoView();", targe)

    def js_scroll_top(self):
        '''回到顶部'''
        js = "window.scrollTo(0, 0)"
        self.driver.execute_script(js)


# if __name__ == "__main__":
#     driver = webdriver.Firefox()
#     base = Base(driver)
#     driver.get("http://www.cnblogs.com/yoyoketang/p/")
#     import time
#     time.sleep(3)
#     # base.js_scroll_end()  # 滚动到底部
#     plun_loc = ("xpath", "//h3[text()='最新评论']")
#     base.js_focus(plun_loc)




    # loc1 = ("id", "kw")  # 定位百度输入框
    # base.sendKeys(loc1, "发送的内容")  # 关键字
    # loc2 = ("css selector", "#su")   # 定位搜索按钮
    # base.click(loc2)
    # news_loc = ("xpath", ".//*[@id='u1']/a[1]")  # 新闻
    # res = base.is_text_in_element(news_loc, "新闻")
    # print(res)
    # btn_loc = ("id", "su")
    # res1 = base.is_value_in_element(btn_loc, "百度一下")
    # print(res1)
