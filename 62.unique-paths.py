#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int):
        if n == 0 or m == 0:
            return 1
        mat = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    mat[i][j] = 1
                else:
                    mat[i][j] = mat[i - 1][j] + mat[i][j - 1]
        return mat[n - 1][m - 1]
    
# @lc code=end

