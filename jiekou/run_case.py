# -*- coding:utf-8 -*-
import unittest
import HTMLTestRunner
import time

casePath='E:\\python3.6.3\\jiekou\\case'

discover=unittest.defaultTestLoader.discover(casePath,'test*.py')
print(discover)


# runner = unittest.TextTestRunner().run(discover)

nowtime=time.strftime('%Y_%m_%d_%H_%M_%S')

reportPath = 'E:\\python3.6.3\\jiekou\\report'+"\\report_% s.html" % nowtime

fp=open(reportPath,'wb')
runner=HTMLTestRunner.HTMLTestRunner(fp,verbosity=1,
                                     title='测试报告',
                                     description='报告内容如下：',
                                     retry=2)

runner.run(discover)
fp.close()
