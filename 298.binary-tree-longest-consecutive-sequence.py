#
# @lc app=leetcode id=298 lang=python3
#
# [298] Binary Tree Longest Consecutive Sequence
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode):
        self.mx = 0
        self.dfs(root, float('-inf'), 0)
        return self.mx
        
    def dfs(self, node, preval, curlen):
        if not node:
            self.mx = max(self.mx, curlen)
            return
        if node.val - preval == 1:
            curlen += 1
        else:
            self.mx = max(self.mx, curlen)
            curlen = 1
        self.dfs(node.left, node.val, curlen)
        self.dfs(node.right, node.val, curlen)


# @lc code=end

