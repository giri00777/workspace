# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 11:42:07 2021

@author: 91638
"""

l1=[[2,3,4,5,6],[3,4,5,1,2]]
import numpy as np
l1=np.array(l1)
l2=np.array(l1)
print(np.mean(l1))
print(np.median(l1))
print(np.max(l1))
print(np.min(l1))
l1.mean()
print(l1[2:3])
print(l1[-1:-2])
#Step slicing
print(l1[1:4:2])
np.where(l1==6)
#2 dimensional array
print(l1.ndim)
#3 dimensional array indexing
l1[1]
l1[0,0]
l1[0,1]
l1.dtype
l1.shape
l1.reshape(2,1)

import pandas as pd
data=pd.read_excel("C:/Users/91638/OneDrive/Desktop/petrol price statistics.xlsx")
data.A.mean()                   
scipy