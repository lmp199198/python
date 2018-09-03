# -*- coding:utf-8 -*-
a=1  # 作用全局
class Lmp():
    b=2   # 作用于类里面
    def __init__(self):
        self.c=3   # 作用整个类   带self的参数整个类都可以调用
        d=4        # 作用该方法

    def add(self):
        self.e=5   # 作用整个类
        f=2        # 作用该方法
        return self.e*f

    def sub(self):
        n=5
        m= self.c-self.b+a-self.e
        print(m)
        return m


if __name__ == '__main__':
    t=Lmp()
    t.add()
    t.sub()
