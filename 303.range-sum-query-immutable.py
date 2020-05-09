#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#

# @lc code=start
class NumArray:

    def __init__(self, nums):
        self.ls = nums
        self.sums = nums.copy()
        for i in range(1, len(nums)):
            self.sums[i] = self.sums[i - 1] + nums[i]

    def sumRange(self, i: int, j: int):
        if i == 0:
            return self.sums[j]
        return self.sums[j] - self.sums[i - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray([1,2,3,4,5])
# param_1 = obj.sumRange(2,5)
# @lc code=end

