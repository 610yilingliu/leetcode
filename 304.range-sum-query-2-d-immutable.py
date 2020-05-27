#
# @lc app=leetcode id=304 lang=python3
#
# [304] Range Sum Query 2D - Immutable
#

# @lc code=start
class NumMatrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int):
        ans = 0
        for i in range(row1, row2 + 1):
            ans += sum(self.matrix[i][col1 : col2 + 1])
        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]])
# param_1 = obj.sumRegion(2,1,4,3)
# print(param_1)
# @lc code=end

