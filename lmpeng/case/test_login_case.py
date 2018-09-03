# -*- coding:utf-8 -*-
from page.login_page import LoginPage
from selenium import webdriver
import unittest
import ddt
from common.readexcel import ExcelUtil

filepath = "testdata.xlsx"


data = ExcelUtil(filepath)
testdata = data.dict_data()  # 读取数据为list
print(testdata)

# # 参数和代码分离
# testdata = [
#         {"username": "admin", "psw": "123456", "result": "admin"},
#         {"username": "admin1", "psw": "123456", "result": ""},
#         {"username": "admin2", "psw": "111111",  "result": "admin2"},
#         {"username": "admin3", "psw": "111111",  "result": "admin3"}]

@ddt.ddt   # 测试类前面加上@ddt.ddt
class LoginCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.loginpage = LoginPage(cls.driver)

    def login_case(self, username, psw):
        # 登录
        self.loginpage.login(username, psw)
        # 判断是否有弹窗
        self.loginpage.is_alert_exsit()
        # 获取结果
        result = self.loginpage.get_login_result()
        return result

    @ddt.data(*testdata)    #测试用例前面：@ddt.ddt，并参数化*
    def test_login_01(self, canshu):
        res = self.login_case(canshu["username"], canshu["psw"])
        self.assertTrue(canshu["result"] == res)

    def tearDown(self):
        self.driver.delete_all_cookies() # 清空cookies
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()

