#
# @lc app=leetcode id=361 lang=python3
#
# [361] Bomb Enemy
#

# @lc code=start
class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        def count(x, y):
            left, right, up, down = 0, 0, 0, 0
            for i in range(x-1, -1, -1):
                if grid[i][y] == 'W':
                    break
                if grid[i][y] == 'E':
                    left += 1
                    
            for i in range(x+1, row):
                if grid[i][y] == 'W':
                    break
                if grid[i][y] == 'E':
                    right += 1
                    
            for j in range(y+1, col):
                if grid[x][j] == 'W':
                    break
                if grid[x][j] == 'E':
                    up += 1
            
            for j in range(y-1, -1, -1):
                if grid[x][j] == 'W':
                    break
                if grid[x][j] == 'E':
                    down += 1
            return left+right+up+down
        
        if not grid: 
            return 0
        row, col = len(grid), len(grid[0])
        ans = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '0':
                    # count the num of enemies 
                    ans = max(ans, count(i, j))
                    
        return ans
# @lc code=end

