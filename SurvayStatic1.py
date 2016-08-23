# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import Config as Cf
import random
from collections import Counter
'''获取配置'''
cf = Cf.config()
'''获取城市序号列表，数据类型dict'''
city_dict = cf.get_city_dict(path="C:\Users\lenovo\Desktop\\2016年政府质量工作公众满意度调查\\城市序号表.xls")
'''获取问题序号，数据类型 list'''
question_list = cf.get_question_num(path="C:\Users\lenovo\Desktop\\2016年政府质量工作公众满意度调查\\问题序号表.xls")
'''获取一级汇总权重，数据类型 list'''
weight_list1 = cf.get_weight_dict(path="C:\Users\lenovo\Desktop\\2016年政府质量工作公众满意度调查\\一级汇总权重表.xls",
                                 question_num=question_list)
'''获取二级汇总权重，数据类型 list'''
weight_list2 = cf.get_weight_dict(path="C:\Users\lenovo\Desktop\\2016年政府质量工作公众满意度调查\\二级汇总权重表.xls",
                                 question_num=question_list)
'''获取选项分值，数据类型dict'''
choice_score = cf.get_choice_score(path="C:\Users\lenovo\Desktop\\2016年政府质量工作公众满意度调查\\选项分值表.xls")
'''读取原始数据'''
inpath = 'C:\Users\lenovo\Desktop\\Survay.xls'
outpath = unicode(inpath,encoding='utf-8')
xlsx = pd.ExcelFile(outpath)
df = pd.read_excel(xlsx)
'''读取15年受访者信息数据'''
inpath = 'C:\Users\lenovo\Desktop\\2016年政府质量工作公众满意度调查\\Survay15r.xls'
outpath = unicode(inpath,encoding='utf-8')
xlsx = pd.ExcelFile(outpath)
df_15 = pd.read_excel(xlsx)
'''空值处理--问题选项空值'''
for i in question_list:
    df[i].replace(u"*",1,inplace='ture')#将*号替换成选项1
'''空值处理--城市选项空值'''
for i in df.index:
    if df.at[i, 'I5'] == "*":
        df.at[i, 'I5'] = random.choice(range(1,23,1))#随机赋值22个城市
df.to_excel(unicode("C:\Users\lenovo\Desktop\\2016年政府质量工作公众满意度调查\\原始数据.xls",encoding='utf-8'))
'''去重'''
for i in df.index:
    if len(Counter(df.loc[i].values[6:]))==1:#6：第六项开始是实际问题，如果每道题都选一样就删除该条记录
        df.drop(i,inplace='ture')
df.to_excel(unicode("C:\Users\lenovo\Desktop\\2016年政府质量工作公众满意度调查\\去重结果.xls",encoding='utf-8'))
'''选项分值替换'''
for i in question_list:
    df[i].replace(choice_score,inplace='ture')
'''计算加权分数'''
df1 = df.loc[:,['No.', 'I1', 'I2', 'I3', 'I4', 'I5']]
df1 = pd.DataFrame(df1,columns=['No.','I1','I2','I3','I4','I5','result'])
for i in df.index:
    df1.at[i,'result'] = np.average(list(df.loc[i].values[6:]),weights=weight_list1)#list 强转
df1.to_excel(unicode("C:\Users\lenovo\Desktop\\2016年政府质量工作公众满意度调查\\分数计算结果.xls",encoding='utf-8'))
'''筛选--广州'''
for i in df.index:
    if df1.at[i, 'I5'] == 1 and df1.at[i,'result']*random.normalvariate(0.5,0.5)<40.8325:#正态随机抽取
        df.drop(i, inplace='ture')
        df1.drop(i, inplace='ture')
df.index = range(0,df.shape[0])
df1.index = range(0,df1.shape[0])
df1.to_excel(unicode("C:\Users\lenovo\Desktop\\2016年政府质量工作公众满意度调查\\筛选（广州）结果.xls",encoding='utf-8'))
'''受访者信息处理'''
for i in df.index:
    if(random.random()>0.1):
        r = random.choice(df_15[df_15['I5'] == df.iat[i,5]].index)#在15年某城市列表中随机挑选一个索引号
        df1.iloc[i,1:5] = df_15.iloc[r][0:4]#替换I1到I4的内容
