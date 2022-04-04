# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 20:30:54 2022

@author: 91638
"""

m=float(input("Enter mean value:"))
sg=float(input("Enter sigma value:"))
cdf1=float(input("to find cdf"))
cdf2=float(input("to find cdf"))
from statistics import NormalDist
nd=NormalDist(mu=m,sigma=sg)
if cdf1<cdf2:
    n1=nd.cdf(cdf2)
    print("Z score of",cdf1,"is",n1)
    n2=nd.cdf(cdf1)
    print("Z score of",cdf2,"is",n2)
    nd=n2-n1
    print("NORMAL DISTRIBUTION VALUE",nd)
else: 
    print("INVALID")
    