# -*- coding:utf-8 -*-
import requests,os
from bs4 import BeautifulSoup

url='http://699pic.com/sousuo-218808-13-1.html'
r=requests.get(url)

html_image=r.content
# print(r.content.decode('utf-8'))

soup=BeautifulSoup(html_image,'html.parser')

# 第一种方法：
# 查找的是img标签下的class属性：
image=soup('img',class_="lazy")


# 第二种方法：
# 查找爷爷标签下的class属性：
# image = soup('div',class_='list')
# for i in image:
#     print(i.a.img)


# 获取当前绝对文件的目录：
# 该目录路径为：E:\python3.6.3\limaopeng\bs
cur_path=os.path.dirname(os.path.realpath(__file__))
print(cur_path)

# 该目录路径为：E:\python3.6.3\limaopeng，多加了一个os.path.dirname，路径返回父目录：
cur_path1=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
print(cur_path1)

# 合并路径和文件夹名称：
img=os.path.join(cur_path1,'img_title')
print(img)

# 判断目录是否存在，如果不存在，则新建一个目录：
if not os.path.exists(img):
    os.mkdir(img)

for i in image:
    # print(i)
    # 尝试去执行相关操作：
    try:
        image_url = i['data-original']
        img_name = i['title']
        print(image_url,img_name)
        r1=requests.get(image_url)
        fp=open(os.path.join(img,'% s.jpg' % img_name),'wb')
        fp.write(r1.content)
        fp.close()
    # Exception接收所有异常，并保存异常信息到msg：
    except Exception as msg:
        print(msg)
    # except:
    #     pass




