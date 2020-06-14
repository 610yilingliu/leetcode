#
# @lc app=leetcode id=250 lang=python3
#
# [250] Count Univalue Subtrees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: TreeNode):
        self.ans = 0
        self.finder(root)
        return self.ans

    def finder(self, root):
        if not root:
            return True
        l, r = self.finder(root.left), self.finder(root.right)
        if l and r and (not root.left or root.left.val == root.val) and (not root.right or root.right.val == root.val):
            self.ans += 1
            return True
        return False


# @lc code=end

