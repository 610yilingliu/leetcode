#
# @lc app=leetcode id=472 lang=python3
#
# [472] Concatenated Words
#

# @lc code=start
# import collections
# class Solution:
#     def findAllConcatenatedWordsInADict(self, words):
#         if not words:
#             return []
#         self.start_d = collections.defaultdict(list)
#         words = set(words)
#         for word in words:
#             if word:
#                 self.start_d[word[0]].append(word)
#         self.ans = set()
#         self.walked = set()
#         for word in words:
#             if word:
#                 self.finder(word, word)
#         return list(self.ans)
        
#     def finder(self, rest, curword):
#         if not rest:
#             if curword not in self.ans:
#                 self.ans.add(curword)
#                 self.walked.add(curword)
#             return
#         if rest in self.walked:
#             if curword not in self.ans:
#                 self.ans.add(curword)
#                 self.walked.add(curword)
#             return
#         currentparing = self.start_d[rest[0]]
#         for ele in currentparing:
#             if ele != curword:
#                 cut_pos = len(ele)
#                 if rest[:cut_pos] == ele:
#                     self.finder(rest[cut_pos:], curword)

# if __name__== '__main__':
#     a = Solution()
#     b = a.findAllConcatenatedWordsInADict()
#     print(b)

class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []
        self.wordSet = set(words)
        for word in words:
            self.wordSet.remove(word)
            if self.search(word):
                ans.append(word)
            self.wordSet.add(word)
        return ans

    def search(self, word):
        if word in self.wordSet:
            return True
        for idx in range(1, len(word)):
            if word[:idx] in self.wordSet and self.search(word[idx:]):
                return True
        return False
# @lc code=end

