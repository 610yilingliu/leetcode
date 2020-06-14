#
# @lc app=leetcode id=757 lang=python3
#
# [757] Set Intersection Size At Least Two
#
import collections
# @lc code=start
class Solution:
    def intersectionSizeTwo(self, intervals):
        if not intervals:
            return 0
        intervals = sorted(intervals, key = lambda x: x[1])
        res = collections.deque()
        # initialize the element in stack
        res.append(intervals[0][-1] - 1)
        res.append(intervals[0][-1])
        ans = 2
        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            if res[0] < start <= res[1]:
                res.popleft()
                res.append(end)
                ans += 1
            elif start > res[1]:
                res.pop()
                res.pop()
                ans += 2
                res.append(end - 1)
                res.append(end)
        return ans

if __name__ == '__main__':
    a = Solution()
    b = a.intersectionSizeTwo([[33,44],[42,43],[13,37],[24,33],[24,33],[25,48],[10,47],[18,24],[29,37],[7,34]])
    print(b)
# @lc code=end

