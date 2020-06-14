#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals):
        if intervals == []:
            return []
        self.ans = []
        intervals.sort()
        self.helper(intervals[0][0], intervals[0][1], 0, intervals)
        return self.ans

    def helper(self, start, end, index, intervals):
        for i in range(index, len(intervals)):
            if intervals[i][0] > end:
                self.ans.append([start, end])
                return self.helper(intervals[i][0], intervals[i][1], i, intervals)
            else:
                start = min(start, intervals[i][0])
                end = max(end, intervals[i][1])
        self.ans.append([start, end])
# @lc code=end

