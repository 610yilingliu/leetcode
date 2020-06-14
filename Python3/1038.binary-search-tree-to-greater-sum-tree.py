#
# @lc app=leetcode id=1038 lang=python3
#
# [1038] Binary Search Tree to Greater Sum Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root):
        if not root:
            return
        self.ls = []
        self.inorder(root)
        def traveller(node):
            if not node:
                return
            idx = self.ls.index(node.val)
            new = sum(self.ls[idx:])
            node.val = new
            traveller(node.left)
            traveller(node.right)
        traveller(root)
        return root


    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.ls.append(root.val)
        self.inorder(root.right)
        
# @lc code=end

