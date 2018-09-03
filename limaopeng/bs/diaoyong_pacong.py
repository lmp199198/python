# -*- coding:utf-8 -*-
import unittest
import requests
from limaopeng.bs.pacong_fengzhuang import Followers

class Fensi(unittest.TestCase):

    def setUp(self):
        self.s=requests.session()
        self.path=r'C:\Users\lenovo\AppData\Roaming\Mozilla\Firefox\Profiles\wxglh3q7.default'
        self.url='https://home.cnblogs.com/u/yoyoketang/relation/followers'
        self.follower=Followers()

    def test01(self):
        '''获取cookies'''
        cookies=self.follower.get_cookie()
        '''添加cookies'''
        self.follower.add_cookie(cookies)
        '''获取粉丝数量'''
        n=self.follower.get_page_num()
        '''断言'''
        self.assertEqual(n,24)
        '''获取粉丝名称'''
        self.follower.save_fensi_name(n)

if __name__ == '__main__':
    unittest.main()





