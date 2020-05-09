#
# @lc app=leetcode id=246 lang=python3
#
# [246] Strobogrammatic Number
#

# @lc code=start
class Solution:
    def isStrobogrammatic(self, num: str):
        if not str:
            return True
        valid = {'0':'0', '1':'1', '6':'9', '8': '8', '9': '6'}
        invalid = {'3', '4', '5', '7'}
        if len(num) == 1:
            if num in {'0', '1', '8'}:
                return True
            return False

        l = len(num)
        mid = l >> 1
        if l & 1:
            if num[mid] not in {'0', '1', '8'}:
                return False
            pre = num[:mid]
            suf = num[mid + 1:]
        else:
            pre = num[:mid]
            suf = num[mid:]

        for i in range(len(pre)):
            if pre[i] in invalid or suf[-i - 1] in invalid:
                return False
            if valid[pre[i]] != suf[-i - 1]:
                return False
        return True
# @lc code=end

