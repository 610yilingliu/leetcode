#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str):
        match = [[False for _ in range(len(s) + 1)] for _ in range(len(p) + 1)]
        match[0][0] = True
        for i in range(1, len(p) + 1):
            if p[i - 1] == '*':
                match[i][0] = match[i - 1][0]
        
        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if s[j - 1] == p[i - 1] or p[i - 1] == '?':
                    match[i][j] = match[i - 1][j - 1]
                if p[i - 1] == '*':
                    match[i][j] = match[i - 1][j] or match[i][j - 1]
        return match[-1][-1]



# @lc code=end

