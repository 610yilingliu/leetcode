#
# @lc app=leetcode id=720 lang=python3
#
# [720] Longest Word in Dictionary
#

# @lc code=start
class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words.sort()
        res = set([''])
        longestWord = ''
        for word in words:
            if word[:-1] in res:
                res.add(word)
                if len(word) > len(longestWord):
                    longestWord = word
        return longestWord

# @lc code=end

