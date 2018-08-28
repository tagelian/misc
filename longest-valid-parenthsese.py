# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 15:16:34 2018

@author: cui
"""

def fun1(s):
    stack = []
    last = -1
    ans = 0
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        elif len(stack) == 0:
            last = i
        else:
            stack.pop()
            if len(stack) == 0:
                ans = max(ans, i - last)
            else:
                ans = max(ans, i - stack[-1])
    return ans
#------------------------------------------------------------------------------
def fun2(s):
    d = [0 for _ in range(len(s))]
    left = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == '(':
            left += 1
        elif left > 0:
            left -= 1
            d[i] = d[i - 1] + 2
            j = i - d[i]
            if j >= 0:
                d[i] += d[j]
            ans = max(ans, d[i])
    return ans
            

s = '()))((()())'
print(fun2(s))