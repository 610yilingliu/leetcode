#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern, str):
        word_ls = str.split(' ')
        d = dict()
        if len(word_ls) != len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in d:
                d[pattern[i]] = word_ls[i]
            else:
                if d[pattern[i]]!=word_ls[i]:
                    return False
        p = list(pattern)
        if len(set(p)) != len(set(word_ls)):
            return False
        return True
if __name__ =='__main__':
    a = Solution()
    b = a.wordPattern("abba", "dog cat cat dog")
    print(b)
# @lc code=end

