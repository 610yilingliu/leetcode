#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str):
        d = dict()
        duplicated = set()
        for i in range(len(s)):
            if s[i] not in d and s[i] not in duplicated:
                d[s[i]] = i
            elif s[i] in d:
                duplicated.add(s[i])
                d.pop(s[i])
        mi_idx = float('inf')
        for k in d:
            if d[k] < mi_idx:
                mi_idx = d[k]
        if not d:
            return -1
        return mi_idx



# @lc code=end

