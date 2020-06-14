#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#

# @lc code=start
class Solution:
    def grayCode(self, n):
        if n==0:
            return [0]
        return self.back(n)
        
    def back(self, n):
        if n==1:
            return [0,1] 
        cur = [] 
        pre= self.back(n-1)
        for x in range(len(pre)-1,-1,-1):
            cur.append(2**(n-1)+pre[x])  
        return pre+cur
# @lc code=end

