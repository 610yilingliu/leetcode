#
# @lc app=leetcode id=953 lang=python3
#
# [953] Verifying an Alien Dictionary
#

# @lc code=start
class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        N = len(words)
        d = {c : i for i, c in enumerate(order)}
        for i in range(N - 1):
            pre, after = words[i], words[i + 1]
            if pre == after: continue
            _len = min(len(pre), len(after))
            for j in range(_len):
                if d[pre[j]] < d[after[j]]:
                    break
                elif d[pre[j]] > d[after[j]]:
                    return False
            if len(pre) > len(after) and pre[:_len] == after:
                return False
        return True

# @lc code=end

