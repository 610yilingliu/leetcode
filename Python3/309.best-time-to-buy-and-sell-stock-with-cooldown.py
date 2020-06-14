#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        s0 = 0
        s1 = -prices[0]
        s2 = float('-inf')
        for i in range(len(prices)):
            pre0 = s0
            pre1 = s1
            pre2 = s2
            s0 = max(pre0, pre2)
            s1 = max(pre0 - prices[i], pre1)
            s2 = pre1 + prices[i]
        return max(s0, s2)

# @lc code=end

