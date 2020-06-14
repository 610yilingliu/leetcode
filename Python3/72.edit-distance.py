#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
class Solution:
    def minDistance(self, word1, word2):
        dp = [[0 for _ in range(len(word1) + 1)] for _ in range(len(word2) + 1)]
        for i in range(len(word2) + 1):
            dp[i][0] = i
        for j in range(len(word1) + 1):
            dp[0][j] = j
        for i in range(1, len(word2) + 1):
            for j in range(1, len(word1) + 1):
                if word2[i - 1] == word1[j - 1]:
                        temp = dp[i - 1][j - 1]
                else: 
                    temp = dp[i - 1][j - 1] + 1
                dp[i][j] = min(temp, dp[i - 1][j] + 1, dp[i][j - 1] + 1)
        return dp[-1][-1]

if __name__ == '__main__':
    a = Solution()
    b = a.minDistance("horse", "ros")
    print(b)
# @lc code=end

