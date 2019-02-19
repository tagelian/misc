# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 21:06:22 2019

@author: lenovo
"""
import copy
import numpy as np
class Sort:
    def __init__(self, A):
        self.A = copy.deepcopy(A)
        self.heap_size = len(A)
    def insert_sort(self):
        A = copy.deepcopy(self.A)
        for i in range(1, len(A)):
            j = i - 1
            temp = A[i]
            while j >= 0 and temp < A[j]:
                A[j+1] = A[j]
                j -= 1
            A[j+1] = temp
        return A
    def bubble_sort(self):
        A = copy.deepcopy(self.A)
        for i in reversed(range(1,len(A))):
            for j in range(i):
                if A[j] > A[j+1]:
                    A[j], A[j+1] = A[j+1], A[j]
        return A
    def selection_sort(self):
        A = copy.deepcopy(self.A)
        for i in range(len(A)-1):
            index = i
            for j in range(i+1, len(A)):
                if A[index] > A[j]:
                    index = j
            A[index], A[i] = A[i], A[index]
        return A
    def shell_sort(self):
        A = copy.deepcopy(self.A)
        gap = (len(A) + 1) // 2
        while gap >= 1:
            for i in range(gap):
                for j in range(i+gap, len(A), gap):
                    k = j - gap
                    temp = A[j]
                    while k >= i and temp < A[k]:
                        A[k+gap] = A[k]
                        k -= gap
                    A[k+gap] = temp
            gap = gap // 2
        return A
    def merge_sort(self, A):
        if len(A) <= 1:
            return A
        mid = (len(A) - 1) // 2
        a1 = self.merge_sort(A[:mid+1])
        a2 = self.merge_sort(A[mid+1:])
        pivot = float('inf')
        a1.append(pivot)
        a2.append(pivot)
        a = []
        i=j=0
        for k in range(len(a1)+len(a2)-2):
            if a1[i] < a2[j]:
                a.append(a1[i])
                i += 1
            else:
                a.append(a2[j])
                j += 1
        return a
    def heap_sort(self):
        self.build_heap()
        for i in reversed(range(1,len(self.A))):
            self.A[i], self.A[0] = self.A[0], self.A[i]
            self.heap_size -= 1
            self.maxify(0)
        return self.A
    def maxify(self, i):
        l = 2 * i + 1 
        r = 2 * i + 2
        largest = i
        if l < self.heap_size and self.A[largest] < self.A[l] :
            largest = l
        if r < self.heap_size and self.A[largest] < self.A[r]:
            largest = r
        if largest != i:
            self.A[largest], self.A[i] = self.A[i], self.A[largest]
            self.maxify(largest)
    def build_heap(self):
        self.heap_size = len(self.A)
        for i in reversed(range(len(self.A)//2)):
            self.maxify(i)
    def quick_sort(self, A, p, r):
        if p < r:
            q = self.partition(A, p ,r)
            self.quick_sort(A,p,q-1)
            self.quick_sort(A,q+1,r)
    def partition(self, A, p, r):
        x = A[r]
        i = p - 1
        for j in range(p,r):
            if A[j] <= x:
                i += 1
                A[i], A[j] = A[j], A[i]
        A[r],A[i+1] = A[i+1], A[r]
        return i + 1
    def checker(self, a):
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                return False
        return True
nums = list(map(int,np.random.rand(8)*100))
obj = Sort(nums)
a1 = obj.insert_sort()
print(obj.checker(a1))
a2 = obj.bubble_sort()
print(obj.checker(a2))
a3 = obj.selection_sort()
print(obj.checker(a3))
a4 = obj.shell_sort()
print(obj.checker(a4))
a55 = copy.deepcopy(nums)
a5 = obj.merge_sort(a55)
print(obj.checker(a5))
a6 = obj.heap_sort()
print(obj.checker(a6))
a7 = copy.deepcopy(nums)
obj.quick_sort(a7,0,len(a7)-1)
print(obj.checker(a7))