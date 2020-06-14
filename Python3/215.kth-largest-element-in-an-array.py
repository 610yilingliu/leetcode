#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int):
        counter = 0
        while counter < k - 1:
            nums.remove(max(nums))
            counter += 1
        return max(nums)
# @lc code=end

