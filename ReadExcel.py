# !/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import xlrd
import Util.config as cf
import Util.log as log
class OpeExcel(object):
    def __init__(self, path):
        self.path = path
    @property
    def getSheet(self):
        # 获取索引
        xl = xlrd.open_workbook(self.path)
        sheet = xl.sheet_by_index(0)
        return sheet

    @property
    def getRows(self):
        # 获取行数
        row = self.getSheet.nrows
        return row

    @property
    def getCol(self):
        # 获取列数
        col = self.getSheet.ncols
        return col

    # 以下是分别获取每一列的数值
    #获取用例ID信息
    @property
    def getId(self):
        TestId = []
        for i in range(1, self.getRows):
            TestId.append(self.getSheet.cell_value(i, 0))
        return TestId

    # 获取用例描述信息
    @property
    def getDes(self):
        TestDes = []
        for i in range(1, self.getRows):
            TestDes.append(self.getSheet.cell_value(i, 1))
        return TestDes

    #获取URL地址信息
    @property
    def getUrl(self):
        TestUrl = []
        for i in range(1, self.getRows):
            TestUrl.append(self.getSheet.cell_value(i, 2))
        return TestUrl

    # 获取用例请求参数信息
    @property
    def getData(self):
        TestData = []
        for i in range(1, self.getRows):
            TestData.append(self.getSheet.cell_value(i, 4))
        return TestData

    # 获取请求方式信息
    @property
    def getMethod(self):
        TestMethod = []
        for i in range(1, self.getRows):
            TestMethod.append(self.getSheet.cell_value(i, 3))
        return TestMethod

    @property
    def getCode(self):
        TestCode = []
        for i in range(1, self.getRows):
            TestCode.append(self.getSheet.cell_value(i, 5))
        return TestCode

if __name__ == '__main__':
     opers = OpeExcel(cf.path)
     print(opers.getId)
     print(opers.getDes)
     print(opers.getUrl)
     print(opers.getMethod)
     print(opers.getData)









