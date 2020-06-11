#
# @lc app=leetcode id=324 lang=python3
#
# [324] Wiggle Sort II
#

# @lc code=start
class Solution:
    def wiggleSort(self, nums: List[int]):
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        mid = (len(nums) + 1) >> 1
        pre = nums[:mid]
        suf = nums[mid:]
        nums[::2] = pre[::-1]
        nums[1::2] = suf[::-1]


        
# @lc code=end

