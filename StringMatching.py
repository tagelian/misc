# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 21:30:42 2018

@author: lenovo
"""

P = 'ababaca'
T = 'cuiababacababaca'
# 3 and 9 shifts
#------------------------------------------------------------------------------
def Naive(T, P):
    n = len(T)
    m = len(P)
    for s in range(n - m + 1):
        if P == T[s : s + m]:
            print(P,' occurs in ',  T, ' with ', s, ' shifts')
#------------------------------------------------------------------------------
def RabinKarp(T, P, d, q):
    n = len(T)
    m = len(P)
    h = pow(d, m - 1) % q
    p = 0
    t = 0
    for i in range(m):
        p = (d * p + ord(P[i]) - 97) % q
        t = (d * t + ord(T[i]) - 97) % q
    for s in range(n - m + 1):
        if p == t:
            if P == T[s : s + m]:
                print(P,' occurs in ',  T, ' with ', s, ' shifts')
        if s < n - m:
            t = (d * (t - h * (ord(T[s]) - 97)) + (ord(T[s + m]) - 97)) % q
#------------------------------------------------------------------------------
def compute(P):
    m = len(P)
    pi = [0 for i in range(m)]
    k = -1
    for q in range(1, m):
        while k > -1 and P[k + 1] != P[q]:
            k = pi[k]
        if P[k + 1] == P[q]:
            k += 1
        k += 1
        pi[q] = k
        print(k)
    return pi
#------------------------------------------------------------------------------
def KMP(T, P):
    n = len(T)
    m = len(P)
    pi = compute(P)
    q = 0
    for i in range(n):
        while q > 0 and T[q + 1] != T[i]:
            q = pi[q]
        if T[q + 1] == T[i]:
            q += 1
        if q == m - 1:
            print(P,' occurs in ',  T, ' with ', i - m + 2, ' shifts')
            q = pi[q]

            
    
            
            
#Naive(T, P)
#RabinKarp(T, P, 26, 13)
test = compute(P)
#KMP(T, P)