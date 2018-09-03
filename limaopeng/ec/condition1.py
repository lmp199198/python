# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import unittest

# dr = webdriver.PhantomJS('phantomjs')
driver = webdriver.Firefox()   # dr = webdriver.Chrome()
url = 'http://www.baidu.com'
search_text_field_id = 'kw'
driver.get(url)

class ECExample(unittest.TestCase):

  def test_title_is(self):
    ''' 判断title是否符合预期 '''
    title_is_baidu = EC.title_is(u'百度一下，你就知道')
    self.assertTrue(title_is_baidu(driver))

  def test_titile_contains(self):
    ''' 判断title是否包含预期字符 '''
    title_should_contains_baidu = EC.title_contains(u'百度')
    self.assertTrue(title_should_contains_baidu(driver))

  def test_presence_of_element_located(self):
    ''' 判断element是否出现在DOM树 '''
    locator = (By.ID, search_text_field_id)
    search_text_field_should_present = EC.visibility_of_element_located(locator)

    ''' 动态等待10s，如果10s内element加载完成则继续执行下面的代码，否则抛出异常 '''
    WebDriverWait(driver, 10,0.5).until(EC.presence_of_element_located(locator))
    WebDriverWait(driver, 10,0.5).until(EC.visibility_of_element_located(locator))

    self.assertTrue(search_text_field_should_present(driver))

  def test_visibility_of(self):
    search_text_field = driver.find_element_by_id(search_text_field_id)
    search_text_field_should_visible = EC.visibility_of(search_text_field)
    self.assertTrue(search_text_field_should_visible('yes'))

  def test_text_to_be_present_in_element(self):
    text_should_present = EC.text_to_be_present_in_element((By.NAME, 'tj_trhao123'), 'hao123')
    self.assertTrue(text_should_present(driver))


  @classmethod
  def tearDownClass(cls):
    print('after all test')
    driver.quit()
    print('quit dr')

if __name__ == '__main__':
  unittest.main()