# -*- coding:utf-8 -*-
from leiduixiang.test3 import Father,Mother
class People():

    def __init__(self,sex,live):   #形式参数
        # 下面设置了参数化，实例化参数时需要带上参数，否则报错
        self.sex=sex    #参数化
        self.live=live

    def zhaoduixiaong(self,age):  # 定义函数加了参数，在调用方法时需要加上该参数，否则报错
        print('找对象的要求1:%s' % self.sex)
        print('找对象的要求2:%s' % self.live)
        print('找对象的要求3:%s' % age)   # 不能加self，会报错

class Son(People,Father,Mother):    # 继承
    pass

if __name__ == '__main__':
    # a=People('boy','die')    # 默认init里面的参数，
    # a.zhaoduixiaong('23岁')  #
    b=Son('boy','die')
    b.zhaoduixiaong(18)
    b.chezi()
