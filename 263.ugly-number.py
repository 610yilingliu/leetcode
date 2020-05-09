#
# @lc app=leetcode id=263 lang=python3
#
# [263] Ugly Number
#

# @lc code=start
class Solution:
    def isUgly(self, num: int):
        if num < 1:
            return False
        if num == 1:
            return True
        if num > (1 << 31) - 1 or num < -(1<<31):
            return False
        while num > 1:
            if num % 2 == 0:
                num = num//2
            elif num % 3 == 0:
                num = num//3
            elif num % 5 == 0:
                num = num//5
            else:
                return False
        return True

# @lc code=end

