#
# @lc app=leetcode id=576 lang=python3
#
# [576] Out of Boundary Paths
#

# @lc code=start
class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int):
        dp = [[[0] * n for _ in range(m)] for _ in range(N + 1)]
        for s in range(1, N + 1):
            for x in range(m):
                for y in range(n):
                    v1 = 1 if x == 0 else dp[s - 1][x - 1][y]
                    v2 = 1 if x == m - 1 else dp[s - 1][x + 1][y]
                    v3 = 1 if y == 0 else dp[s - 1][x][y - 1]
                    v4 = 1 if y == n - 1 else dp[s - 1][x][y + 1]
                    dp[s][x][y] = (v1 + v2 + v3 + v4) % (10**9 + 7)
        return dp[N][i][j]

        
# @lc code=end

