#
# @lc app=leetcode id=244 lang=python3
#
# [244] Shortest Word Distance II
#

# @lc code=start
import collections

class WordDistance:

    def __init__(self, words: List[str]):
        self.d = collections.defaultdict(set)
        for idx, item in enumerate(words):
            self.d[item].add(idx)

    def shortest(self, word1: str, word2: str):
        mi = float('inf')
        for i1 in self.d[word1]:
            for i2 in self.d[word2]:
                mi = min(abs(i1 - i2), mi)
        return mi


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
# @lc code=end

