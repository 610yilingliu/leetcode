#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#

# @lc code=start
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n = set(nums)
        s = [item for item in n]
        s.sort()
        if len(s) > 2:
            return s[-3]
        return s[-1]
# @lc code=end

