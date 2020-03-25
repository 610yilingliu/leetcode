#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution:
    def minPathSum(self, grid):
        if len(grid) == 1:
            return sum(grid[0])
        if len(grid[0]) == 1:
            s = 0
            for i in range(len(grid)):
                s += grid[i][0]
            return s

        h = len(grid)
        l = len(grid[0])
        mat = [[0] * l for _ in range(h)]
        mat[0][0] = grid[0][0]
        first_col = mat[0][0]

        for i in range(1, h):
            mat[i][0] = first_col + grid[i][0]
            first_col += grid[i][0]
        first_row = mat[0][0]

        for j in range(1, l):
            mat[0][j] = first_row + grid[0][j]
            first_row += grid[0][j]

        for i in range(1, h):
            for j in range(1, l):
                mat[i][j] = min(mat[i - 1][j], mat[i][j - 1]) + grid[i][j]
        return mat[h - 1][l - 1]


# @lc code=end

