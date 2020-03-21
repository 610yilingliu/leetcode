#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, str: str) -> int:
        nums = {'0','1','2','3','4','5','6','7','8','9'}
        symbol = {'+', '-'}
        started = 0
        final = ''
        for char in str:
            if char == ' '  and started == 0:
                continue
            elif started == 0 and char in symbol:
                final += char
                started = 1
            elif char in nums:
                started = 1
                final += char
            else:
                break
        if final == '' or final in symbol:
            return 0
        final = int(final)
        max = 2**31 - 1
        min = -2**31
        if final > max:
            return max
        elif final < min:
            return min
        return final
# @lc code=end

