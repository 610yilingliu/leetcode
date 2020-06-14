#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node):
        root = self.dfs(node, {})
        return root
        
    def dfs(self, node, d):
        if not node:
            return None
        if node in d:
            return d[node]
        node_copy = Node(node.val, [])
        d[node] = node_copy
        for item in node.neighbors:
            next_copy = self.dfs(item, d)
            if next_copy:
                node_copy.neighbors.append(next_copy)
        return node_copy
# @lc code=end

