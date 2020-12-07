#
# @lc app=leetcode id=644 lang=python3
#
# [644] Maximum Average Subarray II
#

# @lc code=start

# **Contiguous** subarray
# length >= k, return the maximum average of that subarray
# could have negative integers 
# avg, not abs(avg)

# 1. brut-force sol: O(n^3)
# 2. draft:
# [1, 12, -5, -6]
# [1, 12, -6, -6, 50], [12, -5, -6, 50]
# [1, 12, -6, -6, 50, 3], [12, -5, -6, 50, 3], [-5, -6, 50, 3]
class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :return float
        """
        


# assume: [1, 12, -5, -6, 50, 3], k = 4
# ans: 12.75

# @lc code=end
