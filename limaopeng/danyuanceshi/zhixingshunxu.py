# -*- coding:utf-8 -*-
import unittest
from limaopeng.danyuanceshi.login_out import *   #导入函数：

class Test(unittest.TestCase):

    # def login(self):    #调用login方法，每一条用例都会调用该方法
    #     print('登陆')
    #
    # def logout(self):   #调用logout方法，每一条用例都会调用该方法
    #     print('退出')

    #前置操作条件：（每个用例都会执行一次）
    @classmethod
    def setUp(self):
        print('前置')
        self.login()     #不是Test(unittest.TestCase):里面的内容，不需要self
        self.logout()    #不是Test(unittest.TestCase):里面的内容，不需要self

    #后置操作条件：（每个用例都会执行一次）
    @classmethod
    def tearDown(self):
        print('后置')

    def test_b(self):
        print('1111')

    def test_c(self):
        print('2222')

if __name__ == '__main__':
    unittest.main()
  #  用例执行顺序是按ascii码顺序