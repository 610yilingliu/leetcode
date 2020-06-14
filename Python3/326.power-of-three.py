#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#

# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        mx = 3 ** 19
        return n > 0 and mx % n == 0
# @lc code=end

