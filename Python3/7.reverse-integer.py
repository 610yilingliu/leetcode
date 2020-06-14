#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if abs(x) < 2147483647:
            if x//10 == 0 :
                return x
            else:
                init = 0
                nag = 0
                if x < 0:
                    nag = 1
                    x = -x
                while x > 0:
                    r = x%10
                    init = init * 10 + r
                    x = x//10
                if nag == 1:
                    init = -init
                if abs(init) < 2147483647:
                    return init
                return 0
        return 0
# @lc code=end

