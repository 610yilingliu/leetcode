#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        islands = 0
        h = len(grid)
        l = len(grid[0])
        for i in range(h):
            for j in range(l):
                if grid[i][j] == "1":
                    self.landfinder([i, j], grid)
                    islands += 1
        return islands
    
    def landfinder(self, current_pos, grid):
        x = current_pos[1]
        y = current_pos[0]
        grid[y][x] = "0"
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for d in directions:
            new_x = x + d[1]
            new_y = y + d[0]
            if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid) and grid[new_y][new_x] == "1":
                self.landfinder([new_y, new_x], grid)

if __name__ == '__main__':
    a = Solution()
    b = a.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
    print(b)

# @lc code=end

