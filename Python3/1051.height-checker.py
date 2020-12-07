#
# @lc app=leetcode id=1051 lang=python3
#
# [1051] Height Checker
#

# @lc code=start
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        inc = sorted(heights)
        n = 0
        for i in range(len(inc)):
            if inc[i] != heights[i]:
                n += 1
        return n
# @lc code=end

