#
# @lc app=leetcode id=783 lang=python3
#
# [783] Minimum Distance Between BST Nodes
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDiffInBST(self, root):
        ls = []
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            ls.append(root.val)
            inorder(root.right)
        mi = float('inf')
        inorder(root)
        for i in range(1, len(ls)):
            mi = min(mi, ls[i] - ls[i - 1])
        return mi


# @lc code=end

