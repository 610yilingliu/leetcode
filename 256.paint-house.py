#
# @lc app=leetcode id=256 lang=python3
#
# [256] Paint House
#

# @lc code=start
class Solution:
    def minCost(self, costs: 'List[List[int]]') -> 'int':
        red, blue, green = 0, 0, 0
        for r, b, g in costs:
            red, blue, green = min(blue, green) + r, min(red, green) + b, min(red, blue) + g            
            
        return min(red, blue, green)






# @lc code=end

