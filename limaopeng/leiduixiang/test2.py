# -*- coding:utf-8 -*-

# 创建类用class关键字
#
# 类的名称首字母大写
#
# 类名称后面可以要括号，也可以不用
#
# 括号里面为空默认继承object类
#
# 类里面的方法用def关键字定义
#
# 方法带self参数，self叫实例参数


#object是所有类的基类：

# class Bird():  #括号里面为空时，则为object基类，可以不写,默认为基类时可以不加括号
#
#     def zuiba(self):
#         print('嘴巴吃东西')
#     def chibang(self):
#         print('翅膀可以飞')
#     def jiao(self):
#         print('爪子可以抓东西')
#
#     def xingbie(self):
#         print('该鸟是一只公鸡')
#
# if __name__ == '__main__':
#     a=Bird()
#     a.chibang()
#     a.jiao()
#     a.xingbie()
#     a.zuiba()

# 可以调用多个实例


# 继承：
class Father:
    def fangzi(self):
        print('他有房子')

    def cehzi(self):
        print('他有车子')
    def piaozi(self):
        print('他有票子')

class Son(Father):   #定义一个子类Sun，继承父类Father所有的方法

# 这部分省略了，不用写：

    # def fangzi(self):
    #     print('他有房子')
    #
    # def cehzi(self):
    #     print('他有车子')
    # def piaozi(self):
    #     print('他有票子')

    def qulaopo(self):

        fang=self.fangzi()  # 可以直接调用父类的方法
        che=self.cehzi()
        # qian=self.piaozi()

    def fangzi(self):      #子类的方法的结果会覆盖父类方法的结果
        print('谁的房子')

if __name__ == '__main__':
    erzi=Son()
    erzi.qulaopo()    # 直接调用了qulaopo下面的方法：che,fang,qian
    erzi.piaozi()     # 可以在这里写，也可以在子类的方法中写，通过调用qulaopo
    erzi.fangzi()     # 打印出来
                      # 调用多个，则会打印多次，例如:erzi.piaozi()

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




