#
# @lc app=leetcode id=462 lang=python3
#
# [462] Minimum Moves to Equal Array Elements II
#

# @lc code=start
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        ans = 0 
        nums.sort()
        while l < r:
            ans += nums[r] - nums[l]
            r -= 1
            l += 1
        return ans
# @lc code=end

