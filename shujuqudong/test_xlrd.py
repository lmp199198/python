# -*- coding:utf-8 -*-
import xlrd

# 打开excel表格：
data=xlrd.open_workbook('test_data.xlsx')  # 里面的参数是文件路径

# 读取excel表格数据：
table1=data.sheets()[0]          # 通过索引顺序获取
table=data.sheet_by_index()    # 通过索引顺序获取
table2=data.sheet_by_name('sheet1')  #通过name名称获取，

# 获取行数和列数：
nrows=table.nrows    # 获取总行数
ncols=table.ncols    # 获取总列数

# 通过索引获取：
print(table.row_values(0))  # 获取第一行值
print(table.col_values(0))  # 获取第一列值