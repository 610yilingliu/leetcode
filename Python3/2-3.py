class Solution:
    def canPartition(self, nums):
        n = len(nums)

        if n == 0:
            return False

        s = sum(nums)
        if s & 1 == 1:
            return False

        target = s // 2
        dp = [[False for _ in range(target + 1)] for _ in range(n)]

        for i in range(target + 1):
            dp[0][i] = False if nums[0] != i else True

        for i in range(1, n):
            for j in range(target + 1):
                if j >= nums[i]:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[-1][-1]


a = Solution()
b = a.canPartition([1, 2, 4, 5])
print(b)