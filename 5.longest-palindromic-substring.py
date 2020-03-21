#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (28.80%)
# Likes:    5693
# Dislikes: 477
# Total Accepted:    822K
# Total Submissions: 2.9M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
# 
# Example 1:
# 
# 
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: "cbbd"
# Output: "bb"
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1000:
            res = ''
            if len(s) == 1:
                return s[0]
            for i in range(len(s)):
                res1 = anchor(i,i,s)
                res2 = anchor(i,i+1,s)
                if len(res1) > len(res):
                    res = res1
                if len(res2) > len(res):
                    res = res2
            return res

def anchor(start, end, string):
    l= len(string)
    while start >= 0 and end < l and string[start] == string[end]:
            start = start - 1
            end = end + 1
    return string[start + 1: end]
    
# @lc code=end

