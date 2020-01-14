# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 11:32:50 2020

@author: eva
"""
# https://leetcode.com/problems/triangle/
# task: Find the minimum sum of sequence of a triangle.

# Instead of doing from top, I am doing the calculation from down.
# Using dynamic programming, we are able to record the minimum sum value of each value after its level.
# [
#    [2],    -> [11]         ^
#   [3,4],   -> [9,10]       |
#  [6,5,7],  -> [7,6,10]     |
# [4,1,8,3]  -> [4,1,8,3]    |
#]

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
