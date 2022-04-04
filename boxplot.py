# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 12:04:20 2022

@author: 91638
"""
list1=[100,80,70,60,50,10]
import matplotlib.pyplot as plt
plt.boxplot(list1)
import numpy as np
data=np.random.normal(80,2,100)
plt.hist(data)
plt.boxplot(data)
x=[]
y=[]
import numpy as np
x=np.array([110,120,130,140,150])
y=np.array([50,60,70,80,100])
plt.plot(y,'o')#dot plot
plt.plot(x,y,'o')#scatter plot
plt.plot(x,y)# Line plot
plt.plot(x)# run together to compare
plt.plot(y)# run together to compare
plt.plot(y,'s:b')
plt.plot(y,'^-b')
plt.plot(x,y)
plt.xlabel('height')
plt.ylabel('weight')
plt.title('Height vs weight')
plt.grid()
x=['Red','Yellow','Blue','Purple','Pink']
y=[10,12,14,16,18]
plt.bar(x,y,color='pink')
plt.barh(x,y)
plt.pie(y)
plt.scatter(x,y)
plt.figure(figsize=(12,16))
plt.scatter(x,y)
import seaborn as sns
tips=sns.load_dataset("tips")
tips.head()
tips.columns
plt.figure(figsize=(16,12))
sns.lineplot(x='total_bill',y='tip',data=tips,hue='sex',palette={"Male":'blue',"Female":'pink'})
sns.scatterplot(x='total_bill',y='tip',data=tips,hue='sex',palette={"Male":'blue',"Female":'pink'})
plt.xlabel('BILL')
plt.ylabel('TIPS')
sns.scatterplot(x='total_bill',y='tip',data=tips,size='smoker',hue='sex')
sns.relplot(x='total_bill',y='tip',data=tips,kind='scatter',col_warp=2,size='smoker',hue='sex')
