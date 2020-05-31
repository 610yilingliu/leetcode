#
# @lc app=leetcode id=375 lang=python3
#
# [375] Guess Number Higher or Lower II
#

# @lc code=start
class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        res = self.solve(dp, 1, n)
        return res

    def solve(self, dp, L, R):
        if L >= R: return 0
        if dp[L][R]: return dp[L][R]
        dp[L][R] = min(i + max(self.solve(dp, L, i - 1), self.solve(dp, i + 1, R)) for i in range(L, R + 1))
        return dp[L][R]

if __name__ == '__main__':
    a = Solution()
    b = a.getMoneyAmount(10)
    print(b)
            
# @lc code=end
