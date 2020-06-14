#
# @lc app=leetcode id=884 lang=python3
#
# [884] Uncommon Words from Two Sentences
#

# @lc code=start
import collections
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        A = A.split(' ')
        B = B.split(' ')
        a = set(A)
        ad = collections.Counter(A)
        b = set(B)
        bd = collections.Counter(B)
        subtraction = (a | b) - (a & b)
        ansset = subtraction.copy()
        for ele in subtraction:
            if ele in A:
                if ad[ele] > 1:
                    ansset.remove(ele)
            elif ele in B:
                if bd[ele] > 1:
                    ansset.remove(ele)
        return list(ansset)

# @lc code=end

