#
# @lc app=leetcode id=993 lang=python3
#
# [993] Cousins in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int):
        pre = 0
        curval = 0
        self.x = x
        self.y = y
        self.xdetail = []
        self.ydetail = []
        self.finder(0, 0, root)
        if not self.xdetail or not self.ydetail:
            return False
        if self.xdetail[0] == self.ydetail[0]:
            return False
        if self.xdetail[1] != self.ydetail[1]:
            return False
        return True

    def finder(self, pre, level, node):
        if not node:
            return
        if not self.xdetail or not self.ydetail:
            if node.val == self.x:
                self.xdetail = [pre, level]
            elif node.val == self.y:
                self.ydetail = [pre, level]
            else:
                self.finder(node.val, level + 1, node.left)
                self.finder(node.val, level + 1, node.right)

# @lc code=end

