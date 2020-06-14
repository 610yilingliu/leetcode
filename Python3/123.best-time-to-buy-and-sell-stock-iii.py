#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#
import collections
# @lc code=start
class Solution:
    def maxProfit(self, prices):
        # if len(prices) < 2:
        #     return 0
        # rg = len(prices)
        # prof = [[0] * rg for _ in range(rg)]
        # for i in range(rg):
        #     for j in range(rg):
        #         if i > j and prices[i] - prices[j] > 0:
        #             prof[i][j] = prices[i] - prices[j]
        # maxprof = 0
        # # start from mat[y][0]
        # for x in range(0, rg - 1):
        #     for y in range(x + 1, rg):
        #         temp_prof = prof[y][x]
        #         x2 = y + 1
        #         maxprof = max(maxprof, temp_prof)
        #         if x2 < rg:
        #             while x2 < rg:
        #                 for y2 in range(x2 + 1, rg):
        #                     cur_val = prof[y2][x2]
        #                     maxprof = max(maxprof, temp_prof + cur_val)
        #                 x2 += 1
        # return maxprof

        # state: having a transaction or not
        if len(prices) < 2:
            return 0
        dp = [[[0 for state in range(2)] for trans_did in range(3)] for day in range(len(prices))]
        for t in range(3):
            dp[0][t][0] = 0
            dp[0][t][1] = -prices[0]
        for p in range(1, len(prices)):
            for i in range(1, 3):
                dp[p][i][0] = max(dp[p - 1][i][0], dp[p - 1][i][1] + prices[p])
                dp[p][i][1] = max(dp[p - 1][i][1], dp[p - 1][i - 1][0] - prices[p])
        return dp[-1][-1][0]



if __name__ == '__main__':
    a = Solution()
    b = a.maxProfit([3,3,5,0,0,3,1,4])
    print(b)



# @lc code=end

