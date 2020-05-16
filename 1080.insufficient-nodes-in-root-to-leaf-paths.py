#
# @lc app=leetcode id=1080 lang=python3
#
# [1080] Insufficient Nodes in Root to Leaf Paths
#

# @lc code=start
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int):

        safe = {}
        def findPath(node, tmp):
            if not node:
                return
            tmp.append(node)
            if not node.left and not node.right:
                s = 0
                for item in tmp:
                    s += item.val
                if s >= limit:
                    for item in tmp:
                        safe[item] = 1
            
            findPath(node.left, tmp)
            findPath(node.right, tmp)
            tmp.pop()
            
        findPath(root, [])
        
        def dfs2(node):
            if not node:
                return
            if node.left and safe.get(node.left, 0) == 0:
                node.left = None
            if node.right and safe.get(node.right, 0) == 0:
                node.right = None
            dfs2(node.left)
            dfs2(node.right)
        dfs2(root)
        return root if safe.get(root, 0) == 1 else None
                
        


# @lc code=end

