# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 16:04:49 2018

@author: lenovo
"""
# ord(character) a function that convert character to number
def RabinKarp(P, T, d, q):
    n = len(T)
    m = len(P)
    h = pow(d, m - 1) % q
    p = 0
    t0 = 0
    for i in range(m):
        p = (d * p + (ord(P[i]) - ord('a'))) % q
        t0 = (d * t0 + (ord(T[i]) - ord('a'))) % q
    for s in range(n - m + 1):
        if p == t0:
            if P == T[s : m + s]:
                print(P, " occurs in ", T, " with ", s, " shifts.")
        if s < n - m:
            t0 = (d * (t0 - h * (ord(T[s]) - ord('a'))) + (ord(T[s + m]) - ord('a'))) % q
P = "cui"
T = "njucuinjucui"
RabinKarp(P, T, 26, 13)
        