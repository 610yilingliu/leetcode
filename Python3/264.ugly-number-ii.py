#
# @lc app=leetcode id=264 lang=python3
#
# [264] Ugly Number II
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n):
        if n == 1:
            return 1
        dp = [0, 1]
        p1 = 1
        p2 = 1
        p3 = 1
        for i in range(2, n + 1):
            cur = min(dp[p1] * 2, dp[p2] * 3, dp[p3] * 5)
            if cur == dp[p1] * 2:
                p1 += 1
            if cur == dp[p2] * 3:
                p2 += 1
            if cur == dp[p3] * 5:
                p3 += 1
            dp.append(cur)
        return dp[-1]

if __name__ == '__main__':
    a = Solution()
    b = a.nthUglyNumber(10)
    print(b)

# @lc code=end

