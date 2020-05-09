#
# @lc app=leetcode id=293 lang=python3
#
# [293] Flip Game
#

# @lc code=start
class Solution:
    def generatePossibleNextMoves(self, s):
        for i in range(len(s)):
            res = []
            for i in range(len(s) - 1):
                if s[i:i+2] == "++":
                    res.append(s[:i] + "--" + s[i+2:])
            return res




# @lc code=end

