#
# @lc app=leetcode id=872 lang=python3
#
# [872] Leaf-Similar Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode):
        if not root1 and not root2: 
            return True
        if not root1 or not root2: 
            return False
        t1 = []
        t2 = []
        self.get_leafs(root1, t1)
        self.get_leafs(root2, t2)
        return t1 == t2
    
    def get_leafs(self, root, curset):
        if not root.left and not root.right:
            curset.append(root.val)
        if root.left:
            self.get_leafs(root.left, curset)
        if root.right:
            self.get_leafs(root.right, curset)

# @lc code=end

