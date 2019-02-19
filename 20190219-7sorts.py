# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 11:51:51 2019
@author: lenovo
"""
import numpy as np
import copy
class Sort:
# =============================================================================
#     a1. insert_sort()
#     a2. bubble_sort()
#     a3. selection_sort()
#     a4. shell_sort()
#     a5. merge_sort()
#     a6. heap_sort()
#     a7. quick_sort()
# =============================================================================
    def __init__(self, nums):
        self.nums = nums
        self.heap_size = len(nums)
    def checker(self,a):
        if not a:
            return True
        for i in range(len(self.nums)-1):
            if a[i] > a[i+1]:
                return False
        return True
    def insert_sort(self)->'list[int]':
        a = copy.deepcopy(self.nums)
        for i in range(1, len(a)):
            temp = a[i]
# =============================================================================
#            有时候这种情况时不允许的，我尽可能有while
#             而不是 ranged-based for 切记切记
#             for j in reversed(range(i)):
#                 if temp < a[j]:
#                     a[j+1] = a[j]
#                 else:
#                     break
# =============================================================================
            j = i - 1
            while j >= 0 and temp < a[j]:
                a[j+1] = a[j]
                j -= 1
            a[j+1] = temp
        return a
    def bubble_sort(self):
        a = copy.deepcopy(self.nums)
        for i in reversed(range(len(a))):
            for j in range(i):
                if a[j] > a[j+1]:
                    a[j], a[j+1] = a[j+1], a[j]
        return a
    def selection_sort(self):
        a = copy.deepcopy(self.nums)
        for i in range(len(a)-1):
            index = i
            for j in range(i+1, len(a)):
                if a[j] < a[index]:
                    index = j
            a[index], a[i] = a[i], a[index]
        return a
    def shell_sort(self):
        a = copy.deepcopy(self.nums)
        gap = (len(a) + 1 )//2
        while gap > 1:
            for i in range(gap):
                for j in range(i+gap,len(a),gap):
                    temp = a[j]
                    k = j - gap
                    while k >= i and temp < a[k]:
                        a[k+gap] = a[k]
                        k -= gap
                    a[k+gap] = temp
            gap //= 2
        return a
    def merge_sort(self,nums):
        # 这里有一个 循环 终止条件  一定要定位到 空  或者 一个
        if len(nums) <=1:
            return nums
        left = 0
        right = len(nums)-1
        mid = (left + right) // 2
        a1 = self.merge_sort(nums[left:mid+1])
        a2 = self.merge_sort(nums[mid+1:right+1])
        a = []
        i =j = 0
        a1.append(float('inf'))
        a2.append(float('inf'))
        for k in range(len(a1)+len(a2)-2):
            if a1[i] < a2[j]:
                a.append(a1[i])
                i += 1
            else:
                a.append(a2[j])
                j += 1
        return a
    def heap_sort(self, nums):
        self.build_heap(nums)
        for i in range(len(nums)-1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.heap_size -= 1
            self.maxify(nums,0)
    def maxify(self, nums, i):
        l = i * 2 + 1
        r = i * 2 + 2
        largest = i
        if l < self.heap_size and nums[largest] < nums[l]:
            largest = l
        if r < self.heap_size and nums[largest] < nums[r]:
            largest = r
        if largest != i:
            nums[largest], nums[i] = nums[i], nums[largest]
            self.maxify(nums, largest)
    def build_heap(self, nums):
        self.heap_size = len(nums)
        for i in range(len(nums)//2-1, -1, -1):
            self.maxify(nums, i)
    def quick_sort(self, nums, p, r):
        if p < r:
            q = self.partition(nums, p, r)
            self.quick_sort(nums,p,q-1)
            self.quick_sort(nums,q+1, r)
    def partition(self,nums,p,r):
        x = nums[r]
        i = p -1
        for j in range(p,r):
            if nums[j] <= x:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i+1], nums[r] = nums[r], nums[i+1]
        return i + 1
            
nums = list(map(int, np.random.rand(9)*100))
obj = Sort(nums)
a1 = obj.insert_sort()
print(obj.checker(a1))
a2 = obj.bubble_sort()
print(obj.checker(a2))
a3 = obj.bubble_sort()
print(obj.checker(a3))
a4 = obj.selection_sort()
print(obj.checker(a4))
a5 = obj.merge_sort(nums)
print(obj.checker(a5))
a6 = copy.deepcopy(nums)
obj.heap_sort(a6)
print(obj.checker(a6))
a7 = copy.deepcopy(nums)
obj.quick_sort(a7,0,len(a7)-1)
print(obj.checker(a7))