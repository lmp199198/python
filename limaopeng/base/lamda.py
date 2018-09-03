# -*- coding:utf-8 -*-
def hanshu(a):
    return a+1
print(hanshu(8))   # 函数对象
a=hanshu(5)
print(a)

b=lambda x:x*5   # 匿名函数
print(b(5))

def add(a,b):
    return a/b
print(add(5,7))

c=lambda a,b:a+b
print(c(4,7))

