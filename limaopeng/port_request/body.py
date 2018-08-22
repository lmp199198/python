# -*- coding:utf-8 -*-
# post请求有body的情况
import requests
import json

# json
# 别人公司的网站，你们自己找个吧
url = "https://smc.api.xxx.com/xxx/"

body = {
    "RequestStamp": "stamp-1526131440953",
    "Callback": "110",
    "PostTime": 1526131440953,
    "PostContent": {
        "BusinessType": 3,
        "MemberID": 3805,
        "pageNo": 1,
        "pageSize": 10,
        "ProductID": 0
    },
    "CustomApp": "BWEB",
    "ApiCode": "Product/GetGuessYouLikeProdcutList",
    "Platform": "PC",
    "Token": "bb53ef67349f4c24bb146ed3edd720d8",
    "PageNumber": 1,
    "PageSize": 10
}

# 第一种方法：
# post请求，content-type:application/json格式
# r = requests.post(url, json=body, verify=False) # json=body,verify=False
# print(r.text)


# 第二张方法：
# body内容就是字典格式，需要将字典转换成json格式，用data接收：
# 用data参数传json格式的数据：
# data=json.dumps(body)

# print(r1.text)
# print(type(r1.text))

# data转json：需要导入json：
# print(json.loads(r1.text))
# print(type(json.loads(r1.text)))

# 最简单的json转字典的方式：


r = requests.post(url, data=json.dumps(body), verify=False) # json=body,verify=False
print(r.text)

