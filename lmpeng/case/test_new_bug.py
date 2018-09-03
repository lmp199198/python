# -*- coding:utf-8 -*-
import unittest
from page.login_page  import LoginPage
from page.editbug import NewBug
from selenium import webdriver
import time
class TestNewBug(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.loginpage = LoginPage(cls.driver)
        cls.newbug = NewBug(cls.driver)

    def add_bug(self, bugtitle, bugdeatil):
        '''新建BUG的流程'''
        # 1.登录
        self.loginpage.login()
        # 2.点测试，Bug, 提交bug
        self.newbug.click_test_tab()
        self.newbug.click_bug()
        self.newbug.click_add_bug()
        # 3.编辑BUG
        self.newbug.input_title(bugtitle)
        self.newbug.input_bug_detail(bugdeatil)
        self.newbug.add_truk()
        self.newbug.click_save()
        # 4.获取点完之后的实际结果
        result = self.newbug.get_bug_title()
        print("获取实际结果：%s" % result)
        return result

    def test_add_bug_01(self):
        '''测试提交BUG成功流程'''
        nowtime = time.strftime("%Y_%m_%d_%H_%M_%S")
        bugtitle = "新建一个bug"+nowtime
        bugdetail = "bug详情"
        re = self.add_bug(bugtitle, bugdetail)
        # 5.期望结果
        ex = "[未确认] "+bugtitle
        # 断言：实际结果和期望结果对比
        self.assertEqual(re, ex, msg="如果断言失败，可以自己写一句话")
        self.assertTrue(re == ex)

    def test_add_bug_02(self):
        '''测试提交bug,影响版本为空流程'''
        # 1.登录
        self.loginpage.login()
        # 2.点测试，Bug, 提交bug
        self.newbug.click_test_tab()
        self.newbug.click_bug()
        self.newbug.click_add_bug()
        # 3.编辑BUG
        self.newbug.input_title("标题")
        self.newbug.input_bug_detail("正文")
        self.newbug.click_save()
        # 没勾选版本
        result = self.newbug.get_truck_text()
        print(result)
        self.assertEqual(result, "『影响版本』不能为空。")

    def test_add_bug_03(self):
        '''测试提交bug,影响版本为空流程'''
        # 1.登录
        self.loginpage.login()
        # 2.点测试，Bug, 提交bug
        self.newbug.click_test_tab()
        self.newbug.click_bug()
        self.newbug.click_add_bug()
        # 3.编辑BUG
        self.newbug.input_title("标题")
        self.newbug.input_bug_detail("正文")
        self.newbug.click_save()
        # 没勾选版本
        re = self.newbug.is_truck_text_in("『影响版本』不能为空")
        print(re)
        self.assertTrue(re)

        # result = self.newbug.get_truck_text()
        # print(result)
        # self.assertEqual(result, "『影响版本』不能为空。")


    def tearDown(self):
        # 每次执行完之后，连数据库，执行SQL，删除这条
        pass

if __name__ == "__main__":
    unittest.main()

