# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 13:34:31 2022

@author: 91638
"""

import pandas as pd
diet=pd.read_excel("C:/Users/91638/Downloads/diet.xlsx")
diet.columns=["diet_A","diet_B","diet_C"]
diet.head()
from scipy import stats
stats.shapiro(diet.diet_A)
stats.shapiro(diet.diet_B)
stats.shapiro(diet.diet_C)
stats.ttest_ind(diet.diet_A,diet.diet_B)
stats.ttest_rel(diet.diet_A,diet.diet_B)
stats.ttest_1samp(diet.diet_A,45)
from statsmodels.stats.weightstats import ztest
ztest(diet.diet_A,value=20)
stats.f_oneway(diet.diet_A,diet.diet_B,diet.diet_C)

from  statsmodels
jhonny_talkers=pd.read_excel("C:/Users/91638/Downloads/JohnyTalkers.xlsx")
jhonny_talkers.head()
pd.crosstab(jhonny_talkers.Person,jhonny_talkers.Icecream)
from statsmodels.stats.proportion import proportions_ztest
import numpy as np
count=np.array([58,152])

proportions_ztest(count=482,nobs=2000,value=0.25)
bahaman=pd.read_excel("C:/Users/91638/Downloads/Bahaman.xlsx")
