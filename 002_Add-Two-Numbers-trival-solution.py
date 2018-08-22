# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 22:09:44 2018

@author: lenovo
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        dummy = ListNode(-1)
        p = dummy
        while l1 and l2:
            s = l1.val + l2.val + carry
            if s >= 10:
                carry = 1
                s -= 10
            p.next = ListNode(s)
            l1 = l1.next
            l2 = l2.next
            p = p.next
        t = l1 or l2
        while t:
            s = t.val + carry
            if t >= 10:
                carry = 1
                s -= 10
            p.next = ListNode(s)
            p = p.next
            t = t.next
        if carry:
            p.next = ListNode(carry)
        return dummy.next
            
            