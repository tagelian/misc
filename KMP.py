# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 20:06:04 2018

@author: lenovo
"""

def compute(P):
    m = len(P)
    pi = [0 for i in range(m)]
    k = 0
    for q in range(2):
        while k > 0 and P[k + 1] != P[q]:
            k = pi[k]
        if P[k + 1] == P[q]:
            k += 1
        pi[q] = k
    return pi
    