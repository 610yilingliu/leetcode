#
# @lc app=leetcode id=748 lang=python3
#
# [748] Shortest Completing Word
#

# @lc code=start
import collections

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        if not words:
            return ''
        d = dict()
        for char in licensePlate:
            if char.isalpha():
                char = char.lower()
                d[char] = d.get(char, 0) + 1
        if not d:
            sort_ls = sorted([(len(word), word) for word in words])
            return sort_ls[0]

        mi_l = float('inf')
        ans = ''
        for word in words:
            curd = collections.Counter(word)
            is_in = True
            for k, v in d.items():
                if k not in d or curd[k] < v:
                    is_in = False
                    break
            if is_in:
                if len(word) < mi_l:
                    ans = word
                    mi_l = len(word)
        return ans

# @lc code=end

