# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
def get_city_dict(path = ""):
    outpath = unicode(path,encoding='utf-8')
    df = pd.read_excel(outpath)
    tdict = df.to_dict('list')
    city_dict = dict(zip(tdict[u"城市序号"],tdict[u"城市名称"]))
    return city_dict

inpath = 'C:\Users\lenovo\Desktop\\2016年政府质量工作公众满意度调查\\原始问卷表.xls'
outpath = unicode(inpath,encoding='utf-8')



