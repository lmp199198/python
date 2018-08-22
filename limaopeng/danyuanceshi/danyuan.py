# -*- coding:utf-8 -*-
# def add(a,b):
#     v= a+3*b
#     return v
# if __name__ == '__main__':
#     print(add(3,5))
import unittest

class IntegerArithmeticTestCase(unittest.TestCase):    #定义了一个类：IntegerArithmeticTestCase
# 继承了 unittest.TestCase，没有继承则默认object为基类，例如：
#   class IntegerArithmeticTestCase(object):或者class IntegerArithmeticTestCase:

    def testAdd(self):  # test method names begin with 'test'
        #所有的测试用例必须以test开头
            self.assertEqual((1 + 2), 3)
            self.assertEqual(0 + 1, 1)   #一条测试用例可以有多个断言

    def testMultiply(self):
            self.assertEqual((0 * 10), 0)
            self.assertEqual((5 * 8), 40)

if __name__ == '__main__':
    unittest.main()