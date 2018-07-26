# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 20:11:06 2018

@author: lenovo
"""

# started at 20:11 
# finished at 20:17 done sure not difficult but the idea is quite beautiful
def Partition(A,p,r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[r] = A[i + 1]
    A[i + 1] = x
    return i + 1
def QuickSort(A,p,r):
    if p < r:
        q = Partition(A,p,r)
        QuickSort(A,p,q - 1)
        QuickSort(A,q + 1, r)
test = [0,9,1,0,0,8,0,1,7]
QuickSort(test,0,len(test) - 1)
print(test)