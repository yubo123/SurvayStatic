# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
class config:
    def __init__(self):
        '''构造函数'''
    def get_city_dict(self,path=""):  # 获取城市序号列表
        outpath = unicode(path, encoding='utf-8')
        df = pd.read_excel(outpath)
        tdict = df.to_dict('list')
        city_dict = dict(zip(tdict[u"城市序号"], tdict[u"城市名称"]))
        return city_dict
    def get_weight_dict(self,path="",question_num=[]):
        outpath = unicode(path, encoding='utf-8')
        df = pd.read_excel(outpath)
        tdict = df.to_dict('list')
        weight_list = []
        weight_dict = dict(zip(tdict[u"问题序号"], tdict[u"权重"]))
        for i in question_num:
            weight_list.append(weight_dict[i])
        return weight_list
    def get_question_num(self,path=""):
        outpath = unicode(path, encoding='utf-8')
        df = pd.read_excel(outpath)
        tdict = df.to_dict('list')
        question_list = tdict[u"问题序号"]
        return question_list
    def get_choice_score(self,path=""):
        outpath = unicode(path, encoding='utf-8')
        df = pd.read_excel(outpath)
        tdict = df.to_dict('list')
        choice_score = dict(zip(tdict[u"选项序号"], tdict[u"分值"]))
        return choice_score