#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        self.ans = []
        self.ans.append([])
        for k in range(1, len(nums) + 1):
            self.helper([], nums, k)
        return self.ans
    
    def helper(self, ls, nums, k):
        if k > len(nums):
            return
        if k == 0:
            self.ans.append(ls)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.helper([nums[i]] + ls, nums[i+1:], k - 1)

# @lc code=end

