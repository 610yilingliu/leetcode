#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(int(len(matrix)/2)):
            matrix[i], matrix[len(matrix) - 1-i] = matrix[len(matrix) - 1-i], matrix[i]
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# @lc code=end