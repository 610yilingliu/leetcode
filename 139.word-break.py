#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(dp)):
            for pre in range(i):
                if dp[pre] and s[pre:i] in wordDict:
                    dp[i] = True
        return dp[-1]
# @lc code=end

