#
# @lc app=leetcode id=520 lang=python3
#
# [520] Detect Capital
#
# https://leetcode.com/problems/detect-capital/description/
#
# algorithms
# Easy (53.10%)
# Likes:    455
# Dislikes: 242
# Total Accepted:    110.1K
# Total Submissions: 206.7K
# Testcase Example:  '"USA"'
#
# Given a word, you need to judge whether the usage of capitals in it is right
# or not.
# 
# We define the usage of capitals in a word to be right when one of the
# following cases holds:
# 
# 
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# 
# Otherwise, we define that this word doesn't use capitals in a right way.
# 
# 
# 
# Example 1:
# 
# 
# Input: "USA"
# Output: True
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: "FlaG"
# Output: False
# 
# 
# 
# 
# Note: The input will be a non-empty word consisting of uppercase and
# lowercase latin letters.
# 
#

# @lc code=start
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        import re
        pat = '([A-Z]*|[A-Z][a-z]*|[a-z]*)$'
        return True if re.compile(pat).match(word) else False
# @lc code=end

