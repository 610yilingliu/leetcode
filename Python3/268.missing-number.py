#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums):
        largest = len(nums)
        s1 = 0
        s2 = 0
        for item in range(largest + 1):
            s1 ^= item
        for num in nums:
            s2 ^= num
        return s1 ^ s2

class Solution:
    def missingNumber(self, nums):
        largest = len(nums)
        # n = (0 + largest)/1 + 1
        n = largest + 1
        # arithmetic_sum = int((0 + largest) * n / 2)
        arithmetic_sum = int(largest * n / 2)
        return arithmetic_sum - sum(nums)
# @lc code=end
