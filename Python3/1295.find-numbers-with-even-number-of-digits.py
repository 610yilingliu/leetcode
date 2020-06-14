#
# @lc app=leetcode id=1295 lang=python3
#
# [1295] Find Numbers with Even Number of Digits
#

# @lc code=start
import collections
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        if not nums:
            return 0
        a = 0
        l = [len(str(num)) for num in nums]
        d = collections.Counter(l)
        for k, v in d.items():
            if k & 1 == 0:
                a += v
        return a
# @lc code=end

