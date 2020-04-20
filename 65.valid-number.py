#
# @lc app=leetcode id=65 lang=python3
#
# [65] Valid Number
#

# @lc code=start
class Solution:
    def isNumber(self, s):
        try:
            float(s)
        except:
            return False
        return True



            


# @lc code=end

