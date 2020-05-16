#
# @lc app=leetcode id=918 lang=python3
#
# [918] Maximum Sum Circular Subarray
#

# @lc code=start
class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        def ka(nums):
            res = float('-inf')
            current = float('-inf')
            for num in nums:
                current = max(0, current) + num
                res = max(res, current)
            return res
        if_neg = max(A)
        if if_neg < 0:
            return if_neg
        res1 = ka(A)
        res2 = sum(A) + ka([-num for num in A])
        return max(res1, res2)

# @lc code=end

