#
# @lc app=leetcode id=851 lang=python3
#
# [851] Loud and Rich
#

# @lc code=start

class Solution:
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        m = collections.defaultdict(list)
        for i, j in richer:
            m[j].append(i)

        res = [-1] * len(quiet)

        def dfs(i):
            if res[i] > 0: return res[i]
            res[i] = i
            for j in m[i]:
                if quiet[res[i]] > quiet[dfs(j)]:
                    res[i] = res[j]
            return res[i]

        for i in range(len(quiet)):
            dfs(i)
        return res
            
# @lc code=end

