#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        if not root or (not root.left and not root.right):
            return True
        def checker(lr, rr):
            if lr is None and rr is None:
                return True
            if lr is None or rr is None:
                return False
            if lr.val != rr.val:
                return False
            return checker(lr.left, rr.right) and checker(lr.right, rr.left)
        return checker(root.left, root.right)

# @lc code=end

