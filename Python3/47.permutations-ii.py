#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums) :
        if nums == []:
            return []
        # sort it first for prev to work
        nums.sort()
        self.ans = []
        self.dfs(nums ,[])
        return self.ans

    def dfs(self, nums, ls):
        # you can also use None or anything that will not equal to the number inside nums
        prev = float('inf')
        if not nums:
            self.ans.append(ls)
        for i in range(len(nums)):
            # example: for [1,1,2], the second '1' will be skipped
            if nums[i] == prev:
                continue
            prev = nums[i]
            self.dfs(nums[:i] + nums[i + 1:len(nums)], ls + [nums[i]])

# @lc code=end

