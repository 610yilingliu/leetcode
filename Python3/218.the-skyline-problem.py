#
# @lc app=leetcode id=218 lang=python3
#
# [218] The Skyline Problem
#
# @lc code=start
import heapq

class Solution:
    def getSkyline(self, buildings):
        if not buildings:
            return []
        points = [(l, -h, r) for l, r, h in buildings] + [(r, 0, 0) for r in set(R for _, R, _ in buildings)]
        points.sort()
        heap = [(0, float('inf'))]
        res = [[0, 0]]
        for l, nh, r in points:
            while heap[0][1] <= l:
                heapq.heappop(heap)
            if nh:
                heapq.heappush(heap, (nh, r))
            if res[-1][1] != -heap[0][0]:
                res += [[l, -heap[0][0]]]
        return res[1:]

# @lc code=end

