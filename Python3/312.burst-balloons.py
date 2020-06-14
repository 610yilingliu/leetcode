#
# @lc app=leetcode id=312 lang=python3
#
# [312] Burst Balloons
#

# @lc code=start
class Solution:
    def maxCoins(self, nums: List[int]):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for k in range(2, n):
            for left in range(0, n - k):
                right = left + k
                for i in range(left + 1, right):
                    dp[left][right] = max(dp[left][right], nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
        return dp[0][n - 1]
        
# @lc code=end

