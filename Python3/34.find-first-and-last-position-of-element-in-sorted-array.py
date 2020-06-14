#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(nums) - 1
        isA = True
        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                l, r = m, m
                # 找到左右边界
                while target == nums[l - 1] and l > 0:
                    l -= 1
                while r < len(nums) - 1 and target == nums[r + 1]:
                    r += 1
                isA = False
                break
        if isA is True:
            return [-1, -1]
        else:
            return [l, r]
        
# @lc code=end

