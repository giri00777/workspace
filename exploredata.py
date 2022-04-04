# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 11:35:39 2022

@author: 91638
"""import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
data=pd.read_csv("C:/Users/91638/Downloads/Train.csv")
data.info()
data.head()
data.Item_Type.value_counts()
data.describe()
data.dtypes
plt.boxplot(data.Item_Weight)
data.corr()
data.drop(['Item_Identifier','Outlet_Identifier'],axis=1,inplace=True)
data.head()
data.Item_Weight.hist()
data.isnull().sum()
data.dropna(inplace=True)
data.shape
data.Item_Weight.describe()
data.Item_Weight.fillna(12.857,inplace=True)
data.isnull().sum() 
data.Item_Visibility.max()tats
