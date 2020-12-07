#
# @lc app=leetcode id=858 lang=python3
#
# [858] Mirror Reflection
#

# @lc code=start
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        r = 1
        while True:
            cur = r * q
            if cur % p == 0:
                if r & 1 == 0:
                    return 2
                m = cur // p
                if m & 1 == 0:
                    return 0
                return 1
            r += 1
# @lc code=end

