# -*- coding:utf-8 -*-(完全数)
for i in range(1,1000):
    s=0
    for k in range(1,i):
        if i%k==0:
            s=s+k
    if i==s:
        print(i)

import os

# 获取当前脚本的路径：

print(__file__)    # 左斜杠

# 右斜杠
real=os.path.realpath(__file__)
print(real)    # 当前脚本的真实路径

# 获取当前脚本的文件夹路径：

dirname=os.path.dirname(real)
print(dirname)   # 获取当前脚本的文件夹路径：
qwe=os.path.dirname(dirname)   # 获取当前文件夹的路径：
print(qwe)
con=os.path.join(qwe,'danyuanceshi')    # 拼接路径
print(con)
qwe1=os.path.join(dirname,'qwe.py')
print(qwe1)