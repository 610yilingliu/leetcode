#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    # def subsets(self, nums):
    #     self.ans = []
    #     self.ans.append([])
    #     if nums:
    #         for i in range(1, len(nums) + 1):
    #             self.helper(nums, [], i)
    #     return self.ans
    
    # def helper(self, nums, ls, k):
    #     if k > len(nums):
    #         return
    #     if k == 0:
    #         self.ans.append(ls)
    #     for i in range(len(nums)):
    #         self.helper(nums[i + 1:], [nums[i]] + ls, k - 1)

    def subsets(self, nums):
        self.ans = []
        if nums:
            self.dfs(nums, [], 0)
        return self.ans

    def dfs(self, nums, ls, idx):
        self.ans.append(ls)
        for i in range(idx, len(nums)):
            self.dfs(nums, ls + [nums[i]], i + 1)

        

        

a = Solution()
b = a.subsets([1,2,3])
print(b)
    
# @lc code=end

