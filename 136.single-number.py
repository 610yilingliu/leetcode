#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums):
        d = dict()
        for item in nums:
            if item not in d:
                d[item] = 1
            else:
                d[item] += 1
        for key in d:
            if d[key] == 1:
                return key
# @lc code=end

