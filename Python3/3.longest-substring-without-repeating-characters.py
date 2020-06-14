#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s):
            b = 0
            maxlength = 0
            d = {}
            for i, item in enumerate(s):
                if item in d:
                    b = max(b, d[item] + 1)
                d[item] = i
                maxlength = max(maxlength, i-b+1)
            return maxlength
        return 0

 # @lc code=end