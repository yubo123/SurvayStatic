# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import Config as Cf
import random
from collections import Counter
df = pd.DataFrame(np.random.randn(10,2))
df  = df.applymap(lambda x:x+10)
df['id'] = [1,2,3,1,2,3,1,2,3,1]
gp = df.groupby('id')
gp = gp[1].agg({'q0.25':lambda x:x.quantile(0.25),'mean':np.mean,'q0.75':lambda x:x.quantile(0.75)})
print(df)
print(df.quantile(0.75))
print(df[1].quantile(0.75))
print(df[1].mean())
print(df[1].quantile(0.25))
print(gp)