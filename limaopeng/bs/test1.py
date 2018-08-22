# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup,NavigableString,Comment
import re

lmp = open('lmp.html')
soup=BeautifulSoup(lmp,'html.parser')  # soup对象
# soup=BeautifulSoup(lmp,'lxml')

# print(soup.prettify())
print(type(soup))
print(soup.title.string)

tag=soup.title   # tag对象

print(tag.name)

print(type(tag))
# 修改tag属性：
soup.p['class']='lmp'

# 修改string属性：
tag.string='Li Mao Peng'

print(type(tag.string))   # NavigableString对象
print(tag.string)


# NavigableString() 和 .new_tag() 和 .new_string


# 添加属性
# soup.p.append('LiangMeiPing')
# print(soup('p'))

# 添加文本
soup.p.append(' LiangMeiPing ')
new_string=NavigableString('  lmp ')
soup.p.append(new_string)
print(soup('p'))


# 添加注释：
new_comment=soup.new_string(' I LOVE YOU. ',Comment)
soup.p.append(new_comment)
print(soup('p'))

# 创建新的tag:
original_tag=soup.p
tag=soup.new_tag('c',href='https://www.baidu.com')
original_tag.append(tag)
tag.string='Link Text'
print(original_tag)




# comment=soup.find_all('a',limit=2)
# comment1=soup.find('c')
# print(type(comment))
# print('-------')
# print('comment:',comment)
# print(comment1)
#
# print(soup.p['class'])   # class
# print(soup.p.attrs)   # 返回的字典格式，获取所有的属性
#
# print(soup.b.string)
# print(type(soup.b.string))   # 注释对象
#
# print(soup.find_all(href="http://www.cnblogs.com/yoyoketang/tag/selenium/"))
#
# print(soup.a.get_text())
#
# print(soup.a['class'])
#
# print(soup.a.string)
#
# # 正则表达式查询：
# so=soup.find_all(string=re.compile('python'))
# print(so)
#
#
#
# print(soup.find_all('a'))

# for link in comment:
#     print(link.get('href'))

