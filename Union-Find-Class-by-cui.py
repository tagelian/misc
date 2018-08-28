# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 14:56:39 2018

@author: cui
"""

import  collections as cui
class UF:
    def __init__(self,vertexs):
        
        self.parent = cui.defaultdict(int)
        self.rank = cui.defaultdict(int)
        for vertex in vertexs:
            self.parent[vertex] = vertex
            self.rank[vertex] = 1
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        xx, yy = self.find(x), self.find(y)
        if self.rank[xx] > self.rank[yy]:
            self.parent[yy] = self.parent[xx]
        else:
            self.parent[xx] = self.parent[yy]
            if self.rank[xx] == self.rank[yy]:
                self.rank[yy] += 1
#----------------------------------------test code is below
test = [1,2,3,4]
uf = UF(test)
print(uf.rank.values())
uf.union(2,3)
print(uf.rank.values())
uf.union(2,3)
print(uf.rank.values())
uf.union(2,2)
print(len(set(uf.parent.values())))
