#
# @lc app=leetcode id=474 lang=python3
#
# [474] Ones and Zeroes
#
# https://leetcode.com/problems/ones-and-zeroes/description/
#
# algorithms
# Medium (42.19%)
# Likes:    1027
# Dislikes: 233
# Total Accepted:    49.1K
# Total Submissions: 115K
# Testcase Example:  '["10","0001","111001","1","0"]\n5\n3'
#
# Given an array, strs, with strings consisting of only 0s and 1s. Also two
# integers m and n.
# 
# Now your task is to find the maximum number of strings that you can form with
# given m 0s and n 1s. Each 0 and 1 can be used at most once.
# 
# 
# Example 1:
# 
# 
# Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
# Output: 4
# Explanation: This are totally 4 strings can be formed by the using of 5 0s
# and 3 1s, which are "10","0001","1","0".
# 
# 
# Example 2:
# 
# 
# Input: strs = ["10","0","1"], m = 1, n = 1
# Output: 2
# Explanation: You could form "10", but then you'd have nothing left. Better
# form "0" and "1".
# 
# 
# 
# Constraints:
# 
# 
# 1 <= strs.length <= 600
# 1 <= strs[i].length <= 100
# strs[i] consists only of digits '0' and '1'.
# 1 <= m, n <= 100
# 
# 
#
import collections
# @lc code=start
class Solution:
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for str in strs:
            zeros, ones = 0, 0
            for c in str:
                if c == "0":
                    zeros += 1
                elif c == "1":
                    ones += 1
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
        return dp[m][n]
# @lc code=end

