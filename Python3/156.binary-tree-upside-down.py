#
# @lc app=leetcode id=156 lang=python3
#
# [156] Binary Tree Upside Down
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: TreeNode):
        if not root or (not root.left and not root.right):
            return root
        parent = None
        sib = None
        while root:
            temp = root.left
            root.left = sib
            sib = root.right
            root.right = parent
            parent = root
            root = temp
        return parent


        


# @lc code=end

