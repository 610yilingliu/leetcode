#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str):
        stack = []
        s = path.split('/')
        for item in s:
            if not item or item == '.':
                continue
            if item == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(item)
        return '/' + '/'.join(stack)

# @lc code=end

