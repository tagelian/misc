# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 10:43:16 2018

@author: lenovo
"""

# created by cui 20180717 Tuesday 10:45
# have some problems with line 19, 11:12
def CountSort(A, B, k):
    C = []
    for i in range(k + 1):
        C.append(0)
    for j in range(len(A)):
        C[A[j]] = C[A[j]] + 1
    for i in range(1, k + 1):
        C[i] = C[i] + C[i - 1]
    for j in range(len(A) - 1, -1, -1):
        B[C[A[j]]] = A[j]
        C[A[j]] = C[A[j]] - 1
testList = [9,8,7,6,5,5,2,2,1]
B = [0] * 9
CountSort(testList, B, 9)
print(B)