# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 13:47:02 2022

@author: 91638
"""


import pandas as pd
data=pd.read_csv("C:/Users/91638/Downloads/IPL Matches 2008-2020.csv")
data.head(10)                   
data.tail(10)
data.info()
data.result_margin.mean()
data.result_margin.median()
data.result_margin.mode()
data.result_margin.std()
data.result_margin.var()
data.result_margin.skew()
data.result_margin.kurt()
data.result_margin.hist()
data.winner.mode()