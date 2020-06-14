#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """

        start = newInterval[0]
        end = newInterval[1]

        left, right = [], []
        for interval in intervals:
            if start > interval[1]:
                 left.append(interval)
            elif end < interval[0]:
                right.append(interval)
            else:
                start = min(start, interval[0])
                end = max(end, interval[1])

        return left + [[start, end]] + right


# @lc code=end

