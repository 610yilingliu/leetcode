#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums):
        if len(nums) < 3:
            return len(nums)
        for i in range(len(nums) - 3, -1, -1):
            if nums[i] == nums[i + 1] == nums[i + 2]:
                nums.pop(i)
        return len(nums)
# @lc code=end

