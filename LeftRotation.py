# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 16:12:34 2018

@author: lenovo
"""
# for preserve bst properties, rotation operates in local nodes with O(1) time  
#------------------------------------------------------------------------------
def LeftRotation(root, x):
    y = x.right
    x.right = y.left
    if y.left:
        y.left.parent = x
    y.parent = x.parent
    if x.parent == None:
        root = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y
    y.left = x
    x.parent = y
#------------------------------------------------------------------------------
    