#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start
class Solution:
    def numTrees(self, n: int):
        if n < 2:
            return n
        dp = [0] * n
        

        
# @lc code=end

