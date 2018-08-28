# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 21:43:51 2018

@author: cui
"""

class ListNode:
    def __init__(self, x):
            
        self.val = x
        self.next = None
class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head
        if m == n:
            return head
        pre = None
        cnt = 0
        p = dummy = ListNode(-1)
        p.next = head
        while p and cnt < m:
            cnt += 1
            pre = p
            p = p.next
        slow = None
        temp = p
        while p and cnt <= n:
            q = p.next
            p.next = slow
            slow = p
            p = q
            cnt += 1
        suc = p
        pre.next = slow
        temp.next = suc
        return dummy.next
                    
