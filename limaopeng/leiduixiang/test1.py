# -*- coding:utf-8 -*-
class Count():
    def __init__(self):
        print('初始化')
    def add(self,a=2,b=3):   #实例方法
        return a+b

    def sub(self,a,b):   #self为类的本身实例参数
        return a-b

    def mul(self,a=1,b=3):
        return self.add(a,b)*self.sub(a,b)

    def __add(self):    # 私有方法
        print('nanren')



if __name__ == '__main__':
    #这里的 a 是外部实例参数，self是内部实例参数
    a=Count()   #实例化  #创建实例   可以创建多个实例
    b=Count()   #实例二  #实例化也是创建实例
    print(a.sub(2,3))   #调用对象里的方法
    print(a.add(2,3))
    print(a.mul())
    print(b.mul())
    # print(a._Count__add())



