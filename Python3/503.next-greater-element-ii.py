#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#

# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        records = []
        l = len(nums)
        res = [-1] * l
        for i in range(l * 2):
            i = i % l
            while records and nums[records[-1]] < nums[i]:
                res[records.pop()] = nums[i]
            records.append(i)
        return res

# @lc code=end

