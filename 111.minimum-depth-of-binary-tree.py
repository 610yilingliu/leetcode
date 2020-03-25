#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root):
        if root is None:
            return 0
        l = self.minDepth(root.left) + 1
        r = self.minDepth(root.right) + 1
        if l == 1:
            return r
        if r == 1:
            return l
        return min(l, r)
        

# @lc code=end

