#
# @lc app=leetcode id=500 lang=python3
#
# [500] Keyboard Row
#

# @lc code=start
class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rowdict = {}
        for c in "qwertyuiopQWERTYUIOP":
            rowdict[c] = 1
        for c in "asdfghjklASDFGHJKL":
            rowdict[c] = 2
        for c in "zxcvbnmZXCVBNM":
            rowdict[c] = 3
        res = []
        for word in words:
            if len(set(rowdict[c] for c in word)) == 1:
                res.append(word)
        return res
# @lc code=end

