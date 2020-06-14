#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#

# @lc code=start
class Solution:
    def findTheDifference(self, s, t):
        ssum = 0
        tsum = 0
        for char in s:
            ssum += 1 << (ord(char) - ord('a'))
        for item in t:
            tsum += 1 << (ord(item) - ord('a'))

        res = tsum - ssum
        count = 0
        while res & 1 == 0 and count < 32:
            res >>= 1
            count += 1
        if count == 31:
            return ""
        return chr(ord('a') + count)
# @lc code=end

