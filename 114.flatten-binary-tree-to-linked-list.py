#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        l = root.left
        r = root.right
        root.left = None
        self.flatten(l)
        self.flatten(r)
        root.right = l
        while root.right:
            root = root.right
        root.right = r

    # def flatten(self, root):
    #     if not root:
    #         return
    #     ls = []
    #     def preorder(root):
    #         if not root:
    #             return
    #         ls.append(root)
    #         if root.left:
    #             preorder(root.left)
    #         if root.right:
    #             preorder(root.right)
    #     preorder(root)
    #     for i in range(len(ls) - 1):
    #         ls[i].left = None
    #         ls[i].right = ls[i + 1]
    #     return root


# @lc code=end

