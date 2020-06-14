#
# @lc app=leetcode id=310 lang=python3
#
# [310] Minimum Height Trees
#

# @lc code=start
import collections

class Solution:
    def findMinHeightTrees(self, n: int, edges):
        if n == 0:
            return []
        if n == 1:
            return [0]

        neighbors = collections.defaultdict(set)
        for pair in edges:
            a, b = pair[0], pair[1]
            neighbors[a].add(b)
            neighbors[b].add(a)

        q = collections.deque()
        for k, v in neighbors.items():
            if len(v) == 1:
                q.append(k)
        while n > 2:
            l = len(q)
            n -= l
            for _ in range(l):
                cur = q.popleft()
                for val in neighbors[cur]:
                    neighbors[val].remove(cur)
                    if len(neighbors[val]) == 1:
                        q.append(val)
        return list(q)
            
if __name__ == '__main__':
    a = Solution()
    b = a.findMinHeightTrees(4, [[1,0],[1,2],[1,3]])
    print(b)


# @lc code=end

