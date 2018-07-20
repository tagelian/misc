# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 09:45:33 2018

@author: lenovo
"""
# created by cui 20180720 Friday 09:45
# finished by cui  20180720 Friday 09:56
def CountSort(A, k):
    B = []
    for i in range(len(A)):
        B.append(0)
    
    C = []
    for j in range(k + 1):
        C.append(0)
    
    for i in range(len(A)):
        C[A[i]] = C[A[i]] + 1
    for j in range(1, k + 1):
        C[j] = C[j] + C[j - 1]
    for j in range(len(A)):
        B[C[A[j]] - 1] = A[j]
        C[A[j]] = C[A[j]]  - 1
    return B

testList = [5,4,3,3,2,1,1]
B = CountSort(testList, 10)
print(B)
        
        
    