#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convertBST(self, root):
        self.sum = 0
        self.s(root)
        return root

        
    def s(self, root):
        if root is None:
            return
        self.s(root.right)
        self.sum += root.val
        root.val = self.sum
        self.s(root.left)

# @lc code=end

