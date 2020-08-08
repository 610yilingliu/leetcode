#
# @lc app=leetcode id=442 lang=python3
#
# [442] Find All Duplicates in an Array
#
# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
#
# algorithms
# Medium (64.73%)
# Likes:    2410
# Dislikes: 153
# Total Accepted:    186.6K
# Total Submissions: 278.7K
# Testcase Example:  '[4,3,2,7,8,2,3,1]'
#
# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements
# appear twice and others appear once.
# 
# Find all the elements that appear twice in this array.
# 
# Could you do it without extra space and in O(n) runtime?
# 
# Example:
# 
# Input:
# [4,3,2,7,8,2,3,1]
# 
# Output:
# [2,3]
# 
#

# @lc code=start
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                ans.append(abs(num))
            nums[abs(num) - 1] *= - 1
        return ans 
# @lc code=end

