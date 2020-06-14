#
# @lc app=leetcode id=87 lang=python3
#
# [87] Scramble String
#

# @lc code=start
class Solution:
    def isScramble(self, s1, s2):
        if s1 == s2:
            return True
        if len(s1) != len(s2):
            return False
        if sorted(s1) != sorted(s2):
            return False
        for i in range(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                return True
        return False

# @lc code=end

