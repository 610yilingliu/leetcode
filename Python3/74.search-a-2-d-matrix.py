#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix, target):
        if matrix == [[]] or not matrix:
            return False
        if len(matrix) == 1:
            return self.search_singlerow(matrix[0], target)
        up = 0
        down = len(matrix) - 1

        if target < matrix[up][0] or target > matrix[down][-1]:
            return False
        while up < down:
            if down - up == 1:
                if matrix[up][-1] < target < matrix[down][0]:
                    return False
            mid = (up + down)//2
            if matrix[up][0] <= target <= matrix[up][-1]:
                return self.search_singlerow(matrix[up], target)
            elif matrix[down][0] <= target <= matrix[down][-1]:
                return self.search_singlerow(matrix[down], target)
            elif matrix[mid][0] <= target <= matrix[mid][-1]:
                return self.search_singlerow(matrix[mid], target)
            else:
                if matrix[up][0] < target < matrix[mid][0]:
                    up = up
                    down = mid
                else:
                    up = mid
                    down = down

    def search_singlerow(self, row, target):
        if len(row) == 1:
            if row[0] == target:
                return True
            else:
                return False
        if row[0] == target:
            return True
        if row[-1] == target:
            return True
        l = 0
        r = len(row)
        mid = (l + r)//2
        l_ls = row[:mid]
        r_ls = row[mid:]
        if target == row[mid]:
            return True
        if target < row[mid]:
            return self.search_singlerow(l_ls, target)
        if target > row[mid]:
            return self.search_singlerow(r_ls, target)
# @lc code=end

