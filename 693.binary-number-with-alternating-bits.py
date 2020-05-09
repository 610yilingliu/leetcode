#
# @lc app=leetcode id=693 lang=python3
#
# [693] Binary Number with Alternating Bits
#

# @lc code=start
class Solution:
    def hasAlternatingBits(self, n: int):
        if n == 0 or n == 1:
            return True
        pre = n & 1
        n = n >> 1
        while n > 0:
            cur = n & 1
            if cur == pre:
                return False
            pre = cur
            n = n >> 1
        return True

# if __name__ == '__main__':
#     a = Solution()
#     b = a.hasAlternatingBits(5)
#     print(b)
# @lc code=end

