#
# @lc app=leetcode id=333 lang=python3
#
# [333] Largest BST Subtree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: TreeNode):
        if not root:
            return 0
        self.size = 0
        self.dfs(root)
        return self.size

    def dfs(self, root):
        if not root:
            return True, float('inf'), float('-inf'), 0
        lv, lmi, lmx, ln = self.dfs(root.left)
        rv, rmi, rmx, rn = self.dfs(root.right)
        curv = True
        if lv and rv:
            if root.left and root.val <= lmx:
                curv = False
            if root.right and root.val >= rmi:
                curv = False
            if curv:
                self.size = max(self.size, ln + rn + 1)
                return True, min(root.val, lmi, rmi), max(root.val, lmx, rmx), ln + rn + 1
        return False, float('inf'), float('-inf'), 0

# @lc code=end

