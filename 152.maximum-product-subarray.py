#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    def maxProduct(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        helper = nums.copy()
        helper2 = nums.copy()
        for i in range(1, len(nums)):
            helper[i] = max(nums[i], helper[i - 1] * nums[i], helper2[i - 1] * nums[i])
            helper2[i] = min(nums[i], helper2[i - 1] * nums[i], helper[i - 1] * nums[i])
        return max(helper)

if __name__ == '__main__':
    a = Solution()
    b = a.maxProduct([2,-5,-2,-4,3])
    print(b)
# @lc code=end

