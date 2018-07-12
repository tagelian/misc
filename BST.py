# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 22:33:42 2018

@author: cui
"""
import copy
# created by cui 22:45 20180711 Wednesday
# have some wrong with TreeInsert and TreeConstruct funcs 23:30 20180711 Wednesday

#------------------------------------------------------------------------------
class TreeNode:
    def __init__(self, x):
        self.key = x
        self.left = None
        self.right = None
        self.parent = None
#------------------------------------------------------------------------------
def TreeInsert(root, z):
    y = None
    x = copy.deepcopy(root)
    while x:
        y = copy.deepcopy(x)
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.parent = y
    if y == None:
        root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z
    return root
#------------------------------------------------------------------------------
# =============================================================================
# def test(root):
#     root = TreeNode(7)
#     print(root.key)
# root = TreeNode(1)
# print(root.key)
# test(root)
# print(root.key)
# =============================================================================
#------------------------------------------------------------------------------
def TreeInorder(root):
    if root:
        TreeInorder(root.left)
        print(root.key)
        TreeInorder(root.right)
#------------------------------------------------------------------------------
def TreeConstruct(root, A):
    for i in range(len(A)):
        z1 = TreeNode(A[i])
        z = copy.deepcopy(z1)
        root = TreeInsert(root, z)
    return root
#------------------------------------------------------------------------------
TestList = [1,2,3,4,5]
root1 = None
root = TreeConstruct(root1, TestList)

TreeInorder(root)

a = b = 10
b = 2
print(a,b)
#print(root2.key)

    