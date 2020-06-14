#
# @lc app=leetcode id=214 lang=python3
#
# [214] Shortest Palindrome
#

# @lc code=start
class Solution:
    def shortestPalindrome(self, s: str):
        ls = list(s)
        if self.is_palidrome(ls):
            return s
        for i in range(len(s) - 1, -1, -1):
            if self.is_palidrome(ls[:i]):
                pre = ls[i:][::-1]
                res = pre + ls
                return ''.join(res)

    def is_palidrome(self, ls):
        return ls == ls[::-1]

# @lc code=end

