# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 18:18:20 2018

@author: cui
"""

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n <= 1:
            return s
        from collections import defaultdict
        d = defaultdict(list)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    dp[i][j] = True
        ans = 0
        for i in range(n-1):
            for j in range(i+1, n):
                if j == i + 1:
                    dp[i][j] = s[i] == s[j]
                    if 2 > ans:
                        ans = 2
                        d[ans].append(s[i:j+1])
                        
                if i + 1 <= j - 1 :
                    dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
                    if j - i + 1 > ans:
                        ans = j - i + 1
                        d[ans].append(s[i:j+1])
        res = d[max(d.keys())][0]
        return res
S = Solution()
test = 'abbaaa'
result = S.longestPalindrome(test)