# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 20:44:20 2022

@author: 91638
"""

def cgpaCalc(marks,n):
    grade=[0]*n
    sum=0
    for i in range(n):
        grade[i]=(marks[i]/10)
    for i in range(n):
            sum+=grade[i]
            cgpa=sum/n
            return cgpa
        n=5
        marks=[90,80,99,87,90]
        cgpa=cgpaCalc(marks,n)
        print("CGPA=",'%.1f'%cgpa)
        print("CGPA %="",'%.2f'% (cgpa*9.5")