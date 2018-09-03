# -*- coding:utf-8 -*-
class Father():
    def fangzi(self):
        print("这是房子")
    def chezi(self):
        print("这是车子")

class Mother():
    def gongsi(self):
        print("土豪")

class Son(Father,Mother):  # 继承
    def fangz(self):
         print("重新装修房子")

    def quxifu(self):
         self.fangzi()
         self.chezi()

if __name__ == '__main__':
    d=Son()
    d.gongsi()
    d.quxifu()
    d.chezi()
    d.fangzi()
    d.fangz()
