#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution:
    def intersection(self, nums1, nums2):
        if not nums1 or not nums2:
            return []
        d1 = set(nums1)
        d2 = set(nums2)
        ans = []
        for item in d2:
            if item in d1:
                ans.append(item)
        return ans
        
# @lc code=end

