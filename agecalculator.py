# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 09:20:24 2022

@author: 91638
"""

from datetime import date

def calculateAge(birthDate):
	today = date.today()
	age = today.year - birthDate.year -((today.month, today.day) <(birthDate.month, birthDate.day))

	return age
	
print(calculateAge(date(2001, 8, 28)), "years")