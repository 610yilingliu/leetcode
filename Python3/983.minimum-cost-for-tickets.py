#
# @lc app=leetcode id=983 lang=python3
#
# [983] Minimum Cost For Tickets
#

# @lc code=start
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [float('inf') for _ in range(366)]
        for d in days:
            dp[d] = 0
        dp[0] = 0
        for i in range(1, 366):
            if dp[i] == float("inf"):
                dp[i] = dp[i - 1]
            else:
                cur = dp[i - 1] + costs[0]
                cur = min(dp[max(0, i - 7)] + costs[1], cur)
                cur = min(dp[max(0, i - 30)] + costs[2], cur)
                dp[i] = cur
        return dp[days[-1]]
# @lc code=end

