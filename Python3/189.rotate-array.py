#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    # def rotate(self, nums, k):
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     k = k % len(nums)
    #     templs = [0] * len(nums)
    #     i = 0
    #     idx = k
    #     while idx < len(nums):
    #         templs[idx] = nums[i]
    #         idx += 1
    #         i += 1
    #     j = 0
    #     while i < len(nums):
    #         templs[j] = nums[i]
    #         i += 1
    #         j += 1
    #     for i in range(len(nums)):
    #         nums[i] = templs[i]
    def rotate(self, nums, k):
        k = k % len(nums)
        helper = nums[len(nums) - k :] + nums[:len(nums) - k]
        for i in range(len(nums)):
            nums[i] = helper[i]

if __name__ == '__main__':
    a = Solution()
    b = a.rotate([1,2], 1)
    print(b)        

# @lc code=end

