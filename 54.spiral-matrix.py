#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix):
        ans = self.helper(matrix,[])
        return ans

    def helper(self, matrix, ls):
        if matrix == []:
            return ls
        if len(matrix) == 1:
            ls = ls + matrix[0]
            return ls

        for ele in matrix[0]:
            ls.append(ele)
        matrix.pop(0)

        for i in range(len(matrix)):
            if not matrix[i]:
                return ls
            ls.append(matrix[i].pop())

        for i in range(len(matrix[-1])-1, -1, -1):
            ls.append(matrix[-1][i])
        matrix.pop()

        for i in range(len(matrix) -1, -1, -1):
            if not matrix[i]:
                return ls
            ls.append(matrix[i].pop(0))
            
        return self.helper(matrix, ls)
# @lc code=end

