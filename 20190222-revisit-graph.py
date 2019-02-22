# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 14:26:31 2019

@author: lenovo
"""

# comprehensive graph algorithms
import collections
import heapq

class Vertex:
    def __init__(self, val):
        self.pivot = float('inf')
        self.val = val
        self.color = 0
        self.pre = None
        self.d = self.pivot
        self.key = self.pivot
        self.s = self.pivot
        self.f = self.pivot
class GRAPH:
    def __init__(self, vs, es, flag = 1):
        self.flag = flag
        self.time = float('inf')
        self.G = collections.defaultdict(list)        
        self.vs = vs
        self.es = es
        self.ha_v = collections.defaultdict(Vertex) 
        self.ha_w = collections.defaultdict(float)
    def build(self):
        for v in self.vs:
            self.ha_v[v] = Vertex(v)
            self.G[v] = []
        if self.flag:
            for u,v,w in self.es:
                self.G[u].append(v)
                self.ha_w[(u,v)] = w
        else:
            for u,v,w in self.es:
                self.G[u].append(v)
                self.G[v].append(u)
                self.ha_w[(u,v)] = w
                self.ha_w[(v,u)] = w
    def BFS(self, r):
        for v in self.ha_v.values():
            v.color = 0
            v.d = float('inf')
            v.pre = None
        self.ha_v[r].color = 1
        self.ha_v[r].d = 0
        queue = collections.deque([r])
        while queue:
            u = queue.popleft()
            for v in self.G[u]:
                if self.ha_v[v].color == 0:
                    self.ha_v[v].pre = self.ha_v[u]
                    self.ha_v[v].color = 1
                    self.ha_v[v].d = self.ha_v[u].d + 1
                    queue.append(v)
    def print_BFS(self, r):
        for v in self.vs:
            print('\nthe path from ' + r + ' to ' + v + ' is:')
            self.print_helper(r,v)
    def print_helper(self, r, v):
        stack = [(v,0)]
        while stack:
            u, flag = stack.pop()
            if flag:
                print(u, end = ' ')
                continue
            if u == r:
                stack.append((u,1))
            elif not self.ha_v[u].pre:
                print('no path to '+u)
            else:
                stack.append((u,1))
                stack.append((self.ha_v[u].pre.val, 0))
    def DFS(self):
        for v in self.ha_v.values():
            v.color = 0
            v.pre = None
        self.time = 0
        for v in self.vs:
            if self.ha_v[v].color == 0:
                self.DFS_visit(v)
    def DFS_visit(self, u):
        self.ha_v[u].color = 1
        self.time += 1
        self.ha_v[u].s = self.time
        for v in self.G[u]:
            if self.ha_v[v].color == 0:
                self.ha_v[v].pre = self.ha_v[u]
                self.DFS_visit(v)
        self.ha_v[u].color = 2
        self.time += 1
        self.ha_v[u].f = self.time
# =============================================================================
#         if v == r:
#             print(v, end = ' ')
#         elif not self.ha_v[v].pre:
#             print('no path to ' + v)
#         else:
#             self.print_helper(r, self.ha_v[v].pre.val)
#             print(v, end = ' ')
# =============================================================================
# =============================================================================
# vs = ['a', 'b', 'c', 'd', 'e']        
# es = [
#       ['a', 'b', 1],
#       ['a', 'c', 1],
#       ['b', 'd', 1],
#       ['c', 'd', 1],
#       ['b', 'e', 1],
#       
#       ]
# obj1 = GRAPH(vs,es,0)
# obj1.build()
# obj1.BFS('a')
# obj1.print_BFS('a')
# =============================================================================
#for v in obj1.ha_v.values():
#    print(v.d)
#print(obj1.G, obj1.vs)
# =============================================================================
# vs = ['a', 'b']
# es = [['a','b']]
# obj = GRAPH(vs, es)
# obj.build()
#     
# =============================================================================