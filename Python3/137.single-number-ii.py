#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#

# @lc code=start
class Solution:
    def singleNumber(self, nums):
        nums.sort()
        if len(nums) == 1:
            return nums[0]
        else:
            if nums[0] == nums[1] == nums[2]:
                return self.singleNumber(nums[3:])
            return nums[0]


# @lc code=end

