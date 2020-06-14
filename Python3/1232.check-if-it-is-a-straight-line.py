#
# @lc app=leetcode id=1232 lang=python3
#
# [1232] Check If It Is a Straight Line
#

# @lc code=start
class Solution:
    def checkStraightLine(self, coordinates):
        if len(coordinates) <= 2:
            return True
        x1, x2, y1, y2 = coordinates[0][0], coordinates[1][0], coordinates[0][1], coordinates[1][1]
        if x1 == x2:
            k = 0
        else:
            k = (y1 - y2)/(x1 - x2)
        b = y1 - k * x1
        for item in coordinates[2:]:
            if item[1] != item[0] * k + b:
                return False
        return True

# @lc code=end

