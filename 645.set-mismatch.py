#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#

# @lc code=start
import collections
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = []
        d = collections.Counter(nums)
        for k, v in d.items():
            if v == 2:
                ans.append(k)
                break
        num_set = set(nums)
        full = {i for i in range(1, len(nums) + 1)}
        ans += list(full - num_set)
        return ans
        
# @lc code=end

