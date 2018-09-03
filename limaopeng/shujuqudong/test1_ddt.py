# -*- coding:utf-8 -*-
import requests
import ddt
import unittest
from limaopeng.jiekou_wenjianshangchuan.chandao_login import Zendao_login

data=[{'username':'admin','psw':'e10adc3949ba59abbe56e057f20f883e','expect':True},
      {'username':'admin2','psw':'e10adc3949ba59abbe56e057f20f883e','expect':False},
      {'username':'admin3','psw':'e10adc3949ba59abbe56e057f20f883e','expect':False}]

@ddt.ddt
class Test(unittest.TestCase):

    def setUp(self):
        self.s=requests.session()
        self.log=Zendao_login(self.s)

    @ddt.data(*data)   # '*'指代的是list参数分开传入，多组参数分开传
    def test(self,test_data):   # 使用test_data依次接收data参数：

        # print('测试数据：%s' % test_data)

        # 将list里面的参数用字典的形式放到login里面
        username=test_data['username']
        psw=test_data['psw']

        result=self.log.login(username,psw)
        # print(result)
        login_result=self.log.is_login_success(result)
        print('返回的结果：%s'%login_result)

        expect=test_data['expect']
        self.assertTrue(expect==login_result)
if __name__ == '__main__':
    unittest.main()


