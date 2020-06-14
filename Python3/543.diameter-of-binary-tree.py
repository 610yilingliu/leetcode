#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        self.ans = 0
        self.pathfinder(root)
        return self.ans


    def pathfinder(self, root):
        if root is None:
            return 0
        lh = self.pathfinder(root.left)
        rh = self.pathfinder(root.right)
        self.ans = max(self.ans, lh + rh)
        return max(lh, rh) + 1


# @lc code=end

