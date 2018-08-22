# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 15:37:57 2018

@author: lenovo
"""
def partition1(A, p, r):
    j = r + 1
    i = p - 1
    mid = int((p + r)/2)
    x = A[mid]
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
        
def quicksort(A, p, r):
    if p < r:
        q = partition1(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)

test = [5,4,3,5,4,2,1]
quicksort(test, 0, len(test) - 1)
print(test)