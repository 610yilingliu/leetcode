#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, num: int):
        if num == 0:
            return False
        shift = 32
        started = False
        while shift >= 1:
            if num & 1 == 1:
                if shift & 1 == 1 or started:
                    return False
                else:
                    started = True
            num >>= 1
            shift -= 1
        return True
# @lc code=end

