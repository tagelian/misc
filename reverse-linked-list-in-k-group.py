# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 22:44:23 2018

@author: cui
"""
def reverse1(head, k):
    def reverse(head, k):
        pre = None
        p = head
        i = 0
        while p and i < k:
            i += 1
            q = p.next
            p.next = pre
            pre = p
            p = q
        return (pre, p)
    
    #newhead, nextp = reverse(head, k)
    p1 = head
    c = 0
    while p1:
        c += 1
        p1 = p1.next
    num = c // k
    if num < 1:
        return head
    p = head
    res = None
    prelast = None
    for i in range(num):
        
        newhead, nextp = reverse(p, k)
        if not res:
            res = newhead
        if prelast:
            prelast.next = newhead
        prelast = p
        p = nextp
    prelast.next = p
    return res
        
