#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]):
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        helper = [0] * len(nums)
        helper[0] = nums[0] 
        helper[1]= max(nums[0], nums[1])
        for i in range(2, len(helper)):
            helper[i] = max(helper[i - 1], helper[i - 2] + nums[i])
        return helper[-1]
# @lc code=end

