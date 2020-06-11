#
# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
#

# @lc code=start
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odd = []
        even = []
        for ele in A:
            if ele & 1:
                odd.append(ele)
            else:
                even.append(ele)
        return even + odd
# @lc code=end

