#
# @lc app=leetcode id=265 lang=python3
#
# [265] Paint House II
#

# @lc code=start
class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        if n == 0 : return 0
        elif n == 1 :  return min (costs[0])
        else:
        	k = len(costs[0]) if n else 0
        	dp = [[0 for i in range(k)] for j in range(n)]

        	dp[0] = costs[0]

        	for i in range(1,n):
        		for j in range(0,k):
        			minVal = float('inf')
        			for m in range(0,k):
        				if m != j and dp[i-1][m] < minVal:
        					minVal = dp[i-1][m]
        			dp[i][j] = minVal + costs[i][j]

        	return min(dp[-1])

# if __name__ == '__main__':
#     a = Solution()
#     b = a.minCostII([[1,5,3],[2,9,4]])
#     print(b)
# @lc code=end

