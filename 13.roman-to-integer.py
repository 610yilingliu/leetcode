#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        c = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        v = [1000, 500, 100, 50, 10, 5, 1]
        d = dict(zip(c, v))
        sum = 0
        while len(s) > 1:
            first = s[0]
            second = s[1]
            if d[first] >= d[second]:
                sum += d[first]
                s = s[1:]
            else:
                sum += d[second] - d[first]
                s = s[2:]
        if len(s) == 1:
            sum += d[s[0]]
        return sum
            
# @lc code=end

