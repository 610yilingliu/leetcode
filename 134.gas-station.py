#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1
        current = 0
        rest = 0
        for i in range(len(gas)):
            if gas[i] + rest < cost[i]:
                current = i + 1
                rest = 0
            else:
                rest += gas[i] - cost[i]
        return current
        
if __name__ == '__main__':
    a = Solution()
    b = a.canCompleteCircuit([3,3,4], [3,4,4])
    print(b)
# @lc code=end

