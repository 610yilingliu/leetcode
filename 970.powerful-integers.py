#
# @lc app=leetcode id=970 lang=python3
#
# [970] Powerful Integers
#

# @lc code=start
class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        r = []
        if bound < 2:
            return r
        else:
            i = 0
            while x ** i + y ** 0 <= bound:
                j = 0
                while x ** i + y ** j <= bound:
                    r.append(x ** i + y ** j)
                    if y == 1:
                        break
                    j += 1
                if x == 1:
                    break
                i += 1
            return set(r)

# @lc code=end

