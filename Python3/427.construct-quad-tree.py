#
# @lc app=leetcode id=427 lang=python3
#
# [427] Construct Quad Tree
#

# @lc code=start
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        N = len(grid)
        if N == 1:
            return Node(grid[0][0] == 1, True, None, None, None, None)
        topLeftSum = sum([grid[i][j] for i in range(N//2) for j in range(N//2)])
        topRightSum = sum([grid[i][j] for i in range(N//2) for j in range(N//2, N)])
        bottomLeftSum = sum([grid[i][j] for i in range(N//2, N) for j in range(N//2)])
        bottomRightSum = sum(grid[i][j] for i in range(N//2, N) for j in range(N//2, N))
        node = Node(False, False, None, None, None, None)
        if topLeftSum == topRightSum == bottomLeftSum == bottomRightSum:
            if topLeftSum == 0:
                node.isLeaf = True
                node.val = False
            elif topLeftSum == (N / 2) ** 2:
                node.isLeaf = True
                node.val = True
        if node.isLeaf:
            return node
        node.val = True
        node.topLeft = self.construct([[grid[i][j] for j in range(N//2)] for i in range(N//2)])
        node.topRight = self.construct([[grid[i][j] for j in range(N//2, N)] for i in range(N//2)])
        node.bottomLeft = self.construct([[grid[i][j] for j in range(N//2)] for i in range(N//2, N)])
        node.bottomRight = self.construct([[grid[i][j] for j in range(N//2, N)] for i in range(N//2, N)])
        return node

        
# @lc code=end

