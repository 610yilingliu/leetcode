#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n):
        if n == 0:
            return []
        result = []
        self.helper(n, n, '', result)
        return result
            
    def helper(self, l, r, string, result):
        if r < l:
            return
        if l == 0 and r == 0:
            result.append(string)
        if l > 0:
            self.helper(l - 1, r, string + '(', result)
        if r > 0:
            self.helper(l, r - 1, string + ')', result)

if __name__ == '__main__':
    a = Solution()
    b = a.generateParenthesis(3)
    print(b)
# @lc code=end
