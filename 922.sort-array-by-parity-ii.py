#
# @lc app=leetcode id=922 lang=python3
#
# [922] Sort Array By Parity II
#

# @lc code=start
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        if len(A) < 2:
            return A
        ans = [0] * len(A)
        ep = 0
        op = 1
        for item in A:
            if item & 1:
                ans[op] = item
                op += 2
            else:
                ans[ep] = item
                ep += 2
        return ans
# @lc code=end

