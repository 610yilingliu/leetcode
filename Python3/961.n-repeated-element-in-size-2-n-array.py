#
# @lc app=leetcode id=961 lang=python3
#
# [961] N-Repeated Element in Size 2N Array
#

# @lc code=start
import collections
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        d = collections.Counter(A)
        for k, v in d.items():
            if v > 1:
                return k
# @lc code=end

