#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def inorderTraversal(self, root):
#         self.ans = []
#         self.helper(root)
#         return self.ans

#     def helper(self,root):
#         if root == None:
#             return
#         if root.left != None:
#             self.helper(root.left)
#         self.ans.append(root.val)
#         if root.right != None:
#             self.helper(root.right)

class Solution:
    def inorderTraversal(self, root):
        if not root:
            return []
        stack = []
        ans = []
        while root is not None or stack:
            while root is not None:
                stack.append(root)
                root = root.left
            if stack:
                root = stack.pop()
                ans.append(root.val)
                root = root.right
        return ans
        
# @lc code=end

