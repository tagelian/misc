# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 11:01:08 2018

@author: lenovo
"""

# created by cui 11:02 20180712 Thursday
#------------------------------------------------------------------------------
class TreeNode:
    def __init__(self, x):
        self.key = x
        self.left = None
        self.right = None
        self.parent = None
#------------------------------------------------------------------------------
def TreeInorder(root):
    if root:
        TreeInorder(root.left)
        print(root.key)
        TreeInorder(root.right)
#------------------------------------------------------------------------------
def TreeInsert(root, z):
    y = None
    x = root
    while x:
        y = x
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
def TreeConstruct(root, A):
    """
    按照顺序创建的bst， 跟balance bst 有区别， 这里需要注意 11:20
    """
    for i in range(len(A)):
        root = TreeInsert(root, TreeNode(A[i]))
    return root
#------------------------------------------------------------------------------
def TreeSearch(root, k):
    """
    have some problems with recursive TreeSearch func 11:33 20180712 Thursday
    """
    if root == None or root.key == k:
        return root
    elif k < root.key:
        root = root.left
        TreeSearch(root, k)
    else:
        root = root.right
        TreeSearch(root, k)
#------------------------------------------------------------------------------
def IterativeTreeSearch(root, k):
    while root != None and root.key != k:
        if k < root.key:
            root = root.left
        else:
            root = root.right
    return root
#------------------------------------------------------------------------------
def TreeMinimum(root):
    while root.left:
        root = root.left
    return root
#------------------------------------------------------------------------------
def TreeMaximum(root):
    while root.right:
        root = root.right
    return root
#------------------------------------------------------------------------------
def TreePredecessor(x):
    if x.left:
        return TreeMaximum(x.left)
    y = x.parent
    while y != None and y.left == x:
        x = y
        y = y.parent
    return y
#------------------------------------------------------------------------------
def TreeSuccessor(x):
    if x.right:
        return TreeMinimum(x.right)
    y = x.parent
    while y != None and y.right == x:
        x = y
        y = y.parent
    return y
#------------------------------------------------------------------------------
def transplant(root, u, v):
    """
    注意， 这里要返回root， 不然修改不了
    """
    if u.parent == None:
        root = v
    elif u.parent.left == u:
        u.parent.left = v
    else:
        u.parent.right = v
    if v:
        v.parent = u.parent
    return root
#------------------------------------------------------------------------------
def TreeDelete(root, z):
    """
    注意， 这里要返回root， 不然删除不了 节点
    """
    if z.left == None:
        root = transplant(root, z, z.right)
    elif z.right == None:
        root = transplant(root, z, z.left)
    else:
        y = TreeSuccessor(z)
        if y != z.right:
            root = transplant(root, y, y.right)
            y.right = z.right
            y.right.parent = y
        root = transplant(root, z, y)
        y.left = z.left
        y.left.parent = y
    return root
#------------------------------------------------------------------------------
        
    
testlist = [2,1,3,5,4]
root = None
root = TreeConstruct(root, testlist)
#root= TreeDelete(root, root)
#TreeInorder(root)
#root = transplant(root, root, root.right)
#print(root.key)
#TreeInorder(root)
#print(TreeSuccessor(root.right).key)
#print(TreePredecessor(root.right.right).key)
#print(TreeMinimum(root).key, TreeMaximum(root).key)
#print(IterativeTreeSearch(root,6).key)
#print(TreeSearch(root,1).key)
#TreeInorder(root)
#print(root.right.right.left.key)
            