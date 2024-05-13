#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/4/23 15:13
# Author : smart
# @File : read_excl.py
# @Software : PyCharm
import xlrd
#打开文件
wb=xlrd.open_workbook("../test_user_data.xlsx")
#打开工作簿
sheet1=wb.sheet_by_name("test_user_reg")
#行
print(sheet1.nrows)
#列
print(sheet1.ncols)
#获取第一行第一列的数据
print(sheet1.cell(0,0).value)
#获取第一行中的所有数据
print(sheet1.row_values(0))
#通过循环 把每一行的数据当列表输出
for i in range(sheet1.nrows):
    print(sheet1.row_values(i))
