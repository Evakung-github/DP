# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 21:20:11 2020

@author: eva
"""

class Solution:
    #BFS
    def partition(self, s):
         if len(s) == 1:
             return [[s]]
         elif len(s) == 0:
             return [[]]
         ans = []
        
         for i in range(len(s)):
             temp = []
             if s[:i+1] == s[:i+1][::-1]:
                 temp = [[s[:i+1]]+j for j in self.partition(s[i+1:])]
             ans.extend(temp)
        
         return ans
    
    # If using BFS, then lots of partitions will be calculated repetitively. Hence, it is slow. 
    # If we use dynamic programming, then no repetitive work is made and it is more efficient.
    
    
    #DP
    
    def partition2(self, s):    
        dp = [[[]]]  # Initiate the first one, as we will need it later.
        
        for i in range(1,len(s)):
            temp = [j + [s[i]] for j in dp[-1]] #Simply append next element to previous stage.
            for j in range(i):    # We need to check if adding next element would result in palindrome combinations.
                                     
                if s[j:i+1] == s[j:i+1][::-1]:  # If so, then it is added to the answer.
                    temp.extend([k+[s[j:i+1]] for k in dp[j]])
            dp.append(temp)
        return dp[-1]
    
a = Solution()
a.partition2('bb')


k = ['a','b','c']