#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s):
        if not s:
            return 0
        l = 0
        r = len(s)
        while s[r - 1] == '(' and r > 0:
            r -= 1
        while s[l] == ')' and l < r - 2:
            l += 1
        s = s[l : r]
        if len(s) < 2:
            return 0
        stack = [-1]
        mx = 0
        for i, p in enumerate(s):
            if p == '(':
                stack.append(i)
            elif p == ')':
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    mx = max(mx, i - stack[-1])
        return mx
            
# @lc code=end

