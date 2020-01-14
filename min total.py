# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 11:32:50 2020

@author: eva
"""

class Solution:
    def minimumTotal(self, triangle):
        dp = [triangle[-1]]
        row = len(triangle) -2
        while row>=0:
            temp = []
            for i in range(row+1):
                temp.append(triangle[row][i]+min(dp[-1][i],dp[-1][i+1]))
            dp.append(temp)
            row -= 1
        return dp[-1][0]
    
    
a = Solution()
a.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])