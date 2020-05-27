#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) == len(num2):
            num = 0
            for i in range(len(num1)):
                num = num * 10 + int(num1[i]) + int(num2[i])
            return str(num)
        div = min(len(num1), len(num2))
        if len(num1) > len(num2):
            return generator(num2, num1, div)
        return generator(num1, num2, div)

        def generator(shorter, longer, div):
            curnum = 0
            start = len(longer) - div
            for i in range(start):
                curnum = curnum * 10 + int(longer[i])
            for j in range(len(shorter)):
                curnum = curnum * 10 + int(shorter[j]) + int(longer[j + start])
            return curnum
# @lc code=end

