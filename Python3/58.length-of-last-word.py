#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str):
        w = s.split(' ')
        if w:
            for i in range(len(w)-1, -1, -1):
                if w[i]:
                    return len(w[i])
        return 0


# @lc code=end

