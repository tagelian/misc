# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 10:50:01 2018

@author: lenovo
"""

def NaiveStringMatching(P, T):
    for i in range(len(T) - len(P) + 1):
        if P == T[i:len(P) + i]:
            print(P, " occurs in ", T, " with ", i, " shifts.")
P = "cui"
T = "njucuinjucui"
NaiveStringMatching(P, T)