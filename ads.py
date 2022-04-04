# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 22:15:41 2022

@author: 91638
"""

import pandas as pd
from statsmodels
project_excel=pd.read_excel("C:/Users/91638/OneDrive/Documents/project.xlsx")
pd.crosstab(project_excel.peoples age group,project_excel.Downloads)
from statsmodels.stats.proportion import proportions_ztest
import numpy as np
count=np.array([445,291])
nobs=np.array([695,648])
proportions_ztest(count,nobs)
stat,p_value=proportions_ztest(count=736,nobs=1343,value=0.54)
print(p_value)
