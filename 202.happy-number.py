#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int):
        appeared = {}
        while True:
            s = 0
            while n > 0:
                s += (n % 10) * (n % 10)
                n = n//10
            if s == 1:
                return True
            else:
                if s not in appeared:
                    appeared[s] = True
                    n = s
                else:
                    return False

# @lc code=end

