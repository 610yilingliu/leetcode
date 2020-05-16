#
# @lc app=leetcode id=163 lang=python3
#
# [163] Missing Ranges
#

# @lc code=start
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int):
        if not nums:
            if lower == upper:
                return [str(lower)]
            return [str(lower) + '->' + str(upper)]
        if nums[0] == upper == lower:
            return []
        ans = []
        if nums[0] > lower:
            if nums[0] - lower == 1:
                ans.append(str(lower))
            else:
                ans.append(str(lower) + '->' + str(nums[0] - 1))
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1 or nums[i] == nums[i - 1]:
                continue
            if nums[i] - nums[i - 1] == 2:
                ans.append(str(nums[i - 1] + 1))
            else:
                ans.append(str(nums[i - 1] + 1) + '->' + str(nums[i] - 1))
        if nums[-1] < upper:
            if upper - nums[-1] == 1:
                ans.append(str(upper))
            else:
                ans.append(str(nums[-1] + 1) + '->' + str(upper))
        return ans

# @lc code=end

