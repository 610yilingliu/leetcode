#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int):
        if n <= 0:
            return False
        one_count = 0
        shift = 31
        while shift >= 0:
            if n & 1 == 1:
                one_count += 1
                if one_count > 1:
                    return False
            n >>= 1
            shift -= 1
        return True

if __name__ == '__main__':
    a = Solution()
    b = a.isPowerOfTwo(2)
    print(b)
# @lc code=end

