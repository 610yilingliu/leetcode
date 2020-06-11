#
# @lc app=leetcode id=425 lang=python3
#
# [425] Word Squares
#
# @lc code=start
# #TLE
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
import collections

class Solution:
    def wordSquares(self, words):
        if len(words[0]) == 1:
            return [[word] for word in words]
        d = collections.defaultdict(list)
        l = len(words[0])
        for word in words:
            for i in range(1, l):
                d[word[:i]].append(word)
        ans = []

        def helper(pref, curmatrix):
            curlen = len(curmatrix)
            choices = d[pref]
            for choice in choices:
                if curlen < l - 1:
                    newpref = [item[curlen + 1] for item in curmatrix] + [choice[curlen + 1]]
                    newpref = ''.join(newpref)
                    helper(newpref, curmatrix + [choice])
                else:
                    ans.append(curmatrix + [choice])
        for word in words:
            helper(word[1], [word])
        return ans


# if __name__ == '__main__':
    # a = Solution()
    # b = a.wordSquares(["area","lead","wall","lady","ball"])
    # print(b)
# @lc code=end
