#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start
class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) < 2:
            return s
        i = 0
        j = len(s)- 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1


# @lc code=end

