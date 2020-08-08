#
# @lc app=leetcode id=625 lang=python3
#
# [625] Minimum Factorization
#

# @lc code=start
class Solution(object):
    def smallestFactorization(self, a):
        """
        :type a: int
        :rtype: int
        """
        if a == 1: return 1
        cnt = [0] * 10
        for x in range(9, 1, -1):
            while a % x == 0:
                cnt[x] += 1
                a //= x
        if a > 1: return 0
        ans = int(''.join(str(n) * cnt[n] for n in range(2, 10)))
        return ans <= 0x7FFFFFFF and ans or 0

a = Solution()
b = a.smallestFactorization(48)
print(b)
# @lc code=end

