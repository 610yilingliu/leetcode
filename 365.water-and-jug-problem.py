#
# @lc app=leetcode id=365 lang=python3
#
# [365] Water and Jug Problem
#

# @lc code=start
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int):
        if x + y < z:
            return False
        if x == y and z != 0 and z != x:
            return False
        if z == x or z == y:
            return True
        if not y:
            return x == z
        if not x:
            return y == z
        larger = max(x, y)
        smaller = min(x, y)
        while smaller > 0:
            if z % smaller == 0:
                return True
            tmp = smaller
            smaller = larger % smaller
            larger = tmp
        return False

# @lc code=end

