# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import urllib3
urllib3.disable_warnings()

url='https://www.qiushibaike.com/'
r=requests.get(url,verify=False)

# print(r.content.decode('utf-8'))
soup=BeautifulSoup(r.content.decode('utf-8'),'html.parser')

# qiushi=soup.find_all('span')
# 简写：
qiushi=soup('span')

# id属性
# qiushi_id=soup.find_all(id='lmp')

# name属性
# qiushi_name=soup.find_all(name='lmp')
# 简写
# qiushi_name1=soup(name='lmp')

# 标签和属性
# qiushi_id_new=soup.find_all('a',id='lmp')
# qiushi_name_new=soup.find_all('a',name='lmp')

# qiushi=soup.span.get_text
# print(qiushi)
for i in qiushi:
    print(i.get_text('/',strip=True))   # strip=True  去除获得文本内容的前后空白

