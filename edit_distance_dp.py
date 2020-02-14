# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 11:27:39 2020

@author: eva
"""
# Up:insert
# Left:delete
class Solution:
    def minDistance(self, s: str, t: str) -> int:
        
        dp = [[0]*(len(s)+1) for i in range((1+len(t)))]
        
        for i in range(1,len(s)+1):
            dp[0][i] = i
        for i in range(1,len(t)+1):
            dp[i][0] = i
        
        for r in range(1,len(t)+1):
            for c in range(1,len(s)+1):
                if t[r-1] == s[c-1]:
                    dp[r][c] = min(dp[r-1][c]+1,dp[r][c-1]+1,dp[r-1][c-1])
                else:
                    dp[r][c] = min(dp[r-1][c],dp[r][c-1],dp[r-1][c-1])+1
        
        return dp[-1][-1]
                    
        
        
        
        
