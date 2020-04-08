#
# @lc app=leetcode id=771 lang=python3
#
# [771] Jewels and Stones
#

# @lc code=start
class Solution:
    def numJewelsInStones(self, J, S):
        if not S or not J:
            return 0
        ans = 0
        for item in S:
            if item in J:
                ans +=1
        return ans
# @lc code=end

