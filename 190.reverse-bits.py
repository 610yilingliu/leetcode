#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n):
        ans = 0
        start = 31
        while start >= 0:
            ans = ans + ((n & 1) << start)
            n = (n >> 1)
            start -= 1
        return ans

# if __name__ == '__main__':
#     a = Solution()
#     b = a.reverseBits(11)
#     print(b)

# @lc code=end

