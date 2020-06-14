#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
import collections

class Solution:
    def coinChange(self, coins: List[int], amount: int):
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            for j in range(len(coins)):
                if coins[j] <= i:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)
        if dp[amount] != float('inf'):
            return dp[amount]
        return -1

# @lc code=end

