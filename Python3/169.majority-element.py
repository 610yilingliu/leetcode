#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums):
        result_bits = [0] * 33
        res = 0
        for num in nums:
            # positive/negetive
            result_bits[32] += (num >> 32) & 1
            for i in range(32):
                result_bits[i] += (abs(num) >> i) & 1
        for i in range(32):
            if result_bits[i] > len(nums)/2:
                res += 1 << i
        if result_bits[32] > len(nums)/2:
            return -res
        return res
# @lc code=end

