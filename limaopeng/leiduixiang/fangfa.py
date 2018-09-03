# -*- coding:utf-8 -*-
class Test():
    def __init__(self):
        self.a=3
        self.b=4

    def add(self):
        # 实例方法
        return self.a*self.b

    @classmethod
    def acc(cls):
        '''类方法，隐含参数cls'''
        print('类方法')

    @staticmethod
    def abb():     # 没有@staticmethod则为静态函数
        '''静态方法，不带self参数，和静态函数差不多'''
        print('静态函数')



'''
区别:
类方法和静态方法都可以被类和类实例调用，类实例方法仅可以被类实例调用,
类方法的隐含调用参数是类（cls），而类实例方法的隐含调用参数是类的实例(self)，
静态方法没有隐含调用参数.
'''


