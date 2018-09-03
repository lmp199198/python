# -*- coding:utf-8 -*-
import requests
import unittest
from limaopeng.jiekou_wenjianshangchuan.chandao_login import Zendao_login
from limaopeng.jiekou_wenjianshangchuan.send_file import Sendfile
from limaopeng.jiekou_wenjianshangchuan.submit_bug import Submitbug

class Tibug(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.s=requests.session()


    def test01(self):
        # 上传文件：第一步，登录
        log=Zendao_login(self.s)
        log.login()
        # 第二步，传文件图片
        send=Sendfile(self.s)
        res1=send.send_img()
        # self.assertIn('http://127.0.0.1:81/zentao/data/upload/1/201808/1715390502650ij.png',res1)
        # 第三步，提交bug
        su=Submitbug(self.s)
        l=su.submit()
        su.get_location(l)
        html='/zentao/bug-browse-1-0-byModule-1.html'
        self.assertIn(html,l)


if __name__ == '__main__':
    unittest.main()




