# -*- coding:utf-8 -*-
import requests
import unittest

# post请求没有body的情况
class WeatherChaXun(unittest.TestCase):

    def setUp(self):
        self.url="http://v.juhe.cn/weather/index"
        self.s = requests.session()

    def weather_cx(self,place,keys):
        par={"cityname": place,
            "dtype": "json",
            "format": "2",
            "key": keys
            }
        r1=self.s.get(self.url,params=par)
        j1=r1.json()
        print(j1)
        res=j1['reason']
        print(res)
        return res

    def test01(self):
        result1=self.weather_cx('深圳',"ac2e2a9554bbf184a4df4bb9cb10e149")
        self.assertTrue(result1=='successed!')

    def test02(self):
        result2=self.weather_cx('深圳'," ")
        self.assertTrue(result2=='错误的请求KEY')

        # if res=='successed!':
        #     print('接口测试成功：pass')
        # else:
        #     print('接口测试失败：fail')
        # for i,j in j1.items():
        #     print(i,j)
        #     print(j1[i])

if __name__ == '__main__':
    unittest.main()
