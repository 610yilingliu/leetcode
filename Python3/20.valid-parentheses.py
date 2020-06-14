#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # if s == ""
        if len(s) == 0:
            return True
        d = {
            ')': '(',
            '}' : '{',
            ']' : '['
        }
        temp = []
        for item in s:
            if item not in d:
                temp.append(item)
            else:
                # example: s = ")"
                if temp == []:
                    return False
                if d[item] == temp[-1]:
                    temp.pop()
                else:
                    return False
        if len(temp) > 0:
            return False
        return True 
# @lc code=end

