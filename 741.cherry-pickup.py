#
# @lc app=leetcode id=741 lang=python3
#
# [741] Cherry Pickup
#

# @lc code=start
# class Solution:
#     def cherryPickup(self, grid: List[List[int]]):
#         if not grid or not grid[0]:
#             return 0
#         dp = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
#         y_has1 = False
#         for i in range(len(grid)):
#             if grid[i][0] == -1:
#                 break
#             if grid[i][0] == 1
#         for i in range(1, len(grid)):
#             for j in range(1, len(grid[0])):
#                 if grid[i][j] == 0:
#                     dp[i][j] = (0, 0)
#                 elif grid[i][j] == 1:
#                     dp[i][j] = (1, 0)
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        from functools import lru_cache

        #max cherries from (x1, y1) to (0, 0) + (x2, y2) to (0, 0)
        @lru_cache(None)
        def dp(x1, y1, x2):
            y2 = x1 + y1 - x2
            if x1 < 0 or y1 < 0 or x2 < 0 or y2 < 0: return -1
            if grid[x1][y1] < 0 or grid[x2][y2] < 0: return -1
            if x1 == 0 and y1 == 0: return grid[x1][y1]
            ans = max(dp(x1-1, y1, x2-1), dp(x1, y1-1, x2-1),
                      dp(x1-1, y1, x2), dp(x1, y1-1, x2))
            if ans < 0: return -1
            ans += grid[x1][y1]
            if x1 != x2:
                ans += grid[x2][y2]            
            return ans
        
        return max(0, dp(n-1, n-1, n-1))
    

# @lc code=end

