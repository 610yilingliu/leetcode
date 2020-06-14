#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#
# @lc code=start
class Solution:
    def orangesRotting(self, grid):
        dirs = [(0, 1),(0, -1),(-1, 0),(1, 0)]
        self.h = len(grid)
        self.l = len(grid[0])
        oranges = dict()
        inside = set()
        for ver in range(self.h):
            for hor in range(self.l):
                if grid[ver][hor] not in oranges:
                    oranges[grid[ver][hor]] = {(ver, hor)}
                else:
                    oranges[grid[ver][hor]].add((ver, hor))
        if 1 not in oranges:
            return 0
        if 2 not in oranges:
            return -1
        visited = set()
        ans = self.rotten(oranges, 0, visited, None)
        return ans

    def rotten(self, oranges, step, visited, last_1):
        if len(oranges[1]) == 0:
            return step
        if len(oranges[1]) == last_1:
            return -1
        directions = [(0, 1),(0, -1),(1, 0),(-1, 0)]
        last_1 = len(oranges[1])
        for orange in oranges[2].copy():
            if orange not in visited:
                visited.add(orange)
                for d in directions:
                    new_y = orange[0] + d[0]
                    new_x = orange[1] + d[1]
                    if 0 <= new_y < self.h and 0 <= new_x < self.l:
                        if (new_y, new_x) in oranges[1]:
                            oranges[2].add((new_y, new_x))
                            oranges[1].remove((new_y, new_x))
        step += 1
        return self.rotten(oranges, step, visited, last_1)

if __name__ == '__main__':
    a = Solution()
    b = a.orangesRotting([[1]])
    print(b)
                            
# @lc code=end

