#
# @lc app=leetcode id=938 lang=python3
#
# [938] Range Sum of BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.ans = 0
        self.finder(root, L, R)
        return self.ans

    def finder(self, root, l, r):
        if not root:
            return
        if l <= root.val <= r:
            self.ans += root.val
        if root.val >= r:
            self.finder(root.left, l, r)
        elif root.val <= l:
            self.finder(root.right, l, r)
        else:
            self.finder(root.left, l, r)
            self.finder(root.right, l, r)
# @lc code=end

