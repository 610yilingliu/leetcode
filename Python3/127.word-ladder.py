#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
import collections

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordset = set(wordList)
        if endWord not in wordset:
            return 0
        bfs = collections.deque()
        bfs.append((beginWord, 1))
        chars = {chr(n) for n in range(97,123)}
        while bfs:
            cur, l = bfs.popleft()
            if cur == endWord:
                return l
            for i in range(len(cur)):
                for char in chars:
                    word = cur[:i] + char + cur[i + 1:]
                    if word in wordset and word != cur:
                        wordset.remove(word)
                        bfs.append((word, l + 1))
        return 0
            
if __name__ == '__main__':
    a = Solution()
    b = a.ladderLength("a", "c", ["a","b","c"])
    print(b)


# @lc code=end

