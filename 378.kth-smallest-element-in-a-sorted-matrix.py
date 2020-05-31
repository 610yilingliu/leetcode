#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#

# @lc code=start
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int):
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        q = [(matrix[0][0], 0, 0)]
        for _ in range(k):
            ans, i, j = heapq.heappop(q)
            if j == 0 and i + 1 < m:
                heapq.heappush(q, (matrix[i + 1][j], i + 1, j))
            if j + 1 < n:
                heapq.heappush(q, (matrix[i][j + 1], i, j + 1))
        return ans
        
# @lc code=end


