#
# @lc app=leetcode id=540 lang=python3
#
# [540] Single Element in a Sorted Array
#

# @lc code=start
class Solution:
    # interger only
    # any negative number?
    # length is odd
    def singleNonDuplicate(self, nums: List[int]) -> int:
        s = 0
        for ele in nums:
            s = s ^ ele
        return s
# @lc code=end

