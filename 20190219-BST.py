# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 18:09:49 2019

@author: lenovo
"""
# binary traversal minimum maximum precessor successor insert search delete 2019.02.19 20:56
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.p = None
        self.left = None
        self.right = None
class BST:
    def __init__(self, root= None):
        self.root = root
    def inorder_traversal(self):
        stack = [(self.root,0)]
        while stack:
            node, flag = stack.pop()
            if flag:
                print(node.val, end =' ')
                continue
            if node:
                if node.right:
                    stack.append((node.right, 0))                   
                stack.append((node, 1))
                if node.left:
                    stack.append((node.left,0))                      
    def minimum(self, root):
        if not root:
            return root
        while root.left:
            root = root.left
        return root
    def maximum(self, root):
        if not root:
            return root
        while root.right:
            root = root.right
        return root
    def successor(self, x):
        if x.right:
            return self.minimum(x.right)
        y = x.p
        while y and y.right == x:
            x = y
            y = y.p
        return y
    def precessor(self, x):
        if x.left:
            return self.maximum(x.left)
        y = x.p
        while y and y.left == x:
            x = y
            y = y.p
        return y
    def insert(self, z):
        x = self.root
        y = None
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
    def search(self,root,  node):
        while root and root.val != node.val:
            if node.val < root.val:
                root = root.left
            else:
                root = root.right
        return root
    def transplant(self, u, v):
        if u.p == None:
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
root = c
obj = BST(root)
obj.inorder_traversal()
z = TreeNode(3.3)
obj.insert(z)
print('')
obj.inorder_traversal()
obj.delete(c)
print('')
obj.inorder_traversal()