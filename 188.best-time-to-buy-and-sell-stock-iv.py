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
        rg = len(prices)
        prof = [[0] * rg for _ in range(rg)]
        for i in range(rg):
            for j in range(rg):
                if i > j and prices[i] - prices[j] > 0:
                    prof[i][j] = prices[i] - prices[j]
        maxprof = 0
        # start from mat[y][0]
        for starty in range(1, rg):
            temp_que = collections.deque([0] * k)
            y = starty
            x = 0
            while y < rg and x < rg:
                curval = prof[y][x]
                if curval > temp_que[1]:
                    temp_que.popleft()
                    temp_que.append(curval)
                elif curval > temp_que[0]:
                    temp_que.popleft()
                    temp_que.appendleft(curval)
                x += 1
                y += 1
            maxprof = max(maxprof, sum(temp_que))
        return maxprof  
# @lc code=end

