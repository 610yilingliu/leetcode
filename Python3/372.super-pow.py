#
# @lc app=leetcode id=372 lang=python3
#
# [372] Super Pow
#

# @lc code=start
class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        res = 1
        for x in b:
            res = self.pow(res, 10) * self.pow(a, x) % 1337
        return res
        
    def pow(self, a, b):
        if b == 0 or a == 1: return 1
        if b % 2:
            return a * self.pow(a, b - 1) % 1337
        return self.pow((a * a) % 1337, b >> 1) % 1337
# @lc code=end

