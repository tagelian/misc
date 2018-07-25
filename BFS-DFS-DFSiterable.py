# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 09:20:10 2018

@author: lenovo
"""
#------------------------------------------------------------------------------
class Node(object):
    def __init__(self, x = 'c'):
        """
        white: 0
        gray:  1
        black: 2
        """
        self.val = x
        self.color = 0
        self.d = 606
        self.f = 808
        self.pi = None
#        self.next = None

#------------------------------------------------------------------------------
class Stack:
    """
    默认数组容量为100
    """
    def __init__(self):
        self.length = 100
        self.top = -1
        self.A = [0] * self.length
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
    def push(self, x):
        if self.top == self.length - 1:
            print("stack is going to be overflow, forbid insert, exit.")
            return
        self.top += 1
        self.A[self.top] = x
    def pop(self):
        if self.top == -1:
            print("stack is going to be underflow, forbid delete, exit.")
            return
        self.top -= 1
        return self.A[self.top + 1]
#------------------------------------------------------------------------------
# 先 instance 化 才有 attribute， 我的妈呀 11:01 
# 记得加 () 调用方法、、、、、、、、、、111
# =============================================================================
# S = Stack()
# S.push(0)
# S.push(1)
# S.push(2)
# print(S.pop())
# print(S.pop())
# print(S.pop())
# print(S.pop())
# print(S.isEmpty())
# =============================================================================
class Queue:
    """
    100个数
    """
    def __init__(self):
        self.length = 100
        self.A = [Node()] * self.length
        self.head = 0
        self.tail = 0
    def EnQueue(self, x):
        self.A[self.tail] = x
        self.tail = (self.tail  + 1) % self.length
    def DeQueue(self):
        temp = self.A[self.head]
        self.head = (self.head + 1) % self.length
        return temp
    def isEmpty(self):
        return self.head == self.tail
#------------------------------------------------------------------------------
# =============================================================================
# Q = Queue()
# Q.EnQueue(1)
# Q.EnQueue(2)
# Q.EnQueue(3)
# print(Q.head, Q.tail)
# Q.DeQueue()
# print(Q.head, Q.tail)
# Q.DeQueue()
# print(Q.head, Q.tail)
# Q.DeQueue()
# print(Q.head, Q.tail)
# print(Q.isEmpty())
# =============================================================================
r = Node('r')
s = Node('s')
t = Node('t')
u = Node('u')
v = Node('v')
w = Node('w')
x = Node('x')
y = Node('y')

Adj = {r:[s,v],
       s:[w,r],
       t:[u,w,x],
       u:[x,y,t],
       v:[r],
       w:[x,s,t],
       x:[y,t,u,w],
       y:[u,x]
       }
#print(Adj[0][0].val)
# =============================================================================
# b = [r] * 3
# print(b[1].val)
# =============================================================================
time = 0
def DFSiter(Adj, u):
    S = Stack()
    S.push(u)
    global time
    while not S.isEmpty():
        uu = S.A[S.top]
        if uu.color == 1:
            uu.color = 2
            time += 1
            uu.f = time
            S.pop()
            continue
        if uu.color == 0:
            uu.color = 1
            time += 1
            uu.d = time
        if len(Adj[uu]) != 0:
            
            for v in Adj[uu]:
                if v.color == 0 and v not in S.A:
                
                    v.pi = uu
                    S.push(v)

    
#------------------------------------------------------------------------------
def DFSvisit(Adj, u):
    global time
    u.color = 1
    time += 1
    u.d = time
    for v in Adj[u]:
        if v.color == 0:
            v.pi = u
            DFSvisit(Adj, v)
    u.color = 2
    time += 1
    u.f = time
#------------------------------------------------------------------------------

def DFS(Adj):
    global time
    for u in Adj:
        if u.color == 0:
            DFSvisit(Adj, u)
#------------------------------------------------------------------------------            
#DFS(Adj) 
DFSiter(Adj, s)
print(s.d, s.f)
#------------------------------------------------------------------------------
    
    
#------------------------------------------------------------------------------
def BFS(Adj, s):
    s.color = 1
    s.d = 0
    s.pi = None
    Q = Queue()
    Q.EnQueue(s)
    while not Q.isEmpty():
        u = Q.DeQueue()
        for v in Adj[u]:
            if v.color == 0:
                v.color = 1
                v.d = u.d + 1
                v.pi = u
                Q.EnQueue(v)
        u.color = 2
#------------------------------------------------------------------------------
def printBFS(Adj, s, t):
    if s == t:
        print(s.val)
    else:
        printBFS(Adj, s, t.pi)
        print(t.val)
#------------------------------------------------------------------------------
# =============================================================================
# BFS(Adj, s)
# printBFS(Adj, s, v)
# =============================================================================
#------------------------------------------------------------------------------
# =============================================================================
# for i in [1]:
#     print('c')
# =============================================================================

    
    

        