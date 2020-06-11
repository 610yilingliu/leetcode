#
# @lc app=leetcode id=410 lang=python3
#
# [410] Split Array Largest Sum
#

# @lc code=start
class Solution:
    def splitArray(self, nums: List[int], m: int):
        if not nums or not m:
            return 0
        if m == 1:
            return sum(nums)
        l = len(nums)
        if l == m:
            return min(nums)
        

        
# @lc code=end

