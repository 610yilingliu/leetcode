#
# @lc app=leetcode id=371 lang=python3
#
# [371] Sum of Two Integers
#

# @lc code=start
class Solution:
    def getSum(self, a, b):
        mask = (1 << 32) - 1
        while (b & mask) > 0:
            mid = (a & b) << 1
            a = a ^ b
            b = mid
        if b > 0:
            return a & mask
        return a


if __name__ == '__main__':
    a = Solution()
    b = a.getSum(2,3)
    print(b)

# @lc code=end

