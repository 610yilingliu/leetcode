#
# @lc app=leetcode id=606 lang=python3
#
# [606] Construct String from Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def tree2str(self, t):
        if t is None:
            return ''
        if t.left is None and t.right is None:
            return str(t.val)
        if t.right is None:
            return str(t.val) + '(' + self.tree2str(t.left) + ')'
        return str(t.val) + '(' + self.tree2str(t.left) + ')' + '(' + self.tree2str(t.right) + ')'
        


# @lc code=end

