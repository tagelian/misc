# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 18:52:23 2019

@author: lenovo
"""
# done for union-find 20190222 19:11
class UNION_FIND:
    def __init__(self):
        self.p = {}
    def make_set(self, nums):
        for i in nums:
            self.p[i] = [i,0]
    def find_set(self, x):
        if x != self.p[x][0]:
            self.p[x][0] = self.find_set(self.p[x][0])
        return self.p[x][0]
    def union_set(self,a,b):
        x = self.find_set(a)
        y = self.find_set(b)
        if self.p[x][1] > self.p[y][1]:
            self.p[y][0] = x
        else:
            self.p[x][0] = y
            if self.p[x][1] == self.p[y][1]:
                self.p[y][1] += 1
obj = UNION_FIND()
a = [1,2,3,4]
obj.make_set(a)
obj.union_set(1,2)
obj.union_set(3,4)
print(obj.find_set(1) == obj.find_set(2), obj.find_set(1), obj.find_set(3), )