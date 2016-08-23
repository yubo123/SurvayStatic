# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import Config as Cf
import random
from collections import Counter
'''获取配置'''
cf = Cf.config()
'''读取原始数据'''
inpath = 'C:\Users\lenovo\Desktop\\2016年政府质量工作公众满意度调查\\Survay15.xls'
outpath = unicode(inpath,encoding='utf-8')
xlsx = pd.ExcelFile(outpath)
df = pd.read_excel(xlsx)
'''空值处理--城市选项空值'''
for i in df.index:
    if np.isnan(df.at[i, 'I5']):
        df.at[i, 'I5'] = random.choice(range(1,23,1))#随机赋值22个城市
'''空值处理--性别选项空值'''
for i in df.index:
    if np.isnan(df.at[i, 'I4']):
        df.at[i, 'I4'] = random.choice([1,2])#随机赋值2个性别
df.dropna(inplace='ture')
df.index = range(0,df.shape[0])
df.to_excel(unicode("C:\Users\lenovo\Desktop\\2016年政府质量工作公众满意度调查\\Survay15r.xls",encoding='utf-8'),index='false')