#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return [[]]
        n = len(matrix)
        m = len(matrix[0])
        pos = []
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    pos.append([i, j])
        for item in pos:
            x = item[0]
            y = item[1]
            for i in range(n):
                matrix[i][y] = 0
            for j in range(m):
                matrix[x][j] = 0
        print(matrix)

if __name__ =='__main__':
    a = Solution()
    a.setZeroes([[1,1,1],[1,0,1],[1,1,1]])


# @lc code=end

