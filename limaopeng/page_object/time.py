# -*- coding:utf-8 -*-
import os,time
#now_time=time.strptime('%H:%M')
# k=1
#
# while k<2:
#
#      now_time=time.strftime('%H:%M')
#      if now_time=='16:36':
#          print('脚本开始执行')
#          os.system(r'python E:\python3.6.3\limaopeng\port_request\test_fatie_api.py')
#          print('脚本执行结束')
#          break
#      else:
#          time.sleep(10)
#          print(now_time)

now = time.strftime("%Y_%m_%d_%H_%M_%S")
cur_path = os.path.dirname(os.path.realpath(__file__))
reportName="report"
report_path = os.path.join(cur_path, reportName)  # 用例文件夹
    # 如果不存在这个report文件夹，就自动创建一个
if not os.path.exists(report_path):
    os.mkdir(report_path)
report_abspath = os.path.join(report_path, "%s_result.html"% now)
print("report path:%s"%report_abspath)

