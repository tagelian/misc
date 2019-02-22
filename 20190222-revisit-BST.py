# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 10:20:08 2019

@author: lenovo
"""
#done for BST 20190222 13:23
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.p = None
        self.left = None
        self.right = None
class BST:
    def __init__(self, root = None):
        self.root = root
    def traversal_iter(self):
        if self.root:
            stack = [(self.root, 0)]
            while stack:
                u,flag = stack.pop()
                if flag:
                    print(u.val, end = ' ')
                    continue
                if u.right:
                    stack.append((u.right, 0))
                stack.append((u, 1))
                if u.left:
                    stack.append((u.left, 0))
    def traversal_recursion(self, root):
        if root:
            self.traversal_recursion(root.left)
            print(root.val, end = ' ')
            self.traversal_recursion(root.right)
    def minimum(self, u):
        if not u:
            return None
        else:
            while u.left:
                u = u.left
            return u
    def maximum(self, u):
        if not u:
            return None
        else:
            while u.right:
                u = u.right
            return u
    def precessor(self, u):
        if u.left:
            return self.maximum(u.left)
        else:
            y = u.p
            while y and y.left == u:
                u = y
                y = y.p
            return y
    def successor(self, u):
        if u.right:
            return self.minimum(u.right)
        else:
            y = u.p
            while y and y.right == u:
                u = y
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
        else:
            if z.val < y.val:
                y.left = z
            else:
                y.right = z
    def transplant(self, u,v):
        if not u.p:
            self.root = v
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
            self.transplant(z, z.left)
        else:
            y = self.successor(z)
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
a.right = b
c.left, c.right = a, d
b.p = a
a.p = c
d.p = c
obj = BST(c)
obj.traversal_iter()
#obj.traversal_recursion(c)
z = TreeNode(3.3)
obj.insert(z)
print('')
obj.traversal_iter()
obj.delete(c)
print('')
obj.traversal_iter()