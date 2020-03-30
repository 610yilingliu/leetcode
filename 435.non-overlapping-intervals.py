#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals):
        if len(intervals) == 1 or len(intervals) == 0:
            return 0
        time = 0
        intervals.sort(key = lambda x:(-x[0], -x[1]))
        for i in range(len(intervals) - 2,  -1, -1):
            if intervals[i][0] == intervals[i + 1][0]:
                intervals.pop(i)
                time += 1
            else:
                if intervals[i][1] < intervals[i + 1][1]:
                    intervals.pop(i + 1)
                    time += 1
                if intervals[i][0] < intervals[i + 1][1]:
                    if intervals[i][0] < intervals[i + 1][1]:
                        intervals.pop(i)
                        time +=1
        return time

if __name__ == '__main__':
    a = Solution()
    b = a.eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]])
    print(b)
# @lc code=end

