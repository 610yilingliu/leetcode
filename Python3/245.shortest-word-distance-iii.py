#
# @lc app=leetcode id=245 lang=python3
#
# [245] Shortest Word Distance III
#

# @lc code=start
class Solution:
    def shortestWordDistance(self, words, word1, word2):
        if word1 != word2:
            res = self.helper(words, word1, word2)
            return res
        else:
            pre = -1
            cur = -1
            flag = 0
            mi = float('inf')
            for i in range(len(words)):
                if flag == 0 and words[i] == word1:
                    pre = i
                    if cur > -1:
                        mi = min(mi, abs(pre - cur))
                    flag = 1
                elif flag == 1 and words[i] == word1:
                    cur = i
                    if pre > -1:
                        mi = min(mi, abs(pre - cur))
                    flag = 0
            return mi

        
    def helper(self, words, word1, word2):
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

