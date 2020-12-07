#
# @lc app=leetcode id=1099 lang=python3
#
# [1099] Two Sum Less Than K
#

# @lc code=start
class Solution:
    def twoSumLessThanK(self, A, K):
        A.sort()
        if len(A) < 2 or A[0] + A[1] > K:
            return -1
        curmax = -1
        for i in range(len(A) - 1, 0, -1):
            for j in range(i - 1, -1, -1):
                if A[i] > K:
                    continue
                cursum = A[i] + A[j]
                if cursum < K and cursum > curmax:
                    curmax = cursum
        return curmax
# @lc code=end

