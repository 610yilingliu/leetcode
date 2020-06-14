#
# @lc app=leetcode id=318 lang=python3
#
# [318] Maximum Product of Word Lengths
#

# @lc code=start
class Solution:
    def maxProduct(self, words):
        feature_dic = dict()
        for word in words:
            word_feature = 0
            for i in range(len(word)):
                word_feature |= 1 << (ord(word[i]) - ord('a'))
            feature_dic[word] = word_feature
        ans = 0
        for i in range(len(words)):
            for prev in words[:i]:
                if feature_dic[words[i]] & feature_dic[prev] == 0:
                    ans = max(ans, len(words[i] * len(prev)))
        return ans

if __name__ == '__main__':
    a = Solution()
    b = a.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"])
    print(b)

# @lc code=end

