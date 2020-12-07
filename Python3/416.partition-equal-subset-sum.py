#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start

# non-empty array positive integers only - we don't need to deal with [] input
# can it partitioned into two subset with equal sum? return True if can, False if can't

class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :return: bool
        """
        s = sum(nums)
        # if sum is an odd number
        if s & 1:
            return False
        target = s//2
        if max(nums) > target:
            return False
        nums.sort(reverse = True)
        return self.dfs(nums, 0, target)
        
    def dfs(self, nums, idx, target):
        if target == 0:
            return True
        if target < 0:
            return
        for i in range(idx, len(nums)):
            if self.dfs(nums, i + 1, target - nums[i]):
                return True
        return False

# class Solution:
#     def canPartition(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         def dfs(start, target):
#             if target < 0:
#                 return
#             if target == 0:
#                 return True
#             for i in range(start, len(nums)):
#                 if dfs(i+1, target - nums[i]):
#                     return True
#             return False
            
#         s = sum(nums)
#         if s % 2 != 0:
#             return False
        
#         nums.sort(reverse = True)
#         return dfs(0, s//2)

a = Solution()
b = a.canPartition([2, 2, 1, 1])
print(b)

# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:

#         #Time Complexity: O(n)
#         #Space Complexity: O(n)

#         Sum = sum(nums)

#         if Sum % 2 == 1:
#             return False

#         Sum = Sum//2

#         n = len(nums)

#         dp = [0]*(Sum+1)
#         dp[0] = 1

#         for i in range(1, n+1):
#             dp_new = dp.copy()

#             for j in range(1, Sum+1):
#                 if j - nums[i-1] >= 0 and dp[j-nums[i-1]]:
#                     dp_new[j] = 1
#             dp = dp_new


#         return dp[-1]

# @lc code=end