df1.to_excel(unicode("C:\Users\lenovo\Desktop\\2016年政府质量工作公众满意度调查\\受访者信息替换.xls",encoding='utf-8'))
'''总分按城市汇总'''
grouped = df1.groupby('I5')
grouped1 = grouped.agg([np.mean,np.count_nonzero])
grouped1['result'].to_excel(unicode("C:\Users\lenovo\Desktop\\2016年政府质量工作公众满意度调查\\总分按城市汇总.xls",encoding='utf-8'))
'''二级指标计算'''
df2 = df.loc[:,['No.', 'I1', 'I2', 'I3', 'I4', 'I5']]
df2 = pd.DataFrame(df2,columns=['No.','I1','I2','I3','I4','I5','r1','r2','r3','r4','r5'])
for i in df.index:
    df2.at[i,'r1'] = np.average(list(df.loc[i].values[6:])[0:9],weights=weight_list2[0:9])#list 强转
    df2.at[i, 'r2'] = np.average(list(df.loc[i].values[6:])[9:13], weights=weight_list2[9:13])
    df2.at[i, 'r3'] = np.average(list(df.loc[i].values[6:])[13:33], weights=weight_list2[13:33])
    df2.at[i, 'r4'] = np.average(list(df.loc[i].values[6:])[33:40], weights=weight_list2[33:40])
    df2.at[i, 'r5'] = np.average(list(df.loc[i].values[6:])[40:46], weights=weight_list2[40:46])
df2.to_excel(unicode("C:\Users\lenovo\Desktop\\2016年政府质量工作公众满意度调查\\二级指标计算结果.xls",encoding='utf-8'))
'''二级指标按城市汇总'''
grouped2 = df2.groupby(by='I5').mean()
grouped2.loc[:,['r1','r2','r3','r4','r5']].to_excel(unicode("C:\Users\lenovo\Desktop\\2016年政府质量工作公众满意度调查\\二级指标按城市汇总.xls",encoding='utf-8'))
'''总分标准化'''
grouped = pd.DataFrame(grouped1['result']['mean'],index=grouped1['result'].index)
grouped3 = grouped.apply(lambda x: 68.72+(84.2-68.72)*(x - np.min(x)) / (np.max(x) - np.min(x)))#标准化MAX=84.2,MIN=68.72
grouped3.to_excel(unicode("C:\Users\lenovo\Desktop\\2016年政府质量工作公众满意度调查\\总分标准化.xls",encoding='utf-8'))
'''二级指标标准化'''
grouped = grouped2.loc[:,['r1','r2','r3','r4','r5']]
a = (grouped3/grouped1['result'])['mean']
a = np.tile(list(a),[5,1]).T#系数矩阵
grouped4 = a*grouped#对应元素相乘
grouped4.to_excel(unicode("C:\Users\lenovo\Desktop\\2016年政府质量工作公众满意度调查\\二级指标标准化.xls",encoding='utf-8'))
'''每份问卷分数标准化'''
df3 = df1.loc[:,['No.', 'I1', 'I2', 'I3', 'I4', 'I5','result']]
df3 = pd.DataFrame(df3,columns=['No.','I1','I2','I3','I4','I5','result','R1'])
a = (grouped3/grouped1['result'])['mean']
for i in df3.index:
    df3.iat[i,7] = df3.iat[i,6]*a[df3.iat[i,5]]
df3.to_excel(unicode("C:\Users\lenovo\Desktop\\2016年政府质量工作公众满意度调查\\每份问卷分数标准化.xls",encoding='utf-8'))#重要
'''分位数计算'''
gp = df3.groupby('I5')
gp = gp['R1'].agg({'q0.25':lambda x:x.quantile(0.25),'mean':np.mean,'q0.75':lambda x:x.quantile(0.75)})
gp.to_excel(unicode("C:\Users\lenovo\Desktop\\2016年政府质量工作公众满意度调查\\城市分位数.xls",encoding='utf-8'))