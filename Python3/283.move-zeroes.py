#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        helper = [0] * len(nums)
        pos = 0
        for item in nums:
            if item != 0:
                helper[pos] = item
                pos += 1
        for i in range(len(nums)):
            nums[i] = helper[i]
# @lc code=end

