#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x, n):
        # convert all to positive number
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            x = 1/x
            n = -n
        
        ans = self.helper(x, n, 1, x, 1)
        return ans

    def helper(self, x, n, result, middleware, r):
        if n == 0:
            return result
        if n == 1:
            return result * x
        if n > 2*r:
            n = n - 2 * r
            middleware = middleware * middleware
            r = 2 * r
            result = result * middleware
            return self.helper(x, n, result, middleware, r)
        if n >= r:
            n = n - r
            result = result * middleware
            r = 1
            middleware = x
            return self.helper(x, n ,result, middleware, r)
        return self.helper(x, n, result, x, 1)

# @lc code=end

