#
# @lc app=leetcode id=678 lang=python3
#
# [678] Valid Parenthesis String
#

# @lc code=start
class Solution:
    def checkValidString(self, s):
        left = 0
        right = 0
        for item in s:
            if item == '(' or item =='*':
                left += 1
            else:
                left -= 1
            if left < 0:
                return False
        if left == 0:
            return True
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ')' or s[i] == '*':
                right += 1
            else:
                right -= 1
            if right < 0:
                return False
        return True
        

# @lc code=end

