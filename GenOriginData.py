# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import Config as Cf
import random
from collections import Counter
'''生成替换过受访者信息的问卷原始数据'''
inpath = u'C:/Users/lenovo/Desktop/2016年政府质量工作公众满意度调查/8月17日版本备份/'
'''读取原始数据'''
file = u'STEP2_原始数据.xls'
outpath = inpath+file
xlsx = pd.ExcelFile(outpath)
df = pd.read_excel(xlsx)
'''读取替换后数据'''
file = u'STEP3_受访者信息替换.xls'
outpath = inpath+file
xlsx = pd.ExcelFile(outpath)
df1 = pd.read_excel(xlsx)
df1.index = df1['No.']
for i in df1.index:
    df.iloc[i,1:5] = df1.loc[i][1:5]
file = u'STEP4_原始数据II.xls'
outpath = inpath+file
df.to_excel(outpath)