# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 14:02:14 2018

@author: lenovo
"""
# start at 14:09
# paused at 15:30
# restart at 18:25
# stopped at 22:00 note that bellman-ford Dijkstra Floyd-Warshall not implement 20180731 Tuesday
#because i think know the reason is enough of course i cal implement them about 5 hours

import copy
#------------------------------------------------------------------------------
class Vertex:
    def __init__(self,key = 'c'):
        self.key = key
        self.pi = None
        self.d = 606
        self.f = 0
        self.color = 0
        
        
#------------------------------------------------------------------------------ 
class Queue:
    def __init__(self):
        self.length = 100
        self.A = [Vertex()] * self.length
        self.head = 0
        self.tail = 0
    def Enqueue(self,x):
        if (self.tail + 1) % self.length == self.head:
            print('queue is going to be overflow, exit.')
            return
        self.A[self.tail] = x
        self.tail = (self.tail + 1) % self.length
    def Dequeue(self):
        if self.head == self.tail:
            print('queue is going to be underflow, exit.')
            return
        x = self.A[self.head]
        self.head = (self.head + 1) % self.length
        return x
    def isEmpty(self):
        return self.head == self.tail
#------------------------------------------------------------------------------
        
        
#------------------------------------------------------------------------------
def Trans_List(G):
    '''
    caution: G must be directed graph representing with adjancy list
    '''
    GT = {}
    # initialize new adjancy list reprentation fo transpose of G
    for u in G:
        GT[u] = []
    
    for u in G:
        for v in G[u]:
            GT[v].append(u)
    return GT
#------------------------------------------------------------------------------
def Trans_Matrix(G):
    '''
    caution: G must be directed graph representing with adjancy matrix
    '''
    pass
#------------------------------------------------------------------------------
def BFS(Adj, s):
    '''
    caution: here Adj means the graph G
    color 0 : white
          1 : gray
          2 : black
          
    '''
    s.d = 0
    s.color = 1
    Q = Queue()
    Q.Enqueue(s)
    while not Q.isEmpty():
        u = Q.Dequeue()
        for v in Adj[u]:
            if v.color == 0:
                v.d = u.d + 1
                v.pi = u
                v.color = 1
                Q.Enqueue(v)
        u.color = 2
#------------------------------------------------------------------------------
time1 = 0
def DFS_visit(Adj, u):
#    nonlocal time1
    global time1
    u.color = 1
    time1 += 1
    u.d = time1
    for v in Adj[u]:
        if v.color == 0:
            v.pi = u
            DFS_visit(Adj,v)
    u.color = 2
    time1 += 1
    u.f = time1
#------------------------------------------------------------------------------    
    
#------------------------------------------------------------------------------
def DFS(Adj):
    global time1
    for u in Adj:
        if u.color == 0:
            DFS_visit(Adj, u)
#------------------------------------------------------------------------------
class HEAP:
    '''
    caution: here default we use min priority to support Prim's algorithm
    '''
    def __init__(self, nums, length = 10 ):
        self.length = length
        self.heapSize = self.length
        self.A = nums
    def left(self, i):
        return 2 * i + 1
    def right(self, i):
        return 2 * i + 2
    def parent(self, i):
        return int((i - 1) / 2)
    def minify(self, i):
        l = self.left(i)
        r = self.right(i)
        if l < self.heapSize and self.A[l].d < self.A[i].d:
            smallest = l
        else:
            smallest = i
        if r < self.heapSize and self.A[r].d < self.A[smallest].d:
            smallest = r
        
        if smallest != i:
            self.A[smallest], self.A[i] = self.A[i], self.A[smallest]
            self.minify(smallest)
    def build_heap(self):
        for j in range(int((self.heapSize - 1) / 2), -1, -1):
            self.minify(j)
    def isEmpty(self):
        return self.heapSize == 0
    def extract_min(self):
        if self.isEmpty():
            print('heap is empty, exit.')
            return
        x = self.A[0]
        self.A[0] = self.A[self.heapSize - 1]
        self.heapSize -= 1
        self.minify(0)
        return x
    def decrease_key(self,i,k):
        '''
        caution : here to assume that k is small than A[i]
        '''
        if k >= self.A[i].d:
            print('k should be smaller than A[i], exit.')
            return
        self.A[i].d = k
        p = self.parent(i)
        while p >= 0 and self.A[p].d > self.A[i].d:
            self.A[i], self.A[p] = self.A[p], self.A[i]
            i = p
            p = self.parent[i]
    def insert(self,x):
        if self.heapSize == self.length:
            print('priority is full, exit.')
            return
        Vinfi = copy.deepcopy(x)
        Vinfi.d = infi
        self.A[self.heapSize] = Vinfi
        self.heapSize += 1
        self.decrease_key(self.heapSize, x.d)
#------------------------------------------------------------------------------
# =============================================================================
# aa = Vertex('a')
# aa.d = 1
# bb = Vertex('b')
# bb.d = 2
# cc = Vertex('c')
# cc.d = 3
# dd = Vertex('d')
# dd.d = 4
# nums = [dd,bb,aa]
# H = HEAP(nums, len(nums))
# H.build_heap()
# print([x.d for x in H.A])
# =============================================================================
#H.insert(cc)
#print([x.d for x in H.A])
# =============================================================================
# print(H.extract_min().d)
# print([x.d for x in H.A[:H.heapSize]])
# print(H.extract_min().d)
# print([x.d for x in H.A[:H.heapSize]])
# print(H.extract_min().d)
# print([x.d for x in H.A[:H.heapSize]])
# print(H.extract_min().d)
# print([x.d for x in H.A[:H.heapSize]])
# =============================================================================
        
        
            
            
            
            
        
        
        
#------------------------------------------------------------------------------
def Prim(Adj, s, W, hash1):
    
    s.d = 0
    nums = [x for x in Adj]
    Q = HEAP(nums, len(nums))

    
    while not Q.isEmpty():
        u = Q.extract_min()
        u.color = 1
        for v in Adj[u]:
            if v.color == 0 and v.d > u.d + W[hash1[u]][hash1[v]]:
                v.d = u.d + W[hash1[u]][hash1[v]]
                v.pi = u
#------------------------------------------------------------------------------
            
        
        
#------------------------------------------------------------------------------
def Print(Adj,s,v):
    if s == v:
        print(s.key)
    elif v.pi == None:
        print('there is no path from s to v, exit.')
        return
    else:
        Print(Adj,s,v.pi)
        print(v.key)
#------------------------------------------------------------------------------
a = Vertex('a')
b = Vertex('b')
c = Vertex('c')
test = {a:[b,c],
        b:[c],
        c:[]}
#------------------------------------------------------------------------------
s = Vertex('s')
t = Vertex('t')
x = Vertex('x')
y = Vertex('y')
z = Vertex('z')

G = {s:[t,y],
     t:[x,y],
     x:[z],
     y:[t,x,z],
     z:[s,x]}

#------------------------------------------------------------------------------
a = Vertex('a')
b = Vertex('b')
c = Vertex('c')
d = Vertex('d')
e = Vertex('e')
f = Vertex('f')
g = Vertex('g')
h = Vertex('h')
i = Vertex('i')
infi = 91008017
UG = {a:[b,h],
      b:[c,h,a],
      c:[d,f,i,b],
      d:[e,f,c],
      e:[f,d],
      f:[g,c,d,e],
      g:[h,i,f],
      h:[i,a,b,g],
      i:[c,g,h]}
UW = [[0,4,infi,infi,infi,infi,infi,8,infi],
      [4,0,8,infi,infi,infi,infi,11,infi],
      [infi,8,0,7,infi,4,infi,infi,2],
      [infi,infi,7,0,9,14,infi,infi,infi],
      [infi,infi,infi,9,0,10,infi,infi,infi],
      [infi,infi,4,14,10,0,2,infi,infi],
      [infi,infi,infi,infi,infi,2,0,1,6],
      [8,11,infi,infi,infi,infi,1,0,7],
      [infi,infi,2,infi,infi,infi,6,7,0]]
# caution : W here is a matrix whose value W[][] is an edge-weight
hash2 = {a:0,
         b:1,
         c:2,
         d:3,
         e:4,
         f:5,
         g:6,
         h:7,
         i:8,
         }
hash1 = {    s:0,
             t:1,
             x:2,
             y:3,
             z:4}

W = [[0, 10, infi, 5, infi],
     [infi, 0, 1, 2, infi],
     [infi, infi, 0, infi, 4],
     [infi, 3, 9, 0, 2],
     [7, infi, 6, infi, 0]]
Prim(UG,a,UW,hash2)
#------------------------------------------------------------------------------
class NODE:
    def __init__(self,key):
        self.key = key
        self.p = None
        self.rank = 0
#------------------------------------------------------------------------------
def makeSet(x):
    t = NODE(x)
    t.p = t
    return t
# caution , the below parameter x, y are node, not Vertex.
def findSet(x):
    if x.p != x:
        x.p = findSet(x.p)
    return x.p
def Link(x,y):
    if x.rank > y.rank:
        y.p = x
    else:
        x.p = y
        if x.rank == y.rank:
            y.rank += 1
def Union(x,y):
    Link(findSet(x),findSet(y))    
#------------------------------------------------------------------------------
# =============================================================================
# setA = makeSet(a)
# setB =makeSet(b)
# #Union(setA,setB)
# print(findSet(setA) == findSet(setB))
# =============================================================================
class STACK:
    def __init__(self):
        self.size = 100
        self.top = 0
        self.A = [Vertex()] * self.size
    def push(self,x):
        if self.top >= self.size - 1:
            print('stack is goting to be overflow, exit.')
            return
        self.top += 1
        self.A[self.top] = x
        
    def pop(self):
        if self.top < 0:
            print('stack is going to be underflow, exit.')
            return
        x = self.A[self.top]
        self.top -= 1
        return x
    def isEmpty(self):
        return self.top < 0
#------------------------------------------------------------------------------
time2 = 0
def DFSiterable_visit(Adj, u):
    global time2
    S = STACK()
    u.d = 0
    S.push(u)
    while not S.isEmpty:
        u = S.A[S.top]
        if u.color == 0:
            u.color = 1
            time2 += 1
            u.d = time2
        if u.color == 1:
            
            u.color = 2
            time2 += 1
            u.f = time2
            S.pop()
            continue
        if len(Adj[u]):
            for v in Adj[u]:
                if v.color == 0 and v not in S.A:
                    v.pi = u
                    S.push(v)
            
            
def DFSiterable(Adj):
    global time2
    for u in Adj:
        if u.color == 0:
            DFSiterable_visit(Adj, u)
#------------------------------------------------------------------------------
DFSiterable(G)
for u in G:
    print(u.color, u.f)
            
        




















#------------------------------------------------------------------------------
#Print(UG,a,i)
# =============================================================================
# for x in UG[a]:
#     print(x.key)
# =============================================================================
#------------------------------------------------------------------------------
#DFS(G)
#print(s.d,t.d,x.d,y.d,z.d)
#print(W[hash1[s]][hash1[t]])


# =============================================================================
# BFS(test, a)
# print(a.d,b.d,c.d)
# =============================================================================
# =============================================================================
# test = Queue()
# test.Enqueue(Vertex('a'))
# res = test.Dequeue()
# print(res.color)
# print(test.isEmpty())
# =============================================================================
    
    
            
            
            
    
# =============================================================================
# test = {1:'a',
#         2:'b'}
# for t in test:
#     print(test[t])
# =============================================================================
# =============================================================================
# v = []   
# for i in v:
#     print(i)
#     
# =============================================================================
# =============================================================================
# a = {1:[2,3],
#      2:[3],
#      3:[]}
# b = Trans_List(a)
# print(b)
# =============================================================================
