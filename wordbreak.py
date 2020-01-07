# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 14:14:48 2020

@author: eva
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True]+[False]*len(s)
        
        for i in range(1+len(s)):
            if not dp[i]:
                continue
            for w in wordDict:
                if s[i:].startswith(w):
                    dp[i+len(w)] = True
        
        return dp[-1]
        
        
        
        
        
        
#         if s.replace(' ','') == '':
#             return True
#         elif len(wordDict)==0:
#             return False
        
#         if wordDict[0] in s:
#             c = self.wordBreak(s.replace(wordDict[0],' '),wordDict[1:])
#             nc = self.wordBreak(s,wordDict[1:])
#             return c or nc
#         else:
#             return self.wordBreak(s,wordDict[1:])
#         if s == '':
#             return True
#         elif len(wordDict) == 0:
#             return False
        
#         string = "".join(set(s))
#         wd = "".join(set("".join(wordDict)))
#         for i in string:
#             if i not in wd:
#                 return False
        
        
        
#         ans = False
        
#         for i in range(len(wordDict)):
#             if s.startswith(wordDict[i]):
#                 ans = ans or self.wordBreak(s[len(wordDict[i]):],wordDict)
#                 if ans:
#                     return ans
        
#         else:
#             return False

        
        
            
        
    
        
        
        

        
a = Solution()
a.wordBreak("leetcode",["leet", "code", "sand", "and", "cat"])
        
    

     
