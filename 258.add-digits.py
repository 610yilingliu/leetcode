#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
class Solution:
    def addDigits(self, num: int):
        if num < 10:
            return num
        s = 0
        while num > 0:
            s += num%10
            num = num //10 
        return self.addDigits(s)       


            

# @lc code=end

