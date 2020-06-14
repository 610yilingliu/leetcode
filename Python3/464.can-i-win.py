#
# @lc app=leetcode id=464 lang=python3
#
# [464] Can I Win
#

# @lc code=start
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int):
        # first player must win
        if maxChoosableInteger > desiredTotal:
            return True
        nums = [num for num in range(1, maxChoosableInteger + 1)]
        # will never reach the target, so first player will not win
        if sum(nums) < desiredTotal:
            return False
        self.seen = {}
        
        return self.can_win(nums, desiredTotal)
    
    def can_win(self, nums, target):
        if nums[-1] >= target:
            return True 
        if tuple(nums) in self.seen:
            return self.seen[tuple(nums)]
        
        for i in range(len(nums)):
            # to player2
            if not self.can_win(nums[:i] + nums[i+1:], target-nums[i]):
                self.seen[tuple(nums)] = True 
                return True 
        self.seen[tuple(nums)] = False 
        return False 
# @lc code=end

