#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]):
        d = dict()
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = True
            else:
                return True

        return False

# @lc code=end

