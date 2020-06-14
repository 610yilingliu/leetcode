#
# @lc app=leetcode id=701 lang=python3
#
# [701] Insert into a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)
        if val < root:
            self.insertIntoBST(root.left, val)
        if val > root:
            self.insertIntoBST(root.right, val)
        
# @lc code=end

