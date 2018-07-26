# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 20:11:06 2018

@author: lenovo
"""

# started at 20:11 
# finished at 20:17 done sure not difficult but the idea is quite beautiful
# last modified at 21:56 add Hoare-Partition and tail recursion technique 
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
#------------------------------------------------------------------------------
def Hoare_Partition(A,p,r):
    x = A[p]
    i = p - 1
    j = r + 1
    while True:
        j -= 1
        while A[j] > x:
            j -= 1
        i += 1
        while A[i] < x:
            i += 1
        if i < j:
            A[i], A[j] = A[j], A[i]
        else:
            return j
#------------------------------------------------------------------------------
def Hoare_QuickSort(A,p,r):
    while p < r:
        q = Hoare_Partition(A,p,r)
        Hoare_QuickSort(A,p,q)
        p = q + 1
        
#------------------------------------------------------------------------------

def QuickSort(A,p,r):
    if p < r:
        q = Partition(A,p,r)
        QuickSort(A,p,q - 1)
        QuickSort(A,q + 1, r)
test = [0,9,1,0,0,8,0,1,7]
Hoare_QuickSort(test,0,len(test) - 1)
print(test)