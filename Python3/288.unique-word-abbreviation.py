#
# @lc app=leetcode id=288 lang=python3
#
# [288] Unique Word Abbreviation
#

# @lc code=start
import collections

class ValidWordAbbr:

    def __init__(self, dictionary):
        self.abbrs = dict()
        self.cnt = collections.defaultdict(int)
        for word in dictionary:
            if len(word) < 2 and word not in self.abbrs:
                self.abbrs[word] = word
            else:
                abbr = word[0] + str(len(word[1:-1])) + word[-1]
                self.abbrs[word] = abbr
                self.cnt[abbr] += 1

    def isUnique(self, word: str):
        if len(word) < 2:
            return True
        if word in self.abbrs:
            abbr = self.abbrs[word]
            count = self.cnt[abbr]
            if count > 1:
                return False
            return True
        abbr = word[0] + str(len(word[1:-1])) + word[-1]
        if abbr in self.cnt:
            return False
        return True


# Your ValidWordAbbr object will be instantiated and called as such:
obj = ValidWordAbbr(["a","a"])
param_1 = obj.isUnique("a")
print(param_1)
# @lc code=end

