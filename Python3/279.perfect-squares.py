#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
class Solution:
    def numSquares(self, n: int):
        if n < 2:
            return n
        dp = [n] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[-1]


# @lc code=end

