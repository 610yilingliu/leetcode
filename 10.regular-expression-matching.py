#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # if end pattern, check if s is ended
        if not p:
            return not s
        if s[0] == p[0] or p[0] == '.':
            sym =True
    def helper(self, s, p):
        if p[1] == '*':
            
        
        
                    
# @lc code=en