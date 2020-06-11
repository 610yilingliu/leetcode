#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int):
        if not nums:
            return 0
        if target <= nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) >> 1
            if target == nums[m]:
                return m
            if target > nums[m]:
                l = m + 1
            else:
                r = m - 1
        if target > nums[l]:
            return l + 1
        else:
            return l

# @lc code=end

