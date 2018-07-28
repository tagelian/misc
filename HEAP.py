# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 19:02:51 2018
# start at 08:00 
# done at 10:43 20180726 Thursday 
@author: lenovo
"""
import math
class HEAP:
    def __init__(self, nums):
        self.length = len(nums)
        self.heap_size = 0
        self.A = nums
    def left(self,i):
        return 2 * i + 1
    def right(self,i):
        return 2 * i + 2
    def parent(self,i):
        return math.ceil(i / 2 - 1)
    def HEAP_MAXIFY(self, i):
        l = self.left(i)
        r = self.right(i)
        if l < self.heap_size and self.A[l] > self.A[i]:
            largest = l
        else:
            largest = i
        if r < self.heap_size and self.A[r] > self.A[largest]:
            largest = r
        while largest != i:
            temp = self.A[largest]
            self.A[largest] = self.A[i]
            self.A[i] = temp
            
            i = largest
            l = self.left(i)
            r = self.right(i)
            if l < self.heap_size and self.A[l] > self.A[i]:
                largest = l
            else:
                largest = i
            if r < self.heap_size and self.A[r] > self.A[largest]:
                largest = r
    def HEAP_MINIFY(self, i):
        l = self.left(i)
        r = self.right(i)
        if l < self.heap_size and self.A[l] < self.A[i]:
            smallest = l
        else:
            smallest = i
        if r < self.heap_size and self.A[r] < self.A[smallest]:
            smallest = r
        while smallest != i:
            temp = self.A[smallest]
            self.A[smallest] = self.A[i]
            self.A[i] = temp
            
            i = smallest
            l = self.left(i)
            r = self.right(i)
            if l < self.heap_size and self.A[l] < self.A[i]:
                smallest = l
            else:
                smallest = i
            if r < self.heap_size and self.A[r] < self.A[smallest]:
                smallest = r
    
    def BUILD_MAX_HEAP(self):
        self.heap_size = self.length
        for i in range(math.floor(self.length / 2) - 1, -1, -1):
            self.HEAP_MAXIFY( i)
    def BUILD_MAX_HEAP1(self):
        self.heap_size = 1
        for i in range(1, self.length):
            self.MAX_HEAP_INSERT(self.A[i])
    def BUILD_MIN_HEAP(self):
        self.heap_size = self.length
        for i in range(math.floor(self.length / 2) - 1, -1, -1):
            self.HEAP_MINIFY( i)
    def PRINT_HEAP(self):
        print(self.A[:self.heap_size])
    def HEAPSORT(self):
        self.BUILD_MAX_HEAP()
        for i in range(self.length - 1, 0, -1):
            self.A[0], self.A[i] = self.A[i], self.A[0]
            self.heap_size -= 1
            self.HEAP_MAXIFY(0)
    def HEAP_MAXIMUM(self):
        '''
        caution: whenever call this procedure, make sure that first execute
        the build-heap procedure explicitly
        '''
        return self.A[0]
    def HEAP_EXTRACT_MAX(self):
        '''
        caution: whenever call this procedure, make sure that first execute
        the build-heap procedure explicitly
        '''
        if self.isEmpty():
            print('heap is going to be underflow.exit.')
            return
        max = self.A[0]
        self.A[0] = self.A[self.heap_size - 1]
        self.heap_size -= 1
        self.HEAP_MAXIFY(0)
        return max
    def HEAP_INCREASE_KEY(self, i, k):
        ''' 
        here to assume that k > self.A[i]
        '''
        if k <= self.A[i]:
            print("please make sure that k larger than orignal key value.exit.")
            return
        self.A[i] = k
        while i > 0 and k > self.A[self.parent(i)]:
            self.A[i], self.A[self.parent(i)] =  self.A[self.parent(i)], self.A[i]
            i = self.parent(i)
    def MAX_HEAP_INSERT(self,k):
        if self.heap_size == self.length:
            print("heap is going to be overflow, exit.")
            return
        self.heap_size += 1
        self.A[self.heap_size - 1] = -99999
        self.HEAP_INCREASE_KEY(self.heap_size - 1, k )
    def MAX_HEAP_DELETE(self, i):
        '''
        restricted delete operation 09:23
        '''
        if self.isEmpty():
            print('heap is going to be underflow.exit.')
            return
        l = self.left(i)        
        r = self.right(i)
        self.A[i] = -99999
        if l < self.heap_size and self.A[l] > self.A[i]:
            largest = l
        else:
            largest = i
        if r < self.heap_size and self.A[r] > self.A[largest]:
            largest = r
        while largest != i:
            self.A[i], self.A[largest] = self.A[largest], self.A[i]
            i = largest
            l = self.left(i)        
            r = self.right(i)
            if l < self.heap_size and self.A[l] > self.A[i]:
                largest = l
            else:
                largest = i
            if r < self.heap_size and self.A[r] > self.A[largest]:
                largest = r            
        self.heap_size -= 1
    def MAX_HEAP_MERGE(self, B):
        '''
        b = 0
        for w in B:
            b += len(B)
        self.length = b
        caution: use former code to preprocess before init heap H!
        '''
        # done for merge k sorted arrays into a sorted combined array 10:45
        
        for i in range(len(B)):
            self.MAX_HEAP_INSERT(B[i][-1])
        for j in range(self.length - 1, 0, -1):
            self.A[j] = self.HEAP_EXTRACT_MAX()
            for m in B:
                for n in range(len(m)-2, -1, -1):
                    self.MAX_HEAP_INSERT(m[n])
                    del m[n]
                    
            
            
        
            
        
    def isEmpty(self):
        return self.heap_size == 0
    
#------------------------------------------------------------------------------
B = [[2,2],
     [3,4,5]
     ]
b = 0
for w in B:
    b += len(w)
test = [0] * b
H = HEAP(test)
H.MAX_HEAP_MERGE(B)
# =============================================================================
# H.BUILD_MAX_HEAP()
# H.PRINT_HEAP()
# H.BUILD_MAX_HEAP1()
# H.PRINT_HEAP()
# =============================================================================

print(H.A)

# =============================================================================
# H.HEAP_EXTRACT_MAX()
# H.PRINT_HEAP()
# H.MAX_HEAP_INSERT(10)
# H.PRINT_HEAP()
# H.MAX_HEAP_DELETE(0)
# H.PRINT_HEAP()
# H.MAX_HEAP_DELETE(2)
# H.PRINT_HEAP()
# =============================================================================
# =============================================================================
# H.BUILD_MAX_HEAP()
# 
# H.HEAP_EXTRACT_MAX()
# print(H.heap_size)
# =============================================================================
# =============================================================================
# H.HEAPSORT()
# H.HEAPSORT()
# print(test)
# H.PRINT_HEAP()
# =============================================================================

        
    
        