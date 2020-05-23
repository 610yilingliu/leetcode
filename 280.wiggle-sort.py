#
# @lc app=leetcode id=280 lang=python3
#
# [280] Wiggle Sort
#

# @lc code=start
class Solution:
    def wiggleSort(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums:
            nums.sort()
            for i in range(1, len(nums) - 1, 2):
                nums[i], nums[i + 1] = nums[i + 1], nums[i]


# def swap(ls):
#     for i in range(0, len(ls) - 1, 2):
#         ls[i], ls[i + 1] = ls[i + 1], ls[i]
#     return ls

# if __name__ == '__main__':
#     newls = swap([1,2,3,4,5])
#     print(newls)
# @lc code=end

