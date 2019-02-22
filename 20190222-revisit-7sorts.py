# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 13:23:58 2019

@author: lenovo
"""
#done for 7sorts 20190222 14:25
#1. insert_sort
#2. bubble_sort
#3. selection_sort
#4. shell_sort
#5. merge_sort
#6. heap_sort
#7. quick_sort
import copy
class SORT:
    def __init__(self, nums):
        self.nums = copy.deepcopy(nums)
        self.heapsize = len(nums)
    def insert_sort(self):
        a = copy.deepcopy(self.nums)
        for i in range(1, len(a)):
            j = i - 1
            temp = a[i]
            while j >= 0 and temp < a[j]:
                a[j+1] = a[j]
                j -= 1
            a[j+1] = temp
        return a
    def bubble_sort(self):
        a = copy.deepcopy(self.nums)
        for i in reversed(range(1,len(a))):
            for j in range(i):
                if a[j] > a[j+1]:
                    a[j], a[j+1] = a[j+1], a[j]
        return a
    def selection_sort(self):
        a = copy.deepcopy(self.nums)
        for i in range(len(a)-1):
            index = i
            for j in range(i+1,len(a)):
                if a[index] > a[j]:
                    index = j
            if index != i:
                a[i], a[index] = a[index], a[i]
        return a
    def shell_sort(self):
        a = copy.deepcopy(self.nums)
        gap = (len(a)+1) // 2
        while gap >= 1:
            for i in range(gap):
                for j in range(i+gap, len(a), gap):
                    temp = a[j]
                    k = j - gap
                    while k >= i and temp < a[k]:
                        a[k+gap] = a[k]
                        k -= gap
                    a[k+gap] = temp
            gap //= 2
        return a
    def merge_sort(self, nums):
        if len(nums) <= 1:
            return nums
        mid = (len(nums)+1) // 2
        a1 = self.merge_sort(nums[:mid])
        a2 = self.merge_sort(nums[mid:])
        n = len(nums)
        pivot = float('inf')
        a1.append(pivot)
        a2.append(pivot)
        a=[]
        i = j = 0
        for k in range(n):
            if a1[i] < a2[j]:
                a.append(a1[i])
                i += 1
            else:
                a.append(a2[j])
                j += 1
        return a
    def heap_sort(self):
        self.build_heap()
        for i in reversed(range(1, len(self.nums))):
            self.nums[i], self.nums[0] = self.nums[0], self.nums[i]
            self.heapsize -= 1
            self.maxify(0)
        return self.nums
    def maxify(self, i):
        l = 2 * i + 1
        r = 2 * i + 2
        large = i
        if l < self.heapsize and self.nums[large] < self.nums[l]:
            large = l
        if r < self.heapsize and self.nums[large] < self.nums[r]:
            large = r
        if large != i:
            self.nums[large], self.nums[i] = self.nums[i], self.nums[large]
            self.maxify(large)
    def build_heap(self):
        self.heapsize = len(self.nums)
        for i in reversed(range(len(self.nums)//2)):
            self.maxify(i)
    def quick_sort(self,a,p,r):
        if p < r:
            q = self.partition(a,p,r)
            self.quick_sort(a,p,q-1)
            self.quick_sort(a,q+1,r)
    def partition(self, a,p,r):
        i = p - 1
        x = a[r]
        for j in range(p,r):
            if a[j] <= x:
                i += 1
                a[i], a[j] = a[j], a[i]
        a[i+1], a[r] = a[r], a[i+1]
        return i + 1
    def checker(self, a):
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                return False
        return True
import numpy as np
a = list(map(int, np.random.rand(8)*100))
obj = SORT(a)
a1 = obj.insert_sort()
print(obj.checker(a1))
a2 = obj.bubble_sort()
print(obj.checker(a2))
a3 = obj.selection_sort()
print(obj.checker(a3))
a4 = obj.shell_sort()
print(obj.checker(a4))
a55 = copy.deepcopy(a)
a5 = obj.merge_sort(a55)
print(obj.checker(a5))
a6 = obj.heap_sort()
print(obj.checker(a6))
a7 = copy.deepcopy(a)
obj.quick_sort(a7,0,len(a7)-1)
print(obj.checker(a7))