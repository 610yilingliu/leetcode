#
# @lc app=leetcode id=1041 lang=python3
#
# [1041] Robot Bounded In Circle
#

# @lc code=start
class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        x, y = 0, 0
        curd = 0
        for i in instructions:
            if i == "G":
                x += dirs[curd][0]
                y += dirs[curd % 4][1]
            elif i == "L":
                curd = (curd + 1) % 4
            elif i == "R":
                curd = (curd - 1) % 4
        return (x == 0 and y == 0) or curd != 0
# @lc code=end

