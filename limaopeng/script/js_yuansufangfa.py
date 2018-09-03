# -*- coding:utf-8 -*-
# 1.通过id获取
# document.getElementById(“id”)----------获取的是单个


# 2.通过name获取
#  document.getElementsByName(“Name”)[0]---------获取的是多个
# 返回的是list


# 3.通过标签名选取元素
# document.getElementsByTagName(“tag”) --------获取的是多个


# 4.通过CLASS类选取元素
# document.getElementsByClassName(“class”) --------获取的是多个

# 兼容性：IE8及其以下版本的浏览器未实现getElementsByClassName方法


# 5.通过CSS选择器选取元素
# document.querySelectorAll(“css selector")
# 兼容性：IE8及其以下版本的浏览器只支持CSS2标准的选择器语法
