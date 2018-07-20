# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 09:05:53 2018

@author: lenovo
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def PairSwap(head):
    x = head
    y = x.next
    p1 = y.next
    y.next = x
    x.next = p1
    head = y
    while p1.next:
        x1 = x
        x = p1
        y = x.next
        p1 = y.next
        y.next = x
        x.next = p1
        x1.next = y
    return head

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

def PrintList(head):
    while head:
        print(head.val)
        head = head.next

PrintList(head)
head1 = PairSwap(head)        
PrintList(head1)
