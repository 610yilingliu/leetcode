#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root):
        if not root:
            return 0
        self.s = 0
        self.traveller(root, 0)
        return self.s

    def traveller(self, root, cur_sum):
        zeros = len(str(root.val))
        cur_sum = cur_sum * (10 ** zeros) + root.val
        if not root.left and not root.right:
            self.s += cur_sum
        if root.left:
            self.traveller(root.left, cur_sum)
        if root.right:
            self.traveller(root.right, cur_sum)

# @lc code=end

