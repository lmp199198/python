# -*- coding:utf-8 -*-
from limaopeng.leiduixiang.test3 import Father,Mother


class Sonxiao(Father,Mother):

    def qulaopo(self):

        self.fangzi()
        self.chezi()
        self.gongsi()

    def chei(self):
        lmp='兰博基尼'
        return lmp

    # def nimabi(self):
    #     self.gongsi()

if __name__ == '__main__':
    n=Sonxiao()
    n.qulaopo()
    # n.nimabi()
    # n.chei()
