#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        ans = []
        def preorder(node):
            if not node:
                return None
            ans.append(node.val)
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return ans

# class Solution:
#     def preorderTraversal(self, root):
#         q = []
#         ans = []
#         while q or root:
#             while root:
#                 ans.append(root.val)
#                 q.append(root)
#                 root = root.left
#             root = q.pop()
#             root = root.right
#         return ans

# @lc code=end

