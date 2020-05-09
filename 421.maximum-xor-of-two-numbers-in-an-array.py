#
# @lc app=leetcode id=421 lang=python3
#
# [421] Maximum XOR of Two Numbers in an Array
#

# @lc code=start
class Solution:
    def findMaximumXOR(self, nums: List[int]):
        ans = 0
        mask = 0
        for i in range(31, -1, -1):
            mask |= 1 << i
            pre = {num & mask for num in nums}
            curguess = ans | 1 << i
            for prefix in pre:
                if prefix ^ curguess in pre:
                    ans = curguess
                    break
        return ans

# @lc code=end

