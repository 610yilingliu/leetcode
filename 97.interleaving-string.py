#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#

# @lc code=start
class Solution:
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        dp[0][0] = True
        for i in range(1, len(s1) + 1):
            if s3[i - 1] == s1[i - 1]:
                dp[i][0] = True
            else:
                break
        for j in range(1, len(s2) + 1):
            if s3[j - 1] == s2[j - 1]:
                dp[0][j] = True
            else:
                break
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                if dp[i - 1][j] and s3[i + j - 1] == s1[i - 1]:
                    dp[i][j] = True
                elif dp[i][j - 1] and s3[i + j - 1] == s2[j - 1]:
                    dp[i][j] = True
        return dp[-1][-1]


if __name__ == '__main__':
    a = Solution()
    b = a.isInterleave("aabcc","dbbca","aadbbcbcac")
    print(b)
# @lc code=end

