#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#

# @lc code=start
import collections
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]):
        table = collections.defaultdict(dict)
        for (x, y), value in zip(equations, values):
            table[x][y] = value
            table[y][x] = 1/value
        ans = []
        for pair in queries:
            if pair[0] in table and pair[1] in table:
                ans.append(self.dfs(table, pair[0], pair[1],set()))
            else:
                ans.append(-1)
        return ans
        
    def dfs(self, table, x, y, visited):
        if x == y:
            return 1.0
        visited.add(x)
        for num in table[x]:
            if num in visited:
                continue
            visited.add(num)
            d = self.dfs(table, num, y, visited)
            if d > 0:
                return d * table[x][num]
        return -1


# @lc code=end

