#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num):
        cur = 1
        while True:
            multi = cur * cur
            if multi > num:
                return False
            if multi == num:
                return True
            cur += 1


# @lc code=end

