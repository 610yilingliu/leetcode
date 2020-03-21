#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    def countAndSay(self, n):
        if n == 1:
            return '1'
        init = '1'
        for _ in range(1, n):
            init = self.helper(init)
        return init
            

    def helper(self, s):
        counter = 1
        res = ""
        label = 0
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                counter += 1
                label = 0
            else:
                res = res + str(counter) + str(s[i])
                counter = 1
                label = 1
        if label == 1:
            res = res + '1' + str(s[len(s) - 1])
        else:
            res = res + str(counter) + str(s[len(s) - 1])
        return res

# @lc code=end