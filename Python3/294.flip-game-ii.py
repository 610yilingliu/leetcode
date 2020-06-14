#
# @lc app=leetcode id=294 lang=python3
#
# [294] Flip Game II
#

# @lc code=start
class Solution:
    def canWin(self, s):
        for i in range(len(s) - 1):
            if s[i:i + 2] == '++' and self.canWin(s[:i] + '--' + s[i + 2:]) == False:
                return True
        return False

if __name__ == '__main__':
    a = Solution()
    b = a.canWin("+++++")
    print(b)
# @lc code=end

