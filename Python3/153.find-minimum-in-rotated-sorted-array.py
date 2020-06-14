#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return nums[i + 1]
        return nums[0]
# @lc code=end

