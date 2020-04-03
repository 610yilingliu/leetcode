#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid):
        if not grid or not grid[0]:
            return 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        h = len(grid)
        l = len(grid[0])
        ans = 0
        for i in range(h):
            for j in range(l):
                if grid[i][j] == 1:
                    current = 4
                    for d in directions:
                        ny = i + d[0]
                        nx = j + d[1]
                        if 0 <= ny < h and 0<= nx < l:
                            if grid[ny][nx] == 1:
                                current -= 1
                    ans += current
        return ans

if __name__ == '__main__':
    a = Solution()
    b = a.islandPerimeter([[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]])
    print(b)


# @lc code=end

