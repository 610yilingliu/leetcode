#
# @lc app=leetcode id=461 lang=python3
#
# [461] Hamming Distance
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int):
        if x == y:
            return 0


        cnt = 0
        while x > 0 or y > 0:
            if x & 1 != y & 1:
                cnt += 1
            x = x >> 1
            y = y >> 1
        return cnt

# @lc code=end

