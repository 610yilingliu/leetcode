#
# @lc app=leetcode id=967 lang=python3
#
# [967] Numbers With Same Consecutive Differences
#

# @lc code=start
class Solution(object):
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        if N == 1:
            return [0, 1,2,3,4,5,6,7,8,9]
        res = []
        for i in range(1, 10):
            self.dfs(res, i, N - 1, K)
        return list(set(res))
        
    def dfs(self, res, curint, N, K):
        if N == 0:
            res.append(curint)
            return
        last = curint % 10
        if last + K <= 9:
            self.dfs(res, curint * 10 + last + K, N - 1, K)
        if last - K >= 0:
            self.dfs(res, curint * 10 + last - K, N - 1, K)


# a = Solution()
# b = a.numsSameConsecDiff(2, 1)
# print(b)

# @lc code=end

