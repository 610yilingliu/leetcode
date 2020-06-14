#
# @lc app=leetcode id=311 lang=python3
#
# [311] Sparse Matrix Multiplication
#

# @lc code=start
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n, l = len(A), len(A[0]), len(B[0])
        res = [[0 for _ in range(l)] for _ in range(m)]
        for i in range(m):
            for k in range(n):
                if A[i][k]:
                    for j in range(l):
                        res[i][j] += A[i][k] * B[k][j]
        return res

# if __name__ =='__main__':
#     a = Solution()
#     b = a.multiply([[1,0,0],[-1,0,3]], [[7,0,0],[0,0,0],[0,0,1]])
#     print(b)
# @lc code=end

