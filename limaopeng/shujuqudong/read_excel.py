# -*- coding:utf-8 -*-
import xlrd
class ExcelUtil():
    def __init__(self, excelPath = "test_data.xlsx", sheetName = "Sheet1"):
        # 打开excel
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)   # 通过名称获取
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols
        # table = data.sheets()[0]             # 通过索引顺序获取
        # table = data.sheet_by_index(0)       # 通过索引顺序获取
        # table = data.sheet_by_name(u'Sheet1')  # 通过名称获取

    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in list(range(self.rowNum-1)):
                s = {}
                # 从第二行取对应values值
                # s['rowNum'] = i+2   # 取所在行的序号
                values = self.table.row_values(j)
                for x in list(range(self.colNum)):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            # print(r)
            return r

if __name__ == "__main__":
    data = ExcelUtil()
    # print(data.dict_data())
    print(data.keys)
    for i in data.dict_data():
        print(i)

