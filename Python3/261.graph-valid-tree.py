#
# @lc app=leetcode id=261 lang=python3
#
# [261] Graph Valid Tree
#

# @lc code=start
import collections
class Solution:
    def validTree(self, n: int, edges):
        if len(edges) != n - 1:
            return False
        neighbors = collections.defaultdict(list)
        for item in edges:
            neighbors[item[0]].append(item[1])
            neighbors[item[1]].append(item[0])
        visited = set()
        q = collections.deque([0])
        while q:
            curele = q.popleft()
            visited.add(curele)
            for node in neighbors[curele]:
                if node not in visited:
                    visited.add(node)
                    q.append(node)
        return len(visited) == n

if __name__ == '__main__':
    a = Solution()
    b = a.validTree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]])
    print(b)    
# @lc code=end

