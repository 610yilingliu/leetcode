#
# @lc app=leetcode id=957 lang=python3
#
# [957] Prison Cells After N Days
#

# @lc code=start
class Solution(object):
    def prisonAfterNDays(self, oldcells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        cells = copy.deepcopy(oldcells)
        count = 0
        N %= 14
        if N == 0:
            N = 14
        while count < N:
            newCell = [0] * 8
            for i in range(1, 7):
                if cells[i - 1] == cells[i + 1]:
                    newCell[i] = 1
                else:
                    newCell[i] = 0
            cells = newCell
            count += 1
        return cells

# @lc code=end

