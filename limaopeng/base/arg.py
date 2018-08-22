# -*- coding:utf-8 -*-
def add(*args):
    for i in args:
        print(i)
    return ''
b=[1,2,3,58,6,8]

if __name__ == '__main__':
    print(add(*b))

def add(*args):
    s=sum(args)
    return s
a=range(11)
print(add(*a))