#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        profit = 0
        peak_pos = 0
        velly_pos = 0
        i = 0
        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i += 1
            velly_pos = i
            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
                i += 1
            peak_pos = i
            profit += prices[peak_pos] - prices[velly_pos]

        return profit


if __name__ == '__main__':
    a = Solution()
    b = a.maxProfit([0,5,5,6,2,1,1,3])
    print(b)
# @lc code=end

