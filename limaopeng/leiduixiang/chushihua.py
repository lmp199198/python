# -*- coding:utf-8 -*-

class Son():

    def __init__(self):

        # 初始化，
        # 实例化的时候默认执行init里面的内容：
        self.jinyaoshi='金钥匙'
        print(self.jinyaoshi)

    def zhaolaopo(self):
        print('找老婆')
        print(self.jinyaoshi)

if __name__ == '__main__':
    a=Son()   #实例化的时候会带着初始化内容里面的东西和属性
    a.zhaolaopo()