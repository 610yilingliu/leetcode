#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#

# @lc code=start
class Solution():
    def maximalSquare(self, matrix):
        if not matrix: return 0
        M = len(matrix)
        N = len(matrix[0])
        dp = [[0] * N for _ in range(M)]
        for i in range(M):
            dp[i][0] = int(matrix[i][0])
        for j in range(N):
            dp[0][j] = int(matrix[0][j])
        for i in range(1, M):
            for j in range(1, N):
                if int(matrix[i][j]) == 1:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
        return max(map(max, dp)) ** 2
                        

if __name__ == '__main__':
    a = Solution()
    b = a.maximalSquare([["0","0","0","1"],["1","1","0","1"],["1","1","1","1"],["0","1","1","1"],["0","1","1","1"]])
    print(b)

# @lc code=end

