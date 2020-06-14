#
# @lc app=leetcode id=354 lang=python3
#
# [354] Russian Doll Envelopes
#

# @lc code=start
import bisect
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]):
        if not envelopes:
            return 0
        envelopes.sort(key = lambda x:(x[0], -x[1]))
        heights = []
        for l, h in envelopes:
            curindex = bisect.bisect_left(heights, h)
            if curindex == len(heights):
                heights.append(h)
            else:
                heights[curindex] = h
        return len(heights)
# @lc code=end

