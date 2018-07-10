# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 07:11:11 2018

@author: lenovo
"""

# start    by cui 07:12 20180711 Wednesday
# finished by cui 07:34 20180711 Wednesday 
#------------------------------------------------------------------------------
def Naive(T, P):
    n = len(T)
    m = len(P)
    for s in range(n - m + 1):
        if P == T[s : s + m]:
            print(P, ' occurs in ', T, ' with ', s, ' shifts.')
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
                print(P, ' occurs in ', T, ' with ', s, ' shifts.')
        if s < n - m:
            t = (d * (t - h * (ord(T[s]) - 97)) + ord(T[s + m]) - 97) % q
#------------------------------------------------------------------------------
def compute(P):
    m = len(P)
    pi = [0 for i in range(m)]
    k = 0
    for q in range(1, m):
        while k > 0 and P[k] != P[q]:
            k = pi[k]
        if P[k] == P[q]:
            k += 1
        pi[q] = k
    return pi
#------------------------------------------------------------------------------
def KMP(T, P):
    n = len(T)
    m = len(P)
    pi = compute(P)
    q = -1
    for i in range(n):
        while q > -1 and P[q + 1] != T[i]:
            q = pi[q]
        if P[q + 1] == T[i]:
            q += 1
        if q == m - 1:
            print(P, ' occurs in ', T, ' with ', i - m + 1, ' shifts.')
            q = pi[q]
#------------------------------------------------------------------------------            
T = 'cuiababacababaca'
P = 'ababaca'
#Naive(T, P)
#RabinKarp(T, P, 26, 13)
#KMP(T, P)
