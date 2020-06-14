#
# @lc app=leetcode id=317 lang=python3
#
# [317] Shortest Distance from All Buildings
#

# @lc code=start
import collections

# class Solution:
#     def shortestDistance(self, grid):
#         if not grid or not grid[0]:
#             return -1
#         h = len(grid)
#         l = len(grid[0])
#         empty = []
#         buildings = []
#         self.obstacle = set()
#         for i in range(h):
#             for j in range(l):
#                 if grid[i][j] == 1:
#                     buildings.append((i, j))
#                 elif grid[i][j] == 0:
#                     empty.append([i, j])
#                 else:
#                     self.obstacle.add((i, j))
#         self.buildingfinder = set(buildings)
#         mi = float('inf')
#         for e in empty:
#             s = 0
#             for building in buildings:
#                 curd = self.count_dist(e, building, h, l)
#                 if curd == -1:
#                     s = float('inf')
#                     break
#                 s += curd
#             mi = min(s, mi)
#         if mi == float('inf'):
#             return -1
#         return mi

#     def count_dist(self, grid1, grid2, h, l):
#         q = collections.deque()
#         directions = ((0, 1), (1, 0), (-1, 0), (0, -1))
#         q.append((grid1, 0))
#         while q:
#             curpoint, curstep = q.popleft()
#             if curpoint == grid2:
#                 return curstep
#             for d in directions:
#                 next_y = curpoint[0] + d[0]
#                 next_x = curpoint[1] + d[1]
#                 if 0 <= next_x < l and 0 <= next_y < h:
#                     finder = (next_y, next_x)
#                     b = self.buildingfinder - {grid2}
#                     if finder not in self.obstacle and finder not in b:
#                         q.append(((next_y, next_x), curstep + 1))
#         return -1

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        ## APPROACH : BFS ##
        ## BRUTE FORCE: From each building, we do bfs to every empty land and mark the distance in distances hashmap, after that we loop through all the empty lands and find the land which is least distant to all the buildings ##
		# print and see distances hashmap for better understanding ##
        
        if not grid : return 0
        n = len(grid)
        m = len(grid[0])
        builds = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    builds.append((i, j, 0))
        distances = collections.defaultdict(list)
        for i,build in enumerate(builds):
            queue = [build]
            visited = set()
            while( queue ):
                i, j, d = queue.pop(0)
                for x, y in [ (0,1), (0,-1), (-1,0), (1,0) ]:
                    if 0 <= i + x < n and 0 <= j + y < m and not (grid[ i+x ][ j+y ] >= 1 ) and (i+x, j+y) not in visited:
                        visited.add((i+x, j+y))
                        distances[(i+x,j+y)].append(d+1)
                        queue.append( (i+x, j+y, d+1) )
        ans = float('inf')
        for d in distances.values():
            if( len(d) == len(builds) ):
                ans = min( ans, sum(d) )
        return -1 if(ans == float('inf')) else ans
# if __name__ == '__main__':
#     a = Solution()
#     b = a.shortestDistance([[0,2,1],[1,0,2],[0,1,0]])
#     print(b)
# @lc code=end

