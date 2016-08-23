# -*- coding: utf-8 -*-
from collections import Counter
import numpy as np
import pandas as pd
import xlrd
import xlwt
def get_city_dict(path = ""):#获取城市序号列表
    outpath = unicode(path,encoding='utf-8')
    df = pd.read_excel(outpath)
    tdict = df.to_dict('list')
    city_dict = dict(zip(tdict[u"城市序号"],tdict[u"城市名称"]))
    return city_dict
def open_excel(file='file.xls'):
    try:
        workbook = xlrd.open_workbook(file)
        return workbook
    except Exception,e:
        print str(e)
def excel_table_byindex(file= 'file.xls',first_row=1,by_index=0):#获取一行的数据
    workbook = open_excel(file)
    sheet1 = workbook.sheet_by_index(by_index)
    nrows = sheet1.nrows #行数
    ncols = sheet1.ncols #列数
    list =[]
    for i in range(first_row,nrows):
        list.append(sheet1.row_values(i))
    return list
def excel_table_bycol(file='file.xls',first_col=0,by_index=0):#获取一列的数据
    workbook = open_excel(file)
    sheet1 = workbook.sheet_by_index(by_index)
    ncols = sheet1.ncols
    list = []
    for i in range(first_col,ncols):
        list.append(sheet1.col_values(i))
    return list
def replace_row(lst=[],pattern = {1:100,2:80,3:60,4:40,5:20,"*":80}):#替换选项分值
    rep = [pattern[x] if x in pattern else x for x in lst]
    return rep
def result_cal(row=[],weight=[0.0225, 0.0225, 0.045, 0.0225, 0.0225, 0.0225, 0.0225, 0.0225,0.0225, 0.0375, 0.0375,
                              0.0375, 0.1125, 0.0225, 0.0225, 0.0225,0.0225, 0.0225, 0.0075, 0.0075, 0.0075,0.0075,
                              0.0075, 0.0075,0.0075, 0.0075, 0.0075, 0.0075, 0.0075, 0.0075, 0.0075, 0.0075,0.0075,
                              0.025, 0.025, 0.025, 0.0375, 0.0375, 0.0375, 0.0375,0.016666667, 0.016666667,0.016666667,
                              0.016666667, 0.016666667,0.016666667 ]):#计算得分
    vaule = map(lambda (a,b):float(a)*b, zip(row,weight))
    result = sum(vaule)
    return  result
def result_list(tables=[],first_row=0,last_row_offset=0,first_col=0,last_col_offset=0,choice=0):#计算总分，按选项划分
    last_row = len(tables) - last_row_offset
    last_col = len(tables[0]) - last_col_offset
    result_list = []
    choice_list = []
    num_list = []
    for row in range(first_row, last_row):
        rep = replace_row(tables[row][first_col:last_col])
        result = result_cal(rep)
        result_list.append(result)
        choice_list.append(tables[row][choice])
        num_list.append(tables[row][0])
    return {'num':num_list,'key1':choice_list,'data1':result_list}
def city_result(tables=[],first_row=0,last_row_offset=0,first_col=0,last_col_offset=0,choice=0):
    last_row = len(tables) - last_row_offset
    last_col = len(tables[0]) - last_col_offset
    A,B,C,D,E = [],[],[],[],[]
    choice_list = []
    num_list = []
    for row in range(first_row,last_row):
        rep = replace_row(tables[row][first_col:last_col])
        A.append(result_cal(rep[0:9],weight=[0.1,0.1,0.2,0.1,0.1,0.1,0.1,0.1,0.1]))
        B.append(result_cal(rep[9:13],weight=[0.166666667,0.166666667,0.166666667,0.5] ))
        C.append(result_cal(rep[13:33],weight=[0.1,0.1,0.1,0.1,0.1,0.033333333,0.033333333,0.033333333,0.033333333,
                                               0.033333333,0.033333333,0.033333333,0.033333333,0.033333333,0.033333333,
                                               0.033333333,0.033333333,0.033333333,0.033333333,0.033333333]))
        D.append(result_cal(rep[33:40],weight=[0.111111111,0.111111111,0.111111111,0.166666667,0.166666667,0.166666667,
                                               0.166666667]))
        E.append(result_cal(rep[40:46],weight=[0.166666667,0.166666667,0.166666667,0.166666667,0.166666667,0.166666667]))
        choice_list.append(tables[row][choice])
    return {'key1': choice_list, 'A': A, 'B': B, 'C': C, 'D': D, 'E': E}
