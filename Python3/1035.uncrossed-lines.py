#
# @lc app=leetcode id=1035 lang=python3
#
# [1035] Uncrossed Lines
#

# @lc code=start
class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        if not A or not B:
            return 0
        dp = [[0] * (len(A) + 1) for _ in range(len(B) + 1)]
        for i in range(1, len(B) + 1):
            for j in range(1, len(A) +1):
                if B[i - 1] == A[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return dp[-1][-1]
# @lc code=end

