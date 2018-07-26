# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 07:24:40 2018

@author: lenovo
"""

def partition(A,p,r):
    '''
    这里我这个temp用的就很灵性了
    A[i + 1 -temp, i + 1]共计temp + 1个和主元相同的元素
    A[p, i - temp]严格小于主元
    A[i + 2, r]严格大于主元
    beautiful
    '''
    x = A[r]
    i = p - 1
    temp = 0
    for j in range(p, r):
        if A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i]
        if A[j] == x:
            temp += 1
            i += 1
            A[i], A[j] = A[j], A[i]
            
            
    A[r] = A[i + 1]
    A[i + 1] = x
    return [i + 1 - temp, i + 1]
def QuickSort(A,p,r):
    while p < r:
        q,t = partition(A,p,r)
        QuickSort(A,p,q - 1)
        p = t + 1
test = [1,2,3,3,2,2,1,5,5,5]
#a=partition(test,0,len(test)-1)
QuickSort(test,0,len(test)-1)
print(test)