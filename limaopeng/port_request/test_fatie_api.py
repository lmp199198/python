# -*- coding:utf-8 -*-
import unittest
import requests
from limaopeng.port_request.fatie_api import Blog

class Fatie(unittest.TestCase):

    def setUp(self):
        self.s=requests.session()
        self.blog=Blog()
    def test01(self):
        '''登陆'''
        self.blog.zidong_login()
        '''发帖'''
        fatie_url=self.blog.fatie()
        '''获取postid'''
        postid=self.blog.get_postid(fatie_url)
        '''删帖'''
        deletetiezi=self.blog.deletejiekou(postid)
        '''断言'''
        self.assertEqual(deletetiezi,True)

if __name__ == '__main__':
    unittest.main()


