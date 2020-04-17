#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k):
        self.ls = []
        self.inorder(root)
        return self.ls[k - 1]

    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        self.ls.append(node.val)
        self.inorder(node.right)



# @lc code=end

