#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        mini = prices[0]
        ans = 0
        for p in prices:
            if p < mini:
                mini = p
            elif p - mini > ans:
                ans = p - mini
        return ans

if __name__ == '__main__':
    a = Solution()
    b = a.maxProfit([2,1,2,0,1])
    print(b)

# @lc code=end

