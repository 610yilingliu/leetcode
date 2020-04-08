#
# @lc app=leetcode id=563 lang=python3
#
# [563] Binary Tree Tilt
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root):
        self.sum = 0
        self.finder(root)
        return self.sum

        
    def finder(self, root):
        if root is None:
            return 0
        lh = self.finder(root.left)
        rh = self.finder(root.right)
        self.sum += abs(lh - rh)
        return lh + rh + root.val

# @lc code=end

