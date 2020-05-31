#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if not K:
            return []
        if K >= len(points):
            return points
        q = []
        for point in points:
            heapq.heappush(q, [point[0] * point[0] + point[1] * point[1], [point[0], point[1]]])
        
        ans = []
        for _ in range(K):
            ans.append(heapq.heappop(q)[1])
        return ans


# @lc code=end

