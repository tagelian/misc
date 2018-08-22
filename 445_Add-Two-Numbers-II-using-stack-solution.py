# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 14:21:36 2018

@author: lenovo
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def addTwoNumbers(self, l1, l2):
        s1 = []
        s2 = []
        while l1:
            s1.append(l1)
            l1 = l1.next
        while l2:
            s2.append(l2)
            l2 = l2.next
        carry = 0
        p = None
        while len(s1) != 0 and len(s2) != 0:
            t1 = s1.pop()
            t2 = s2.pop()
            s = t1.val + t2.val + carry
            carry = 0
            if s >= 10:
                carry = 1
                s -= 10
            t3 = ListNode(s)
            t3.next = p
            p = t3
        if len(s1) != 0:
            t = s1
        else:
            t = s2
        while len(t) != 0:
            t1 = t.pop()
            s = t1.val  + carry
            carry = 0
            if s >= 10:
                carry = 1
                s -= 10
            t3 = ListNode(s)
            t3.next = p
            p = t3            
        if carry:
            t3 = ListNode(1)
            t3.next = p
            p = t3
        return p
            
            