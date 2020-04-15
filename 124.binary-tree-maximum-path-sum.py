#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode):
        self.mx = float('-inf')
        self.traveller(root, 0)
        return self.mx

    def traveller(self, node, cursum):
        if not node:
            return cursum
        cursum += node.val
        l = 0
        r = 0
        if node.left:
            l = self.traveller(node.left, cursum)
        if node.right:
            r = self.traveller(node.right, cursum)
        # self.mx: keep the origional maximum value
        # l + r + node.val: left sum + right sum + current val
        # node.val: current val (if left sum < 0 and right sum < 0, use this one)
        # l + node.val: left sum + current val
        # r + node.val: right sum + current val
        self.mx = max(self.mx, l + r + node.val, node.val, l + node.val, r + node.val)
        return max(l + node.val, r + node.val, node.val)


# @lc code=end

