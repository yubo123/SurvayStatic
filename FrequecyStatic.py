# -*- coding: utf-8 -*-
from collections import Counter
import xlrd
import xlwt
def open_excel(file='file.xls'):
    try:
        workbook = xlrd.open_workbook(file)
        return workbook
    except Exception,e:
        print str(e)
def excel_table_bycol(file='file.xls',first_col=0,by_index=0):
    workbook = open_excel(file)
    sheet1 = workbook.sheet_by_index(by_index)
    ncols = sheet1.ncols
    list = []
    for i in range(first_col,ncols):
        list.append(sheet1.col_values(i))
    return list
def counter_repeat(row=[]):
    return Counter(row).__len__()

wbk = xlwt.Workbook()
sheet1 = wbk.add_sheet('sheet 1',cell_overwrite_ok=True)
tables = excel_table_bycol(file='C:\Users\lenovo\Desktop\\test.xlsx')
for row in range(0,len(tables)):
    C = Counter(tables[row])
    keys = C.keys()
    keys.sort()
    C = map(C.get,keys)
    for i in range(0,len(keys)-1):
        sheet1.write(2*row,i,keys[i])
        sheet1.write((2*row+1),i,C[i])
    print(keys)
    print(C)
wbk.save('C:\Users\lenovo\Desktop\\test2.xlsx')