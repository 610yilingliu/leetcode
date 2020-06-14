#
# @lc app=leetcode id=1029 lang=python3
#
# [1029] Two City Scheduling
#

# @lc code=start
 
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: x[0]-x[1])
        return sum(i[0] for i in costs[:len(costs)//2]) + sum(j[1] for j in costs[len(costs)//2:])

# @lc code=end

