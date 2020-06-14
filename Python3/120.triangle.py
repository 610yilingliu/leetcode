#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle):
        if len(triangle) == 1:
            return triangle[0][0]
        s = 0
        start_x = 0
        size = len(triangle)
        mat = [[0] * (size) for _ in range(size)]
        mat[0][0] = triangle[0][0]
        # adjacent: next[idx] = prev[idx] or prev[idx + 1]
        for i in range(1, size):
            mat[i][0] = mat[i - 1][0] + triangle[i][0]
            mat[i][i] = mat[i - 1][i - 1] + triangle[i][i]
            for j in range(1, len(triangle[i]) - 1):
                mat[i][j] = min(mat[i - 1][j - 1], mat[i - 1][j]) + triangle[i][j]
        return min(mat[-1])

# @lc code=end

