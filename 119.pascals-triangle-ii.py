#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        ls  = [1, 1]
        ans = self.helper(rowIndex - 1, ls)
        return ans
        
    def helper(self, n, prev_list):
        if n == 0:
            return prev_list
        new_ls = [0] * (len(prev_list) + 1)
        new_ls[0] = 1
        new_ls[-1] = 1
        for i in range(1, len(new_ls) - 1):
            new_ls[i] = prev_list[i - 1] + prev_list[i]
        return self.helper(n - 1, new_ls)
# @lc code=end

