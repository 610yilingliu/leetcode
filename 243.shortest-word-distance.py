#
# @lc app=leetcode id=243 lang=python3
#
# [243] Shortest Word Distance
#

# @lc code=start
class Solution:
    def shortestDistance(self, words, word1, word2):
        d = {word1: -1, word2: -1}
        mi = float('inf')
        if word1 == word2:
            return
        for i in range(len(words)):
            if words[i] == word1:
                d[word1] = i
                if d[word2] != -1:
                    mi = min(abs(d[word1] - d[word2]), mi)
            elif words[i] == word2:
                d[word2] = i
                if d[word1] != -1:
                    mi = min(abs(d[word1] - d[word2]), mi)
        return mi



# @lc code=end

