#
# @lc app=leetcode id=527 lang=python3
#
# [527] Word Abbreviation
#

# @lc code=start
class Solution:
    def wordsAbbreviation(self, dict: List[str]) -> List[str]:
        def helper(words, pre):
            d = defaultdict(list)
            for word in words:
                if pre >= len(word) - 2:
                    self.ans[word] = word
                    continue
                prefix = word[:pre]
                suffix = str(len(word) - pre - 1) + word[-1]
                d[prefix+suffix].append(word)

            for k, v in d.items():
                if len(v) == 1:
                    self.ans[v[0]] = k
                else:
                    helper(v, pre + 1)
            
        self.ans = {}
        helper(dict, 1)
        return [self.ans[word] for word in dict]
        

            
# @lc code=end

