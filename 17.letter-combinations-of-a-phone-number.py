#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    # result: list
    def letterCombinations(self, digits):
        if digits == "":
            return []
        d = {
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'
        }
        result = [""]
        for item in digits:
            temp = []
            for num in d[int(item)]:
                for chars in result:
                    temp.append(chars + num)
            result = temp
        return result
# @lc code=end

