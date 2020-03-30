#
# @lc app=leetcode id=201 lang=python3
#
# [201] Bitwise AND of Numbers Range
#

# @lc code=start
class Solution:
    def rangeBitwiseAnd(self, m, n):
        step = 0
        while m!= n:
            m = m >> 1
            n = n >> 1
            step += 1
        return m << step
# @lc code=end

