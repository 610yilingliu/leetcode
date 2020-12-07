#
# @lc app=leetcode id=779 lang=python3
#
# [779] K-th Symbol in Grammar
#

# @lc code=start
class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        if N == 1: return 0
        if K == 2: return 1
        if K <= 1 << N - 2: return self.kthGrammar(N - 1, K)
        K -= 1 << N - 2
        return 1 - self.kthGrammar(N - 1, K)

# @lc code=end

