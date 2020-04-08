#
# @lc app=leetcode id=669 lang=python3
#
# [669] Trim a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:
#     def trimBST(self, root, L, R):
#         if not root:
#             return None
#         if root.val < L:
#             return self.trimBST(root.right, L, R)
#         elif root.val > R:
#             return self.trimBST(root.left, L, R)
#         else:
#             root.left = self.trimBST(root.left, L, R)
#             root.right = self.trimBST(root.right, L, R)
#             return root
class Solution:
    	def trimBST(self, root: TreeNode, L: int, R: int):
            if not root:return None
            def trim(node):
                if not node:return node
                if node.val>=L and node.val<=R:
                    node.left=trim(node.left)
                    node.right=trim(node.right)
                else:
                    if not node.left and not node.right:
                        return None
                    if node.val<L:
                        return trim(node.right)
                    if node.val>R:
                        return trim(node.left)
                return node
            return trim(root)

# @lc code=end

