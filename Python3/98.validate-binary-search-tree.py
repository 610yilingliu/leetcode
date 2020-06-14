#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        if not root:
            return True
        def router(root, mx, mi):
            if not root:
                return True
            if root.val >= mx or root.val <= mi:
                return False
            return router(root.left, root.val, mi) and router(root.right, mx, root.val)
        return router(root, float('inf'), float('-inf'))



# @lc code=end

