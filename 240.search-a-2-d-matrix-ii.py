#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        y_start = 0
        x_start = len(matrix[0]) - 1
        while x_start >= 0 and y_start < len(matrix):
            if target == matrix[y_start][x_start]:
                return True
            if target > matrix[y_start][x_start]:
                y_start += 1
            else:
                x_start -= 1
        return False


if __name__ == '__main__':
    a = Solution()
    b = a.searchMatrix([[-5]], -5)
    print(b)
# @lc code=end

