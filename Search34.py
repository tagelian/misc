# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 15:28:30 2018

@author: lenovo
"""

def Search34(A, target):
    left = 0
    right = len(A) - 1
    while left <= right:
        if target < A[0] or target > A[right]:
            return -1
        mid = int((left + right) / 2)
        if A[mid] == target:
            return mid
        if A[left] <= target <= A[mid]:
            right = mid -1
        else:
            left = mid + 1
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
def fun1(A, pos):
    if pos == -1:
        return [-1, -1]
    i = pos + 1
    if A[len(A) - 1] == A[pos]:
        end = len(A) - 1
    while i < len(A) and A[i] == A[pos] :
        i += 1
    if i == pos + 1:
        end = pos
    if i != len(A):
        end = i - 1
    j = pos - 1
    if A[0] == A[pos]:
        start = 0
    while j > -1 and A[j] == A[pos]:
        j -= 1

    if j != -1:
        start = j + 1
    if j == pos - 1:
        start = pos
    return [start, end]
#------------------------------------------------------------------------------
testList = [1,2,2,3,3,3,3,3,4,5]
pos = Search34(testList,5)
print(pos)
final = fun1(testList, pos)
print(final)