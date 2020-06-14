#
# @lc app=leetcode id=1002 lang=python3
#
# [1002] Find Common Characters
#
import collections
# @lc code=start
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if not A:
            return []
        if len(A) == 1:
            return [char for char in A[0]]
        pred = collections.Counter(A[0])
        for i in range(1, len(A)):
            curd = collections.Counter(A[i])
            pred = self.findcommon(pred, curd)
        ans = []
        for k, v in pred.items():
            for _ in range(v):
                ans.append(k)
        return ans

    def findcommon(self, d1, d2):
        rd = dict()
        for k in d1:
            if k in d2:
                rd[k] = min(d1[k], d2[k])
        return rd
# @lc code=end

