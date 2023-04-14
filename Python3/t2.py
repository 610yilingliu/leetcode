class Solution:
    def maximumGain(self, s, x, y):
        n = len(s)
        dp = n * [0]
        for i in range(1, n):
            if s[i] == 'b' and s[i - 1] == 'a':
                dp[i] = max(dp[i - 1] + x, dp[i - 2] if i > 1 else 0)
            elif s[i] == 'a' and s[i - 1] == 'b':
                dp[i] = max(dp[i - 1] + y, dp[i - 2] if i > 1 else 0)
            else:
                dp[i] = dp[i - 1]
        return dp[-1]


a = Solution()
b = a.maximumGain("cdbcbbaaabab", 4, 5)