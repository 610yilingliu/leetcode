#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
import collections
class Solution:
    def isMatch(self, s, p):
        dp = [[False for _ in range(len(s) + 1)] for _ in range(len(p) + 1)]
        dp[0][0] = True
        for i in range(2, len(p) + 1):
            if p[i - 1] == '*':
                dp[i][0] = dp[i - 2][0]

        for j in range(1, len(s) + 1):
            for i in range(1, len(p) + 1):
                # case: cur_s = cur_p
                if s[j - 1] == p[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                # case: cur_p == '.'
                elif p[i - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[i - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i - 2][j] or (dp[i][j - 1] and (s[j - 1] == p[i - 2] or p[i - 2] == '.'))
        return dp[-1][-1]


if __name__ == '__main__':
    a = Solution()
    b = a.isMatch( "mississippi", "mis*is*p*.")
    print(b)
            
        
        
                    
# @lc code=en