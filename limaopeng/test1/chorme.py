# -*- coding:utf-8 -*-

from selenium import webdriver
import time

#打开游览器
driver=webdriver.Chrome()

#time.sleep(2)  #浏览器休眠3s
driver.get('http://wwww.baidu.com')

time.sleep(2)
driver.quit()


# lists = [1,5,3,6,5,6,65,23,45,1,2]
# count = len(lists)
# for i in range(count):
#     print(i,end=' ')
#     for j in range(i+1,count):
#         if lists[i] > lists[j]:
#             lists[i],lists[j] =lists[i],lists[j]
#
# if __name__ == '__main__':
#     lists = [1,5,3,6,5,6,65,23,45,1,2]
#     print('冒泡排序:')
#     bubble=sorted(lists,reverse=False)
#     print(bubble)
# for i in range(1,10):
#
#     for j in range(1,10):
#
#         if i>=j:
#             print('{0}*{1}={2}'.format(i,j,i*j),end=' ')
#     print()
#
# for i in range(10,1000):
#     sum=0 #各个位数的立方和
#     temp=i
#     while temp:
#         sum=sum+(temp%10)**3   #累加
#         temp//=10   #地板除
#     if sum==i:
#         print(i)