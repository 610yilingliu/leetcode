#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root):
        if root == None:
            return True
        self.getheight(root)
        lh = root.left.val if root.left else 0
        rh = root.right.val if root.right else 0
        if abs(lh - rh) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

    def getheight(self, root):
        if root == None:
            return 0
        root.val = 1 + max(self.getheight(root.left), self.getheight(root.right))
        return root.val




# @lc code=end

