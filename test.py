# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import Config as Cf
import random
from collections import Counter
df = pd.DataFrame(np.tile(range(1, 6), [22, 1]))
df1 = pd.DataFrame(np.tile(range(1, 23), [5, 1])).T
df1[5] = df[4]
df.iloc[2,0:4] = pd.Series([0,0,0,0])
df[4] = pd.Series([0,0,0],index = [1,3,5])
df.replace(np.NaN,5,inplace= 'ture')
gp = df.groupby(4)
'''print(df)
for i in df.index:
    if(random.random()>0.1):
        r = int(random.choice(df1.index))
    #print(df1.iloc[r][0:4])
        df.iloc[i,0:4] = df1.iloc[r][0:4]
print(df)'''
print(df.quantile(0.75))


