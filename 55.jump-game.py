#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums):
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False
        result = self.helper(nums, 0)
        return result
    
    def helper(self,nums, cur_pos):
        cur_step = nums[cur_pos]
        farthest = 0
        next_start = 0
        for i in range(cur_pos, cur_pos + cur_step + 1):
            s = i + nums[i]
            if s >= len(nums) - 1:
                return True
            if  s > farthest:
                farthest = s
                next_start = i
        if farthest < cur_pos + cur_step + 1:
            return False
        return self.helper(nums, next_start)

# @lc code=end

