#
# @lc app=leetcode id=188 lang=python3
#
# [188] Best Time to Buy and Sell Stock IV
#

# @lc code=start
import collections
# @lc code=start
class Solution:
    def maxProfit(self, k, prices):
        if len(prices) < 2:
            return 0
        if k > len(prices)//2:
            return sum(i - j for i, j in zip(prices[1:], prices[:-1]) if i - j > 0)
        dp = [[[0 for state in range(2)] for trans in range(k + 1)] for day in range(len(prices))]
        for trans in range(k + 1):
            dp[0][trans][0] = 0
            dp[0][trans][1] = -prices[0]
        for p in range(1, len(prices)):
            for i in range(1, k + 1):
                dp[p][i][0] = max(dp[p - 1][i][0], dp[p - 1][i][1] + prices[p])
                dp[p][i][1] = max(dp[p - 1][i][1], dp[p - 1][i - 1][0] - prices[p])
        return dp[-1][-1][0]

# if __name__ == '__main__':
#     a = Solution()
#     b = a.maxProfit(3, [3,3,5,0,0,3,1,4])
#     print(b)

# @lc code=end

