#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums):
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
        self.quick(nums, 0, len(nums) - 1)


    def quicksort(self, nums, l ,r):
        base = nums[l]
        while l < r:
            while l < r and nums[r] >= base:
                r -= 1
            while l < r and nums[r] < base:
                nums[l] = nums[r]
                l += 1
                nums[r] = nums[l]
        nums[l] = base
        return l

    def quick(self, nums, l, r):
        if l < r:
            key = self.quicksort(nums, l, r)
            self.quick(nums, l, key)
            self.quick(nums, key + 1, r)

# @lc code=end

