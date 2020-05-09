#
# @lc app=leetcode id=425 lang=python3
#
# [425] Word Squares
#
# @lc code=start
# class Solution:
#     def wordSquares(self, words):
#         self.mxstep = len(words[0])
#         self.ans = []
#         self.words = words
#         for w in words:
#             self.backtracker([w], 1)
#         return self.ans
    
#     def backtracker(self, curpath, step):
#         if step == self.mxstep:
#             self.ans.append(curpath[:])
#             return
#         pref_ls = [word[step] for word in curpath]
#         pref = ''.join(pref_ls)
#         for item in self.get_pref(pref):
#             curpath.append(item)
#             self.backtracker(curpath, step + 1)
#             curpath.pop()

#     def get_pref(self, pref):
#         for word in self.words:
#             if word.startswith(pref):
#                 yield word

class Solution:
    def wordSquares(self, words):
        self.words = words
        self.N = len(words[0])
        results = []
        word_squares = []
        for word in words:
            word_squares = [word]
            self.backtracking(1, word_squares, results)
        return results

    def backtracking(self, step, word_squares, results):
        if step == self.N:
            results.append(word_squares[:])
            return
        prefix = ''.join([word[step] for word in word_squares])    
        for candidate in self.getWordsWithPrefix(prefix):
            word_squares.append(candidate)
            self.backtracking(step+1, word_squares, results)
            word_squares.pop()

    def getWordsWithPrefix(self, prefix):
        for word in self.words:
            if word.startswith(prefix):
                yield word

# if __name__ == '__main__':
#     a = Solution()
#     b = a.wordSquares(["area","lead","wall","lady","ball"])
#     print(b)
# @lc code=end
