# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 07:45:29 2022

@author: 91638
"""

def flames(name1,name2):
    namestr = name1 + name2
    for c in namestr:
        if namestr.count(c) != 1:
            namestr = namestr.replace(c,"")
    print("FLAMES....")
    print("F = Friend \nL = Love \nA = Affection \nM = Marriage \nE = Enemy \nS = Siblings \n\n")
    
    number = len(namestr) % 6
    rel = ""
    if number == 1:
        rel += "Friends"
    elif number == 2:
        rel += "Love"
    elif number == 3:
        rel += "Affection"
    elif number == 4:
        rel += "Marriage"
    elif number == 5:
        rel += "Enemy"
    elif number == 0:
        rel += "Siblings"
    else:
        pass
    return rel
n1 = input("Enter your name : ")
n2 = input("Enter name of your crush : ")
print(f"Your Relationship is : {flames(n1,n2)}")
