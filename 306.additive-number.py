#
# @lc app=leetcode id=306 lang=python3
#
# [306] Additive Number
#

# @lc code=start
class Solution:
    def isAdditiveNumber(self, num: str):
        return self.dfs(num, [])

    def dfs(self, num, path):
        if len(path) >= 3 and path[-3] + path[-2] != path[-1]:
            return False
        if not num and len(path) >= 3:
            return True
        for i in range(len(num)):
            cur = num[:i + 1]
            if cur[0] == '0' and len(cur) != 1:
                continue
            if self.dfs(num[i + 1:], path + [int(cur)]):
                return True
        return False


# @lc code=end

