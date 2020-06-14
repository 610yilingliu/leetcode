#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start
class Solution:
    def multiply(self, num1, num2):
        s = 0
        for i in range(len(num1) - 1, -1, -1):
            p1 = 10 ** (len(num1) - 1 - i)
            for j in range(len(num2) - 1, -1, -1):
                p2 = 10 ** (len(num2) - 1 - j)
                up = int(num1[i]) * p1
                down = int(num2[j]) * p2
                s += up * down
        return str(s)
                
# @lc code=end

