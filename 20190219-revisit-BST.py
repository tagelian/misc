# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 22:10:52 2019

@author: lenovo
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.p = None
        self.left = None
        self.right = None
class BST:
    def __init__(self, root = None):
        self.root = root
    def traversal(self):
        stack = [(self.root,0)]
        while stack:
            p, flag = stack.pop()
            if flag:
                print(p.val,end=' ')
                continue
            if p:
                if p.right:
                    stack.append((p.right,0))
                stack.append((p,1))
                if p.left:
                    stack.append((p.left,0))
    def minimum(self, x:'TreeNode')->'TreeNode':
        if not x:
            return x
        while x.left:
            x = x.left
        return x
    def maximum(self, x:'TreeNoded')->'TreeNode':
        if not x:
            return x
        while x.right:
            x = x.right
        return x
    def precessor(self, x):
        if x.left:
            return self.maximum(x.left)
        else:
            y = x.p
            while y and y.left == x:
                x = y
                y = y.p
            return y
    def successor(self, x):
        if x.right:
            return self.minimum(x.right)
        else:
            y = x.p
            while y and y.right == x:
                x = y
                y = y.p
            return y
    def insert(self, z):
        y = None
        x = self.root
        while x:
            y = x
            if z.val < x.val:
                x = x.left
            else:
                x = x.right
        z.p = y
        if not y:
            self.root = z
        elif z.val < y.val:
            y.left = z
        else:
            y.right = z
    def transplant(self, u, v):
        if not u.p:
            self.root=v
        elif u.p.left == u:
            u.p.left = v
        else:
            u.p.right = v
        if v:
            v.p = u.p
    def delete(self, z):
        if not z.left:
            self.transplant(z,z.right)
        elif not z.right:
            self.transplant(z,z.left)
        else:
            y = self.minimum(z.right)
            if z.right != y:
                self.transplant(y,y.right)
                y.right = z.right
                y.right.p = y
            self.transplant(z,y)
            y.left = z.left
            y.left.p = y
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
c.left, c.right = a, d
a.right = b
a.p = c
d.p = c
b.p = a
obj = BST(c)
obj.traversal()
z = TreeNode(3.3)
obj.insert(z)
print('')
obj.traversal()
obj.delete(c)
print('')
obj.traversal()