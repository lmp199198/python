# -*- coding:utf-8 -*-
import json
a={'as':'we','w':12,'ewq':True,"eq":False,'LMP':None,'a':('ada',852,True),12:['lmp']}
# # 删除
# del a['as']
# del(a['w'])
# print(a)
# # 增加
# a['c']='852'
# print(a)
#
# # 查询
# print(a['ewq'])

print(type(a))
# 字典转json,json变成字符串格式
print('---字典转json---')
a_json = json.dumps(a)
print(a_json)
print(type(a_json))


# json转字典
print("---json转字典---")
a_dict=json.loads(a_json)
# a_dict=json.loads(a_json)
print(a_dict)