def counter_repeat(row=[]):#计算重复次数
    return len(Counter(row))
def del_repeat(tables=[],first_row=0,last_row_offset=0,first_col=0,last_col_offset=0):#去重
    last_row = len(tables) - last_row_offset
    last_col = len(tables[0]) - last_col_offset
    fin_tables = []
    for row in range(first_row, last_row):
        if counter_repeat(tables[row][first_col:last_col]) == 1:
            continue
        fin_tables.append(tables[row])
    return fin_tables
def rec_repeat(tables=[],first_row=0,last_row_offset=0,first_col=0,last_col_offset=0):#记录重复数
    last_row = len(tables) - last_row_offset
    last_col = len(tables[0]) - last_col_offset
    fin_tables = []
    for row in range(first_row,last_row):
        new_row = []
        for i in tables[row]:
            new_row.append(i)
        new_row.append(counter_repeat(tables[row][first_col:last_col]))
        fin_tables.append(new_row)
    return fin_tables

wbk = xlwt.Workbook(encoding = 'utf-8')
sheet1 = wbk.add_sheet('sheet 1',cell_overwrite_ok=True)
tables = excel_table_byindex(file='C:\Users\lenovo\Desktop\\Survay.xlsx')
del_repeat_tables = del_repeat(tables,first_row=1,first_col= 6)#去重
re_dict = result_list(del_repeat_tables,first_col= 6,choice= 5)#获取数据
df = pd.DataFrame(re_dict)
df.to_excel('C:\Users\lenovo\Desktop\\test4.xls',sheet_name='Sheet1')
grouped = df.groupby(by='key1')#按城市分类汇总平均值
grouped = grouped.agg([np.mean,np.count_nonzero])
grouped = grouped.drop("*",axis=0)#删除空数据
grouped = grouped['data1'].sort_values(by='mean',ascending=False)#排序
sheet1.write(0,0,"城市序号")
sheet1.write(0,1,"城市名称")
sheet1.write(0,2,"得分")
sheet1.write(0,3,"数量")
city_list = replace_row(grouped.index,pattern=get_city_dict(path="C:\Users\lenovo\Desktop\\2016年政府质量工作公众满意度调查\\城市序号表.xls"))
for i,j in enumerate(grouped.index):
    sheet1.write(i+1,0,j)
for i,j in enumerate(city_list):
    sheet1.write(i+1,1,j)
for i,j in enumerate(grouped['mean']):
    sheet1.write(i + 1, 2, j)
for i,j in enumerate(grouped['count_nonzero']):
    sheet1.write(i + 1, 3, j)
city_dict = city_result(del_repeat_tables,first_row=0,first_col= 6,choice= 5)
df = pd.DataFrame(city_dict)
grouped = df.groupby(by='key1').mean()
grouped = grouped.drop("*",axis=0)
grouped.to_excel('C:\Users\lenovo\Desktop\\test3.xls',sheet_name='Sheet1')


'''sheet2 = wbk.add_sheet('sheet 2',cell_overwrite_ok=True)
rec_re_tables =  rec_repeat(tables,first_row=1,first_col= 6)
for i,row in enumerate(rec_re_tables):
   for j,cell in enumerate(row):
       sheet2.write(i,j,cell)'''


wbk.save('C:\Users\lenovo\Desktop\\test2.xlsx')