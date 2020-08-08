#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str):
        a_l = len(a)
        b_l = len(b)
        if a_l > b_l:
            b = "0" * (a_l - b_l) + b
        elif b_l > a_l:
            a = "0" * (b_l - a_l) + a
        return self.addtwo(a, b)
    
    def addtwo(self, num1, num2):
        prev = 0
        res = ""
        for i in range(len(num1) - 1, -1, -1):
            curnum = int(num1[i]) + int(num2[i]) + prev
            if curnum == 2:
               res = "0" + res
               prev = 1
            elif curnum == 3:
                res = "1" + res
                prev = 1
            else:
                res = str(curnum) + res
                prev = 0
        if prev:
            res = str(prev) + res
        return res

# @lc code=end

