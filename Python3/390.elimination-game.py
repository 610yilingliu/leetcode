#
# @lc app=leetcode id=390 lang=python3
#
# [390] Elimination Game
#

# @lc code=start
class Solution:
    def lastRemaining(self, n: int):
        return self.l2r(n)

    def l2r(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n & 1:
            return self.r2l((n - 1) >> 1) << 1
        return self.r2l(n >> 1) << 1
    
    def r2l(self, n):
        if n == 1 or n == 2:
            return 1
        if n & 1:
            return self.l2r((n - 1) >> 1) << 1
        return (self.l2r(n >> 1) << 1) - 1


# @lc code=end

