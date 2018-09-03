# -*- coding:utf-8 -*-
import unittest
import os
import HTMLTestRunner
import time
# # python2.7要是报编码问题，就加这三行，python3不用加
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
cur_path = os.path.dirname(os.path.realpath(__file__))   # 当前脚本所在文件真实路径
case_path = os.path.join(cur_path, "testcase")  # 测试用例的路径
#  case_path的另一种方法：
# case_path=os.path.join(os.getcwd(),'testcase')

report_path = os.path.join(cur_path, "report")  # 报告存放路径
#  c=os.getcwd()  恒等于  cur_path = os.path.dirname(os.path.realpath(__file__))

# 如果不存在report_path这个文件。则自动创建这个文件：
if not os.path.exists(report_path):
    os.mkdir(report_path)

print(cur_path)
print(case_path)
print(report_path)
# print(c)


def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,
                                                   "test*.py")
    print(discover)
    return discover

if __name__ == '__main__':
    run = HTMLTestRunner.HTMLTestRunner(title="可以装逼的测试报告",
                                            description="测试用例参考",
                                            stream=open(report_path+"\\result.html", "wb"),
                                            retry=1)

    run.run(all_case())


