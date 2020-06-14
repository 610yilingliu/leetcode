#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums)<=3: return max(nums)
        return max(self.get_max(nums[1:]), self.get_max(nums[:-1]))
        
    def get_max(self, nums):
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[:2])
        for i in range(2,n):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])       
        return dp[-1]

# @lc code=end

