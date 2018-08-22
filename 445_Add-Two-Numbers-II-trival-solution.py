# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 14:02:51 2018

@author: lenovo
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def fun(self, l1, l2):
        def reverse(head):
            cur = head
            pre = None
            while cur:
                q = cur.next
                cur.next = pre
                pre = cur
                cur = q
            return pre
        l11, l22 = reverse(l1), reverse(l2)
        carry = 0
        p = dummy = ListNode(-1)
        while l11 and l22:
            s = l11.val + l22.val + carry
            carry = 0
            if s >= 10:
                carry = 1
                s -= 10
            p.next = ListNode(s)
            p = p.next
            l11 = l11.next
            l22 = l22.next
        t = l11 or l22
        while t:
            s = t.val + carry
            carry = 0
            if s >= 10:
                carry = 1
                s -= 10
            p.next = ListNode(s)
            p = p.next
            t = t.next
        if carry:
            p.next = ListNode(1)
            p = p.next
        ans = reverse(dummy.next)
        return ans
        
        
            
                