# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 08:09:46 2018

@author: lenovo
"""

import random
# created by cui 08:10 20180710 Tuesday
# finished by cui 09:02 20180710 Tuesday
#------------------------------------------------------------------------------
def BubbleSort(A):
    for i in range(len(A) - 1, 0, -1):
        for j in range(i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
#------------------------------------------------------------------------------
def SelectionSort(A):
    for i in range(len(A) - 1):
        for j in range(i + 1, len(A)):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]
#------------------------------------------------------------------------------
def InsertSort(A):
    for i in range(1, len(A)):
        j = i - 1
        temp = A[i]
        while j >= 0 and temp < A[j]:
            A[j], A[j + 1] = A[j + 1], A[j]
            j -= 1
        A[j + 1] = temp
#------------------------------------------------------------------------------
def ShellSort(A):
    incre = int(len(A) / 2)
    while incre > 0:
        for k in range(incre):
            for i in range(k + incre, len(A), incre):
                temp = A[i]
                j = i - incre
                while j >= k and temp < A[j]:
                    A[j], A[j + incre] = A[j + incre], A[j]
                    j -= incre
                A[j + incre] = temp
        incre = int(incre / 2)
#------------------------------------------------------------------------------
def merge(A, p, q, r):
    diff = 99999
    L = []
    R = []
    for i in range(p, q + 1):
        L.append(A[i])
    L.append(diff)
    for j in range(q + 1, r + 1):
        R.append(A[j])
    R.append(diff)
    i = 0
    j = 0
    for k in range(p, r + 1):
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
def MergeSort(A, p, r):
    if p < r:
        q = int((p + r) / 2)
        MergeSort(A, p, q)
        MergeSort(A, q + 1, r)
        merge(A, p, q, r)
#------------------------------------------------------------------------------
def maxify(A, i, size):
    l = 2 * i + 1
    r = 2 * i + 2
    if l < size and A[i] < A[l]:
        largest = l
    else:
        largest = i
    if r < size and A[largest] < A[r]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        maxify(A, largest, size)
def HeapSort(A):
    size = len(A)
    for i in range(int(size / 2) - 1, -1, -1):
        maxify(A, i, size)
    for j in range(size - 1, 0, -1):
        A[j], A[0] = A[0], A[j]
        size -= 1
        maxify(A, 0, size)
#------------------------------------------------------------------------------
def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[r] = A[i + 1]
    A[i + 1] = x
    return i + 1
def QuickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        QuickSort(A, p, q - 1)
        QuickSort(A, q + 1, r)
#------------------------------------------------------------------------------
TestNums = 10000
TestList = [random.randint(0, 10000) for i in range(TestNums)]
#BubbleSort(TestList)
#SelectionSort(TestList)
#InsertSort(TestList)
#ShellSort(TestList)
#MergeSort(TestList, 0, TestNums - 1)
#HeapSort(TestList)
#QuickSort(TestList, 0, TestNums - 1)
