#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid[0][0] == 1:
            return 0
        if len(obstacleGrid) == 1:
            for item in obstacleGrid[0]:
                if item == 1:
                    return 0
            return 1
        if len(obstacleGrid) == 1:
            for item in obstacleGrid:
                if item == [1]:
                    return 0
            return 1
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        mat = [[0] * m for _ in range(n)]
        mat[0][0] = 1
        for i in range(1, m):
            if obstacleGrid[0][i] == 1:
                break
            else:
                mat[0][i] = mat[0][i-1]
        for j in range(1, n):
            if obstacleGrid[j][0] == 1:
                    break
            else:
                mat[j][0] = mat[j - 1][0]
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[j][i] == 0:
                    mat[j][i] = mat[j-1][i] + mat[j][i-1]
                else:
                    mat[j][i] == 0
        return mat[n-1][m-1]

# @lc code=end

