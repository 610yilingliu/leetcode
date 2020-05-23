#
# @lc app=leetcode id=296 lang=python3
#
# [296] Best Meeting Point
#

# @lc code=start
class Solution:
    def minTotalDistance(self, grid):
        if not grid or not grid[0]:
            return 0
        points = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    points.append([i, j])
        if len(points) == 0:
            return 0
        points.sort(key = lambda x : x[0])
        mid_x = points[len(points)//2][0]
        points.sort(key = lambda x : x[1])
        mid_y = points[len(points)//2][1]
        ans = 0
        for point in points:
            ans += abs(point[0] - mid_x)
            ans += abs(point[1] - mid_y)

        return ans

if __name__ == '__main__':
    a = Solution().minTotalDistance([[1],[1]])
    print(a)
# @lc code=end

