#
# @lc app=leetcode id=276 lang=python3
#
# [276] Paint Fence
#

# @lc code=start
class Solution:
    def numWays(self, n: int, k: int):
        if n == 0:
            return 0
        if n == 1:
            return k
        same = 0
        diff = k
        for _ in range(1, n):
            tmp = diff
            diff = (same + diff) * (k - 1)
            same = tmp
        return same + diff

# @lc code=end

