#
# @lc app=leetcode id=513 lang=python3
#
# [513] Find Bottom Left Tree Value
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        self.ans = [None, float('inf'), float('-inf')]
        self.finder(root, 0, 0)
        return self.ans[0]

    def finder(self, root, x, y):
        if not root:
            return
        if y > self.ans[2]:
            self.ans = [root.val, x, y]
        elif y == self.ans[2]:
            if x < self.ans[1]:
                self.ans = [root.val, x, y]
        self.finder(root.left, x - 1, y + 1)
        self.finder(root.right, x + 1, y + 1)

# @lc code=end

