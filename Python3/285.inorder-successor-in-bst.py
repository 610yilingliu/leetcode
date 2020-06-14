#
# @lc app=leetcode id=285 lang=python3
#
# [285] Inorder Successor in BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode'):
#         if not root or not p:
#             return None
#         self.ls = []
#         self.finder(root)
#         if p == self.ls[-1]:
#             return None
#         for i in range(len(self.ls)):
#             if self.ls[i] == p:
#                 return self.ls[i + 1]

#     def finder(self, root):
#         if not root:
#             return
#         self.finder(root.left)
#         self.ls.append(root)
#         self.finder(root.right)
            
# Sol2
class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """       
        ans = None
        while root:
            if p.val < root.val:
                ans = root
                root = root.left
            else:
                root = root.right
        return ans

# @lc code=end

