#
# @lc app=leetcode id=154 lang=python3
#
# [154] Find Minimum in Rotated Sorted Array II
#

# @lc code=start
class Solution:
    def findMin(self, nums):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return nums[i + 1]
        return nums[0]
# @lc code=end

