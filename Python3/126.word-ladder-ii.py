#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#

# @lc code=start
import collections

class Solution:
    # def findLadders(self, beginWord, endWord, wordList):
    #     self.ans = []
    #     self.target = endWord
    #     self.minstep = float('inf')
    #     visited = set()
    #     self.findpath(beginWord, visited, 1, [beginWord], wordList)
    #     real_ans = []
    #     for item in self.ans:
    #         if len(item) == self.minstep:
    #             real_ans.append(item)
    #     return real_ans


    # def findpath(self, cur, visited, step, path, wordlist):
    #     charlist = {chr(n) for n in range(97, 123)}
    #     if cur == self.target:
    #         self.ans.append(path)
    #         if step < self.minstep:
    #             self.minstep = step
    #     elif step > self.minstep:
    #         return
    #     for idx in range(len(cur)):
    #         for char in charlist:
    #             if char != cur[idx]:
    #                 word = cur[:idx] + char + cur[idx + 1:]
    #                 if word in wordlist and word not in visited:
    #                     new_vis = visited.copy()
    #                     new_vis.add(word)
    #                     self.findpath(word, new_vis, step + 1, path + [word], wordlist)
    

    def findLadders(self, beginWord, endWord, wordList):
        words = set(wordList)
        layer = {beginWord:[[beginWord]]}
        chars = {chr(n) for n in range(97, 123)}
        ans = []
        while layer:
            newlayer = collections.defaultdict(list)
            for word in layer:
                if word == endWord:
                    ans.extend([item for item in layer[word]])
                else:
                    for i in range(len(word)):
                        for char in chars:
                            if char != word[i]:
                                nw = word[:i] + char + word[i + 1:]
                                if nw in words:
                                    newlayer[nw] += [item + [nw] for item in layer[word]]
            words -= set(newlayer.keys())
            layer = newlayer
        return ans



if __name__ == '__main__':
    a = Solution()
    b = a.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"])
    print(b)
# @lc code=end

