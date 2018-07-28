# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 12:01:27 2018

@author: cui
"""
#------------------------------------------------------------------------------
def COUNTING_SORT(A, k):
    B = [0] * len(A)
    C = [0] * (k + 1)
    for i in range(len(A)):
        C[A[i]] = C[A[i]] + 1
    for j in range(1, k + 1):
        C[j] = C[j] + C[j - 1]
    for i in range(len(A) - 1, -1, -1):
        '''
        caution: the mirror difference  C[] need to jian 1
        '''
        B[C[A[i]] - 1] = A[i]
        C[A[i]] = C[A[i]] -  1
    return B
#------------------------------------------------------------------------------
# =============================================================================
# def C824(A,k,a,b):
#     C = [0] * (k + 1)
#     for w in A:
#         C[w] = C[w] + 1
#     for j in range(1, k + 1):
#         C[j] = C[j] + C[j - 1]
#     maxa = A[0]
#     for a in A:
#         
#         if a > maxa:
#             maxa = a
#     maxb = A[0]
#     for a in A:
#         if a > maxb
#     
# =============================================================================
#------------------------------------------------------------------------------
test = [0,9,1,0,0,8,0,1,7]
B=COUNTING_SORT(test, 100)
print(B)
    