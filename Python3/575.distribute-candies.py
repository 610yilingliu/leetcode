#
# @lc app=leetcode id=575 lang=python3
#
# [575] Distribute Candies
#

# @lc code=start
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        s = set(candies)
        if len(s) <= len(candies) >> 1:
            return len(s)
        return len(candies) >> 1

# @lc code=end

