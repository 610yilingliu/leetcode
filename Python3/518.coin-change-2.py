#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change 2
#

# @lc code=start
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(1, amount + 1):
                if coin <= i:
                    dp[i] += dp[i - coin]
        return dp[-1]

# if __name__ == '__main__':
#     a = Solution()
#     b = a.change(3, [2])
#     print(b)
# @lc code=end

