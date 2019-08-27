# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 18:26:10 2019

@author: lenovo
"""

class QUEUE:
    def __init__(self, nums):
        self.nums = nums
        self.heap_size = len(nums)
    def maxify(self, i):
        l = 2*i+1
        r = 2*i+2
        big = i
        if l <self.heap_size and self.nums[big] < self.nums[l]:
            big = l
        if r <self.heap_size and self.nums[big] < self.nums[r]:
            big = r
        if big != i:
            self.nums[big], self.nums[i] = self.nums[i], self.nums[big]
            self.maxify(big)
    def build_heap(self):
        self.heap_size = len(self.nums)
        for i in reversed(range(len(self.nums)//2)):
            self.maxify(i)
    def maximum(self):
        return self.nums[0]
    def extract_maximum(self):
        x = self.nums[0]
        self.nums[0], self.nums[-1] = self.nums[-1],self.nums[0]
        self.heap_size -= 1
        self.maxify(0)
        return x
    def incre_key(self,i, key):
        if key <= self.nums[i]:
            print('key no larger than nums[i]')
        else:
            k = i
            j = (i - 1) // 2
            self.nums[i] = key
            while j >= 0 and key > self.nums[j]:
                self.nums[k] = self.nums[j]
                k = j
                j = (k-1) // 2
            self.nums[k] = key
    def insert(self, key):
        self.nums.append(float('-inf'))
        self.heap_size += 1
        self.incre_key(self.heap_size-1,key)
#import numpy as np
a = [2,1,3,4.1,-1,10]
obj = QUEUE(a)
obj.build_heap()
print(obj.maximum())
obj.insert(100)
print(obj.maximum())
print(obj.extract_maximum(), obj.maximum())


        
            
        