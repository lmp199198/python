# -*- coding:utf-8 -*-
import unittest
from limaopeng.sale_project.common.HTMLTestRunner import HTMLTestRunner
import time

# 找出所有的执行用例：
# discover后面接执行用例的路径:"E:\\python3.6.3\\sale_project\\testcase"，和匹配规则：test*.py
discover=unittest.defaultTestLoader.discover("E:\\python3.6.3\\sale_project\\testcase",
                                             "test*.py")
# 打印disover，查看加载情况
# print(discover)

# discover2=unittest.defaultTestLoader.discover("E:\\python3.6.3\\sale_project\\testcase",
#                                              "test*.py")


# 合并多个用例：根据路径的不同来执行：
# all=unittest.TestSuite()
# for i in discover1:
#     all.addTests(i)
# for j in discover2:
#     all.addTests(j)

nowtime=time.strftime('%Y_%m_%d_%H_%M_%S')   #获取系统当前时间
print(nowtime)

report_path="E:\\python3.6.3\\sale_project\\report"+"\\report %s.html" % nowtime  #测试报告路径

fp=open(report_path,"wb")

runner=HTMLTestRunner(fp,verbosity=2,
                      title="这是我的报告：",
                      description='报告内容如下',
                      retry=2)

runner.run(discover)         #执行

