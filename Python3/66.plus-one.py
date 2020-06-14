#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]):
        if not digits:
            return []
        curd = len(digits) - 1
        digits[curd] += 1
        while digits[curd] > 9:
            digits[curd] = 0
            if curd == 0:
                return [1] + digits
            curd -= 1
            digits[curd] += 1
        return digits
# @lc code=end

