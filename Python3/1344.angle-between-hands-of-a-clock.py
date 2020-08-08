#
# @lc app=leetcode id=1344 lang=python3
#
# [1344] Angle Between Hands of a Clock
#

# @lc code=start
class Solution:
    def angleClock(self, hour: int, minutes: int):
        h_angle = hour * 30 + 0.5 * minutes
        min_angle = minutes * 6
        ang = abs(h_angle - min_angle)
        return ang if ang <= 180 else 360 - ang
# @lc code=end

