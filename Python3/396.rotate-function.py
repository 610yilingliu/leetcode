#
# @lc app=leetcode id=396 lang=python3
#
# [396] Rotate Function
#

# @lc code=start
class Solution:
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        _sum = 0
        N = len(A)
        f = 0
        for i, a in enumerate(A):
            _sum += a
            f += i * a
        res = f
        for i in range(N - 1, 0, -1):
            f = f + _sum - N * A[i]
            res = max(res, f)
        return res

        
# @lc code=end

